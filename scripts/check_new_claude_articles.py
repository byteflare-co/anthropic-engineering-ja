"""Claude ブログに新着記事があるかを確認する。

claude.com/blog は SPA なので Playwright で取得する。

使い方:
    uv run python scripts/check_new_claude_articles.py

出力:
    - 標準出力に JSON: {"new_articles": [...], "count": N, ...}
    - GitHub Actions 環境では `$GITHUB_OUTPUT` に `new_count` を書き出す。
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from claude_articles import CLAUDE_ARTICLES  # noqa: E402

INDEX_URL = "https://claude.com/blog"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Safari/537.36"
)
SLUG_RE = re.compile(r"^/blog/([^/?#]+)/?$")

EXCLUDED_PREFIXES = ("category/", "blog-category/")


def fetch_index_html() -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent=USER_AGENT, locale="en-US")
        page = context.new_page()
        page.goto(INDEX_URL, wait_until="domcontentloaded", timeout=30000)
        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            pass
        html = page.content()
        context.close()
        browser.close()
    return html


def _clean_title(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


HEADING_TAGS = ("h1", "h2", "h3", "h4")


def _title_from_anchor(a) -> str:
    for tag in HEADING_TAGS:
        heading = a.find(tag)
        if heading:
            text = heading.get_text(strip=True)
            if text:
                return _clean_title(text)
    return _clean_title(a.get_text(strip=True))


def _card_title_for_href(soup, href: str) -> str | None:
    """Find the card title for a given href by looking at the heading that
    DOM-precedes any anchor pointing to href (i.e. the title shown before
    the "Read more" link in the same card).
    """
    anchors = [a for a in soup.find_all("a", href=True) if a["href"] == href]
    best: str | None = None
    best_distance = 10**9
    for a in anchors:
        heading = a.find_previous(list(HEADING_TAGS))
        if heading is None:
            continue
        text = heading.get_text(strip=True)
        if not text or text.lower() in {"blog", "read more"}:
            continue
        # Use DOM position distance as proxy for "nearest"
        distance = sum(1 for _ in heading.next_elements) - sum(
            1 for _ in a.next_elements
        )
        if distance < best_distance:
            best = _clean_title(text)
            best_distance = distance
    return best


def extract_articles(html: str) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    candidates: dict[str, list[str]] = {}
    order: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("https://claude.com/blog/"):
            href = href.replace("https://claude.com", "")
        match = SLUG_RE.match(href)
        if not match:
            continue
        slug = match.group(1)
        if any(slug.startswith(p) for p in EXCLUDED_PREFIXES):
            continue
        title = _title_from_anchor(a)
        if not title or len(title) < 5:
            continue
        if slug not in candidates:
            candidates[slug] = []
            order.append(slug)
        candidates[slug].append(title)

    generic_titles = {"read more", "learn more", "continue reading"}

    found: list[dict[str, str]] = []
    for slug in order:
        texts = set(candidates[slug])
        specific = [t for t in texts if t.lower() not in generic_titles and t]
        if specific:
            title = max(specific, key=len)
        else:
            href = f"/blog/{slug}"
            card_title = _card_title_for_href(soup, href)
            if card_title:
                title = card_title
            else:
                title = max(texts, key=len) if texts else slug
        found.append(
            {
                "slug": slug,
                "title": title,
                "url": f"https://claude.com/blog/{slug}",
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
    existing_slugs = {a.slug for a in CLAUDE_ARTICLES}
    html = fetch_index_html()
    found = extract_articles(html)
    new = [a for a in found if a["slug"] not in existing_slugs]

    result = {
        "checked_url": INDEX_URL,
        "existing_count": len(CLAUDE_ARTICLES),
        "found_total": len(found),
        "count": len(new),
        "new_articles": new,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

    write_github_output(new)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
