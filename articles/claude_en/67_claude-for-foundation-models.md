---
date: '2026-06-08'
final_url: https://claude.com/blog/claude-for-foundation-models
number: 67
selector_used: main
slug: claude-for-foundation-models
source_url: https://claude.com/blog/claude-for-foundation-models
title: Building intelligent apps for Apple platforms with Claude in the Foundation
  Models framework
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

# Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

Today we're releasing Foundation Models framework support for Claude through a new Swift package that lets Apple developers use Apple's Foundation Models framework to call Claude for more complex workflows.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a26f71ab79bc169ff9bdec4_8dfc12d1.png)

Apple’s Foundation Models framework gives developers access to tap into models natively from Swift. It is very easy to use and can return typed Swift values through guided generation in as few as three lines of code. Developers can use this to tap into Apple’s on-device models for fast, local tasks like summarization or extraction.

Developers can now use Apple’s Foundation Models framework to hand off to Claude when a request calls for multi-step reasoning, code generation, and more. Claude can also search the web for current information and execute code for data analysis. Stream Claude's response back into the same view.

Because Apple's framework returns typed Swift values from @Generable annotations, developers arrive at the Claude API call with clean inputs instead of raw user text.

## What this unlocks

The Foundation Models framework already powers a range of intelligent on-device features — journaling apps that surface personalized prompts, document apps that summarize contracts, learning apps that explain a concept at a student's level. Adding Claude extends each of those patterns.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a26f71ab79bc169ff9bdec1_7c4a5aaf.png)

A journaling app can generate daily prompts on-device, then asks Claude to find threads across months of entries. A study app can define a term on-device, then hands off to Claude when the student follows up with "why does this matter for everything else we've covered?"

It's one experience for the user, backed by the right model for each step.

## Getting started

Claude support with the Foundation Models framework will be available tomorrow and works through Apple's Foundation Models framework on iOS 27, iPadOS 27, macOS 27, and visionOS 27, and watch OS 27. Add it to your project, sign in with an Anthropic API key, and pass typed outputs from Apple's on-device pass into a Claude request — the package handles streaming, tool calls, and structured responses back into your SwiftUI view.
