---
date: '2026-08-06'
final_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
number: 108
selector_used: main
slug: run-claude-code-sessions-on-your-own-compute
source_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
title: Run Claude Code sessions on your own compute
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22651dd05046d0fdb0b_39c40393e610cc0a5e65f50ad12ff5ada273f792-1000x1000.svg)

# Run Claude Code sessions on your own compute

Now in public beta, self-hosted environments let you run Claude Code sessions on your own infrastructure. Start a session from the web, mobile, desktop, or a routine, and it runs inside your network, next to your internal services, toolchains, and security controls, rather than on Anthropic-hosted infrastructure.

For most enterprises, we strongly recommend our hosted offering for operational simplicity with no infrastructure to run or maintain. Self-hosted environments are for teams whose network, tooling, or compliance requirements call for keeping agent execution on infrastructure they control. If you go this route, plan to staff engineering to own setup and ongoing maintenance.

### **Why self-host**

We saw organizations in our preview program adopt self-hosted environments for a few key reasons:

- **Network access:** sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet
- **Customizability:** pre-install compilers, SDKs, and internal CLIs in your environment so every session starts ready to build
- **Compliance:** source code and build artifacts stay on infrastructure you control

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5b9_6a71ea6c8fc8ac632732466a_logo_faire-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5bd_6a71ea6c2122143c0b574194_logo_faire-dark.svg)

“Self-hosted environments let us integrate Claude Code into our existing development workflows while maintaining our security and operational controls. This setup means Claude can generate PRs, help fix CI issues, and respond to developer workflow events, with compute that can scale based on demand. Claude understands our codebase, making it a strong fit for how our engineering teams build.”

George Jacob, Senior Engineering Manager

### **Getting started**

Self-hosted environments are available in public beta to organizations on Claude Team and Enterprise plans. They are off by default and not available for organizations using ZDR.

Plan on a platform, developer experience, or developer productivity team owning setup and ongoing operation, including building and maintaining the runner image, updating runners, and running the orchestrator if you use on-demand mode.

See the [documentation](https://code.claude.com/docs/en/self-hosted-environments) to learn more. Share feedback via [GitHub](https://github.com/anthropics/claude-code/issues) or through your Anthropic account team.
