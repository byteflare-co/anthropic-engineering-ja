"""日本語訳 Markdown と HTML テンプレートから書籍風 PDF を生成する。

使い方:
    uv run python scripts/build_pdf.py --slug building-effective-agents
    uv run python scripts/build_pdf.py --all

articles/ja/NN_slug.md が存在しない場合は英語版（articles/en/NN_slug.md）を
フォールバックとして使う（翻訳前の動作確認用）。
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date as _date
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
EN_DIR = ROOT / "articles" / "en"
JA_DIR = ROOT / "articles" / "ja"
PDF_DIR = ROOT / "pdfs"

sys.path.insert(0, str(SCRIPTS))
from articles import ARTICLES, ArticleMeta, find_by_slug  # noqa: E402


def load_source(meta: ArticleMeta) -> tuple[frontmatter.Post, bool]:
    """ja を優先、なければ en にフォールバック。is_ja フラグを返す。"""
    ja_path = JA_DIR / f"{meta.stem}.md"
    en_path = EN_DIR / f"{meta.stem}.md"
    if ja_path.exists():
        return frontmatter.load(ja_path), True
    if en_path.exists():
        return frontmatter.load(en_path), False
    raise FileNotFoundError(f"No markdown for {meta.stem} (ja/en いずれも無し)")


_NEXT_IMAGE_RE = re.compile(r"(/_next/image\?[^)\s\"']+)")


def _decode_next_image(path: str) -> str:
    """/_next/image?url=<encoded>&w=...&q=... → 実際の CDN URL に戻す。"""
    try:
        q = parse_qs(urlparse(path).query)
        url = q.get("url", [None])[0]
        if url:
            return unquote(url)
    except Exception:
        pass
    return path


def _rewrite_next_images(md_text: str) -> str:
    def sub(match: re.Match[str]) -> str:
        return _decode_next_image(match.group(1))

    return _NEXT_IMAGE_RE.sub(sub, md_text)


def md_to_html(md_text: str) -> str:
    md_text = _rewrite_next_images(md_text)
    ext = [
        "extra",       # tables, fenced_code, footnotes, etc.
        "sane_lists",
        "toc",
    ]
    html = markdown.markdown(md_text, extensions=ext, output_format="html5")
    return html


def render_html(meta: ArticleMeta, post: frontmatter.Post, is_ja: bool) -> str:
    env = Environment(
        loader=FileSystemLoader(str(SCRIPTS)),
        autoescape=select_autoescape(enabled_extensions=("html",)),
    )
    tmpl = env.get_template("template.html")
    css = (SCRIPTS / "style.css").read_text(encoding="utf-8")

    body_html = md_to_html(post.content)

    # 日本語訳のタイトルは frontmatter の `title_ja` を優先、無ければ metadata 側
    title_ja = post.metadata.get("title_ja") or post.metadata.get("title") or meta.title

    return tmpl.render(
        title=title_ja,
        original_title=post.metadata.get("title") or meta.title,
        number=meta.number,
        date=post.metadata.get("date", meta.date),
        source_url=post.metadata.get("source_url", meta.source_url),
        build_date=_date.today().isoformat(),
        body=body_html,
        css=css,
        is_ja=is_ja,
    )


def html_to_pdf(html: str, out: Path) -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        # file:// にする必要はなく、set_content で十分だが、
        # 相対パスの画像等を解決するために BASE URL をセットできると尚良い。
        page.set_content(html, wait_until="networkidle")
        page.emulate_media(media="print")
        # カバーページの背景色など印刷用スタイルを出力するため
        out.parent.mkdir(parents=True, exist_ok=True)
        page.pdf(
            path=str(out),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        context.close()
        browser.close()


def build_one(meta: ArticleMeta) -> Path:
    post, is_ja = load_source(meta)
    html = render_html(meta, post, is_ja)
    out = PDF_DIR / f"{meta.stem}.pdf"
    html_to_pdf(html, out)
    flag = "ja" if is_ja else "en(fallback)"
    print(f"[pdf][{flag}] {out}", file=sys.stderr)
    return out


def run(targets: list[ArticleMeta]) -> int:
    failed: list[str] = []
    for m in targets:
        try:
            build_one(m)
        except Exception as e:
            print(f"[error] {m.stem}: {e}", file=sys.stderr)
            failed.append(m.slug)
    if failed:
        print(f"\n失敗: {failed}", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--slug")
    g.add_argument("--all", action="store_true")
    args = ap.parse_args()

    if args.all:
        targets = list(ARTICLES)
    else:
        meta = find_by_slug(args.slug)
        if meta is None:
            print(f"unknown slug: {args.slug}", file=sys.stderr)
            return 2
        targets = [meta]

    return run(targets)


if __name__ == "__main__":
    raise SystemExit(main())
