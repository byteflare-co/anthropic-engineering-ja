---
name: publish-engineering-article-ja
description: Anthropic の Engineering ブログに新しい記事が公開されたとき、このプロジェクト（~/dev/byteflare-co/anthropic-engineering-ja/）の日本語 PDF コレクションに追加するための skill。「新しいブログが出た」「engineering ブログの新記事」「新記事の PDF を作って」「anthropic engineering の更新」「新しい記事を追加して」「engineering blog ja に追加」のようなキーワードで必ず起動すること。このプロジェクト内で作業しているときにブログ記事の追加や更新が話題に出たら、ためらわずにこの skill を使う。fetch・翻訳・PDF 生成・index.json 更新までの一連のワークフローを実行する。
---

# 新しい Engineering ブログ記事を日本語 PDF 化する

`~/dev/byteflare-co/anthropic-engineering-ja/` プロジェクトには、Anthropic Engineering ブログを
日本語 PDF の「読み物」にするツール一式が用意されている。新しい記事が公開されたとき、
この skill に従えば既存の流儀を崩さずに PDF を追加できる。

## 作業ディレクトリ

すべてのコマンドは必ずこのディレクトリで実行する:

```bash
cd ~/Documents/anthropic-engineering-ja
```

## 全体のワークフロー

1. **現在の目録を確認** — `scripts/articles.py` の `ARTICLES` リストを読んで、
   既に登録されている最大の番号と、各記事の slug を把握する。
2. **ブログ一覧から新記事を発見** — WebFetch で
   `https://www.anthropic.com/engineering` を取得し、目録に無い記事があるか調べる。
3. **目録に追加** — 新しい `ArticleMeta(...)` を `scripts/articles.py` に足す。
4. **英語 Markdown を取得** — `fetch_article.py --slug <新 slug>`
5. **日本語訳を書く** — `articles/ja/NN_slug.md` に翻訳を書き込む（スタイルは後述）
6. **PDF を生成** — `build_pdf.py --slug <新 slug>`
7. **index.json を更新**
8. **動作確認** — PDF のページ数と本文冒頭を目視チェック

## ステップ詳細

### 1. 既存目録の確認

```bash
cd ~/Documents/anthropic-engineering-ja
```

`scripts/articles.py` を Read して、`ARTICLES` リストの最大 `number` を把握する。

### 2. 新記事を発見する

WebFetch で engineering ブログ一覧を取り、目録に無いタイトル/slug を見つける。
URL は `https://www.anthropic.com/engineering/<slug>` の形式。

### 3. 目録に追加する

`scripts/articles.py` の `ARTICLES` リストの末尾に Edit で行を足す。
番号は連番（既存 max + 1）。slug は URL の末尾部分をそのまま使う
（大文字小文字も維持。例: `AI-resistant-technical-evaluations`）。

```python
ArticleMeta(23, "new-article-slug", "Original English Title", "2026-04-15"),
```

日付は ISO 形式 `YYYY-MM-DD`。未発表の場合は空文字列 `""`。

### 4. 英語 Markdown の取得

```bash
cd ~/Documents/anthropic-engineering-ja
uv run python scripts/fetch_article.py --slug <new-slug>
```

`articles/en/NN_new-slug.md` が生成される。フロントマターは自動付与される。

一気に複数記事を扱うなら `--all` でも良い（既存ファイルはスキップされる）。
既存を上書きしたい場合のみ `--force`。

### 5. 日本語訳を書く

`articles/en/NN_new-slug.md` を Read し、Write で
`articles/ja/NN_new-slug.md` を新規作成する。

フロントマターは英語版のキーを踏襲し、`title_ja` を追加する:

```yaml
---
date: '2026-04-15'
final_url: https://www.anthropic.com/engineering/new-article-slug
number: 23
selector_used: article
slug: new-article-slug
source_url: https://www.anthropic.com/engineering/new-article-slug
title: Original English Title
title_ja: 日本語タイトル
---
```

### ⚠️ YAML フロントマターの落とし穴

`title_ja` に **コロン `:` が含まれる場合は必ずダブルクォートで囲む**。
そうしないと YAML パーサが辞書だと解釈して `build_pdf.py` が失敗する。

```yaml
# ❌ 失敗する
title_ja: 権限プロンプトの先へ: Claude Code をより安全にする

# ✅ 正しい
title_ja: "権限プロンプトの先へ: Claude Code をより安全にする"
```

### 翻訳スタイルガイド

このプロジェクトの既存記事は以下の流儀で訳されている。新記事もこれに合わせる。

- **文体**: 「です・ます」調で統一（「である」調は使わない）
- **コードブロック**: 原文のまま維持（コメントも英語のまま）。翻訳しない。
- **固有名詞は原文維持**: Claude, Anthropic, MCP, Opus, Sonnet, Haiku,
  SWE-bench, Terminal-Bench, GitHub, Playwright, RAG, LLM, API, Trainium,
  Vertex AI, Bedrock, TPU, XLA, BrowseComp, etc.
- **技術用語の扱い**: 日本語訳が定着していない場合は「日本語（原語）」の形で併記。
  例: `拡張思考（extended thinking）`, `文脈化検索（Contextual Retrieval）`
- **見出し**: `#`, `##`, `###` の階層を保ち、日本語に訳す
- **リスト**: `-` や `1.` の構造を保ち、項目を日本語化
- **リンク**: `[リンクテキスト](URL)` の URL はそのまま、テキスト部分のみ日本語化
- **画像**: `![alt](/_next/image?url=...&w=...&q=...)` の URL はそのまま維持。
  `alt` テキストと画像直後のキャプション（しばしば `*斜体*`）は日本語に訳す
