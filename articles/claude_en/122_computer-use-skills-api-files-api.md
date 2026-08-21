---
date: '2026-08-20'
final_url: https://claude.com/blog/computer-use-skills-api-files-api
number: 122
selector_used: main
slug: computer-use-skills-api-files-api
source_url: https://claude.com/blog/computer-use-skills-api-files-api
title: Build production agents with computer use, the Skills API, and the Files API
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Build production agents with computer use, the Skills API, and the Files API

Computer use, the Skills API, and the Files API are generally available on the Claude Platform today. Computer use also adds a new browser use tool for agents that work in web applications. Together they let you build agents that operate software, apply your team's expertise, and return finished files.

### **Building agents on the Claude Platform**

**Computer use** lets you build agents that operate software they can see. Given a screenshot, the agent clicks, types, and scrolls the way someone at the keyboard would. That lets it work in applications that were never built for automation. The new **browser use tool** extends this to the web. Alongside the screenshot, the agent reads the structure of the page and acts on a specific field or button rather than a position on screen.

The **Skills API** and the **Files API** let you give that agent your expertise and your documents. A skill is a folder of instructions, scripts, and templates that Claude loads only when a task calls for it. With the **Skills API** you upload and version your own skills, then attach them to any request. They run in Claude's code execution sandbox, so there is nothing for you to host. The **Files API** is storage for the documents an agent reads and writes: upload a PDF or spreadsheet once, reference it by ID in later requests instead of re-sending it, and download the files the agent creates.

Say you're building a claims agent. It reads the intake document from the Files API, follows a skill that encodes the team's filing procedure, completes the submission in an insurer's web portal with the browser use tool, and saves the confirmation back as a file. Code execution and web search, already generally available, fit into the same loop.

### **What's new with general availability**

- **Computer use:** the updated computer use tool lets Claude take several actions per turn instead of one per model call, so tasks finish in fewer calls and less time. Computer use is also now eligible for HIPAA-regulated workloads under our BAA.
- **Browser use tool:** new in computer use today. It uses the same multi-action turns and adds page structure, so agents target web elements more reliably than with pixels alone.
- **Skills API:** a simpler API for uploading and versioning your own skills.
- **Files API:** automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d86b69e80750cfefc646_Asteroid_Logo_Black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d83ff9fbb0abe47899c7_Asteroid_Logo_White.svg)

"Our agents work inside healthcare and insurance systems that have no API. On the new computer use tool, our longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow we tested, and completion hit 100%, with no changes to our prompts."

Davide Locatelli, Research Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

"The Skills API gave us a straightforward way to build specialized document creation into Box Agent. For a bank, a skill captures the firm's credit methodology and approved memo format; Box Agent applies it to the financial statements and deal documents already in Box and produces a source-grounded credit memo for analyst review. Banks get agents for complex workflows without building each one from scratch."

Matthew Midson, Managing Director of Banking
