---
date: '2026-11-25'
final_url: https://www.anthropic.com/research/migrating-api-to-rust
number: 30
selector_used: article
slug: migrating-api-to-rust
source_url: https://www.anthropic.com/engineering/migrating-api-to-rust
title: Migrating our Messages API to Rust
---

###

Many problems have a *generator–verifier* gap: it’s often far easier to verify that a solution is correct than to come up with one. Sudoku is a classic example. It’s simple to check the solution (just count the numbers in each row, column, and box), but finding that solution can take a long time. Many ambitious Claude projects have relied on this gap: formalizing [proofs](https://alpo.ge/remark.pdf) in mathematics or [migrating](https://bun.com/blog/bun-in-rust) large, well-tested codebases are tasks Claude can take on as long as it has a reliable way to verify its work.

But as Claude has become more capable, it’s begun to take on projects in live systems, where generating the work is easier than verifying it. In these systems, users often rely on edge cases and quirks that [fall outside the test suite](https://github.blog/2016-02-03-scientist/), and it’s hard to write [a definition of “correct” that covers everything](https://www.anthropic.com/research/formal-verification). Without a reliable way to check Claude’s work, the migration of a live system is hard to trust—however quickly Claude can generate the code for it.

We ran into this problem when we migrated our [Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages) from Python to Rust. This API is the primary way that customers—as well as our own apps, like Claude Code and Cowork—reach Claude. From early 2024 to fall 2026, API traffic grew roughly 1,800 times. Rust would allow us to use far less CPU per request. Claude wrote a first version of the API’s core request path in about a week. But building trust in the migration required us to find a way to verify that our Rust API was at parity with our production API. This proved hard for several reasons, including that the Python API continued changing throughout the migration, so parity was a moving target; Claude can reply nondeterministically to the same request, so a difference between two outputs didn’t necessarily mean a bug; and we couldn't read customer requests, so we weren't able to easily see where the two versions diverged.

In this post, we share how we turned the production Messages API itself into a verifier—and how that helped us test the new Rust version on production traffic, find where it differed, and automatically dispatch agents to fix those differences. This allowed us to ship an API on Rust that uses about 70% less CPU per request and cuts median time to first token by about 20% without ever taking the service offline or freezing feature development.

## Why migrate?

We built the Messages API in 2023 and wrote it in Python, which was widely used internally for much of our research code. At first, it was simple. The Messages API passed requests to the model and sent back what the model wrote. (One engineer at the time called it “basically a request forwarder.”) But as the Messages API became more capable and deeply integrated with our codebases, it also developed shared dependencies with Python libraries that were owned by our research and inference teams, which made it hard to move. If we ever wanted to move to another language, it would mean building logging, metrics, and tools all over again.

This calculus gradually began to change. By late 2025, every Messages API request had to be validated, converted into the prompt, tokenized, and screened by our safety classifiers. As each reply arrived, the stream of tokens had to be sorted into text, thinking, and tool calls, and Python added overhead to every one of those steps each time it created an object, freed memory, or handed its work to the next task. Traffic eventually grew far beyond what the initial Python service was built for (Figure 1), and we quickly needed to find a way to make the service much more efficient.

![Bar chart of API requests per day by month, from January 2024 to October 2026. Bars are barely visible through 2024, rise gradually in 2025, and climb steeply in 2026 to their highest point in October.](https://assets.claude.com/b4764d8023bcde58a15900b16cbb8dd2a6f82010.png?w=3840&q=75&fm=webp&fit=max)

The monthly average of API requests per day on our own platform, including our own use.

### Incremental or all at once?

Full rewrites of large production systems are often approached cautiously, for at least two reasons. First, there is no guarantee that test suites cover 100% of production code behavior, and rewriting it is risky. Second, the sheer effort required often makes such work intractable. (In 2024, after one of our engineers suggested migrating to Go or Rust, another temporarily settled the question: “*We are not rewriting the API in go or rust!*”)

The standard advice if you’re looking for performance gains is thus to rewrite only the parts that are slowing the system down, so that’s where we started. In Rust, we rewrote the code that parses a model’s output and called it from Python. This reduced the API’s CPU usage by about 8% to 10%. However, incremental solutions often incur added complexity, and it’s important to make sure that incremental improvements justify those costs. In our case, the gains didn’t justify the added complexity. Each token now crossed between Python and Rust three times (Figure 2), creating new sources of overhead.

![Two diagrams of the request path. In the partial rewrite (March 2026), Rust receives and parses tokens while Python does the other steps, so each token crosses between languages three times. In the full rewrite (September 2026), Python hands over the request and Rust does every other step around the model.](https://assets.claude.com/a518c8d4f3c915a99fc745d5cced4fa806274650.png?w=3840&q=75&fm=webp&fit=max)

After the incremental rewrite, each token of a reply crossed between Python and Rust three times.

As Claude became increasingly capable, we began to question whether the usual reasons to avoid a full migration still held. The effort required to undertake the project was dropping fast: by May 2026, Claude was writing [more than 80% of the code Anthropic merged](https://www.anthropic.com/institute/recursive-self-improvement). We wondered if Claude could now help us write code that would empirically capture every behavior and fix in the production system. But the question became: how could we verify that the behavior of our migration was correct? Verification, not generation, had become the bottleneck.

## How we verified the migration

### General approaches

To verify the migration, we first needed to define what “correct” meant. You can do this in a few ways (Figure 3). If you’re lucky, you can simply write a rule. A [theorem in mathematics](https://claude.dev/blog/safely-scaling-multi-agent-teams-with-fable-5-2/) is a precise statement, and a proof assistant (like Lean) can check each step of a proof against a fixed set of rules. Other times—and more frequently in software engineering—you define “correct” with a set of examples, like tests. For instance, when [Bun moved](https://bun.com/blog/bun-in-rust) from Zig to Rust, its test suite was written in TypeScript, so the same tests could judge both versions. In our case, neither approach was sufficient, so we used the existing system as an oracle to test parity during the migration. In this case, our existing system (the Messages API) kept changing. We were releasing new models and shipping new features regularly, which made the definition of “correct” a moving target.

![Three rows, each sending a signal to a Claude agent. A rule, like Lean for proofs, is all written down and flags a step that doesn’t follow. Examples, like Bun’s test suite, are partly written down and flag a failing test. An existing system, like our Python service, has no answers written down, so you build a checker that flags where the two differ.](https://assets.claude.com/339fa8648be547a2bbcef4a3023ae1df2ec8ab71.png?w=3840&q=75&fm=webp&fit=max)

Three common sources of “correctness.”

### Tests

Tests were the easiest place for us to start, since we already had an existing set of about 700 integration tests. However, two problems limited our ability to trust them to verify the correctness of a migration as high stakes as this (Figure 4).

**The tests were coupled to the Python implementation.** An integration test sends a request, then checks the reply and what was sent to other services. Our tests ran the Python API inside the test’s process and mocked services, like billing and rate limiting, in Python’s memory. The tests had to change along with the code, and Claude helped with both. Now, a “pass” could mean that the code was right, or that the test had been changed in a way that let wrong code through. We saw this happen: when we audited the ported tests, we found more than 100 weakened assertions.

**The tests were incomplete.** The Messages API has dozens of features, and there are far too many configurations to test them exhaustively. Just 20 binary options make over a million combinations—that translates to 12 days of tests at a second each, for one model, before we even vary the prompts inside them. In practice, engineers test a subset that tries to approximate production, but that process inevitably misses cases. Some projects, like Bun, have an independent suite that’s extensive enough to judge a rewrite. Many production services don’t; what counts as correct depends as much on how they behave as on what’s in their tests or documentation.

![Two panels. Left, tests coupled to the legacy implementation: a Python test is ported to a Rust test that Claude also wrote, which checks a smaller area and misses differences. Right, incomplete tests: a few small clusters of checked cases in a large grid of feature combinations, with many missed differences outside them.](https://assets.claude.com/d62ca948354e121f976d85764b91d117d5481523.png?w=3840&q=75&fm=webp&fit=max)

A ported test may check less than the original (dashed), and tests cover only the combinations someone thought of.

### Detecting parity with production

Production data is sometimes “[the only true test](https://github.blog/2016-02-03-scientist/)” that new code behaves like the old code. Running requests through old and new code and comparing the results is often called *shadowing*. To understand what we needed to compare, it helps to walk through what happens to a single request on the Messages API (Figure 5). The API validates each request, converts it into a prompt a model can read (the prompt for inference), tokenizes it, and runs it through safety classifiers. A model then writes a reply, one token at a time. On the output side, the API sorts those tokens into text, thinking, and tool calls, streams them to the customer, and counts usage for limits and billing.

![Flow diagram of a request. The input path accepts or rejects it, resolves settings, and builds the prompt; about a quarter of inputs matched at first. Claude runs once. The output path sorts the reply, streams it, and counts usage. Examples of differences include a rejected field, a 1M limit read as 200K, a missing tool description, stripped newlines, and missing usage fields. The risk designed against is a copy counted twice.](https://assets.claude.com/4903891e9b23665e42dcc20a72be12336b8eba18.png?w=3840&q=75&fm=webp&fit=max)

The Messages API’s input and output paths. Filled dots are examples of differences we found between Python and Rust. The hollow dot is a risk we had to prevent.

The migration covered both the input and output paths. Some differences were obvious, such as when the Rust API rejected a request that Python had accepted. But many were subtle. For instance, if the Rust API left out part of a prompt, the request would still succeed and the model would still answer, though sometimes with minor differences.

Our Rust API passed about 98% of its tests in April, yet only about a quarter of inputs matched on production traffic (Figure 6). The gap came partly from cases in production traffic that our tests didn’t cover. For example, when Python writes JSON tool calls, it escapes certain characters (e.g., an emoji) by replacing them with text codes. Rust wrote those characters as is, so the two prompts differed by a few bytes. Production also weighted bugs differently. In a test suite, each case counts once, but in live traffic, a bug will show up in each request where it’s triggered, which means a single common bug can cause many mismatches.

![Line chart of the share of inputs that matched, from late April to August. It starts at 24%, drops to 6.5% in early May, then rises sharply as fixes roll out, with two falls from changes on the Rust side, and ends at 99.6%. The comparison began on our own traffic and then moved to a wider sample.](https://assets.claude.com/7de2a8325622d82fedbce7ef4ff369b2e27c3042.png?w=3840&q=75&fm=webp&fit=max)

How often Rust’s input matched Python’s on the requests we compared. Replies were compared separately. Each dot is a day, and the line is a seven-day median. What we compared changed over time, and six misleading days are left out.

[Common](https://github.blog/2016-02-03-scientist/) [tools](https://blog.x.com/en/engineering/diffy-testing-services-without-writing-tests) for shadowing often assume that a request can safely run twice, or that a service is deterministic. These assumptions didn’t apply in our case. We had to ensure that a request only counted once toward a customer’s limits and bill. In addition, Claude is nondeterministic, meaning that replies [can differ for the same input](https://platform.claude.com/docs/en/about-claude/glossary) (Figure 7). To address this, we ran the model once and replayed the model output to Rust.

With both versions working from the same model output, we still had to compare every stage before and after the model call, and the results had to match exactly. In many systems, bad input causes an error somewhere down the stack. But since Claude accepts almost any prompt, even a small deviation can change its reply without triggering an error. We compared each step before and after the model call, so that we could pin down any deviation that might change what a customer received.

![Two comparisons. In a typical service, two old copies and a new one match on ID, the new copy shows a bug in the total, and the time varies, so it is ignored as noise. In an inference API, two Python copies and Rust each word the answer to “Is 91 prime?” differently, so the whole reply would count as noise and go unchecked.](https://assets.claude.com/2219fb4da126171dd071056b7290e47ed37bf0f3.png?w=3840&q=75&fm=webp&fit=max)

Diff tools often run the old code twice to learn what varies on its own, then ignore it. Claude's replies vary, so those tools would ignore them, along with any bugs in them.

It was important to us to do this in a way that protected user privacy. To do that we had to work without reading user requests or Claude’s replies to them, which means we couldn’t easily see where the Rust and Python versions of the API differed. So instead of looking at text, we recorded the *shape* of each difference, such as where it happened in the service and how big it was. We did this using a few different approaches:

- **Checkpointing.** Both API versions handle a request using the same steps: accept or reject it, resolve its settings, build the prompt. Every step produces some result, such as an error or the pieces of the prompt, that we could compare step by step, and within the prompt, piece by piece. The first place they differed indicated roughly where the migration code differed from production code (Figure 8).

![Python and Rust compared at each step, with the model called once and its output replayed to Rust. Building the prompt is the first step to differ: in piece 2, two keys are in a different order from byte 17. The record passed to a Claude agent lists the step, piece, both lengths of 190 bytes, and first differing byte, but no text.](https://assets.claude.com/32dee017ccc9f7496eb80f0b926bf655215edb83.png?w=3840&q=75&fm=webp&fit=max)

Comparing at checkpoints, simplified, with made-up values. The first step to differ shows where to look. The record gives the piece, the lengths, and where they first differ, but not the text.

- **Fingerprint.** Once we knew roughly where each diff resided, we still needed a way to distinguish one bug from another. We recorded where each difference began in the prompt, as well as the length difference between the two versions. Combined with the step and piece of the prompt isolated in checkpointing, we found that bugs presented with a specific fingerprint. That is, one bug tends to leave the same fingerprint on every request it affects (Figure 9). We could then group errors by fingerprint, which helped us triage the fixes.

![Four dot grids show mismatches being counted, grouped by fingerprint, split by build, and regrouped after a fix. Fingerprint A accounts for nearly all mismatches; fixing it reveals two older groups, B and C. A table below distinguishes the three by piece and position in the prompt, length gap, and hash.](https://assets.claude.com/92be3b81d1414839e070e7ab04406fb397e320c7.png?w=3840&q=75&fm=webp&fit=max)

Fingerprints from one kind of request. A, at the start of the prompt, hid older differences. Once it was fixed, they appeared as B and C. Dots are illustrative.

The result was a shadowing system that produced a small record of each difference between our Rust and Python APIs. Here is an example, with made-up values:

```
step:        build prompt     ← where in the code
piece:       2                ← where in the prompt
first diff:  byte 17          ← fingerprint
python:      190 bytes        ← fingerprint
rust:        190 bytes        ← fingerprint
```

We could then pass this record to an agent to fix it.

## Verification loops

Each request that differed left a record in our logs. A single bug could produce hundreds of thousands of nearly identical diff records. Rather than send each to an agent, we ran a script every 10 to 30 minutes that grouped them by which fields differed, then alerted a coordinating Claude agent only when it saw a new *kind* of record. This coordinator assigned a worker agent to own each new kind of record. It also created a new thread in a shared Slack channel where human engineers could follow along and steer it when necessary.

To tackle the many bugs, we set up a series of verification loops. A fast *inner* loop gave agents a sandbox in which they could test ideas and propose fixes. A slower *outer* loop then validated fixes in production. In addition, a *memory loop* recorded any mistakes along the way, saving them so that agents could learn over time (Figure 10).

![Three nested loops. The inner loop asks whether an edit fixes the difference, using local checks that take under a second to compare. The outer loop asks whether it is gone in production, using shadowed live traffic over hours or days. The memory loop asks why it keeps happening, and turns people’s corrections into new rules.](https://assets.claude.com/3a4d129ebad6ab2c1188fe6cd02dbc34c2a06e5b.png?w=3840&q=75&fm=webp&fit=max)

Verification loops. An edit is checked in a sandbox, and then on shadowed live traffic. People’s corrections become rules. Each loop can catch what the one inside it misses.

### Inner loop

When we first started testing this in April, we gave each agent a record that showed where the Rust and Python versions differed. Agents would guess the root cause from the code and open a pull request. Once the fix was reviewed and merged, they deployed it to staging, a preproduction copy of the Rust API where we ran the same shadow comparison on test traffic. The agents checked whether the difference was eliminated. Since every hypothesis needed a review and a deployment, feedback was taking hours or days.

We needed agents to get a signal from verification much sooner, so we moved them into their own workspace. We redesigned the inner loop so that agents could have a place to test ideas quickly and fail safely. Each agent ran in a cloud sandbox with both codebases and fast, local checks for what happens before and after the model call. The input check took a request, built the prompt that each version would send to the model, and showed what differed. Because this check never actually called the model, comparing the versions took under a second. We later added an output check, which ran both versions against a fake model. The output check passed a scripted reply, such as a tool call, through each version and compared the results.

The main limitation was that agents could only see the fingerprint, not the request behind each record. So an agent would hypothesize what had caused the difference, then write its own request or model reply to try to reproduce the difference. Since each agent was writing these itself, it could read both results in full. If the results matched, its guess was wrong and the agent tried again. If they differed the same way the record described, the agent edited the Rust until the two versions matched, then added a test that failed on the old code and passed on the new (Figure 11).

![The inner loop, highlighted. From a fingerprint, the agent guesses the cause and writes a triggering request or reply. Input and output checks run it through both versions. If they match, it guesses again; if they differ as the record did, it edits the Rust and rechecks. Once they match after the edit, it opens a PR with a fix and a test.](https://assets.claude.com/52e44ff8f08880a4d0f6877c97cdf77a140a8552.png?w=3840&q=75&fm=webp&fit=max)

Inner loop. From a fingerprint, an agent guesses the cause and writes a request or reply that should trigger it. Local checks run it through both versions until an edit makes them match.

The seam between the inner and outer loops was a good checkpoint for human review. Inside the sandbox, a wrong guess cost an agent only a few seconds and had no impact on users. Agents could iterate on their own. We allowed a fix to cross into the outer loop only after it had undergone PR review; this allowed engineers to focus their attention on proposed fixes (rather than on guesses) and on the questions the verifiers couldn’t answer, such as whether a difference between the Rust and Python APIs was the result of a bug or a deliberate change.

Agents posted their fixes and evidence to their Slack threads for engineers to review. In mid-May, one of the largest remaining differences between the Rust and Python APIs came from web search. The production API retrieved the web search tool’s description from an internal service. The Rust API didn’t call this service yet, so the tool description was missing from the prompts. An agent proposed a shortcut to copy the text into files that would be readable by Rust. The prompts then matched, and the fix passed the local verifier. But an engineer turned it down because it didn’t solve the problem: Rust would still need to call the service before launch, at which point the workaround would be thrown out (Figure 12).

But the verifier rewarded matching outputs, and the agent found the cheapest way to produce them. A verifier can tell an agent whether the outputs matched, but not whether the fix is good enough to ship. That’s why human review was an important gate.

![A Slack channel, #rust-migration. An engineer asks a coordinating Claude agent to explain its next target. Claude agents trace the mismatch to web search, find it is already tracked, and open a fix that loads the description from text files. A second engineer replies: “We know we have to fetch that text before we ship, so this seems like throwaway code. Abandon that PR.”](https://assets.claude.com/6be648dd915614c56b00d3d0cb392f86bd6ef031.png?w=3840&q=75&fm=webp&fit=max)

Agents trace a mismatch to the web search tool across four Slack threads and propose a fix, which an engineer rejects as throwaway code. We shortened and reworded the messages and added the thread names and agent labels.

### Outer loop

In the inner loop, agents debugged differences and proposed fixes. At the seam between the inner loop and the outer loop, engineers reviewed the proposed fixes, gave feedback, and approved them to deploy. The outer loop then compared Rust API deployments with and without each fix.

To make that comparison fair, we logged facts about each request we compared, but not its text, including which model and API features it used—for example, prompt caching, tools, or extended thinking. These details let agents compare requests of the same kind (Figure 13) and ask how often the bug’s fingerprint appeared on builds with and without the fix. This way, agents could monitor the new builds for the bug.

![The outer loop, highlighted. An engineer reviews the PR, which merges and deploys to a test environment, then production. Shadowed live traffic is watched for the fingerprint. If it remains, work returns to the inner loop. If repeated checks find it gone, the task closes, and the thread reopens if it returns.](https://assets.claude.com/79fc91e736881cb4d25983fbf989076d3e7c0014.png?w=3840&q=75&fm=webp&fit=max)

Outer loop. An engineer reviews the fix, it deploys, and shadowed traffic shows whether its fingerprint is gone. If not, the task returns to the inner loop.

We designed the outer loop to catch problems that the inner loop missed. The inner loop simulated production quickly but imperfectly: agents could test a hypothesis in seconds, but only on requests they had written, and with a local verifier that wasn’t always configured exactly like production.

This means that sometimes a fix passed in the sandbox and production still showed the difference. The agent assigned to the bug would either see the difference in the new build’s records, or be alerted by the coordinating agent. It then went back to the inner loop and used that evidence to form a new hypothesis.

### Memory loop

The inner and outer loops fixed one difference at a time. The [memory](https://www.anthropic.com/research/components-of-agent-memory) loop improved how agents made those fixes. We didn’t want engineers to have to make the same correction twice, so we recorded what came out of reviews and agents’ own work and applied it to every agent that followed.

For example, when an engineer turned down the web search shortcut (Figure 12), the agent saved a note to memory explaining the decision, the reason for it, and the correct fix, which was to have Rust call the service that supplies tool descriptions.

Building that call took our team weeks, and in the meantime the bug kept producing records. Some had new fingerprints, because the missing text fell at other positions in the prompt or belonged to another tool that used the same service. Agents checked the memory note, recognized the known bug, and linked those records to it, instead of writing another workaround (Figure 14).

Other lessons became general rules for porting and writing Rust. After one agent guessed at Python’s behavior, an engineer made it a rule to port exactly what Python did. An agent then compared the existing code with that rule and found seven more places where the port had relied on a guess.

In June, an agent also went through about 60 of the team’s review comments, grouped the recurring problems and proposed rules, which an engineer edited and approved for [CLAUDE.md](https://code.claude.com/docs/en/memory) (Figure 14).

The memory loop also encoded some lessons in permanent checks. This included new tests that failed when Rust drifted from Python, lints that banned patterns reviewers kept flagging, and later a merge check that required anyone changing the Python code to make a matching change in Rust or request an exemption.

![The memory loop, highlighted. A repeated mistake prompts an engineer’s correction, “Did you make that up yourself?” It becomes a rule each new agent reads first, a search by another agent that finds the same mistake in seven places, and a test that fails if the versions drift. A daily read of merged changes flags what Rust might need to mirror.](https://assets.claude.com/086ed2a9f3c27c6bfd24e67a3cea341417d40ffe.png?w=3840&q=75&fm=webp&fit=max)

Memory loop. An engineer’s correction becomes three things: a rule that each new agent reads, a search for the same mistake, and a test.

## Looking ahead

It’s increasingly feasible to migrate production systems with Claude, either for better performance or security, without taking an API offline or slowing feature development. Now that the hard part is no longer writing new code, we need to build sufficient confidence that the new system behaves like the old one.

The usual approach to migration is a bit like rebuilding the Ship of Theseus, in which the old ship was replaced plank by plank. Generally it’s been possible to replace planks while the ship still sails, but changing too many planks at once requires coming into dock. To fully stretch the metaphor, Claude now makes it possible to build an identically functioning ship alongside the first—even as the first keeps sailing and having its planks replaced. Agents kept the new ship in step as the old one changed, and we kept checking that the two behaved the same. Once we trusted that they did, we moved the passengers over a few at a time. The new ship sails faster and more efficiently than the old one.

### Lessons learned

**Verification is the new bottleneck.** Previously, large software projects like migrations were hard to justify because they took too much effort and carried too much risk. But if writing code is no longer the bottleneck, the main constraint becomes how quickly you can verify results. In general, ambition can be increased as long as there’s a way for Claude to verify correctness.

**Verification is how you earn confidence.** In math, we use a proof assistant to verify that each step of a proof Claude wrote is valid. For software, tests or [formal verification](https://www.anthropic.com/research/formal-verification) can help us gain similar confidence. But when these checks aren’t enough, a production system itself can also be a verifier.

**Carefully design the verification signal.** A verifier provides a signal that Claude can act on. We can calibrate this signal to show Claude where things went wrong. Where a proof assistant points to the failing step or a test names the failing case, a production system often offers no such signal by default. Much of our effort for this project went to building such a signal. In this case, checkpoints located each difference *in the code* and fingerprints helped *tell one bug from another*.

**Build loops that let Claude autonomously act on the signal.** Our inner loop was fast and ran locally in a sandbox. Agents tested hypotheses in seconds using requests they wrote themselves. The outer loop was slower and checked fixes on shadowed production traffic. The outermost loop was just prose, with corrections saved as rules in memory that could be read by every agent later in the process. Together, these loops allowed us to migrate the Messages API to Rust, which uses about 70% less CPU per request and reduces median time to first token by about 20% (Figure 15).

![Three charts of the move from Python to Rust. CPU used per request falls by about 70% and memory used per request by more than 80%, both from August to October. Median time to first token falls by about 20% between roughly September 7 and 21.](https://assets.claude.com/5991f46db78fd73fa00095ab708ffd1eaf240a76.png?w=3840&q=75&fm=webp&fit=max)

CPU and memory used per request, and median time to first token, as requests moved from Python (gray) to Rust (blue). Lines are seven-day averages, 100 is about the level just before the move, and each arrow shows the change from the first dot to the second. CPU is one region, memory is all of production, and time to first token is customers' Claude Code requests over a shorter period. In the third panel, the fall before the first dot came while almost all of those requests were still on Python.

**Keep the loops simple, so they scale with Claude’s capability.** We tried to put human judgment only into what counted as correct; otherwise we left it up to Claude how to get there. Agents chose which hypotheses to test, how to reproduce each bug, and how to fix it. The verifiers judged the result. Simple loops around strong verifiers allowed us to move productively over time (Figure 16).

![Bar chart of changes merged per two-week period, April 6 to September 7, 2026. Changes climb from under 100 to roughly 1,000 by late June, level off through July, then jump to more than 3,000 in the period starting August 10 and stay above 2,500 for the next two periods.](https://assets.claude.com/f3fe7bd0615da0366ab5c2f3181579ee7ca94647.png?w=3840&q=75&fm=webp&fit=max)

Changes merged to our API's Rust code in each two-week period, from April until public traffic moved to Rust in September 2026. Not all of them are migration work.

**Move toward outer loops.** At first, we had our engineers working inside the inner loop, running Claude and chasing differences themselves. Later, they moved to the seam between loops, helping to steer agents and reviewing fixes in Slack. But as the system matured, they increasingly moved to the edge, where they could provide the highest leverage, writing the rules and checks that agents worked within. As Claude grew more intelligent (and as we grew more intelligent at working with it), we evolved from directing Claude to Claude directing itself, relying on humans mainly for important judgment calls.

## Authors & acknowledgements

### Acknowledgements

Written by Lance Martin, Jake Eaton, Arvin Aminpour, Emma Webb, Bharat Mediratta, and Ravi Trivedi with editorial guidance and feedback from Caitlin Love.

See our Messages API docs [here](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).
