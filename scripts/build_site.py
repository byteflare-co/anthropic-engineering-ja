"""静的サイトをビルドする。

2 系統のブログを一括ビルドする。

- Anthropic Engineering ブログ (`articles/ja/*.md`) → `site/anthropic/`
- Claude ブログ (`articles/claude_ja/*.md`) → `site/claude/`
- トップランディング (`scripts/site_templates_landing/`) → `site/index.html`

GitHub Pages で公開することを想定。

使い方:
    uv run python scripts/build_site.py
    uv run python scripts/build_site.py --serve  # 簡易サーバで動作確認

出力:
    site/
    ├── index.html                             — ランディング (2 ブログ選択)
    ├── assets/landing.css
    ├── anthropic/
    │   ├── index.html                         — Anthropic 記事一覧
    │   ├── articles/NN_slug.html              — 各記事
    │   ├── pdfs/NN_slug.pdf                   — PDF
    │   └── assets/site.css
    └── claude/
        ├── index.html                         — Claude 記事一覧
        ├── articles/NN_slug.html              — 各記事
        └── assets/claude.css
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from datetime import date as _date
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
TEMPLATES_ANTHROPIC = SCRIPTS / "site_templates"
TEMPLATES_CLAUDE = SCRIPTS / "site_templates_claude"
TEMPLATES_LANDING = SCRIPTS / "site_templates_landing"
SITE = ROOT / "site"

sys.path.insert(0, str(SCRIPTS))
from articles import ARTICLES, ArticleMeta  # noqa: E402
from claude_articles import CLAUDE_ARTICLES, ClaudeArticleMeta  # noqa: E402


# ---- Markdown preprocessing --------------------------------------------

_NEXT_IMAGE_RE = re.compile(r"(/_next/image\?[^)\s\"']+)")


def _decode_next_image(path: str) -> str:
    """/_next/image?url=<encoded>&... → 実 CDN URL を取り出す。"""
    try:
        q = parse_qs(urlparse(path).query)
        url = q.get("url", [None])[0]
        if url:
            return unquote(url)
    except Exception:
        pass
    return path


def _rewrite_next_images(md_text: str) -> str:
    return _NEXT_IMAGE_RE.sub(lambda m: _decode_next_image(m.group(1)), md_text)


def _strip_leading_h1(md_text: str) -> str:
    """本文の先頭にある # 見出しを削除する（HTML 側で別途表示するため）。"""
    return re.sub(r"^#\s+[^\n]+\n+", "", md_text, count=1)


def _md_to_html(md_text: str) -> str:
    md_text = _rewrite_next_images(md_text)
    md_text = _strip_leading_h1(md_text)
    return markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists", "toc", "fenced_code"],
        output_format="html5",
    )


def _extract_summary(md_content: str, max_len: int = 180) -> str:
    """本文の先頭段落から要約を作る（リスト・見出し・画像は除外）。"""
    text = _strip_leading_h1(md_content)
    for raw_line in text.split("\n"):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith("![") or line.startswith("-") or line.startswith(">"):
            continue
        if line.startswith("```"):
            continue
        # inline markdown を剥がす
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"[*_`]", "", line)
        line = line.strip()
        if not line:
            continue
        if len(line) > max_len:
            return line[:max_len].rstrip() + "…"
        return line
    return ""


# ---- Article loading ----------------------------------------------------

def _load_article(meta: ArticleMeta) -> dict | None:
    ja_path = ROOT / "articles" / "ja" / f"{meta.stem}.md"
    if not ja_path.exists():
        return None
    post = frontmatter.load(ja_path)
    title_ja = post.metadata.get("title_ja") or meta.title
    date = post.metadata.get("date") or meta.date or ""
    return {
        "number": meta.number,
        "slug": meta.slug,
        "stem": meta.stem,
        "title": meta.title,
        "title_ja": title_ja,
        "date": str(date),
        "source_url": meta.source_url,
        "summary": _extract_summary(post.content),
        "body_html": _md_to_html(post.content),
    }


def _load_claude_article(meta: ClaudeArticleMeta) -> dict | None:
    ja_path = ROOT / "articles" / "claude_ja" / f"{meta.stem}.md"
    if not ja_path.exists():
        return None
    post = frontmatter.load(ja_path)
    title_ja = post.metadata.get("title_ja") or meta.title
    date = post.metadata.get("date") or meta.date or ""
    return {
        "number": meta.number,
        "slug": meta.slug,
        "stem": meta.stem,
        "title": meta.title,
        "title_ja": title_ja,
        "date": str(date),
        "source_url": meta.source_url,
        "summary": _extract_summary(post.content),
        "body_html": _md_to_html(post.content),
    }


# ---- Site build ---------------------------------------------------------

def _sort_key(article: dict) -> tuple:
    """日付降順でソートするためのキー。

    - 日付がある記事は日付文字列（ISO 形式）で降順比較。
    - 日付が無い記事（articles.py に日付未登録 = 新着）は「最新」扱いとして
      先頭に来るよう、ダミーの '9999' を使う。
    - 同じ日付同士では article.number（連番）で tiebreak し、大きい番号を前に。
    """
    return (article["date"] or "9999", article["number"])


