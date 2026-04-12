---
date: '2026-03-13'
final_url: https://claude.com/blog/1m-context-ga
number: 12
selector_used: main
slug: 1m-context-ga
source_url: https://claude.com/blog/1m-context-ga
title: 1M context is now generally available for Opus 4.6 and Sonnet 4.6
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

# 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Claude Opus 4.6 and Sonnet 4.6 now include the full 1M context window at standard pricing on the Claude Platform. Standard pricing applies across the full window — $5/$25 per million tokens for Opus 4.6 and $3/$15 for Sonnet 4.6. There's no multiplier: a 900K-token request is billed at the same per-token rate as a 9K one.

**What's new with general availability:**

- **One price, full context window.** No long-context premium.
- **Full rate limits at every context length.** Your standard account throughput applies across the entire window.
- **6x more media per request**. Up to 600 images or PDF pages, up from 100. Available today on Claude Platform natively, Microsoft Foundry, and Google Cloud’s Vertex AI.
- ​​**No beta header required.** Requests over 200K tokens work automatically. If you're already sending the beta header, it's ignored so no code changes are required.

**1M context is now included in Claude Code for Max, Team, and Enterprise users with Opus 4.6.** Opus 4.6 sessions can use the full 1M context window automatically, meaning fewer compactions and more of the conversation kept intact. 1M context previously required extra usage.

### **Long context that holds up**

A million tokens of context only matters if the model can recall the right details and reason across them. Opus 4.6 scores 78.3% on MRCR v2, the highest among frontier models at that context length.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b49c06e1c573f3ce50276b_image%20(3).png)

Claude Opus 4.6 and Sonnet 4.6 maintain accuracy across the full 1M window. Long context retrieval has improved with each model generation.

That means you can load an entire codebase, thousands of pages of contracts, or the full trace of a long-running agent — tool calls, observations, intermediate reasoning — and use it directly. The engineering work, lossy summarization, and context clearing that long-context work previously required are no longer needed. The full conversation stays intact.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

Scientific discovery requires reasoning across research literature, mathematical frameworks, databases, and simulation code simultaneously. Claude Opus 4.6’s 1M context and expanded media limits let our agentic systems synthesize hundreds of papers, proofs, and codebases in a single pass, helping us dramatically accelerate fundamental and applied physics research.

Dr. Alex Wissner-Gross, Co-Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d248b84e40f85eca3f68_GC%20AI%20220px%20navy%20(1).png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d24b433e03540b6f6bc5_GC%20AI%20220px%20(1).png)

With Claude's 1M context, an in-house lawyer can bring five turns of a 100-page partnership agreement into one session and finally see the full arc of a negotiation. No more toggling between versions or losing track of what changed three rounds ago.

Bardia Pourvakil, Co-founder and CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

Large-scale production systems have endless context, and production incidents can get very complex. With Claude's 1M context window, we are able to keep every entity, signal, and working theory in view from first alert to remediation without having to repeatedly compact or compromise the nuances of these systems.

Mayank Agarwal, Founder & CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016becf0259a067d4331fa_logo_hex-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016beff1534c67cafdc9b5_logo_hex-dark.svg)

We raised our Opus context window from 200k to 500k and the agent runs more efficiently — it actually uses fewer tokens overall. Less overhead, more focus on the goal at hand.

Izzy Miller, AI Research Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e72946ac912c35a42e8_Endex%20Combined%20Transparent.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b4b0ec5b32b9b274cbac47_Endex%20Combined%20Transparent%20White.svg)

Real-world spreadsheet tasks require deep research and complex multi-step plans. Claude's 1M context window let’s us maintain task adherence and attention to detail.

Tarun Amasa, CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

Claude Code can burn 100K+ tokens searching Datadog, Braintrust, databases, and source code. Then compaction kicks in. Details vanish. You're debugging in circles. With 1M context, I search, re-search, aggregate edge cases, and propose fixes — all in one window.

Anton Biryukov, Software Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e943b167e62bb019de7_Logo_green.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e9850d979b6157caf78_Logo_white.svg)

Before Opus 4.6's 1M context window, we had to compact context as soon as users loaded large PDFs, datasets, or images — losing fidelity on exactly the work that mattered most. We've seen a 15% decrease in compaction events. Now our agents hold it all and run for hours without forgetting what they read on page one.

Jon Bell, CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96fc452118ce3fff64d_Cognition_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96abcdb567698a5166a_Cognition_dark.svg)

