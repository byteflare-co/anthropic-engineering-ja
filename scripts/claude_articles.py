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
]


def find_by_slug(slug: str) -> ClaudeArticleMeta | None:
    for a in CLAUDE_ARTICLES:
        if a.slug == slug:
            return a
    return None
