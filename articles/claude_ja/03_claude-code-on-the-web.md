---
date: '2025-10-20'
final_url: https://claude.com/blog/claude-code-on-the-web
number: 2
selector_used: main
slug: claude-code-on-the-web
source_url: https://claude.com/blog/claude-code-on-the-web
title: Claude Code on the web
title_ja: ウェブ上の Claude Code
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# ウェブ上の Claude Code

***アップデート:*** *ウェブ上の Claude Code は、Pro および Max ユーザーに加えて、プレミアムシートを持つ Team・Enterprise ユーザー向けのリサーチプレビューとして利用可能になりました。これらのユーザーに対してはデフォルトでオンになっており、アカウント管理者は Claude 設定からアクセスを切り替えられます。2025 年 11 月 12 日*

本日、ブラウザから直接コーディングタスクを委任できる新しい方法——ウェブ上の Claude Code を発表します。

リサーチプレビューのベータ版として、Anthropic が管理するクラウドインフラ上で動作する複数のコーディングタスクを Claude に割り当てられるようになりました。バグバックログへの対応、ルーチン的な修正、並列開発作業に最適です。

## 複数のコーディングタスクを並列で実行

ウェブ上の Claude Code を使えば、ターミナルを開かずにコーディングセッションを始められます。GitHub リポジトリを接続し、何が必要かを説明すれば、あとは Claude が実装を担当します。

各セッションは独自の分離された環境で実行され、リアルタイムの進捗追跡が付いてきます。また、タスクの実行中に Claude に積極的に指示を出して軌道修正することもできます。

Claude Code がクラウドで動くことで、**複数のタスクを異なるリポジトリにまたがって並列で実行**でき、単一のインターフェースから管理できます。さらに自動 PR 作成と明確な変更サマリで、**より速くリリース**できます。

## あらゆるワークフローに柔軟に対応

このウェブインターフェースは、既存の Claude Code ワークフローを補完します。クラウドでタスクを実行するのは、特に次のようなケースで効果的です。

- プロジェクトの仕組みやリポジトリのマッピングについての質問への回答
- バグ修正やルーチン的な、きちんと定義されたタスク
- バックエンドの変更。Claude Code はテスト駆動開発で変更を検証できます

Claude Code はモバイルでも使えます。このリサーチプレビューの一環として、iOS アプリで Claude Code を利用可能にしました。開発者は外出先でも Claude とのコーディングを試せます。まだ初期のプレビューであり、皆さんのフィードバックをもとにモバイル体験を素早く改善していきたいと考えています。

## セキュリティ優先のクラウド実行

Claude Code のすべてのタスクは、ネットワークとファイルシステムに制限がかかった分離されたサンドボックス環境で実行されます。Git のやり取りはセキュアなプロキシサービス経由で扱われ、Claude が許可されたリポジトリにのみアクセスできるようにします——ワークフロー全体を通じてコードと認証情報を保護するのに役立ちます。

また、カスタムネットワーク設定を追加すれば、Claude Code がサンドボックス内から接続できるドメインを選択できます。たとえば Claude に対してインターネット経由で npm パッケージのダウンロードを許可し、テストを実行して変更を検証できるようにすることも可能です。

Claude Code のサンドボックス化アプローチを深掘りしたい方は、[エンジニアリングブログ](https://www.anthropic.com/engineering/claude-code-sandboxing)と[ドキュメント](https://docs.claude.com/en/docs/claude-code/sandboxing)をご覧ください。

## 始め方

ウェブ上の Claude Code は、本日より Pro および Max ユーザー向けのリサーチプレビューとして利用可能です。[claude.com/code](http://claude.com/code) にアクセスして、最初のリポジトリを接続してタスクを委任してみてください。

クラウドベースのセッションは、他のすべての Claude Code 利用とレートリミットを共有します。詳しくは[ドキュメント](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web)をご覧ください。
