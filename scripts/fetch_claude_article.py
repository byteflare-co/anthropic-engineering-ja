"""Claude ブログ記事を取得し、英語 Markdown として保存する。

claude.com/blog は SPA で、記事本文は `article` または `main` 配下にレンダリングされる。
Playwright でレンダリング後に本文を取り出し、markdownify で Markdown 化する。

使い方:
    uv run python scripts/fetch_claude_article.py --slug claude-managed-agents
    uv run python scripts/fetch_claude_article.py --all
    uv run python scripts/fetch_claude_article.py --slug claude-managed-agents --force
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
EN_DIR = ROOT / "articles" / "claude_en"

CONTENT_SELECTORS = [
    "article",
    "main article",
    "main",
    '[role="main"]',
    "div.prose",
]

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
    '[class*="related" i]',
    '[class*="recommend" i]',
    'button',
]

sys.path.insert(0, str(Path(__file__).parent))
from _date_extract import extract_published_date  # noqa: E402
from claude_articles import CLAUDE_ARTICLES, ClaudeArticleMeta, find_by_slug  # noqa: E402


def extract_main(html: str) -> tuple[Tag, str]:
    soup = BeautifulSoup(html, "html.parser")
    for sel in CONTENT_SELECTORS:
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 500:
            return node, sel
    raise RuntimeError("本文要素が見つかりません")


def strip_noise(root: Tag) -> None:
    for sel in STRIP_SELECTORS:
        for n in root.select(sel):
            n.decompose()


def normalize_markdown(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = text.strip() + "\n"
    return text


def clean_claude_blog_markdown(md_text: str) -> str:
    """claude.com/blog の記事 Markdown からテンプレ由来のノイズを除去する。

    - 冒頭の Category/Product/Date/Reading time/Share ブロック
    - 末尾の "No items found." / Prev/Next / eBook / FAQ / CTA ブロック
    - 重複する証言カルーセル (同一画像ロゴを含むブロック)
    """
    lines = md_text.split("\n")

    # ---- 1) 冒頭のメタブロック除去 ---------------------------------
    # h1 の後、記事本文の前に Category/Product/Date/Reading time/Share の
    # テンプレメタが挟まる。さらに一部の記事ではサブタイトルが "word\n\nword" の
    # 形式でバラバラに入ることがあるので、h1 以降 "- Category" ブロックの末尾
    # (= share URL) までを丸ごと捨てる。
    h1_idx = -1
    for idx, line in enumerate(lines):
        if line.startswith("# ") and h1_idx == -1:
            h1_idx = idx
            break
    if h1_idx != -1:
        # "- Category" 行を探す
        cat_idx = -1
        for idx in range(h1_idx, len(lines)):
            if lines[idx].strip().startswith("- Category"):
                cat_idx = idx
                break
        if cat_idx != -1:
            # "- Category" から始まる箇条書きメタブロックの末尾を探す。
            # メタブロックは "- Category / - Product / - Date / - Reading time / - Share"
            # の 5 項目で、Share の中には URL 行まで含む。次の通常段落が来るまで
            # スキップする。最大 40 行で打ち切り。
            end = cat_idx
            for idx in range(cat_idx, min(cat_idx + 40, len(lines))):
                ln = lines[idx].strip()
                # share URL 行 (Copy link の下の生 URL) まで辿ったら次を見る
                if ln.startswith("https://claude.com/blog/"):
                    end = idx
                    break
            # URL 行が見つからなかった場合は、次の空行 + 通常テキストのペアを境界とする
            if end == cat_idx:
                for idx in range(cat_idx + 1, len(lines)):
                    if (
                        lines[idx].strip()
                        and not lines[idx].lstrip().startswith(("- ", "!["))
                        and not lines[idx].strip().startswith(("http", "[Copy"))
                        and len(lines[idx].strip()) > 40
                    ):
                        end = idx - 1
                        break
            lines = lines[: h1_idx + 1] + lines[end + 1 :]

    # ---- 2) 末尾のテンプレ除去 -------------------------------------
    # 以下のマーカーのうちいずれかが現れたら、そこ以降を切り捨てる。
    trailing_markers = [
        r"^\[Prev\]\(#\)\s*$",
        r"^## Transform how your organization operates with Claude\s*$",
        r"^Get the developer newsletter\s*$",
        r"^eBook\s*$",
    ]
    trailing_res = [re.compile(p) for p in trailing_markers]
    cut = len(lines)
    for idx, line in enumerate(lines):
        if any(r.match(line) for r in trailing_res):
            cut = idx
            break
    lines = lines[:cut]

    # ---- 3) "No items found." / FAQ 等のノイズ行除去 ---------------
    noise_lines = {
        "No items found.",
        "FAQ",
    }
    lines = [ln for ln in lines if ln.strip() not in noise_lines]

    # ---- 4) 証言カルーセルの重複除去 ------------------------------
    # 同じパラグラフ（30 文字以上の引用テキスト）が 2 回以上現れたら以降は捨てる。
    seen: set[str] = set()
    deduped: list[str] = []
    dup_block_started = False
    for ln in lines:
        stripped = ln.strip()
        if dup_block_started:
            continue
        # 引用文は "〜" や """ で始まることが多い
        if len(stripped) >= 60 and (stripped.startswith(("\u201c", '"', "“"))):
            key = stripped[:80]
            if key in seen:
                dup_block_started = True
                continue
            seen.add(key)
        deduped.append(ln)
    lines = deduped

    # 末尾の孤立した画像のみの行/空行は削除
    while lines and (
        not lines[-1].strip()
        or re.match(r"^!\[[^\]]*\]\([^)]+\)(\s*!\[[^\]]*\]\([^)]+\))*\s*$", lines[-1].strip())
    ):
        lines.pop()

    text = "\n".join(lines)
    # 連続空行を再圧縮
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def fetch_one(page, meta: ClaudeArticleMeta) -> str:
    print(f"[fetch] {meta.stem}: {meta.source_url}", file=sys.stderr)
    response = page.goto(meta.source_url, wait_until="domcontentloaded", timeout=60000)
    final_url = page.url
    if response is None:
        raise RuntimeError(f"no response for {meta.source_url}")
    if response.status >= 400:
        raise RuntimeError(f"HTTP {response.status} for {final_url}")

    try:
        page.wait_for_load_state("networkidle", timeout=10000)
    except Exception:
        pass

    html = page.content()
    main, used_sel = extract_main(html)
    published_date = extract_published_date(html) or meta.date
    if published_date != meta.date:
        print(
            f"[date] {meta.stem}: using {published_date} from HTML "
            f"(was {meta.date!r} in claude_articles.py)",
            file=sys.stderr,
        )
    strip_noise(main)

    body_md = md(
        str(main),
        heading_style="ATX",
        bullets="-",
        code_language="",
    )
    body_md = normalize_markdown(body_md)
    body_md = clean_claude_blog_markdown(body_md)

    post = frontmatter.Post(
        content=body_md,
        title=meta.title,
        date=published_date,
        slug=meta.slug,
        number=meta.number,
        source_url=meta.source_url,
        final_url=final_url,
        selector_used=used_sel,
    )
    return frontmatter.dumps(post) + "\n"


def save(meta: ClaudeArticleMeta, content: str) -> Path:
    EN_DIR.mkdir(parents=True, exist_ok=True)
    out = EN_DIR / f"{meta.stem}.md"
    out.write_text(content, encoding="utf-8")
    return out


def run(targets: list[ClaudeArticleMeta], force: bool) -> int:
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
        targets = list(CLAUDE_ARTICLES)
    else:
        meta = find_by_slug(args.slug)
        if meta is None:
            print(f"unknown slug: {args.slug}", file=sys.stderr)
            return 2
        targets = [meta]

    return run(targets, force=args.force)


if __name__ == "__main__":
    raise SystemExit(main())
