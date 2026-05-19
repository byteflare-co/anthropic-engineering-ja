---
date: '2026-05-19'
final_url: https://claude.com/blog/claude-managed-agents-updates
number: 50
selector_used: main
slug: claude-managed-agents-updates
source_url: https://claude.com/blog/claude-managed-agents-updates
title: 'New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels'
title_ja: "Claude Managed Agents の新機能: セルフホストサンドボックスと MCP トンネル"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

# Claude Managed Agents の新機能: セルフホストサンドボックスと MCP トンネル

本日より、Claude Managed Agents は、お客様自身がコントロールするサンドボックスの中で動作し、プライベートな Model Context Protocol (MCP) サーバーへ接続できるようになります。エージェントがツールを実行するサンドボックスと、そこから到達するサービスの両方が、お客様のエンタープライズに既に確立されている境界の内側で、お客様自身のセキュリティとランタイム制御のもとで動作します。

サンドボックスはお客様自身のインフラストラクチャ上で動作させることもできますし、[Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/)、[Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents)、[Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox/tree/main)、[Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox) のようなマネージドプロバイダーに、コンピュートと分離を任せることもできます。

Claude Platform では、[セルフホストサンドボックス](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) がパブリックベータで、MCP トンネルがリサーチプレビューで利用可能です（[アクセスを申請する](https://claude.com/form/claude-managed-agents)）。

## **エージェントの実行を境界の内側にとどめる**

セルフホストサンドボックスを使うと、機密性のあるファイル、パッケージ、サービスを、お客様自身のインフラストラクチャ、あるいはマネージドサンドボックスプロバイダーの内側にとどめておけます。オーケストレーション、コンテキスト管理、エラーリカバリーを担う [エージェントループ](https://www.anthropic.com/engineering/managed-agents) は Anthropic のインフラストラクチャ上に残り、ツールの実行だけがお客様自身が設定した環境へと移ります。

お客様の境界の内側には、ネットワークポリシー、監査ログ、セキュリティツールが既に整っており、ファイルやリポジトリが外に出ていくこともありません。コンピュートもお客様がコントロールできます。リソースのサイズとランタイムイメージはお客様側で設定するため、長時間のビルドや画像生成のようなコンピュート負荷の高い作業を実行するエージェントも、そのタスクに必要な CPU、メモリ、キャパシティを得られます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b4fa5fbae3bdfc63be57c_Sandboxes.png)

## **サンドボックスクライアントを選ぶ**

任意のサンドボックスクライアントを持ち込むこともできますし、サポートされているプロバイダーのいずれかから始めることもできます。

- [**Cloudflare**](https://developers.cloudflare.com/sandbox/claude-managed-agents/) は、microVM と、より軽量な isolate を使って、サンドボックスをスケールさせて動かします。アウトバウンドのネットワークリクエストはお客様のコントロール下にあり、ゼロトラストでのシークレット注入、エグレスを監査・経路変更・改変するためのカスタマイズ可能なプロキシ、Cloudflare のネットワーク経由で内部サービスに接続する機能などを利用できます。[**Amplitude**](https://amplitude.com/) は、ブランドに沿ったモックアップやデザインのクリティークを行う社内ツール「Design Agent」を、より緊密な可観測性とコントロールのために Managed Agents と Cloudflare の上に構築しています。
- [**Daytona**](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents) のサンドボックスは、フルにコンポーザブルで、長時間稼働かつステートフルなコンピュータです。同じプリミティブで、ちょっとしたバースト実行も、何時間にもわたって作業するエージェントも動かせます。サンドボックスはセッション稼働中も SSH か認証付きのプレビュー URL からアクセスできる状態を保ち、状態を完全に保持したまま一時停止して再開することもできます。[**Clay**](http://clay.com/) の GTM エンジニアリングエージェント Sculptor は、Managed Agents と Daytona の上で、ワークフローを自律的にビルド・テスト・モニタリングしています。
- [**Modal**](https://modal.com/blog/introducing-claude-managed-agents-with-modal-sandboxes) は AI ワークロード向けに作られたクラウドプラットフォームで、サンドボックスは Modal の関数、ストレージ、ネットワーキングのプリミティブと同じ基盤を共有しており、本番品質の AI システムを構築するために必要なものがすべて揃っています。Modal のカスタムコンテナランタイムは、どんなイメージでも高速に起動でき、何十万もの同時サンドボックスへスケールし、必要に応じて CPU と GPU リソースを提供します。
- [**Vercel**](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox) のサンドボックスは、VM のセキュリティ、VPC ピアリング、bring your own cloud をミリ秒単位の起動時間と組み合わせています。Managed Agents がモデル・ツール・セッション状態を扱い、その一方で Vercel Sandbox のファイアウォールがネットワーク境界でクレデンシャルを注入するため、クレデンシャルがサンドボックスの中に入ることはありません。機関投資家向けの金融 AI プラットフォーム [**Rogo**](https://rogo.ai/) は、プロプライエタリなデータを安全に扱うアナリストエージェントを、Managed Agents と Vercel Sandbox の上に構築しています。

## **プライベートネットワーク内のサービスに接続する**

[MCP トンネル](http://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) を使うと、エージェントはプライベートネットワーク内の MCP サーバーへ、それらをパブリックインターネットに晒すことなくリーチできます。内部データベース、プライベート API、ナレッジベース、チケッティングシステムが、エージェントから呼び出せるツールになります。お客様がデプロイする軽量なゲートウェイがアウトバウンド接続を 1 本張るだけで、インバウンドのファイアウォールルールも、パブリックエンドポイントも不要で、トラフィックはエンドツーエンドで暗号化されます。

MCP トンネルは Managed Agents と Messages API でサポートされます。MCP トンネルは [Claude Console](https://platform.claude.com/) のワークスペース設定から、組織管理者によって管理されます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b4fdc9749bb31acafa95b_MCP%20tunnel%20(1).png)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69010941df4d50c5b91b2ba1_Clay-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69010943d7b5a7bb5f07d8d6_Clay-dark-theme.svg)

「Clay の GTM ワークフローを自律的にビルド・テストする GTM エンジニアリングエージェント Sculptor を構築するなかで、私たちはツールをループで叩くだけよりも、より柔軟でパワフルにアクションを取らせる方法をエージェントに与えたいと考えていました。Claude Managed Agents によって、ローカルエージェントのパワーを、クラウドエージェントの信頼性、バージョニング、バックグラウンド実行とともに再現できました。さらに、Daytona のような自分たちのサンドボックスでこれを動かせるおかげで、ファイルシステムをコントロールでき、外部のファイルストアをマウントしたり、その場でパッケージをインストールしたりできます。」

Ryan Chang, AI Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699dfac701ab4fcb02c3d870_rogo-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699dfacb9075a218012e1f11_rogo-dark.svg)

「Claude Managed Agents がエージェントループを担い、Vercel のサンドボックスが自分たちのワークロード向けに構成できる環境を提供してくれます。これによって、ベストインクラスのインフラストラクチャを活用しつつ、金融 AI プラットフォームとして複利で効いてくる領域、つまりツールとデータの深さと広さ、そして投資家やバンカーが実際に働く方法に合わせて作り込まれたプロダクト面に集中できます。」

Strib Walker, Head of Product

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15dc2d99d53c20667cf5_mason-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15e9d43b72bc8726b778_mason-dark.svg)

「私たちのユースケースでは、複雑なプロダクト面をまたいで内部ツールを安全にオーケストレーションすることが求められます。Modal のサンドボックスはエンタープライズのお客様が必要とするセキュリティ境界を提供してくれ、これを Claude Managed Agents と組み合わせることで、追加の複雑さを手作りせずにパワフルなハーネスが手に入ります。1 週間もかからずに動くバージョンを立ち上げ、お客様向けの信頼性を引き上げられました。」

Sai Yandapalli, CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f90d548130a5b392eef2bb_logo_amplitude-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f90d57fa27a4ce120cdf71_logo_amplitude-dark.svg)

「Claude Managed Agents と Cloudflare のおかげで、自分たちが既に使い慣れて信頼しているインフラストラクチャの上で、デザインエージェントの最初の使えるバージョンを 2 日で動かせるようになりました。」

Will Newton, Design

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa585b66f744445eaec7_Doordash_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa5e900d8af5fd782dd2_Doordash_dark.svg)

「地域のビジネス向けにエージェント型コマースをスケールさせていくなかで、私たちは本番への高効率なパスと、ハーネスのフルなコントロール、スケール、信頼性を必要としています。Modal をベースにした AI インフラストラクチャの上で、この次のステップに向けて Claude Managed Agents を評価していけることを楽しみにしています。」

Andy Fang, Co-founder
