---
date: '2026-10-22'
final_url: https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
number: 197
selector_used: article
slug: claude-models-on-google-cloud-anthropic-managed
source_url: https://claude.com/blog/claude-models-on-google-cloud-anthropic-managed
title: The full Claude Platform, available on Google Cloud
title_ja: Claude Platform のすべてが Google Cloud で利用可能に（The full Claude Platform, available on Google Cloud）
---

# Claude Platform のすべてが Google Cloud で利用可能に（The full Claude Platform, available on Google Cloud）

Claude Models on Google Cloud (Anthropic managed) の一般提供を開始しました。これにより Google Cloud のお客様は、Google Cloud の IAM 認証情報、請求、コミットメントの消化をそのまま利用しながら、Claude Platform の全機能を使えるようになります。なお、Google がデータ処理者となる Google managed の提供形態でも、引き続き Claude をご利用いただけます。

## Google Cloud で Claude Platform のすべてにアクセス

Anthropic managed の提供形態では、Google Cloud のお客様は Claude API の全機能を利用でき、新機能やベータ版もネイティブの Claude Platform で公開されたその日に提供されます。

Anthropic managed の提供形態は既存の Google Cloud IAM 認証情報で動作するため、チームはすでに管理しているツールや権限の範囲内で作業を続けられます。請求は Google Cloud の単一の請求書にまとめられ、Claude の利用分は既存の Google Cloud コミットメントから差し引かれます。

Claude Models on Google Cloud (Anthropic managed) は現在、US および Global エンドポイントで利用可能です。

![Abacus.AI](https://assets.claude.com/3000fcaf4ad00ac2cc4096d3f5aa236cc9eb415d.png)

> 「Anthropic managed の提供形態により、Google Cloud をアクセスレイヤーとしてネイティブの Claude API を使えるようになりました。新機能に初日からアクセスできることは重要です。私たちはエンタープライズ向けに AI エージェントやアシスタントを構築しており、Claude の新しい機能を素早く自社製品に取り込む必要があります。既存の IAM 設定をそのまま使え、利用分が Google Cloud コミットメントに計上されることもわかっていたので、チームにとって導入は簡単な決断でした。」

Arvind Sundararajan, CTO

![Triple Whale](https://assets.claude.com/3720f77d05a852bc6857ae3eca424467270055b6.png)

> 「EC ブランド向けの AI ハーネスである Moby は Claude 上で動いています。Anthropic managed の提供形態により、私たちのチームがすでに開発に使っているのと同じ Claude API で、Moby を Google Cloud 上で運用しています。プロンプトキャッシュは Moby を大規模かつ低コストで運用するうえで中心的な役割を担っており、請求とアクセスを Google Cloud 経由にしながらも、それを維持できています。」

Maksim Gorev, Head of AI Engineering

## 含まれる機能

Anthropic managed の提供形態を利用する Google Cloud のお客様は、Claude Platform の全機能を利用でき、次のようなことが可能です。

**エージェントの構築とデプロイ：**

- [Claude Managed Agents (beta) (opens in new tab)](https://platform.claude.com/docs/en/managed-agents/overview)：インフラを管理することなく、長時間稼働するエージェントを動かせます
- [Code execution (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)：API 呼び出しの中で Python コードの実行、可視化の作成、データ分析を行えます
- [Computer use (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)：Claude がブラウザやデスクトップを操作してタスクを完了できるようにします
- [Agent skills (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)：繰り返し行うワークフローを Claude に教え、一貫した結果を出せるようにします
- [Advisor strategy (beta) (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)：アドバイザーモデルに相談させることで、エージェントの知能を底上げします

**システムやナレッジとの接続：**

- [Files API (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/files)：ドキュメントをアップロードし、会話をまたいで参照できます
- [Citations (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/citations)：応答をソースドキュメントに基づかせます
- [Web search (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) と [web fetch (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)：Web 上の最新の実世界データで Claude の知識を補強します
- [MCP connector (beta) (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)：クライアントコードを書かずに Claude を他のツールと接続できます

**コストとパフォーマンスの管理：**

- [Prompt caching (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)：繰り返し使うコンテキストのコストとレイテンシを削減します
- [Batch processing (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/batch-processing)：大量の非同期ワークロードを処理します

Claude Opus 5.5 の Fast Mode も、Claude Models on Google Cloud (Anthropic managed) を利用するお客様向けに一般提供されています。Fast mode は速度を優先し、出力トークンの生成を最大 2.5 倍高速化します。素早いイテレーション、ライブデバッグ、そして出力速度がユーザー体験の向上につながるインタラクティブなエージェントに適しています。料金は入力トークンが 100 万トークンあたり $8、出力トークンが $40 です。

Claude Models on Google Cloud で利用可能な機能の一覧は、[ドキュメント (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed) をご覧ください。

Anthropic managed の提供形態を利用するお客様は、Claude Console にもアクセスできます。Claude Console は、Claude を使ったエージェントを観測・管理するための Anthropic の開発環境です。プロンプトの作成やエージェントの設定、ホスト環境での実行、使用量とコストのモニタリング、ワークスペースごとのアクセスとセキュリティの管理を行うツールが含まれています。

Claude Fable 5.1、Opus 5.5、Sonnet 5.5、Haiku 5.5 が利用可能で、新しいモデルもリリースと同時に Anthropic managed の提供形態で提供されます。

## Claude で構築するための 2 つの選択肢

Google Cloud で Claude を使って構築する方法は 2 つあります。

**Claude Models on Google Cloud (Anthropic managed)** は、ベータ版および一般提供中の Claude Platform の全機能にゼロデイでアクセスしたいお客様向けです。Google Cloud 経由でアクセスしつつ、Claude Platform と完全に同等の機能を求めるお客様に最適です。サービスは Anthropic が運用し、データ処理者も Anthropic となります。

**Claude Models on Google Cloud (Google managed)** は、Google Cloud をデータ処理者とする必要があるお客様、厳格なリージョン単位のデータ所在地要件があるお客様、または Model Armor や Agent Engine といった Google Cloud のネイティブ統合を利用したいお客様にとって、引き続き最適な選択肢です。

## 始めるには

Anthropic managed の提供形態は本日より一般提供されています。始めるには、[Claude Models on Google Cloud (Anthropic managed) (opens in new tab)](https://console.cloud.google.com/marketplace/product/anthropic/anthropic-managed-claude) を開くか、[ドキュメント (opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed) をご覧ください。

既存の割引が適用されている場合は、割引が正しく適用されるよう、Anthropic managed の提供形態を使い始める前に Anthropic または Google Cloud のアカウントエグゼクティブにご連絡ください。割引を過去の利用分に遡って適用することはできません。
