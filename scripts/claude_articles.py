"""Claude ブログ記事の目録。

claude.com/blog からの取得対象。2025年10月以降の記事のみ。
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
    ClaudeArticleMeta(1, "claude-and-slack", "Claude and Slack", "2025-10-01"),
    ClaudeArticleMeta(2, "skills", "Introducing Agent Skills", "2025-10-16"),
    ClaudeArticleMeta(3, "claude-code-on-the-web", "Claude Code on the web", "2025-10-20"),
    ClaudeArticleMeta(4, "building-ai-agents-in-financial-services", "Building AI agents for financial services", "2025-10-30"),
    ClaudeArticleMeta(5, "improving-frontend-design-through-skills", "Improving frontend design through Skills", "2025-11-12"),
    ClaudeArticleMeta(6, "how-enterprises-are-building-ai-agents-in-2026", "How enterprises are building AI agents in 2026", "2025-12-09"),
    ClaudeArticleMeta(7, "interactive-tools-in-claude", "Your favorite work tools are now interactive connectors inside Claude", "2026-01-26"),
    ClaudeArticleMeta(8, "cowork-plugins", "Customize Cowork with plugins", "2026-01-30"),
    ClaudeArticleMeta(9, "improved-web-search-with-dynamic-filtering", "Increase web search accuracy and efficiency with dynamic filtering", "2026-02-17"),
    ClaudeArticleMeta(10, "code-review", "Bringing Code Review to Claude Code", "2026-03-09"),
    ClaudeArticleMeta(11, "claude-builds-visuals", "Claude now creates interactive charts, diagrams and visualizations", "2026-03-12"),
    ClaudeArticleMeta(12, "1m-context-ga", "1M context is now generally available for Opus 4.6 and Sonnet 4.6", "2026-03-13"),
    ClaudeArticleMeta(13, "code-with-claude-san-francisco-london-tokyo", "Code with Claude comes to San Francisco, London, and Tokyo", "2026-03-18"),
    ClaudeArticleMeta(14, "auto-mode", "Auto mode for Claude Code", "2026-03-24"),
    ClaudeArticleMeta(15, "harnessing-claudes-intelligence", "Harnessing Claude's intelligence", "2026-04-02"),
    ClaudeArticleMeta(16, "claude-managed-agents", "Claude Managed Agents: get to production 10x faster", "2026-04-08"),
    ClaudeArticleMeta(17, "the-advisor-strategy", "The advisor strategy: Give agents an intelligence boost", "2026-04-09"),
    ClaudeArticleMeta(18, "cowork-for-enterprise", "Making Claude Cowork ready for enterprise", "2026-04-09"),
    ClaudeArticleMeta(19, "product-management-on-the-ai-exponential", "Product management on the AI exponential", "2026-03-19"),
    ClaudeArticleMeta(20, "dispatch-and-computer-use", "Put Claude to work on your computer", "2026-03-23"),
    ClaudeArticleMeta(21, "claude-platform-compliance-api", "Audit Claude Platform activity with the Compliance API", "2026-03-30"),
    ClaudeArticleMeta(22, "subagents-in-claude-code", "How and when to use subagents in Claude Code", "2026-04-07"),
    ClaudeArticleMeta(23, "carta-healthcare-clinical-abstractor", "How Carta Healthcare gets AI to reason like a clinical abstractor", "2026-04-08"),
    ClaudeArticleMeta(24, "preparing-your-security-program-for-ai-accelerated-offense", "Preparing your security program for AI-accelerated offense", "2026-04-10"),
    ClaudeArticleMeta(25, "seeing-like-an-agent", "Seeing like an agent: how we design tools in Claude Code", "2026-04-10"),
    ClaudeArticleMeta(26, "multi-agent-coordination-patterns", "Multi-agent coordination patterns: Five approaches and when to use them", "2026-04-10"),
]


def find_by_slug(slug: str) -> ClaudeArticleMeta | None:
    for a in CLAUDE_ARTICLES:
        if a.slug == slug:
            return a
    return None
