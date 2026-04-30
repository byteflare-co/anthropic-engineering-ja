---
date: '2026-04-30'
final_url: https://claude.com/blog/claude-security-public-beta
number: 35
selector_used: main
slug: claude-security-public-beta
source_url: https://claude.com/blog/claude-security-public-beta
title: Claude Security is now in public beta
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Claude Security is now in public beta

Claude Security is now available in public beta to Claude Enterprise customers.

AI cybersecurity capabilities are advancing fast. Today’s models are already highly effective at finding flaws in software code; the next generation will be more capable still, and will be particularly effective at autonomously *exploiting* these flaws. Now is the time for organizations to act to improve their security, preparing for a world in which working software exploits are much easier to discover.

Recently, we made Claude Mythos Preview—which can match or surpass even elite human experts at both finding and exploiting software vulnerabilities—available to a number of partners as part of [Project Glasswing.](https://www.anthropic.com/glasswing)

But our cybersecurity efforts go beyond Glasswing: with Claude Security, a much wider set of organizations can put our most powerful generally-available model, Claude Opus 4.7, to work across their codebases. Opus 4.7 is among the strongest models available for finding and patching software vulnerabilities, and for discovering complex, context-dependent issues that might otherwise be missed.

Claude Security—previously known as Claude Code Security—has already been tested by hundreds of organizations of all sizes in limited research preview, helping teams scan their codebases for vulnerabilities and generate targeted patches. Their feedback has shaped today’s release, which makes Claude Security available to all Enterprise customers. It comes with scheduled and targeted scans, easier integration with audit systems, and improved tracking of triaged findings. No API integration or custom agent build is required: if your organization uses Claude, you can start scanning today.

Opus 4.7’s capabilities are also being brought to cyber defenders through Claude’s integration into software tools that many enterprises already use. Our technology partners, including [CrowdStrike](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-puts-claude-opus-4-7-to-work-across-falcon-platform-project-quiltworks/), Microsoft Security, [Palo Alto Networks](https://www.paloaltonetworks.com/blog/2026/04/ai-driven-defense-anthropics-claude-opus/), SentinelOne, [TrendAI](https://newsroom.trendmicro.com/2026-04-30-TrendAI-TM-and-Anthropic-Advance-AI-Powered-Vulnerability-Detection-and-Risk-Mitigation-with-Claude-Opus-4-7), and [Wiz](https://www.wiz.io/blog/red-agent-claude-opus) are embedding Opus 4.7 into their tools; in addition, services partners like Accenture, BCG, Deloitte, Infosys and PwC are now helping organizations deploy Claude-integrated security solutions.

We are entering a pivotal time for cybersecurity. AI is compressing the timeline between vulnerability discovery and exploitation. We believe the right response is to make sure defenders have access to frontier capabilities in the ways most accessible to them, through Claude directly and through our partners.

## **How Claude Security works**

[Claude Security](https://youtu.be/0SgCiUfoYo8) can be accessed directly from the Claude.ai sidebar, or at [claude.ai/security](http://claude.ai/redirect/claudedotcom.v1.ec06f8c9-04ff-472c-b95a-05decd18f5eb/security). To begin, select one of your repositories (or scope to a specific directory or branch), then start a scan.

While scanning, Claude reasons about code much like a security researcher. Rather than finding vulnerabilities by searching for known patterns, Claude seeks to understand how components interact across files and modules, traces data flows, and reads the source code.

Once complete, Claude provides a detailed explanation of each of its findings, including its confidence that the vulnerability is real, how severe it is, its likely impact, and how it can be reproduced. It also generates instructions for a targeted patch, which users can open in Claude Code on the Web to work through the fix in context.

## **What we've learned since our initial preview**

Over the past two months, we’ve refined Claude Security in line with what we learned from its use in production across hundreds of enterprises. Specifically, we’ve seen that:

**Detection quality is paramount.** Teams have told us that high-confidence findings are what really accelerate security work. Claude Security's multi-stage validation pipeline independently examines each finding before it reaches an analyst, which drives down false positives, and Claude attaches a confidence rating to every result. This means that the signal that reaches the team is worth acting on.

**Time from scan to fix is the metric that matters.** Early users pointed to this consistently, with several teams going from scan to applied patch in a single sitting, instead of days of back-and-forth between security and engineering teams.

**Teams want ongoing coverage, not one-off audits.** We've added the option to schedule scans, so teams can set a regular cadence around reviewing and acting on findings.

With this release, we've also added the ability to target a scan at a particular directory within a repository, dismiss findings with documented reasons (so that future reviewers can trust prior triage decisions), export findings as CSV or Markdown for existing tracking and audit systems, and send scan results to Slack, Jira, or other tools via webhooks.

Here, organizations who’ve used Claude Security describe their experience:

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa585b66f744445eaec7_Doordash_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa5e900d8af5fd782dd2_Doordash_dark.svg)

“We are adapting our proactive security efforts through our Anthropic partnership. Claude Security helps us accelerate how we generate and secure new code at the scale and speed of DoorDash— it surfaces deep vulnerabilities accurately, and pipes findings right into our workflows so engineers can act on them in context.”

Suha Can, Vice President and Chief Security Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ada683bb0532fc4582a3_Snowflake_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5adab7a0103ed60805b38_Snowflake_dark.svg)

“Claude Security surfaced novel, high-quality findings during our early testing of the research preview that helped us identify and address potential security issues before they could affect our environment or our customers. We see strong potential as we expand its use.”

Krzysztof Katowicz-Kowalewski, Staff Product Security Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f37e9aa5aaf2be13e1fc87_column-logo-black.png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f38ff88ca62b8275c66f36_logo_column-dark-mode.png)

"Claude Security grasps the actual business logic behind our code. Our security team can now go from scan to fixes in a few clicks within our trusted tooling."

Greg Janowiak, Information Security Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f3877190da77141c92e1e5_684b70d717a5356f5a6f8793_yuno_wordmark_dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f390df66611aa841df95df_logo_yuno-dark-mode%20(1).svg)

"The scan quality is why we're working to plug Claude Security directly into our vulnerability management program—so real issues reach engineering faster, with less triage overhead in between."

Chiara La Valle, Head of Security

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f3a87453ecfe9d53a39_Hebbia-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f3d5a2f38a808068b47_Hebbia-dark-theme.svg)

"Given the increasing pace of vulnerability discovery, the strongest signal for us is how quickly a finding turns into a PR we can actually merge, not a ticket. We've used patches built with Claude Security to close real vulnerabilities in minutes, not days."

Matt Aromatorio, Head of Security
