---
date: '2026-07-28'
final_url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
number: 104
selector_used: main
slug: bringing-mcp-2026-07-28-to-claude
source_url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
title: Bringing MCP 2026-07-28 to Claude
title_ja: Claude に MCP 2026-07-28 を導入
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

# Claude に MCP 2026-07-28 を導入

Model Context Protocol の5回目のスペックリリースである [**MCP 2026-07-28**](https://modelcontextprotocol.io/specification/2026-07-28) が本日公開されました。最新スペックは MCP をステートレスなコアへと移行させると同時に、認可の強化と公式拡張機能の正式リリースを実現しています。サポートは Claude 製品全体で順次展開されています。

## **MCP の新機能**‍

MCP は先ごろ月間 SDK ダウンロード数が4億件を突破し、今年だけで4倍に増加、AI エージェントをアプリケーションに接続するための業界標準となりました。MCP 2026-07-28 はこれまでで最も重要なスペックリリースのひとつです。**ステートレスコア。** MCP は双方向のステートフルなプロトコルから、リクエスト/レスポンス型のモデルへと移行します。サーバーはサーバーレスやエッジのインフラ上にデプロイできるようになりました。これにより、Claude 向けの MCP サーバーを構築し、採用が拡大するにつれて利用規模を拡張していく体験がシンプルになります。

**拡張機能の標準化。** [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview) と [Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) は、バージョン管理された拡張機能フレームワークの下で正式にリリースされます。これにより開発者は、コアプロトコルを変更することなく、インタラクティブな UI や長時間実行される処理といった機能を追加するための正式な手段を得られます。

**認可の強化。** 認可は本番環境の OAuth 2.0 および OIDC デプロイメントに準拠するようになり、MCP サーバーは Entra や Okta のようなエンタープライズ ID システムに回避策なしで接続できます。

エコシステム全体の企業が、ベータ版の頃から MCP コミュニティとともに新スペック上での構築を進めてきました。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee4cb7c69d15a44ec7d6_Figma%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee481c19e67f332ef755_Figma%20Light.svg)

「より多くのビルダーが、私たちの MCP サーバーを使って生成した成果物を Figma のキャンバスに取り込み、チームとともに探求し、練り上げ、洗練させて、際立つプロダクトへと仕上げています。利用が拡大するにつれ、私たちのステートレスなアーキテクチャはそれに合わせてスケールできますし、MCP Apps、Tasks、そして Enterprise-Managed Auth によって、デザインとコードを一つの連携したフローにまとめるためにさらに多くのことができるようになります。」

Josh Clemm 氏、VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689e68f0c0711f4b55978e_intuit-blue.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689e68f0c0711f4b55978e_intuit-blue.svg)

「MCP は AI エージェントをツールやデータに接続するための業界標準であり、Intuit は新しい MCP 2026-07-28 スペックをサポートできることを誇りに思います。ステートレスなプロトコルコアと、MCP Apps や Tasks を含む拡張機能フレームワークにより、私たちのエンジニアやお客様はエンタープライズ規模でエージェント型の体験を構築・連携できるようになり、Intuit は1億人の消費者・事業者に対して、働く場所を問わず信頼される金融インテリジェンス体験を届け続けることができます。」

Chris Kasten 氏、Chief Architect and SVP of Engineering, Platform and Development、Xceleration Group

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6b97730efbbe48c60cf7_Netlify_Logo_0%201%20(1).svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf70fe8bd1d6d413430b7f_Netlify_Logo_0%202%20(1).svg)

「2026-07-28 スペックにおけるステートレスコアにより、MCP はセッション管理を回避する必要のない、ファーストクラスの HTTP ワークロードになります。私たちのお客様は、Netlify 上の MCP がプラットフォームの他の部分と同じくらいシンプルであることを望んでおり、この新しいスペックはその核心部分でそれを実現します。MCP Apps を新しい拡張機能フレームワークに組み込むことは、エコシステム全体のスケーラビリティ、アクセシビリティ、そして機能性にとって大きな前進です。」

Sean Roberts 氏、VP of Applied AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a68a0572ec430ef25573811_posthog-logo.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a68a05e4db3770d9eccece8_posthog-logo-white.svg)

