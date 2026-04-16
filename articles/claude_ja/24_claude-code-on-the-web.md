---
date: '2025-10-20'
final_url: https://claude.com/blog/claude-code-on-the-web
number: 24
selector_used: main
slug: claude-code-on-the-web
source_url: https://claude.com/blog/claude-code-on-the-web
title: Claude Code on the web
title_ja: "Claude Code on the web"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Claude Code on the web

***更新:*** *Claude Code on the web は、Pro および Max ユーザーに加え、プレミアムシートを持つ Team および Enterprise ユーザー向けにもリサーチプレビューとして利用可能になりました。これらのユーザーに対して Claude Code on the web はデフォルトで有効化されており、アカウント管理者は Claude の設定からアクセスを切り替えることができます。2025 年 11 月 12 日*

本日、ブラウザから直接コーディングタスクを委任できる新しい方法、Claude Code on the web をご紹介します。

リサーチプレビューとしてベータ版で公開された本機能では、Anthropic が管理するクラウドインフラストラクチャ上で実行される複数のコーディングタスクを Claude に割り当てることができます。バグの積み残し解消、定型的な修正、並行開発作業に最適です。

## コーディングタスクを並行実行する

Claude Code on the web では、ターミナルを開くことなくコーディングセッションを開始できます。GitHub リポジトリを接続し、必要な作業を記述すれば、Claude が実装を担当します。

各セッションは独立した隔離環境で実行され、リアルタイムで進捗を追跡できます。また、作業中の Claude に対して積極的に指示を出し、方向を修正することも可能です。

Claude Code がクラウドで実行されることで、単一のインターフェースから異なるリポジトリにまたがる**複数のタスクを並行して実行**でき、自動的な PR 作成と明確な変更サマリーにより**より速くシップ**できるようになります。

## あらゆるワークフローに柔軟に対応

Web インターフェースは、既存の Claude Code ワークフローを補完します。クラウドでのタスク実行は、特に以下のような作業に効果的です。

- プロジェクトの仕組みやリポジトリの構成に関する質問への回答
- バグ修正や定型的で明確に定義されたタスク
- テスト駆動開発を活用して変更を検証できるバックエンドの変更

Claude Code はモバイルでも利用できます。このリサーチプレビューの一環として、iOS アプリでも Claude Code を利用可能にし、開発者が外出先でも Claude を使ったコーディングを試せるようにしました。まだ初期のプレビュー段階であり、皆さまのフィードバックを基にモバイル体験を迅速に改善していきたいと考えています。

## セキュリティファーストのクラウド実行

すべての Claude Code タスクは、ネットワークおよびファイルシステムの制限が適用された隔離されたサンドボックス環境で実行されます。Git のやり取りはセキュアなプロキシサービスを通じて処理され、Claude が認可されたリポジトリにのみアクセスできるようにすることで、ワークフロー全体を通じてコードと認証情報を保護します。

また、カスタムネットワーク設定を追加して、Claude Code がサンドボックスから接続できるドメインを選択することもできます。たとえば、Claude がインターネット経由で npm パッケージをダウンロードし、テストを実行して変更を検証できるように設定できます。

Claude Code のサンドボックスアプローチの詳細については、[エンジニアリングブログ](https://www.anthropic.com/engineering/claude-code-sandboxing)と[ドキュメント](https://docs.claude.com/en/docs/claude-code/sandboxing)をご覧ください。

## 始めましょう

Claude Code on the web は、Pro および Max ユーザー向けにリサーチプレビューとして現在ご利用いただけます。[claude.com/code](http://claude.com/code) にアクセスして、最初のリポジトリを接続し、タスクの委任を始めましょう。

クラウドベースのセッションは、他のすべての Claude Code 利用とレート制限を共有します。詳細については[ドキュメント](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web)をご覧ください。
