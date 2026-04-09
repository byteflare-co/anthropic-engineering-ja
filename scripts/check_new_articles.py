"""Anthropic Engineering ブログに新着記事があるかを確認する。

ローカルでも GitHub Actions でも動かせるシンプルなチェッカ。Playwright は使わず
httpx + BeautifulSoup だけで完結する。

使い方:
    uv run python scripts/check_new_articles.py

出力:
    - 標準出力に JSON: {"new_articles": [...], "count": N, ...}
    - GitHub Actions 環境では `$GITHUB_OUTPUT` に `new_count` を書き出す。
    - 終了コードは新着の有無に関わらず常に 0（CI 側で count を使って分岐する）。
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

import httpx
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from articles import ARTICLES  # noqa: E402

INDEX_URL = "https://www.anthropic.com/engineering"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Safari/537.36"
)
SLUG_RE = re.compile(r"^/engineering/([^/?#]+)/?$")


def fetch_index_html() -> str:
    with httpx.Client(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
        timeout=30,
    ) as client:
        response = client.get(INDEX_URL)
        response.raise_for_status()
        return response.text


def extract_articles(html: str) -> list[dict[str, str]]:
    """ブログ一覧ページから (slug, title, url) を抽出する。

    `<a href="/engineering/<slug>">` 形式のリンクを集め、初出順に返す。
    """
    soup = BeautifulSoup(html, "html.parser")
    found: list[dict[str, str]] = []
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        match = SLUG_RE.match(href)
        if not match:
            continue
        slug = match.group(1)
        if slug in seen:
            continue
        seen.add(slug)
        title = a.get_text(strip=True) or slug
        found.append(
            {
                "slug": slug,
                "title": title,
                "url": f"https://www.anthropic.com{href}",
            }
        )
    return found


def write_github_output(new_articles: list[dict[str, str]]) -> None:
    out_file = os.environ.get("GITHUB_OUTPUT")
    if not out_file:
        return
    with open(out_file, "a", encoding="utf-8") as f:
        f.write(f"new_count={len(new_articles)}\n")
        f.write("new_slugs=" + ",".join(a["slug"] for a in new_articles) + "\n")


def main() -> int:
    existing_slugs = {a.slug for a in ARTICLES}
    html = fetch_index_html()
    found = extract_articles(html)
    new = [a for a in found if a["slug"] not in existing_slugs]

    result = {
        "checked_url": INDEX_URL,
        "existing_count": len(ARTICLES),
        "found_total": len(found),
        "count": len(new),
        "new_articles": new,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

    write_github_output(new)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
