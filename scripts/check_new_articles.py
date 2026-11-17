"""Anthropic Engineering ブログに新着記事があるかを確認する。

ローカルでも GitHub Actions でも動かせるシンプルなチェッカ。Playwright は使わず
httpx + BeautifulSoup だけで完結する。

使い方:
    uv run python scripts/check_new_articles.py

出力:
    - 標準出力に JSON: {"new_articles": [...], "count": N, ...}
    - GitHub Actions 環境では `$GITHUB_OUTPUT` に `new_count` を書き出す。
    - 一覧から 1 本も抽出できないときは終了コード 1（サイト側の HTML 変更を
      成功扱いにしない）。それ以外は新着の有無に関わらず 0。
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
# 2026-11 時点で記事 URL は /engineering/<slug> から /research/<slug> へ
# 308 リダイレクトされている。一覧ページの href も /research/ になっている。
SLUG_RE = re.compile(r"^/(?:engineering|research)/([^/?#]+)/?$")

EXCLUDED_PREFIXES = ("team", "team/")


def fetch_index_html() -> str:
    with httpx.Client(
        headers={"User-Agent": USER_AGENT},
        follow_redirects=True,
        timeout=30,
    ) as client:
        response = client.get(INDEX_URL)
        response.raise_for_status()
        return response.text


def _clean_title(text: str) -> str:
    """候補テキストを正規化する。"Featured" プレフィックスと連続空白を除去。"""
    text = text.strip()
    # "Featured" カードでは先頭に "Featured" が結合されていることがある
    if text.startswith("Featured"):
        text = text[len("Featured"):].lstrip()
    # 連続する空白（改行含む）を 1 つにまとめる
    text = re.sub(r"\s+", " ", text)
    return text


def _title_from_anchor(a) -> str:
    """アンカー要素からクリーンなタイトルを取り出す。

    アンカーの内側に `<h1>` 〜 `<h4>` があればそれを優先する（Featured カード
    は 1 個の `<a>` に `<h2>` タイトル + 説明文が入っているため、見出しだけを
    使わないと説明まで拾ってしまう）。見出しが無ければアンカー全体のテキスト。
    """
    for tag in ("h1", "h2", "h3", "h4"):
        heading = a.find(tag)
        if heading:
            text = heading.get_text(strip=True)
            if text:
                return _clean_title(text)
    return _clean_title(a.get_text(strip=True))


def extract_articles(html: str) -> list[dict[str, str]]:
    """ブログ一覧ページから (slug, title, url) を抽出する。

    同じ slug に対して複数のアンカー（Featured カード + 通常カード）が
    存在することがあるので、slug ごとに候補タイトルを集めた上で最も短い
    （= 最もクリーンな）ものを選ぶ。
    """
    soup = BeautifulSoup(html, "html.parser")
    candidates: dict[str, list[str]] = {}
    urls: dict[str, str] = {}
    order: list[str] = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("https://www.anthropic.com"):
            href = href.replace("https://www.anthropic.com", "", 1)
        match = SLUG_RE.match(href)
        if not match:
            continue
        slug = match.group(1)
        if any(slug == p or slug.startswith(p) for p in EXCLUDED_PREFIXES):
            continue
        title = _title_from_anchor(a)
        if not title:
            continue
        if slug not in candidates:
            candidates[slug] = []
            order.append(slug)
            urls[slug] = f"https://www.anthropic.com{href}"
        elif href.startswith("/research/"):
            urls[slug] = f"https://www.anthropic.com{href}"
        candidates[slug].append(title)

    generic_titles = {"read more", "learn more", "continue reading"}
    found: list[dict[str, str]] = []
    for slug in order:
        texts = [t for t in set(candidates[slug]) if t.lower() not in generic_titles]
        if not texts:
            texts = list(set(candidates[slug]))
        texts = sorted(texts, key=len)
        found.append(
            {
                "slug": slug,
                "title": texts[0],
                "url": urls[slug],
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
    if not found:
        print(
            "error: extracted 0 articles from the engineering index; "
            "the page structure may have changed",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