Opus 4.6 with 1M context window made our Devin Review agent significantly more effective. Large diffs didn't fit in a 200K context window so the agent had to chunk context, leading to more passes and loss of cross-file dependencies. With 1M context, we feed the full diff and get higher-quality reviews out of a simpler, more token-efficient harness.

Adhyyan Sekhsaria, Founding Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b3147bbe3d3dd4357707fb_Logo%20-%20Black%20on%20Transparent%20Background.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31483fee3cafc3e1abc8b_Logo%20-%20White%20on%20Transparent%20Background.svg)

Eve defaults to 1M context because plaintiff attorneys' hardest problems demand it. Whether it's cross-referencing a 400-page deposition transcript or surfacing key connections across an entire case file, the expanded context window lets us deliver materially higher-quality answers than before.

Mauricio Wulfovich, ML Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

Scientific discovery requires reasoning across research literature, mathematical frameworks, databases, and simulation code simultaneously. Claude Opus 4.6’s 1M context and expanded media limits let our agentic systems synthesize hundreds of papers, proofs, and codebases in a single pass, helping us dramatically accelerate fundamental and applied physics research.

Dr. Alex Wissner-Gross, Co-Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d248b84e40f85eca3f68_GC%20AI%20220px%20navy%20(1).png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d24b433e03540b6f6bc5_GC%20AI%20220px%20(1).png)

With Claude's 1M context, an in-house lawyer can bring five turns of a 100-page partnership agreement into one session and finally see the full arc of a negotiation. No more toggling between versions or losing track of what changed three rounds ago.

Bardia Pourvakil, Co-founder and CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

Large-scale production systems have endless context, and production incidents can get very complex. With Claude's 1M context window, we are able to keep every entity, signal, and working theory in view from first alert to remediation without having to repeatedly compact or compromise the nuances of these systems.

Mayank Agarwal, Founder & CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016becf0259a067d4331fa_logo_hex-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016beff1534c67cafdc9b5_logo_hex-dark.svg)

We raised our Opus context window from 200k to 500k and the agent runs more efficiently — it actually uses fewer tokens overall. Less overhead, more focus on the goal at hand.

Izzy Miller, AI Research Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e72946ac912c35a42e8_Endex%20Combined%20Transparent.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b4b0ec5b32b9b274cbac47_Endex%20Combined%20Transparent%20White.svg)

Real-world spreadsheet tasks require deep research and complex multi-step plans. Claude's 1M context window let’s us maintain task adherence and attention to detail.

Tarun Amasa, CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

Claude Code can burn 100K+ tokens searching Datadog, Braintrust, databases, and source code. Then compaction kicks in. Details vanish. You're debugging in circles. With 1M context, I search, re-search, aggregate edge cases, and propose fixes — all in one window.

Anton Biryukov, Software Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e943b167e62bb019de7_Logo_green.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e9850d979b6157caf78_Logo_white.svg)

Before Opus 4.6's 1M context window, we had to compact context as soon as users loaded large PDFs, datasets, or images — losing fidelity on exactly the work that mattered most. We've seen a 15% decrease in compaction events. Now our agents hold it all and run for hours without forgetting what they read on page one.

Jon Bell, CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96fc452118ce3fff64d_Cognition_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96abcdb567698a5166a_Cognition_dark.svg)

Opus 4.6 with 1M context window made our Devin Review agent significantly more effective. Large diffs didn't fit in a 200K context window so the agent had to chunk context, leading to more passes and loss of cross-file dependencies. With 1M context, we feed the full diff and get higher-quality reviews out of a simpler, more token-efficient harness.

Adhyyan Sekhsaria, Founding Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b3147bbe3d3dd4357707fb_Logo%20-%20Black%20on%20Transparent%20Background.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31483fee3cafc3e1abc8b_Logo%20-%20White%20on%20Transparent%20Background.svg)

Eve defaults to 1M context because plaintiff attorneys' hardest problems demand it. Whether it's cross-referencing a 400-page deposition transcript or surfacing key connections across an entire case file, the expanded context window lets us deliver materially higher-quality answers than before.

Mauricio Wulfovich, ML Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

Scientific discovery requires reasoning across research literature, mathematical frameworks, databases, and simulation code simultaneously. Claude Opus 4.6’s 1M context and expanded media limits let our agentic systems synthesize hundreds of papers, proofs, and codebases in a single pass, helping us dramatically accelerate fundamental and applied physics research.

Dr. Alex Wissner-Gross, Co-Founder
