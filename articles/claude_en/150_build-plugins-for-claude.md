---
date: '2026-09-25'
final_url: https://claude.com/blog/build-plugins-for-claude
number: 150
selector_used: main
slug: build-plugins-for-claude
source_url: https://claude.com/blog/build-plugins-for-claude
title: Build plugins for Claude
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Build plugins for Claude

Every day, millions of people connect Claude to their apps, work tools, and data. Today, we're making it easier for developers to reach them.

Plugins package MCP connectors, Agent Skills, or both, and are the main way to build third-party extensions for Claude. Build a plugin, submit it through the new directory submission portal, and once approved, it's listed in the [Claude directory](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory).

## ‍**Submit and track plugins in the directory submission portal**

The [directory submission portal](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory/manage/new) is open to developers on paid Claude plans. There are two ways to submit and get your plugin published in the Claude directory:

- **Single MCP connector:** point to your remote MCP server.
- **Plugin bundle:** combine MCP servers and skills, host them on GitHub, and submit the repo. In Claude Code, plugins can also include LSPs, commands, hooks, and agents.

Whichever path you choose, the portal will guide you from submission to launch. You can:

- **Auto-validate your plugin.** Each submission is checked and safety-scanned as soon as you submit, so you catch issues early.
- **Review status and feedback.** See where your plugin is in the review process, results from the safety scan, and recommended changes.
- **Publish when you’re ready.** Once approved, you decide when to publish your plugin in Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab6a76f77cf7911a03be1bd_d852ff4a.png)

Stylized view of review status and recommended changes for a plugin. Data is illustrative.

## **Monitor and improve your plugin once it's published**

Once your plugin is live, usage analytics show installs by product surface and version, so you can prioritize fixes and features for your users. On the discovery side, you’ll see how often your listing is viewed and which searches lead people to it, so you can refine it to reach new users.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab6a76f77cf7911a03be1c0_ec09f8b2.png)

Stylized view of usage metrics for a published plugin. Data is illustrative.

## **Bring a rich experience to users with MCP 2.0 and its extensions**

Claude supports the latest MCP spec, commonly referred to as [MCP 2.0](https://modelcontextprotocol.io/specification/2026-07-28), which includes a stateless core. You can improve the experience of using your plugin with two [MCP extensions](https://modelcontextprotocol.io/extensions/overview): [MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/getting-started), for interactive UI inside chat, and [Enterprise Managed Auth](https://claude.com/docs/connectors/building/enterprise-managed-auth), for zero-touch OAuth for enterprise users. Support for more MCP features and extensions is coming soon.

## **Start building plugins for Claude**

Plugins are the main way for third-party developers to create extensions for Claude. Over the coming weeks, one discovery experience will roll out across Claude and Claude Code.

Skills and MCP connectors stay as building blocks, and the Claude directory will continue to list them. In the future, developers will be able to turn their connector listing into a plugin. If you have an existing skill, connector, or plugin on the Claude directory, you do not need to make any changes.

To get started with building plugins, read our docs for [how to build a plugin](https://claude.com/docs/build/overview) and submit your plugin [here](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory/manage/new).