「MCP をステートレスなプロトコルに移行させることで、私たち自身のサービスのスケールが容易になり、お客様の MCP サーバー向けの分析機能を追加しやすくなります。これにより、人々が自分の MCP ツールがどう使われているか、そしてユーザーが求めているのにまだ足りていないツールが何かを把握しやすくなります。このプロトコルがこの方向に成長していくのを見るのは嬉しいことです。」

Paul D'Ambra 氏、Product Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689fd3ac5b9fc22a54b573_Xero%20Wordmark__Blue.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a689fec4db3770d9ecc9a00_Xero%20Wordmark_White.png)

「Anthropic はフロンティアモデルと、常に基準を引き上げ続ける開発者体験を組み合わせています。オープンな MCP 2026-07-28 スペックにおけるステートレスコアは、私たちが管理すべき複雑さを減らしてくれるため、より多くの機能をより速く、より大規模にお客様へ届けることができます。」

Andrew Goodman 氏、VP of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c1e924b89aa4ed22b0d827_cs-logo-zoom-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c1e9282f4c49a5abab41de_cs-logo-zoom-dark-theme.svg)

「Zoom では、組織のコンテキストこそが AI に意味のある成果をもたらす鍵だと考えており、だからこそ Zoom のミーティングインテリジェンスを Claude のような AI プラットフォームに安全に取り込む MCP サーバーを構築してきました。新しい MCP スペックにより、標準的な HTTP インフラ上で MCP サーバーをデプロイ・スケールすることがはるかに容易になります。これにより、ユーザーは日々頼りにしている AI ワークフローの中で、Zoom のミーティングインテリジェンスをより速く、より確実に利用できるようになります。」

Ross Mayfield 氏、Head of Product for AI Platform

## ‍**Claude における MCP の進化**‍

Claude は現在、[connectors ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.claude_com.v1.bda2a45d-921b-42d9-bf5f-516f57967b81/directory/connectors)に950を超える MCP サーバーを掲載しており、毎日何百万人もの人々に利用されています。今年 Anthropic は、新しいプロトコル拡張機能へのサポートに加えて、MCP をより構築・デプロイしやすくする機能を出荷してきました。

[MCP Apps](https://claude.com/blog/interactive-tools-in-claude) により、サーバーは会話の中で直接インタラクティブな UI をレンダリングできます。ユーザーはコネクタが何をしているかを確認し、タブを切り替えることなくインラインで操作できます。

[Enterprise-managed auth](https://claude.com/blog/enterprise-managed-auth) により、管理者は ID プロバイダーを通じて組織全体に MCP コネクタをプロビジョニングできます。管理者がコネクタを一度承認すれば、ユーザーは既存の IdP グループを通じてアクセス権を継承し、初回ログイン時に接続が完了します。エンドユーザーにとってはセットアップ不要です。

[コネクタを構築する開発者向けの可観測性](https://claude.com/blog/observability-for-developers-building-connectors)は、ディレクトリに公開されたコネクタに対して、Claude の各製品面でのパフォーマンスを示すダッシュボードを提供します。開発者はこれを使って採用状況を追跡し、エラーやレイテンシを診断し、製品ごとの利用状況を分析できます。

[MCP tunnels (research preview)](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) は、プライベートネットワーク内の MCP サーバーを、パブリックインターネットに公開することなく Claude に接続します。チームは、インバウンドのファイアウォールルールも、パブリックエンドポイントも、オリジン側での IP 許可リストも必要とせずに、社内ツールを Claude に取り込めます。

2026-07-28 におけるステートレスコア、標準化された拡張機能、そして強化された認可は、開発者がより多くのアプリケーションを Claude に取り込み、より低摩擦で一貫性のあるエンドユーザー体験を実現する助けとなるでしょう。私たちは今後も、オープンスタンダードとしての MCP へ、コミュニティとともに投資を続けるとともに、MCP を本番環境でより利用しやすく効果的なものにする Claude の機能への投資も続けていきます。

## ‍**はじめに**

**‍**まずは [スペック](https://modelcontextprotocol.io/specification/2026-07-28/) と [SDK](https://modelcontextprotocol.io/docs/sdk) をご覧ください。サポートは間もなく Claude 製品全体で順次展開されます。あなたの MCP サーバーを Claude の[connectors ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.claude_com.v1.bda2a45d-921b-42d9-bf5f-516f57967b81/directory/connectors)に登録する予定があれば、詳細は[こちら](https://claude.com/docs/connectors/building/submission)をご覧ください。
