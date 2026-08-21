"""Claude ブログ記事の目録。

claude.com/blog からの取得対象。2026年3月以降の記事のみ。
fetch_claude_article.py / build_site.py から共有される。
番号は公開日昇順で割り当てる。
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ClaudeArticleMeta:
    number: int
    slug: str
    title: str
    date: str  # ISO 形式、未公表は空文字

    @property
    def stem(self) -> str:
        """ファイル名に使う接頭辞付きスラッグ。"""
        return f"{self.number:02d}_{self.slug}"

    @property
    def source_url(self) -> str:
        return f"https://claude.com/blog/{self.slug}"


CLAUDE_ARTICLES: list[ClaudeArticleMeta] = [
    ClaudeArticleMeta(1, "code-review", "Bringing Code Review to Claude Code", "2026-03-09"),
    ClaudeArticleMeta(2, "claude-builds-visuals", "Claude now creates interactive charts, diagrams and visualizations", "2026-03-12"),
    ClaudeArticleMeta(3, "1m-context-ga", "1M context is now generally available for Opus 4.6 and Sonnet 4.6", "2026-03-13"),
    ClaudeArticleMeta(4, "code-with-claude-san-francisco-london-tokyo", "Code with Claude comes to San Francisco, London, and Tokyo", "2026-03-18"),
    ClaudeArticleMeta(5, "product-management-on-the-ai-exponential", "Product management on the AI exponential", "2026-03-19"),
    ClaudeArticleMeta(6, "dispatch-and-computer-use", "Put Claude to work on your computer", "2026-03-23"),
    ClaudeArticleMeta(7, "auto-mode", "Auto mode for Claude Code", "2026-03-24"),
    ClaudeArticleMeta(8, "claude-platform-compliance-api", "Audit Claude Platform activity with the Compliance API", "2026-03-30"),
    ClaudeArticleMeta(9, "harnessing-claudes-intelligence", "Harnessing Claude's intelligence", "2026-04-02"),
    ClaudeArticleMeta(10, "subagents-in-claude-code", "How and when to use subagents in Claude Code", "2026-04-07"),
    ClaudeArticleMeta(11, "claude-managed-agents", "Claude Managed Agents: get to production 10x faster", "2026-04-08"),
    ClaudeArticleMeta(12, "carta-healthcare-clinical-abstractor", "How Carta Healthcare gets AI to reason like a clinical abstractor", "2026-04-08"),
    ClaudeArticleMeta(13, "the-advisor-strategy", "The advisor strategy: Give agents an intelligence boost", "2026-04-09"),
    ClaudeArticleMeta(14, "cowork-for-enterprise", "Making Claude Cowork ready for enterprise", "2026-04-09"),
    ClaudeArticleMeta(15, "preparing-your-security-program-for-ai-accelerated-offense", "Preparing your security program for AI-accelerated offense", "2026-04-10"),
    ClaudeArticleMeta(16, "seeing-like-an-agent", "Seeing like an agent: how we design tools in Claude Code", "2026-04-10"),
    ClaudeArticleMeta(17, "multi-agent-coordination-patterns", "Multi-agent coordination patterns: Five approaches and when to use them", "2026-04-10"),
    ClaudeArticleMeta(18, "using-claude-code-session-management-and-1m-context", "Using Claude Code: session management and 1M context", "2026-04-15"),
    ClaudeArticleMeta(19, "claude-code-desktop-redesign", "Redesigning Claude Code on desktop for parallel agents", "2026-04-14"),
    ClaudeArticleMeta(20, "introducing-routines-in-claude-code", "Introducing routines in Claude Code", "2026-04-14"),
    ClaudeArticleMeta(21, "how-enterprises-are-building-ai-agents-in-2026", "How enterprises are building AI agents in 2026", "2025-12-09"),
    ClaudeArticleMeta(22, "improving-frontend-design-through-skills", "Improving frontend design through Skills", "2025-11-12"),
    ClaudeArticleMeta(23, "building-ai-agents-in-financial-services", "Building AI agents for financial services", "2025-10-30"),
    ClaudeArticleMeta(24, "claude-code-on-the-web", "Claude Code on the web", "2025-10-20"),
    ClaudeArticleMeta(25, "claude-and-slack", "Claude and Slack", "2025-10-01"),
    ClaudeArticleMeta(26, "best-practices-for-using-claude-opus-4-7-with-claude-code", "Best practices for using Claude Opus 4.7 with Claude Code", "2026-04-16"),
    ClaudeArticleMeta(27, "meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon", "Meet the winners of our Built with Opus 4.6 Claude Code hackathon", "2026-04-20"),
    ClaudeArticleMeta(28, "building-agents-that-reach-production-systems-with-mcp", "Building agents that reach production systems with MCP", "2026-04-22"),
    ClaudeArticleMeta(29, "connectors-for-everyday-life", "New connectors in Claude for everyday life", "2026-04-23"),
    ClaudeArticleMeta(30, "claude-managed-agents-memory", "Built-in memory for Claude Managed Agents", "2026-04-23"),
    ClaudeArticleMeta(31, "onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development", "Onboarding Claude Code like a new developer: Lessons from 17 years of development", "2026-04-28"),
    ClaudeArticleMeta(32, "claude-api-skill", "Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp", "2026-04-29"),
    ClaudeArticleMeta(33, "product-development-in-the-agentic-era", "Product development in the agentic era", "2026-04-29"),
    ClaudeArticleMeta(34, "new-guide-deploying-claude-across-the-enterprise-with-claude-cowork", "Deploying Claude across the enterprise with Claude Cowork", "2026-04-29"),
    ClaudeArticleMeta(35, "claude-security-public-beta", "Claude Security is now in public beta", "2026-04-30"),
    ClaudeArticleMeta(36, "lessons-from-building-claude-code-prompt-caching-is-everything", "Lessons from building Claude Code: Prompt caching is everything", "2026-04-30"),
    ClaudeArticleMeta(37, "building-ai-agents-for-the-enterprise", "Building AI agents for the enterprise", "2026-04-30"),
    ClaudeArticleMeta(38, "how-kepler-built-verifiable-ai-for-financial-services-with-claude", "How Kepler built verifiable AI for financial services with Claude", "2026-04-30"),
    ClaudeArticleMeta(39, "how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks", "How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks", "2026-05-01"),
    ClaudeArticleMeta(40, "deploying-claude-across-financial-services", "Deploying Claude across financial services", "2026-05-05"),
    ClaudeArticleMeta(41, "new-in-claude-managed-agents", "New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration", "2026-05-06"),
    ClaudeArticleMeta(42, "collaborate-with-claude-across-excel-powerpoint-word-and-outlook", "Collaborate with Claude across Excel, PowerPoint, Word and Outlook", "2026-05-07"),
    ClaudeArticleMeta(43, "claude-platform-on-aws", "Introducing the Claude Platform on AWS", "2026-05-11"),
    ClaudeArticleMeta(44, "agent-view-in-claude-code", "Agent view in Claude Code", "2026-05-11"),
    ClaudeArticleMeta(45, "code-w-claude-sf-2026-sf", "Code w/ Claude SF 2026: Building on the AI exponential", "2026-05-12"),
    ClaudeArticleMeta(46, "how-anthropic-uses-claude-cybersecurity", "How Anthropic's cybersecurity team built a threat detection platform with Claude Code", "2026-05-12"),
    ClaudeArticleMeta(47, "how-claude-code-works-in-large-codebases-best-practices-and-where-to-start", "How Claude Code works in large codebases: Best practices and where to start", "2026-05-14"),
    ClaudeArticleMeta(48, "the-founders-playbook", "The founder's playbook: Building an AI-native startup", "2026-05-14"),
    ClaudeArticleMeta(49, "deploying-claude-across-the-legal-industry", "Deploying Claude across the legal industry", "2026-05-15"),
    ClaudeArticleMeta(50, "claude-managed-agents-updates", "New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels", "2026-05-19"),
    ClaudeArticleMeta(51, "using-claude-code-the-unreasonable-effectiveness-of-html", "Using Claude Code: The unreasonable effectiveness of HTML", "2026-05-20"),
    ClaudeArticleMeta(52, "how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book", "How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book", "2026-05-20"),
    ClaudeArticleMeta(53, "compliance-api-security-partners", "Claude now works with more security and compliance tools", "2026-05-21"),
    ClaudeArticleMeta(54, "how-our-partners-are-putting-opus-to-work-for-cybersecurity", "How our partners are putting Opus to work for cybersecurity", "2026-05-21"),
    ClaudeArticleMeta(55, "how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers", "How Anthropic's finance team uses Claude to shape the narrative behind the numbers", "2026-05-22"),
    ClaudeArticleMeta(56, "code-w-claude-london-2026-rethinking-how-we-build", "Code w/ Claude London 2026: Rethinking how we build", "2026-05-26"),
    ClaudeArticleMeta(57, "how-coderabbit-used-claude-to-build-an-agent-orchestration-system", "How CodeRabbit Used Claude to Build an Agent Orchestration System", "2026-05-27"),
    ClaudeArticleMeta(58, "using-llms-to-secure-source-code", "Using LLMs to secure source code", "2026-05-27"),
    ClaudeArticleMeta(59, "zero-trust-for-ai-agents", "Zero Trust for AI agents", "2026-05-27"),
    ClaudeArticleMeta(60, "introducing-dynamic-workflows-in-claude-code", "Introducing dynamic workflows in Claude Code", "2026-05-28"),
    ClaudeArticleMeta(61, "running-an-ai-native-engineering-org", "Running an AI-native engineering org", "2026-06-03"),
    ClaudeArticleMeta(62, "a-harness-for-every-task-dynamic-workflows-in-claude-code", "A harness for every task: dynamic workflows in Claude Code", "2026-06-02"),
    ClaudeArticleMeta(63, "lessons-from-building-claude-code-how-we-use-skills", "Lessons from building Claude Code: How we use skills", "2026-06-03"),
    ClaudeArticleMeta(64, "how-anthropic-enables-self-service-data-analytics-with-claude", "How Anthropic enables self-service data analytics with Claude", "2026-06-03"),
    ClaudeArticleMeta(65, "the-claude-cowork-product-guide", "The Claude Cowork product guide", "2026-06-05"),
    ClaudeArticleMeta(66, "how-anthropic-uses-claude-gtm-engineering", "How one Anthropic seller rebuilt his team's workflows with Claude Code", "2026-06-05"),
    ClaudeArticleMeta(67, "claude-for-foundation-models", "Building intelligent apps for Apple platforms with Claude in the Foundation Models framework", "2026-06-08"),
    ClaudeArticleMeta(68, "observability-for-developers-building-connectors", "Observability for developers building connectors", "2026-06-08"),
    ClaudeArticleMeta(69, "whats-new-in-claude-managed-agents", "New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults", "2026-06-09"),
    ClaudeArticleMeta(70, "building-with-claude-managed-agents", "The evolution of agentic surfaces: building with Claude Managed Agents", "2026-06-10"),
    ClaudeArticleMeta(71, "meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon", "Meet the winners of Built with Opus 4.7 Claude Code hackathon", "2026-06-15"),
    ClaudeArticleMeta(72, "meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon", "Meet the winners of our Claude Opus 4.8 Build Day hackathon", "2026-06-17"),
    ClaudeArticleMeta(73, "workload-identity-federation", "Secure access to the Claude Platform with Workload Identity Federation", "2026-06-17"),
    ClaudeArticleMeta(74, "steering-claude-code-skills-hooks-rules-subagents-and-more", "Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more", "2026-06-18"),
    ClaudeArticleMeta(75, "enterprise-managed-auth", "Centrally manage authorization for MCP connectors", "2026-06-18"),
    ClaudeArticleMeta(76, "artifacts-in-claude-code", "Claude Code now supports artifacts", "2026-06-18"),
    ClaudeArticleMeta(77, "the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry", "The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry", "2026-06-22"),
    ClaudeArticleMeta(78, "agent-identity-access-model", "Agent identity in Claude Tag: a new access model for autonomous, team-wide AI", "2026-06-24"),
    ClaudeArticleMeta(79, "building-effective-human-agent-teams", "Building effective human-agent teams", "2026-06-24"),
    ClaudeArticleMeta(80, "claude-in-microsoft-foundry", "Claude in Microsoft Foundry is now generally available", "2026-06-29"),
    ClaudeArticleMeta(81, "introducing-the-claude-apps-gateway", "Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud", "2026-06-29"),
    ClaudeArticleMeta(82, "getting-started-with-loops", "Getting started with loops", "2026-06-30"),
    ClaudeArticleMeta(83, "giving-admins-more-visibility-and-control-over-claude-usage-and-spend", "Giving admins more visibility and control over Claude spend", "2026-07-02"),
    ClaudeArticleMeta(84, "a-field-guide-to-claude-fable-finding-your-unknowns", "A Field Guide to Claude Fable: Finding Your Unknowns", "2026-07-06"),
    ClaudeArticleMeta(85, "bringing-claude-code-and-claude-cowork-to-government", "Bringing Claude Code and Claude Cowork to government", "2026-07-07"),
    ClaudeArticleMeta(86, "how-people-are-using-claude-cowork", "How people are using Claude Cowork", "2026-07-07"),
    ClaudeArticleMeta(87, "working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work", "Working at the frontier: How Thomson Reuters builds AI for high-stakes professional work", "2026-07-08"),
    ClaudeArticleMeta(88, "how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds", "How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds", "2026-07-08"),
    ClaudeArticleMeta(89, "working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night", "Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night", "2026-07-10"),
    ClaudeArticleMeta(90, "working-at-the-frontier-how-hebbia-builds-ai-for-financial-diligence-that-cant-miss-a-detail", "Working at the frontier: How Hebbia builds AI for financial diligence that can't miss a detail", "2026-07-13"),
    ClaudeArticleMeta(91, "working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work", "Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work", "2026-07-15"),
    ClaudeArticleMeta(92, "ai-code-migration", "How Anthropic runs large-scale code migrations with Claude Code", "2026-07-16"),
    ClaudeArticleMeta(93, "working-with-claude-fable-5-in-claude-cowork", "Working with Claude Fable 5 in Claude Cowork", "2026-07-16"),
    ClaudeArticleMeta(94, "ciso-guide-to-agentic-ai", "Zero risk isn't the job: a CISO's guide to agentic AI", "2026-07-17"),
    ClaudeArticleMeta(95, "working-at-the-frontier-rakuten", "Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5", "2026-07-20"),
    ClaudeArticleMeta(96, "how-anthropic-secures-its-ai-native-software-development-lifecycle", "How Anthropic Secures Its AI-Native Software Development Lifecycle", "2026-07-21"),
    ClaudeArticleMeta(97, "how-datadog-built-a-universal-machine-tool-for-claude-code", "How Datadog built a “universal machine tool” for Claude Code", "2026-07-21"),
    ClaudeArticleMeta(98, "building-verification-loops-in-claude-code-with-skills", "Building verification loops in Claude Code with skills", "2026-07-22"),
    ClaudeArticleMeta(99, "how-outtake-built-a-cyber-investigator-on-claude", "How Outtake built a cyber investigator on Claude", "2026-07-22"),
    ClaudeArticleMeta(100, "four-role-based-claude-certifications", "Four role-based certifications for the people who put Claude to work for customers", "2026-07-23"),
    ClaudeArticleMeta(101, "think-through-hard-problems-in-voice-mode", "Think through hard problems in voice mode", "2026-07-23"),
    ClaudeArticleMeta(102, "how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them", "How the product designer who built Claude Design uses it to explore ideas before building them", "2026-07-24"),
    ClaudeArticleMeta(103, "claude-models-explained-choosing-the-best-model-for-your-use-case", "Claude models explained: choosing the best model for your use case", "2026-07-24"),
    ClaudeArticleMeta(104, "bringing-mcp-2026-07-28-to-claude", "Bringing MCP 2026-07-28 to Claude", "2026-07-28"),
    ClaudeArticleMeta(105, "a-guide-to-cost-visibility-and-control-in-claude", "A guide to cost visibility and control in Claude", "2026-08-04"),
    ClaudeArticleMeta(106, "claude-enterprise-inference-hooks", "Inference hooks: inline data loss prevention for Claude Enterprise", "2026-08-05"),
    ClaudeArticleMeta(107, "millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude", "Millennium and Anthropic are building a digital risk analyst with Claude", "2026-08-06"),
    ClaudeArticleMeta(108, "run-claude-code-sessions-on-your-own-compute", "Run Claude Code sessions on your own compute", "2026-08-06"),
    ClaudeArticleMeta(109, "auto-mode-default-in-claude-code", "Auto mode is now the default in Claude Code for Pro, Max, and Team plans", "2026-08-07"),
    ClaudeArticleMeta(110, "auto-mode-in-production", "Running auto mode in production", "2026-08-07"),
    ClaudeArticleMeta(111, "how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale", "How Anthropic's business development team uses Claude to run inbound and outbound at scale", "2026-08-07"),
    ClaudeArticleMeta(112, "compliance-api-cowork-and-claude-code", "Compliance API coverage extends to Claude Cowork and Claude Code", "2026-08-11"),
    ClaudeArticleMeta(113, "cowork-chrome-side-panel", "The Claude in Chrome side panel is now Claude Cowork", "2026-08-12"),
    ClaudeArticleMeta(114, "claude-tag-now-reads-even-more-of-the-room", "Claude Tag now reads even more of the room", "2026-08-13"),
    ClaudeArticleMeta(115, "self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions", "Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions", "2026-08-13"),
    ClaudeArticleMeta(116, "how-jetbrains-evaluates-and-deploys-claude-fable-5", "Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5", "2026-08-13"),
    ClaudeArticleMeta(117, "maximizing-the-value-of-your-claude-code-sessions", "Maximizing the value of your Claude Code sessions", "2026-08-14"),
    ClaudeArticleMeta(118, "turning-conversation-into-knowledge-how-slack-builds-human-agent-teams", "Turning conversation into knowledge: how Slack builds human-agent teams", "2026-08-19"),
    ClaudeArticleMeta(119, "the-claude-science-product-guide", "The Claude Science product guide", "2026-08-18"),
    ClaudeArticleMeta(120, "anthropics-approach-to-teaching-and-learning-ai", "Anthropic's approach to teaching and learning AI", "2026-08-20"),
    ClaudeArticleMeta(121, "claude-code-guide-for-startups", "The Claude Code guide for startups", "2026-08-20"),
    ClaudeArticleMeta(122, "computer-use-skills-api-files-api", "Build production agents with computer use, the Skills API, and the Files API", "2026-08-20"),
]


def find_by_slug(slug: str) -> ClaudeArticleMeta | None:
    for a in CLAUDE_ARTICLES:
        if a.slug == slug:
            return a
    return None
