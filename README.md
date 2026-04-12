# Anthropic / Claude ブログ 日本語版

Anthropic の [Engineering ブログ](https://www.anthropic.com/engineering) と
[Claude ブログ](https://claude.com/blog) の記事を日本語で読めるようにまとめた
コレクションです。

**→ https://byteflare-co.github.io/anthropic-engineering-ja/**

## 収録範囲

| ブログ | 対象期間 | 記事数 | 特徴 |
|--------|---------|--------|------|
| Anthropic Engineering | 全期間 | 22 本 | 技術記事 — PDF 版あり |
| Claude Blog | 2026-03〜 | 17 本 | 製品アップデート・活用事例 |

新しい記事が公開されると、GitHub Actions が自動で取得・翻訳・デプロイします。

## ディレクトリ構成

```
├── scripts/
│   ├── articles.py                  # Anthropic 記事の目録
│   ├── claude_articles.py           # Claude 記事の目録
│   ├── fetch_article.py             # Anthropic 記事取得 (Playwright)
│   ├── fetch_claude_article.py      # Claude 記事取得 (Playwright)
│   ├── build_site.py                # 静的サイト生成 (Jinja2)
│   ├── build_pdf.py                 # PDF 生成
│   ├── check_new_articles.py        # Anthropic 新着チェッカ
│   ├── check_new_claude_articles.py # Claude 新着チェッカ
│   ├── site_templates/              # Anthropic 用テンプレート (セリフ調)
│   ├── site_templates_claude/       # Claude 用テンプレート (モダン sans)
│   └── site_templates_landing/      # ランディングページ
├── articles/
│   ├── en/          # Anthropic 英語原文 Markdown
│   ├── ja/          # Anthropic 日本語訳 Markdown
│   ├── claude_en/   # Claude 英語原文 Markdown
│   └── claude_ja/   # Claude 日本語訳 Markdown
├── pdfs/            # Anthropic 記事の PDF（書籍風）
├── site/            # ビルド出力（GitHub Pages にデプロイ）
│   ├── index.html           — ランディング（2 ブログ選択）
│   ├── anthropic/           — Anthropic Engineering セクション
│   └── claude/              — Claude Blog セクション
└── .github/workflows/
    ├── deploy-pages.yml             # push 時にサイトをビルド・デプロイ
    ├── check-new-articles.yml       # 毎日 Anthropic 新着を検出
    ├── publish-new-article.yml      # Anthropic 記事を自動翻訳・登録
    ├── check-new-claude-articles.yml  # 毎日 Claude 新着を検出
    └── publish-new-claude-article.yml # Claude 記事を自動翻訳・登録
```

## セットアップ

```bash
uv sync
uv run playwright install chromium   # 初回のみ
```

## 使い方

### 記事を取得する（英語 Markdown）

```bash
# Anthropic Engineering
uv run python scripts/fetch_article.py --slug building-effective-agents
uv run python scripts/fetch_article.py --all

# Claude Blog
uv run python scripts/fetch_claude_article.py --slug claude-managed-agents
uv run python scripts/fetch_claude_article.py --all
```

### サイトをビルドする

```bash
uv run python scripts/build_site.py
uv run python scripts/build_site.py --serve   # ローカルで確認
```

### PDF を生成する（Anthropic 記事のみ）

```bash
uv run python scripts/build_pdf.py --slug building-effective-agents
uv run python scripts/build_pdf.py --all
```

### 新着記事をチェックする

```bash
uv run python scripts/check_new_articles.py          # Anthropic
uv run python scripts/check_new_claude_articles.py    # Claude
```

## 自動更新パイプライン

```
毎日 00:17 UTC — check-new-articles.yml (Anthropic)
毎日 00:47 UTC — check-new-claude-articles.yml (Claude)
        ↓ 新着あり
   Issue 作成 (new-article / new-claude-article ラベル)
        ↓
   publish-new-*-article.yml (Claude Code Action)
   → fetch → 翻訳 → (PDF 生成) → commit → push → Issue close
        ↓
   deploy-pages.yml → GitHub Pages 更新
```

## 翻訳について

- 本文・見出し・箇条書きは日本語化。
- コードブロックは原文維持（コメントも原文のまま）。
- 固有名詞（Claude, MCP, Anthropic, Opus, Sonnet 等）は原文維持。
- 技術用語は初出時に（必要に応じて）原語併記。
- 翻訳はすべて Claude（機械翻訳）による。

## 本リポジトリの位置付け・著作権について

本リポジトリは Anthropic Engineering Blog および Claude Blog の
**非公式な日本語訳** です。Anthropic 社とは一切関係ありません。

- **原文の著作権は Anthropic PBC に帰属**します。翻訳は個人の学習・参照目的で
  作成したものであり、原著作権者の権利を主張・置き換えるものではありません。
- 翻訳はすべて Claude（機械翻訳）によるもので、正確性は保証しません。
  正確な内容は必ず原文をご確認ください。
  - [Anthropic Engineering](https://www.anthropic.com/engineering)
  - [Claude Blog](https://claude.com/blog)
- 本コンテンツの再配布・商用利用を希望する場合は、Anthropic 側のポリシーに
  従ってください。翻訳部分についても上記原著作権の範囲内で扱う必要があります。
- 翻訳の誤りや原文の解釈について、本リポジトリは **Issue・Pull Request を
  受け付けていません**。指摘事項がある場合でも対応できない点をご了承ください。

明示的なオープンソースライセンス（MIT 等）は付与していません。原著作権者の
許諾なく翻訳物に自由なライセンスを付与することはできないためです。
