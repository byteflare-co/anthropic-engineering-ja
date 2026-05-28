---
date: '2026-05-28'
final_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
number: 60
selector_used: main
slug: introducing-dynamic-workflows-in-claude-code
source_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
title: Introducing dynamic workflows in Claude Code
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

# Introducing dynamic workflows in Claude Code

Today we're introducing dynamic workflows in Claude Code, helping Claude take on the most challenging tasks end-to-end. Work you'd normally plan in quarters now finishes in days. Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

Some problems are too big for one pass by a single agent, especially in complex, legacy codebases: a bug hunt across an entire service, a migration that touches hundreds of files, a plan you want stress-tested from every angle before you commit to it. Dynamic workflows can handle all of these end-to-end.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186b2e070156fbb2df90ad_166befe7.png)

Dynamic workflows are available today in research preview in the Claude Code CLI, Desktop, and the VS code extension for Max, Team, and Enterprise (if admin enabled) plans, as well as on the Claude API, on Amazon Bedrock, Vertex AI, and Microsoft Foundry.

Note: Dynamic workflows can consume substantially more tokens than a typical Claude Code session, so we recommend starting on a scoped task to get a feel for usage in your work.

For the best experience, turn on auto mode when using dynamic workflows. From there, you have two ways to start a workflow:

1. Ask Claude to create a dynamic workflow directly (e.g.,  “Create a workflow”), or
2. Switch on a new Claude Code-specific setting called `ultracode`. This is accessible through the effort menu and it sets the effort level to xhigh, while letting Claude decide automatically when to use a workflow to handle your task.

## **Dynamic workflows in action**

Early access users and teams inside Anthropic have been using dynamic workflows for a wide range of use cases, including:

- **Codebase-wide bug hunts, profiler-guided optimization audits, and security audits:** Claude searches a service or repo in parallel, then runs independent verification on every finding so the report surfaces real issues. The same shape works for hardening passes:  auth checks, input validation, and unsafe patterns across an entire codebase.
- **Large migrations and modernization efforts:** Claude can handle framework swaps, API deprecations, language ports that span thousands of files end-to-end.**‍**
- **Critical work you need checked twice:** When the cost of a wrong answer is high, a workflow gives Claude independent attempts at the problem and adversarial agents working to break the result before you see it.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186eb7c527a0f35719a37b_Klarna-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186eb3a5f68864d977de69_Klarna-dark.svg)

“Dynamic workflows have been especially valuable for discovery and review tasks across large codebases. We’ve seen strong results using it to identify dead code and surface cleanup opportunities that traditional static analysis missed, helping our engineers move faster on maintenance and refactoring work.”

Alessio Vallero, Senior Engineering Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186fa3128d757bc62363f8_cyberagent-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186faafd2bd2ff345e25ec_cyberagent-dark.svg)

“Dynamic workflows fill the gap between firing off a single subagent and building out a full agent team. Plan to implementation just flows, so we can trust longer runs without losing visibility.”

Ken Takao, Lead Systems Engineer