def _build_anthropic(env: Environment, build_date: str) -> int:
    """Anthropic Engineering ブログを site/anthropic/ にビルドする。"""
    out_dir = SITE / "anthropic"
    (out_dir / "articles").mkdir(parents=True)
    (out_dir / "pdfs").mkdir(parents=True)
    (out_dir / "assets").mkdir(parents=True)

    loaded: list[dict] = []
    for meta in ARTICLES:
        article = _load_article(meta)
        if article is None:
            print(f"[skip] no ja md (anthropic): {meta.stem}", file=sys.stderr)
            continue
        loaded.append(article)
    loaded.sort(key=_sort_key, reverse=True)

    featured = loaded[0] if loaded else None
    others = loaded[1:]
    total_pages = _count_pdf_pages()

    index_tmpl = env.get_template("index.html")
    (out_dir / "index.html").write_text(
        index_tmpl.render(
            prefix="",
            site_root_prefix="../",
            featured=featured,
            others=others,
            total=len(loaded),
            total_pages=total_pages,
            build_date=build_date,
        ),
        encoding="utf-8",
    )

    article_tmpl = env.get_template("article.html")
    for i, article in enumerate(loaded):
        prev_article = loaded[i + 1] if i + 1 < len(loaded) else None
        next_article = loaded[i - 1] if i - 1 >= 0 else None
        out = out_dir / "articles" / f"{article['stem']}.html"
        out.write_text(
            article_tmpl.render(
                prefix="../",
                site_root_prefix="../../",
                article=article,
                prev_article=prev_article,
                next_article=next_article,
                build_date=build_date,
            ),
            encoding="utf-8",
        )

    shutil.copy(TEMPLATES_ANTHROPIC / "site.css", out_dir / "assets" / "site.css")

    src_pdfs = ROOT / "pdfs"
    for pdf in sorted(src_pdfs.glob("*.pdf")):
        shutil.copy(pdf, out_dir / "pdfs" / pdf.name)

    print(f"✓ built {len(loaded)} anthropic articles to {out_dir}")
    return len(loaded)


def _build_claude(env: Environment, build_date: str) -> int:
    """Claude ブログを site/claude/ にビルドする。"""
    out_dir = SITE / "claude"
    (out_dir / "articles").mkdir(parents=True)
    (out_dir / "assets").mkdir(parents=True)

    loaded: list[dict] = []
    for meta in CLAUDE_ARTICLES:
        article = _load_claude_article(meta)
        if article is None:
            print(f"[skip] no ja md (claude): {meta.stem}", file=sys.stderr)
            continue
        loaded.append(article)
    loaded.sort(key=_sort_key, reverse=True)

    featured = loaded[0] if loaded else None
    others = loaded[1:]

    index_tmpl = env.get_template("index.html")
    (out_dir / "index.html").write_text(
        index_tmpl.render(
            prefix="",
            site_root_prefix="../",
            featured=featured,
            others=others,
            total=len(loaded),
            build_date=build_date,
        ),
        encoding="utf-8",
    )

    article_tmpl = env.get_template("article.html")
    for i, article in enumerate(loaded):
        prev_article = loaded[i + 1] if i + 1 < len(loaded) else None
        next_article = loaded[i - 1] if i - 1 >= 0 else None
        out = out_dir / "articles" / f"{article['stem']}.html"
        out.write_text(
            article_tmpl.render(
                prefix="../",
                site_root_prefix="../../",
                article=article,
                prev_article=prev_article,
                next_article=next_article,
                build_date=build_date,
            ),
            encoding="utf-8",
        )

    shutil.copy(TEMPLATES_CLAUDE / "claude.css", out_dir / "assets" / "claude.css")

    print(f"✓ built {len(loaded)} claude articles to {out_dir}")
    return len(loaded)


def _build_landing(anthropic_total: int, claude_total: int) -> None:
    """ルートに 2 ブログ選択用のランディングページを配置する。"""
    (SITE / "assets").mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_LANDING)),
        autoescape=select_autoescape(),
    )
    tmpl = env.get_template("index.html")
    (SITE / "index.html").write_text(
        tmpl.render(
            anthropic_total=anthropic_total,
            claude_total=claude_total,
        ),
        encoding="utf-8",
    )
    shutil.copy(TEMPLATES_LANDING / "landing.css", SITE / "assets" / "landing.css")
    print(f"✓ built landing page to {SITE / 'index.html'}")


def build() -> Path:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    build_date = _date.today().isoformat()

    anthropic_env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_ANTHROPIC)),
        autoescape=select_autoescape(),
    )
    claude_env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_CLAUDE)),
        autoescape=select_autoescape(),
    )

    anthropic_total = _build_anthropic(anthropic_env, build_date)
    claude_total = _build_claude(claude_env, build_date)
    _build_landing(anthropic_total, claude_total)

    # .nojekyll: GitHub Pages に Jekyll 処理を抑制させる（_ で始まるファイル保護など）
    (SITE / ".nojekyll").write_text("")

    total_pdfs = len(list((SITE / "anthropic" / "pdfs").glob("*.pdf")))
    print()
    print(f"✓ built site to {SITE}")
    print(f"  - landing: 1")
    print(f"  - anthropic articles: {anthropic_total}")
    print(f"  - claude articles: {claude_total}")
    print(f"  - PDFs: {total_pdfs}")
    return SITE


def _count_pdf_pages() -> int:
    """index.json の pdf_size_bytes があるのでそれを使っても良いが、
    代わりに pypdf で集計する。失敗したら既定値。"""
    try:
        from pypdf import PdfReader
    except ImportError:
        return 0
    total = 0
    for pdf in (ROOT / "pdfs").glob("*.pdf"):
        try:
            total += len(PdfReader(str(pdf)).pages)
        except Exception:
            pass
    return total


def serve(port: int = 8000) -> None:
    import http.server
    import socketserver
    import os
    os.chdir(SITE)
    with socketserver.TCPServer(("127.0.0.1", port), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"serving {SITE} at http://127.0.0.1:{port}")
        httpd.serve_forever()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="ビルド後に簡易 HTTP サーバで公開")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()
    build()
    if args.serve:
        serve(args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
