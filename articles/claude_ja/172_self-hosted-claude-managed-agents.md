---
date: '2026-11-12'
final_url: https://claude.com/resources/articles/self-hosted-claude-managed-agents
number: 172
selector_used: article
slug: self-hosted-claude-managed-agents
source_url: https://claude.com/blog/self-hosted-claude-managed-agents
title: Operate Claude Managed Agents inside your security perimeter
title_ja: 自社のセキュリティ境界内で Claude Managed Agents を運用する
---

[セルフホスト版 Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/self-hosted) がプライベートベータとして利用可能になりました。開発者は、自社のコードや社内システムで直接作業するエージェントを構築し、そのエージェントを自社の環境で実行できます。

セルフホストは、自律型エージェントを構築・デプロイするための組み合わせ可能な API 群である [Managed Agents](https://claude.com/platform/claude-managed-agents) の新しい実行方法です。Managed Agents は、長時間稼働するエージェントを本番環境に投入するためのエージェントハーネス、サンドボックス、認証情報の管理、セッション履歴を提供します。

## エージェントのコントロールプレーンを自社環境で実行する

Managed Agents は当初、Anthropic がインフラを運用する Claude Platform 上のホステッドサービスとして提供を開始しました。その後、コードを自社環境内に留めておく必要があるチーム向けに、[セルフホスト型サンドボックス](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)を追加しました。

それ以来、エージェントはより高い能力を備え、壊れたビルドの修正、リリースのテスト、アラートのトリアージ、バグバックログの消化など、より重要な仕事を担うようになっています。エージェントは人の監視なしにコード上で動作し、社内システムへのアクセスも必要とします。そのレベルのアクセス権を持つエージェントについては、サンドボックスだけでなくサービス全体を自社環境に置きたいと考えるチームもあります。これまでは、そのためにはプラットフォームを自前で構築する必要がありました。

セルフホスト版 Managed Agents では、ハーネス、サンドボックス、認証情報、セッション履歴を含むサービスのあらゆる部分が、自社のクラウドまたはオンプレミスで動作します。Managed Agents サーバー、そのデータベース、そしてエージェントがシェルやファイルツールを実行するワーカーは、お客様自身が運用します。モデルへのリクエストの送信先は、Anthropic への直接接続、利用中のクラウドプロバイダー（Amazon Bedrock、Google の Agent Platform、Microsoft Foundry）、あるいは自社のゲートウェイから自由に選べます。開発者は引き続き、ホステッド版 Managed Agents と同じコア API でエージェントを構築できます。

セッション履歴は自社のデータベースに保存されます。組織が Anthropic と[ゼロデータ保持（ZDR）](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope)の契約を結んでいる場合、Claude に送信されるリクエストには、他の Messages API 呼び出しと同様に ZDR が適用されます。

![図 1: セルフホスト版 Claude Managed Agents](https://assets.claude.com/7607c90e3d3d6e3bf9f7d1af0d39afb006be1413.svg)

## エージェントのセキュリティを前提とした設計

エージェントが人の監視なしにコードやシステムの内部で動作する場合、すべてのステップを人が確認することには頼れません。そのため、制限はシステム自体に組み込まれている必要があります。だからこそエージェントのセキュリティはアーキテクチャから始まるのであり、私たちは Managed Agents を 4 つの原則に基づいて設計しました。これらの原則は、Anthropic がすべてをホストする場合でも、サンドボックスだけを自社でホストする場合でも、サービス全体を自社でホストする場合でも同様に適用されます。

**頭脳と手を分離する**

ハーネス（頭脳）は Claude を呼び出し、サンドボックス（手）はエージェントのコードが実行される場所です。両者は設計上、分離されています。エージェントのコードはサンドボックス内で実行される一方、エージェントループ、セッション履歴、Vault のシークレットはその外側に置かれます。[両者を分離する](https://www.anthropic.com/engineering/managed-agents)ことで、エージェントは 1 つのサンドボックスが実行全体を通して存続することに依存せずに済み、サンドボックスはツールが必要としたときにだけ起動し、セッション履歴はイベントログとしてサンドボックスの外側に保持されます。

**認証情報をサンドボックスの外に置く**

Vault は、認証情報をサンドボックスに入れないように設計されています。MCP ツールやサポート対象の API 呼び出しでは、[サンドボックスの外側にあるプロキシがリクエストに認証情報を付加します](https://platform.claude.com/docs/en/managed-agents/vaults)。セルフホスト版 Managed Agents では、認証情報を自社のシークレットマネージャーに保存することもできます。

**ネットワークアクセスを制限できる**

各環境を[許可されたホストのリスト](https://platform.claude.com/docs/en/managed-agents/secure-deployment)に制限でき、それ以外のホストへのリクエストはブロックされます。壊れたビルドを修正するエージェントであれば、そのリストは git ホストとパッケージレジストリだけで済むかもしれません。サンドボックスを自社でホストする場合は、同じ制限を自社のファイアウォールで設定します。

**すべてのセッションが完全な記録を残す**

Managed Agents は、エージェントが行ったすべてのステップについて、実行したツール呼び出しとその結果を含めて記録します。この記録は [OpenTelemetry](https://platform.claude.com/docs/en/manage-claude/opentelemetry) 経由でエクスポートできるため、すでに利用している監視ツールに送り、他のシステムと合わせてエージェントの活動をレビューできます。

## はじめに

セルフホスト版 Claude Managed Agents は現在、プライベートベータとして利用可能です。アクセスをリクエストするには Anthropic のアカウントチームにお問い合わせいただくか、[ドキュメント](https://platform.claude.com/docs/en/managed-agents/self-hosted)で詳細をご確認ください。