- **テーブル**: ヘッダとセルの内容を日本語化。構造は維持
- **強調**: `**太字**`, `*italic*` は維持
- **引用**: `>` は維持し、中身を日本語化
- **脚注**: 末尾の `[1]`, `[2]` や `---` 以下の脚注も訳す
- **謝辞 (Acknowledgements)**: 執筆者名・貢献者名はそのまま残し、文章だけ訳す
- **URL の自動リンク化注意**: `[text](http://claude.md)` のように書くと
  `claude.md` がローカルファイルリンクに見えることがある。原文のまま維持する。

### 翻訳の参考にする既存記事

スタイルに迷ったら既存の翻訳を参照する:

- 解説型の記事: `articles/ja/02_building-effective-agents.md`
- 技術詳細の記事: `articles/ja/13_advanced-tool-use.md`
- ポストモーテム系: `articles/ja/09_a-postmortem-of-three-recent-issues.md`
- 短めの技術ノート: `articles/ja/18_eval-awareness-browsecomp.md`

### 長い記事を書くときの注意

1 つの Write 呼び出しで長文すぎて失敗する場合は、最初に一部を Write し、
残りを Edit で追記する。ただし 1 回の Write で数千行入っても通常は問題ない。

### 6. PDF の生成

```bash
cd ~/Documents/anthropic-engineering-ja
uv run python scripts/build_pdf.py --slug <new-slug>
```

成功すると `pdfs/NN_new-slug.pdf` が作られる。

複数記事をまとめて処理する場合は `--all`。既存の PDF も再生成される点に注意。

### 7. index.json の更新

```bash
cd ~/Documents/anthropic-engineering-ja && uv run python -c "
import json, sys
from pathlib import Path
sys.path.insert(0, 'scripts')
from articles import ARTICLES
out = []
for a in ARTICLES:
    en = Path(f'articles/en/{a.stem}.md')
    ja = Path(f'articles/ja/{a.stem}.md')
    pdf = Path(f'pdfs/{a.stem}.pdf')
    out.append({
        'number': a.number,
        'slug': a.slug,
        'title': a.title,
        'date': a.date,
        'source_url': a.source_url,
        'en_path': str(en) if en.exists() else None,
        'ja_path': str(ja) if ja.exists() else None,
        'pdf_path': str(pdf) if pdf.exists() else None,
        'pdf_size_bytes': pdf.stat().st_size if pdf.exists() else None,
    })
Path('index.json').write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'written index.json with {len(out)} entries')
"
```

### 8. 動作確認

```bash
cd ~/Documents/anthropic-engineering-ja
# 0 バイトファイルが無いこと
find pdfs -name "*<new-slug>*" -size 0
# ページ数と冒頭テキストの確認
uv run --with pypdf python -c "
from pypdf import PdfReader
import sys
r = PdfReader('pdfs/NN_new-slug.pdf')
print(f'Pages: {len(r.pages)}')
print('--- Cover ---')
print(r.pages[0].extract_text()[:300])
print('--- Body start ---')
if len(r.pages) > 1:
    print(r.pages[1].extract_text()[:400])
"
```

目視で下記をチェックする:

- カバーページに日本語タイトルが表示されている
- ページ数が妥当（短い記事で 5 ページ、長い記事で 10〜20 ページ程度）
- 本文が文字化けせず日本語で読める
- コードブロックや画像が壊れていない

問題なければ `open pdfs/NN_new-slug.pdf` でビューアに表示して完了。

## 複数記事を一括で追加する場合

ブログ一覧を見たら新記事が複数あった場合:

1. 全記事を `scripts/articles.py` にまとめて追加（番号は連番）
2. `uv run python scripts/fetch_article.py --all` で一括取得（既存はスキップされる）
3. 各記事を順番に翻訳（1 本ずつ丁寧に）
4. `uv run python scripts/build_pdf.py --all` で一括 PDF 化
5. index.json を 1 回だけ更新

翻訳ステップはどうしても時間がかかる。急がず 1 本ずつ品質を担保すること。

## トラブルシューティング

### fetch_article.py が "本文要素が見つかりません" エラー

記事が `code.claude.com/docs/...` のような別サイトにリダイレクトされていて、
`scripts/fetch_article.py` の `CONTENT_SELECTORS` が該当 HTML をカバーできて
いない可能性が高い。開発者ツールで本文を囲む要素を調べ、`CONTENT_SELECTORS`
にセレクタを追加する。

### build_pdf.py が YAML エラー

`mapping values are not allowed in this context` のようなエラーは
フロントマターのコロン問題。`title_ja` や他のフィールドにコロンが
含まれていないか確認し、ダブルクォートで囲む。

### PDF の画像が表示されない・右ボーダーが切れる

- 画像 URL は Next.js の `/_next/image?url=...` 形式だが、
  `build_pdf.py` が CDN URL にデコードする。デコード処理で失敗している
  場合は `scripts/build_pdf.py` の `_NEXT_IMAGE_RE` を確認。
- 画像ボーダーが切れる問題は `box-sizing: border-box` で対処済み
  （`scripts/style.css` 参照）。

### 和文フォントが効かない

macOS の「游ゴシック」を前提にしている。`scripts/style.css` の `--font-jp`
変数を見直すか、Chromium が別のフォントを拾えるようフォールバックを追加する。

## この skill の意図

- **誤訳を防ぐ**: 既存 22 本の翻訳スタイルから逸脱しないためのガイド
- **コマンドの取り違えを防ぐ**: 作業ディレクトリと `uv run` を忘れがち
- **フロントマターの罠を避ける**: 過去に 1 本だけ YAML エラーになった経験を反映
- **手順の漏れを防ぐ**: 特に index.json の更新と動作確認は忘れやすい

新しい記事が出るたびにゼロから思い出さなくて済むように、
このプロジェクトの流儀を 1 つの文書に固めたもの。
