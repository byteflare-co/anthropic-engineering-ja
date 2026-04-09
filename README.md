# Anthropic Engineering ブログ 日本語版

Anthropic の [Engineering ブログ](https://www.anthropic.com/engineering) 全 22 記事を、
日本語の PDF 読み物として保存するためのツール・成果物置き場です。

## ディレクトリ構成

```
├── scripts/
│   ├── articles.py       # 22記事の目録（slug, title, date）
│   ├── fetch_article.py  # 記事を取得して英語 Markdown 化
│   ├── build_pdf.py      # 日本語 Markdown から書籍風 PDF 生成
│   ├── template.html     # HTML テンプレート（Jinja2）
│   └── style.css         # 印刷向け CSS（A4、游ゴシック）
├── articles/
│   ├── en/               # 英語原文 Markdown（fetch 結果）
│   └── ja/               # 日本語訳 Markdown（人手＋Claude 翻訳）
├── pdfs/                 # 最終成果物（22 PDF）
├── index.json            # 全記事のメタデータ目録
└── pyproject.toml
```

## セットアップ

```bash
uv sync
uv run playwright install chromium   # 初回のみ
```

## 使い方

### 記事を取得する（英語 Markdown）

```bash
# 単一記事
uv run python scripts/fetch_article.py --slug building-effective-agents

# 全記事（既存ファイルはスキップ）
uv run python scripts/fetch_article.py --all

# 上書きしたい場合
uv run python scripts/fetch_article.py --all --force
```

出力: `articles/en/NN_slug.md`

### PDF を生成する

`articles/ja/NN_slug.md`（日本語訳）を元に PDF を作ります。無ければ英語版を
フォールバックとして使います。

```bash
# 単一記事
uv run python scripts/build_pdf.py --slug building-effective-agents

# 全記事
uv run python scripts/build_pdf.py --all
```

出力: `pdfs/NN_slug.pdf`

### 記事を読む

```bash
# 1 本ずつ開く
open pdfs/02_building-effective-agents.pdf

# 一覧表示
ls pdfs/
```

## 記事一覧

番号順。日付は原文の公開日。

| # | slug | タイトル | 日付 |
|---|------|---------|------|
| 01 | contextual-retrieval | Introducing Contextual Retrieval | 2024-09-19 |
| 02 | building-effective-agents | Building effective agents | 2024-12-19 |
| 03 | swe-bench-sonnet | Raising the bar on SWE-bench Verified with Claude 3.5 Sonnet | 2025-01-06 |
| 04 | claude-think-tool | The "think" tool | 2025-03-20 |
| 05 | claude-code-best-practices | Claude Code: Best practices for agentic coding | 2025-04-18 |
| 06 | multi-agent-research-system | How we built our multi-agent research system | 2025-06-13 |
| 07 | desktop-extensions | Desktop Extensions | 2025-06-26 |
| 08 | writing-tools-for-agents | Writing effective tools for agents — with agents | 2025-09-11 |
| 09 | a-postmortem-of-three-recent-issues | A postmortem of three recent issues | 2025-09-17 |
| 10 | effective-context-engineering-for-ai-agents | Effective context engineering for AI agents | 2025-09-29 |
| 11 | claude-code-sandboxing | Beyond permission prompts: Claude Code sandboxing | 2025-10-20 |
| 12 | code-execution-with-mcp | Code execution with MCP | 2025-11-04 |
| 13 | advanced-tool-use | Introducing advanced tool use on the Claude Developer Platform | 2025-11-24 |
| 14 | effective-harnesses-for-long-running-agents | Effective harnesses for long-running agents | 2025-11-26 |
| 15 | demystifying-evals-for-ai-agents | Demystifying evals for AI agents | 2026-01-09 |
| 16 | AI-resistant-technical-evaluations | Designing AI-resistant technical evaluations | 2026-01-21 |
| 17 | building-c-compiler | Building a C compiler with a team of parallel Claudes | 2026-02-05 |
| 18 | eval-awareness-browsecomp | Eval awareness in Claude Opus 4.6's BrowseComp performance | 2026-03-06 |
| 19 | harness-design-long-running-apps | Harness design for long-running application development | 2026-03-24 |
| 20 | claude-code-auto-mode | Claude Code auto mode | 2026-03-25 |
| 21 | managed-agents | Scaling Managed Agents | - |
| 22 | infrastructure-noise | Quantifying infrastructure noise in agentic coding evals | - |

## 実装メモ

- 取得は Playwright + Chromium で、`www.anthropic.com/engineering/<slug>` から。
  記事 05（claude-code-best-practices）は `code.claude.com/docs/en/best-practices`
  にリダイレクトされるので、`.mdx-content` セレクタで本文を取っている。
- 本文抽出後は `markdownify` で Markdown 化、`python-frontmatter` でフロントマター付与。
- PDF 生成は Playwright を使った HTML → PDF。書籍風の余白・見出し階層・ページ番号
  を CSS の `@page` ルールで定義。和文フォントは **游ゴシック** をメイン、モノスペース
  は Menlo。
- Markdown の `<img>` に含まれる Next.js 画像 URL（`/_next/image?url=...`）は
  `build_pdf.py` で元 CDN の URL にデコードしてから埋め込む。
- ページヘッダには記事タイトル、フッタにはページ番号が出る。カバーページ（1 ページ目）
  はヘッダ・フッタを隠し、番号＋原題＋原文 URL を記載。

## 翻訳について

- 本文・見出し・箇条書きは日本語化。
- コードブロックは原文維持（コメントも原文のまま）。
- 固有名詞（Claude, MCP, Anthropic, Opus, Sonnet 等）は原文維持。
- 技術用語は初出時に（必要に応じて）原語併記。
- 翻訳はすべて Claude（機械翻訳）による。

## 本リポジトリの位置付け・著作権について

本リポジトリは Anthropic Engineering Blog の **非公式な個人的日本語訳** です。
Anthropic 社とは一切関係ありません。

- **原文の著作権は Anthropic PBC に帰属**します。翻訳は個人の学習・参照目的で
  作成したものであり、原著作権者の権利を主張・置き換えるものではありません。
- 翻訳はすべて Claude（機械翻訳）によるもので、正確性は保証しません。
  正確な内容は必ず[原文](https://www.anthropic.com/engineering) をご確認ください。
- 本コンテンツの再配布・商用利用を希望する場合は、Anthropic 側のポリシーに
  従ってください。翻訳部分についても上記原著作権の範囲内で扱う必要があります。
- 翻訳の誤りや原文の解釈について、本リポジトリは **Issue・Pull Request を
  受け付けていません**。指摘事項がある場合でも対応できない点をご了承ください。

明示的なオープンソースライセンス（MIT 等）は付与していません。原著作権者の
許諾なく翻訳物に自由なライセンスを付与することはできないためです。
