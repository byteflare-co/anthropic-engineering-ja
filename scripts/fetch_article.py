"""Anthropic Engineering ブログ記事を取得し、英語 Markdown として保存する。

使い方:
    uv run python scripts/fetch_article.py --slug building-effective-agents
    uv run python scripts/fetch_article.py --all
    uv run python scripts/fetch_article.py --slug building-effective-agents --force

- Playwright で取得することで SSR/CSR 両対応・308 リダイレクトも自動追随。
- 本文は `<article>`, `<main>`, `role=main`, docs サイトの `.prose` など複数セレクタで抽出。
- 取得した HTML を markdownify で Markdown 化し、フロントマター付きで
  `articles/en/NN_slug.md` に保存する。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import frontmatter
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as md
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
EN_DIR = ROOT / "articles" / "en"

# 本文抽出セレクタ（先に一致したものを使用）
CONTENT_SELECTORS = [
    "article",
    "main article",
    ".mdx-content",  # code.claude.com/docs
    "#content",      # code.claude.com/docs fallback
    "main",
    '[role="main"]',
    "div.prose",
    "div.markdown",
]

# 本文から除外する要素
STRIP_SELECTORS = [
    "nav",
    "header",
    "footer",
    "aside",
    "script",
    "style",
    "noscript",
    "form",
    '[class*="subscribe" i]',
    '[class*="newsletter" i]',
    '[class*="share" i]',
    '[class*="social" i]',
    '[class*="breadcrumb" i]',
    '[aria-label*="breadcrumb" i]',
    "button",
]

sys.path.insert(0, str(Path(__file__).parent))
from articles import ARTICLES, ArticleMeta, find_by_slug  # noqa: E402


def extract_main(html: str) -> tuple[Tag, str]:
    """メイン記事本文を BeautifulSoup のタグとして返す。

    戻り値: (main_tag, used_selector)
    """
    soup = BeautifulSoup(html, "html.parser")
    for sel in CONTENT_SELECTORS:
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 500:
            return node, sel
    raise RuntimeError("本文要素が見つかりません")


def strip_noise(root: Tag) -> None:
    """ヘッダ/フッタ/購読ブロックなどを削除。"""
    for sel in STRIP_SELECTORS:
        for n in root.select(sel):
            n.decompose()


def normalize_markdown(text: str) -> str:
    """markdownify 出力を軽く整形する。"""
    # 連続空行を 2 行までに圧縮
    text = re.sub(r"\n{3,}", "\n\n", text)
    # 行末空白削除
    text = re.sub(r"[ \t]+\n", "\n", text)
    # 先頭/末尾の空白除去
    text = text.strip() + "\n"
    return text


def fetch_one(page, meta: ArticleMeta) -> str:
    """1 記事の Markdown 文字列を返す。フロントマター付き。"""
    print(f"[fetch] {meta.stem}: {meta.source_url}", file=sys.stderr)
    response = page.goto(meta.source_url, wait_until="domcontentloaded", timeout=60000)
    final_url = page.url
    if response is None:
        raise RuntimeError(f"no response for {meta.source_url}")
    if response.status >= 400:
        raise RuntimeError(f"HTTP {response.status} for {final_url}")

    # ネットワークが落ち着くまで軽く待つ
    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass

    html = page.content()
    main, used_sel = extract_main(html)
    strip_noise(main)

    # h1 は冒頭の見出しとして残す（markdownify が拾う）
    body_md = md(
        str(main),
        heading_style="ATX",
        bullets="-",
        code_language="",
        strip=["a"] if False else None,  # リンクは残す
    )
    body_md = normalize_markdown(body_md)

    post = frontmatter.Post(
        content=body_md,
        title=meta.title,
        date=meta.date,
        slug=meta.slug,
        number=meta.number,
        source_url=meta.source_url,
        final_url=final_url,
        selector_used=used_sel,
    )
    return frontmatter.dumps(post) + "\n"


def save(meta: ArticleMeta, content: str) -> Path:
    EN_DIR.mkdir(parents=True, exist_ok=True)
    out = EN_DIR / f"{meta.stem}.md"
    out.write_text(content, encoding="utf-8")
    return out


def run(targets: list[ArticleMeta], force: bool) -> int:
    failed: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/145.0.0.0 Safari/537.36"
            ),
            locale="en-US",
        )
        page = context.new_page()
        for meta in targets:
            out_path = EN_DIR / f"{meta.stem}.md"
            if out_path.exists() and not force:
                print(f"[skip] {meta.stem} (exists)", file=sys.stderr)
                continue
            try:
                content = fetch_one(page, meta)
                path = save(meta, content)
                print(f"[ok] {path}", file=sys.stderr)
            except Exception as e:
                print(f"[error] {meta.stem}: {e}", file=sys.stderr)
                failed.append(meta.slug)
        context.close()
        browser.close()
    if failed:
        print(f"\n失敗: {failed}", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--slug", help="対象スラッグ")
    g.add_argument("--all", action="store_true", help="全記事を取得")
    ap.add_argument("--force", action="store_true", help="既存ファイルがあっても上書き")
    args = ap.parse_args()

    if args.all:
        targets = list(ARTICLES)
    else:
        meta = find_by_slug(args.slug)
        if meta is None:
            print(f"unknown slug: {args.slug}", file=sys.stderr)
            return 2
        targets = [meta]

    return run(targets, force=args.force)


if __name__ == "__main__":
    raise SystemExit(main())
