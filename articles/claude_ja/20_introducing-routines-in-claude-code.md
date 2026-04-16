---
date: '2026-04-14'
final_url: https://claude.com/blog/introducing-routines-in-claude-code
number: 20
selector_used: main
slug: introducing-routines-in-claude-code
source_url: https://claude.com/blog/introducing-routines-in-claude-code
title: Introducing routines in Claude Code
title_ja: "Claude Code に routines を導入"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

# Claude Code に routines を導入

本日、Claude Code の routines をリサーチプレビューとして公開します。routine とは、プロンプト・リポジトリ・コネクタを含めて一度設定しておけば、スケジュールに沿って実行したり、API 呼び出しで実行したり、イベントに応じて実行したりできる Claude Code の自動化のことです。routines は [Claude Code のウェブインフラ](https://code.claude.com/docs/en/claude-code-on-the-web)上で動作するため、ラップトップを開いたままにしておく必要はありません。

すでに多くの開発者が Claude Code をソフトウェア開発サイクルの自動化に利用していますが、これまで cron ジョブやインフラ、MCP サーバーのような追加ツールは自分たちで管理する必要がありました。routines には自分のリポジトリと[コネクタ](https://claude.com/connectors)へのアクセスが最初から備わっているので、自動化をパッケージ化してスケジュールやトリガーで実行させることができます。

## 仕組み

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de678887f94fb639698fa7_dd878b86.png)

### スケジュール実行の routine

Claude Code にプロンプトとサイクル（毎時、毎晩、毎週）を与えれば、そのスケジュール通りに実行されます。

```
Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.
```

CLI で [/schedule](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options) を使っている場合、これらのタスクはスケジュール実行の routine として扱われるようになりました。

### API 経由の routine

routine は API 呼び出しで起動するよう設定することもできます。各 routine は専用のエンドポイントと認証トークンを持ちます。メッセージを POST すればセッション URL が返ってきます。アラートやデプロイフック、社内ツールなど、HTTP リクエストを送れる場所ならどこからでも Claude Code を組み込めます。

```
Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.
```

### Webhook 経由の routine、まずは GitHub から

GitHub リポジトリのイベントに応じて自動的に起動する routine を登録できます。フィルタに一致するすべての PR に対して Claude が新しいセッションを作成し、routine を実行します。

```
Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.
```

Claude は PR ごとに 1 つのセッションを開き、その PR の更新情報をセッションに継続的に流し込んでいくので、コメントや CI の失敗などのフォローアップにも対応できます。

今後、Webhook ベースの routine はさらに多くのイベントソースから起動できるように拡張していく予定です。

## チームが作っているもの

早期ユーザーが routine を作る際に、いくつかの共通パターンが見えてきました。

### スケジュール実行の routine

- バックログ管理: 毎晩新しい issue をトリアージし、ラベル付け・アサインを行い、Slack にサマリーを投稿する
- ドキュメントのズレ: 毎週マージされた PR をスキャンし、変更のあった API を参照しているドキュメントをフラグ付けして、更新 PR を開く

### API 経由の routine

- デプロイ検証: CD パイプラインが各デプロイ後に routine へ通知し、Claude が新しいビルドに対してスモークチェックを走らせ、エラーログにリグレッションがないか確認し、リリースチャンネルに go/no-go を投稿する
- アラートのトリアージ: Datadog を routine のエンドポイントに向けておけば、Claude がトレースを取得し、最近のデプロイと突き合わせ、オンコール担当がページを開く前にドラフトの修正案を用意してくれる
- フィードバックへの対応: ドキュメントのフィードバックウィジェットや社内ダッシュボードがレポートを投稿すると、Claude がその issue を文脈として読み込んだセッションをリポジトリに対して開き、変更をドラフトする

### GitHub 経由の routine

- ライブラリ移植: Python SDK に PR がマージされるたびに routine がトリガーされ、同じ変更を並行する Go SDK に移植して、対応する PR を開く
- 独自のコードレビュー: PR がオープンされたら、セキュリティやパフォーマンスについてチーム独自のチェックリストを実行し、人間のレビュアーが目を通す前にインラインコメントを残しておく

## 始め方

routines は本日より、[Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web#who-can-use-claude-code-on-the-web) が有効になっている Pro、Max、Team、Enterprise プランの Claude Code ユーザーに提供されます。最初の routine を作成するには [claude.ai/code](http://claude.ai/redirect/claudedotcom.v1.3e0e9b70-1ea9-44b2-b25b-98aec51944ff/code) にアクセスするか、CLI で /schedule と入力してください。

routines はインタラクティブなセッションと同じようにサブスクリプションの利用枠を消費します。加えて、routines には 1 日あたりの実行上限があります。Pro ユーザーは 1 日あたり最大 5 回、Max ユーザーは最大 15 回、Team と Enterprise のユーザーは最大 25 回まで routine を実行できます。この上限を超えて routine を追加で実行したい場合は、追加の利用枠を使うことが可能です。詳しくは[ドキュメント](http://code.claude.com/docs/en/routines)をご覧ください。
