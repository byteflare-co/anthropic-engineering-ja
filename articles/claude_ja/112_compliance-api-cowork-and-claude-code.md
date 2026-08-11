---
date: '2026-08-11'
final_url: https://claude.com/blog/compliance-api-cowork-and-claude-code
number: 112
selector_used: main
slug: compliance-api-cowork-and-claude-code
source_url: https://claude.com/blog/compliance-api-cowork-and-claude-code
title: Compliance API coverage extends to Claude Cowork and Claude Code
title_ja: "Compliance API のカバー範囲が Claude Cowork と Claude Code に拡大"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Compliance API のカバー範囲が Claude Cowork と Claude Code に拡大

Claude の Compliance API は、デスクトップアプリ、ウェブ、モバイルにまたがる Cowork、そして CLI とデスクトップアプリの Claude Code をカバーするようになりました。この対応は Claude Enterprise のお客様向けにベータ版として提供されます。コンプライアンス・セキュリティチームは、Claude のチャットで既に使っているのと同じ Compliance API インターフェースを通じて、両製品のセッションコンテンツとメタデータを取得できるようになります。

新しいエンドポイントは追加的なものです。今日 Compliance API から取得しているデータに変更は一切ありません。

セキュリティ・コンプライアンスチームは、監査や eディスカバリーのために、各サーフェスごとに別々のロギングインフラを構築することなく、組織全体で Claude がどのように使われているかを把握するために Compliance API に依存しています。Cowork と Claude Code にカバー範囲を拡大することで、これまでのギャップが埋まります。これらのセッションも、Claude のチャットと並んで表示されるようになります。

## 仕組み

新しいセッションエンドポイントは、Cowork と Claude Code の各セッションについて、統合されサーバー側でホストされたトランスクリプトを返します。そのため、プロンプト、レスポンス、ツールの活動がひとつのセッション記録としてまとめて返ってきます。

各セッション記録は 2 種類のデータを含みます。

- **セッションコンテンツ:** プロンプトとレスポンス、ツール呼び出しの内容（ウェブおよび MCP）、そして skill とアーティファクトの内容がトランスクリプトのテキストとして記録されます。
- **セッションメタデータ:** 検証済みのユーザー ID とメールアドレス、組織 ID、セッション ID とメッセージごとの ID、タイムスタンプ。

このベータ版には、ウェブ版の Claude Code、Claude Platform 経由でアクセスする Claude Code、Amazon Bedrock、Google Cloud の Vertex AI、Microsoft Foundry 上で実行されるセッションは含まれません。

すでに OpenTelemetry データをエクスポートしている組織は、それをそのまま継続できます。Compliance API は、御社側にインフラを追加することなく、それと並行して動作させることができます。

## 利用を開始する

Cowork と Claude Code のカバー範囲は本日から利用可能で、既存の Compliance Access Key を使って Compliance API に含まれます。別途構築が必要な統合はありません。すでに組織で有効になっている場合は、新しいセッションエンドポイントに直接クエリを実行してください。まだの場合は、Compliance API の[ドキュメント](https://platform.claude.com/docs/en/manage-claude/compliance-api)を確認して有効化してください。
