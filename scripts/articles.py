"""Anthropic Engineering ブログ記事の目録。

fetch_article.py / build_pdf.py から共有される。
番号順に並べる。番号は PDF の並び順でもある。
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ArticleMeta:
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
        return f"https://www.anthropic.com/engineering/{self.slug}"


ARTICLES: list[ArticleMeta] = [
    ArticleMeta(1, "contextual-retrieval", "Introducing Contextual Retrieval", "2024-09-19"),
    ArticleMeta(2, "building-effective-agents", "Building effective agents", "2024-12-19"),
    ArticleMeta(3, "swe-bench-sonnet", "Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet", "2025-01-06"),
    ArticleMeta(4, "claude-think-tool", 'The "think" tool: Enabling Claude to stop and think in complex tool use situations', "2025-03-20"),
    ArticleMeta(5, "claude-code-best-practices", "Claude Code: Best practices for agentic coding", "2025-04-18"),
    ArticleMeta(6, "multi-agent-research-system", "How we built our multi-agent research system", "2025-06-13"),
    ArticleMeta(7, "desktop-extensions", "Desktop Extensions: One-click MCP server installation for Claude Desktop", "2025-06-26"),
    ArticleMeta(8, "writing-tools-for-agents", "Writing effective tools for agents — with agents", "2025-09-11"),
    ArticleMeta(9, "a-postmortem-of-three-recent-issues", "A postmortem of three recent issues", "2025-09-17"),
    ArticleMeta(10, "effective-context-engineering-for-ai-agents", "Effective context engineering for AI agents", "2025-09-29"),
    ArticleMeta(11, "claude-code-sandboxing", "Beyond permission prompts: making Claude Code more secure and autonomous", "2025-10-20"),
    ArticleMeta(12, "code-execution-with-mcp", "Code execution with MCP: Building more efficient agents", "2025-11-04"),
    ArticleMeta(13, "advanced-tool-use", "Introducing advanced tool use on the Claude Developer Platform", "2025-11-24"),
    ArticleMeta(14, "effective-harnesses-for-long-running-agents", "Effective harnesses for long-running agents", "2025-11-26"),
    ArticleMeta(15, "demystifying-evals-for-ai-agents", "Demystifying evals for AI agents", "2026-01-09"),
    ArticleMeta(16, "AI-resistant-technical-evaluations", "Designing AI-resistant technical evaluations", "2026-01-21"),
    ArticleMeta(17, "building-c-compiler", "Building a C compiler with a team of parallel Claudes", "2026-02-05"),
    ArticleMeta(18, "eval-awareness-browsecomp", "Eval awareness in Claude Opus 4.6's BrowseComp performance", "2026-03-06"),
    ArticleMeta(19, "harness-design-long-running-apps", "Harness design for long-running application development", "2026-03-24"),
    ArticleMeta(20, "claude-code-auto-mode", "Claude Code auto mode: a safer way to skip permissions", "2026-03-25"),
    ArticleMeta(21, "managed-agents", "Scaling Managed Agents: Decoupling the brain from the hands", ""),
]


def find_by_slug(slug: str) -> ArticleMeta | None:
    for a in ARTICLES:
        if a.slug == slug:
            return a
    return None
