---
date: '2026-05-19'
final_url: https://claude.com/blog/claude-managed-agents-updates
number: 50
selector_used: main
slug: claude-managed-agents-updates
source_url: https://claude.com/blog/claude-managed-agents-updates
title: 'New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels'
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Starting today, Claude Managed Agents can operate in a sandbox you control and connect to your private Model Context Protocol (MCP) servers. Both the sandbox where an agent executes tools and the services it reaches run within the established boundaries of your enterprise, under your security and runtime controls.

The sandbox runs on your own infrastructure, or with managed providers like [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox/tree/main), or [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox) to handle the compute and isolation for you.

On the Claude Platform, [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) is available in public beta and MCP tunnels in research preview ([request access](https://claude.com/form/claude-managed-agents)).

## **Keep agent execution within your perimeter**

With self-hosted sandboxes, you keep sensitive files, packages, and services in your own infrastructure or with a managed sandbox provider. The [agent loop](https://www.anthropic.com/engineering/managed-agents) that handles orchestration, context management, and error recovery stays on Anthropic’s infrastructure, while tool execution moves to your own configured environment.

Inside your perimeter, network policies, audit logging, and security tooling are already in place, and files and repositories don't leave. You also control the compute: resource sizing and the runtime image are set on your side, so agents running compute-heavy work such as long builds or image generation get the CPU, memory, and capacity the task needs.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b4fa5fbae3bdfc63be57c_Sandboxes.png)

## **Choose your sandbox client**

Bring any sandbox client you want, or start with one of our supported providers:

- [**Cloudflare**](https://developers.cloudflare.com/sandbox/claude-managed-agents/) runs sandboxes at scale using microVMs and lighter weight isolates. Outbound network requests are in your control with zero-trust secrets injection, customizable proxies to audit, reroute, or modify egress, and the ability to connect to internal services over Cloudflare's network. [**Amplitude**](https://amplitude.com/) is building Design Agent, an internal tool for on-brand mockups and design critiques, on Managed Agents and Cloudflare for tighter observability and control.
- [**Daytona**](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents) sandboxes are full composable computers, long-running and stateful. The same primitive runs a quick burst or an agent that works for hours. The sandbox stays accessible while a session runs over SSH or an authenticated preview URL, or can be paused and restored with full state preserved. [**Clay’s**](http://clay.com/)GTM engineering agent, Sculptor, builds, tests, and monitors workflows autonomously on Managed Agents and Daytona.
- [**Modal**](https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes) is a cloud platform built for AI workloads, where sandboxes share the same foundation as Modal's functions, storage, and networking primitives, giving you everything you need to build production AI systems. Modal's custom container runtime delivers fast startup on any image, scales to hundreds of thousands of concurrent sandboxes, and gives you CPU and GPU resources on demand.
- [**Vercel**](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox)sandboxes combine VM security, VPC peering, and bring your own cloud with millisecond startup time. Managed Agents handles the model, tools, and session state, while the Vercel Sandbox firewall injects credentials at the network boundary so they never enter the sandbox. [**Rogo**](https://rogo.ai/), an AI platform for institutional finance, is building an analyst agent on Managed Agents and Vercel Sandbox to handle their proprietary data securely.

## **Connect to services within your private network**

With [MCP tunnels](http://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview), your agents reach MCP servers inside your private network without exposing them to the public internet. Internal databases, private APIs, knowledge bases, and ticketing systems become tools your agents can call. A lightweight gateway you deploy makes a single outbound connection, no inbound firewall rules, no public endpoints, and traffic encrypted end to end.

MCP tunnels is supported in Managed Agents and the Messages API. MCP tunnels is managed from workspace settings within the [Claude Console](https://platform.claude.com/) by organization admins.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b4fdc9749bb31acafa95b_MCP%20tunnel%20(1).png)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69010941df4d50c5b91b2ba1_Clay-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69010943d7b5a7bb5f07d8d6_Clay-dark-theme.svg)

“When building Sculptor, Clay's GTM engineering agent for building and testing GTM workflows autonomously, we wanted to give it a more flexible and powerful way to take actions than just tools in a loop. Claude Managed Agents let us replicate the power of a local agent with the reliability, versioning, and background execution of a cloud agent. And running it with our sandboxes, like Daytona, gives us control over the filesystem, so we can mount external file stores and install packages on the fly.”

Ryan Chang, AI Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699dfac701ab4fcb02c3d870_rogo-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699dfacb9075a218012e1f11_rogo-dark.svg)

“Claude Managed Agents handles the agent loop, Vercel's sandboxes give us an environment we can configure for our workloads. This gives us the option to leverage best-in-class infrastructure while we focus on what compounds for a financial AI platform: depth and breadth of tools and data, and a product surface built for how investors and bankers actually work.”

Strib Walker, Head of Product

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15dc2d99d53c20667cf5_mason-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15e9d43b72bc8726b778_mason-dark.svg)

“Our use cases require secure orchestration of internal tools across a complex product surface. Modal's sandbox gives us the security boundary our enterprise customers need, and combining it with Claude Managed Agents gives us a powerful harness without hand-rolling extra complexity. We had a working version up in under a week, raising reliability for our customers.”

Sai Yandapalli, CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f90d548130a5b392eef2bb_logo_amplitude-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f90d57fa27a4ce120cdf71_logo_amplitude-dark.svg)

“Claude Managed Agents and Cloudflare let us get the first useful version of our design agent running in two days on infrastructure we already know and trust.”

Will Newton, Design

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa585b66f744445eaec7_Doordash_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa5e900d8af5fd782dd2_Doordash_dark.svg)

“As we scale agentic commerce for local businesses, we need a highly efficient path to production with full harness control, scale, and reliability. We're excited to evaluate Claude Managed Agents for this next step, building on our Al infrastructure with Modal!”

Andy Fang, Co-founder
