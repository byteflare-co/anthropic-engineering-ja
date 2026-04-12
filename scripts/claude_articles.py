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
    ClaudeArticleMeta(2, "claude-code-on-the-web", "Claude Code on the web", "2025-10-20"),
    ClaudeArticleMeta(3, "building-ai-agents-in-financial-services", "Building AI agents for financial services", "2025-10-30"),
    ClaudeArticleMeta(4, "improving-frontend-design-through-skills", "Improving frontend design through Skills", "2025-11-12"),
    ClaudeArticleMeta(5, "how-enterprises-are-building-ai-agents-in-2026", "How enterprises are building AI agents in 2026", "2025-12-09"),
    ClaudeArticleMeta(6, "claude-builds-visuals", "Claude now creates interactive charts, diagrams and visualizations", "2026-03-12"),
    ClaudeArticleMeta(7, "harnessing-claudes-intelligence", "Harnessing Claude's intelligence", "2026-04-02"),
    ClaudeArticleMeta(8, "claude-managed-agents", "Claude Managed Agents: get to production 10x faster", "2026-04-08"),
]


def find_by_slug(slug: str) -> ClaudeArticleMeta | None:
    for a in CLAUDE_ARTICLES:
        if a.slug == slug:
            return a
    return None
