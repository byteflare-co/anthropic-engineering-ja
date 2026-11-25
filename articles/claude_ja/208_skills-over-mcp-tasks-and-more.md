---
date: '2026-11-24'
final_url: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more
number: 208
selector_used: article
slug: skills-over-mcp-tasks-and-more
source_url: https://claude.com/blog/skills-over-mcp-tasks-and-more
title: MCP servers can now ship skills, run tasks, and more with Claude
title_ja: "MCP サーバーが Claude でスキルの提供やタスクの実行などに対応（MCP servers can now ship skills, run tasks, and more with Claude）"
---

Claude で Skills over MCP がパブリックベータになり、MCP サーバーがツールと一緒にスキルを提供できるようになりました。あわせて、サーバーが Claude とともに、より長く、よりインタラクティブな作業を扱うための手段も提供します。Tasks と Elicitation が一般提供（GA）となり、File Uploads もまもなく展開を開始します。

2 年前、Anthropic は AI エージェントをデータが存在するシステムに接続するための新しい標準として、[Model Context Protocol（MCP）をリリースしました](https://www.anthropic.com/news/model-context-protocol)。仕様は本番環境で稼働するエージェントの接続ニーズに応えるべく進化を続けており、エージェント間のメッセージングやオーケストレーションの基盤になりつつあります。

本日のアップデートにより、Claude は別のエージェントと協働するのと同じような形でサーバーと連携できるようになります。サーバーから学び、サーバーに作業を委任し、その過程で入力やファイルをやり取りするのです。

## Skills over MCP でツールとともに専門知識を提供する

ツールの名前や説明は、サーバーに何ができるかを Claude に伝えますが、具体的なユースケースをどう扱うべきかまではカバーしていません。[Skills over MCP](https://modelcontextprotocol.io/extensions/skills/overview) を使えば、サーバーはツールと一緒にスキルを公開でき、Claude がより長い複数ステップの作業に取り組めるよう支援できます。Claude はスキルを必要なときにだけ読み込むため、コンテキストの使用量は低く抑えられます。スキルはサーバーとともに更新されるので、開発者はツールとガイダンスをまとめて提供でき、ユーザーは別途何かをインストールする必要がありません。

スキルには、ベストプラクティス、ステップバイステップのワークフロー、さらにはユーザーのアカウントや組織に合わせたプレイブックまで含めることができます。Skills over MCP の活用例は次のとおりです。

- [Shopify](https://claude.com/marketplace/connectors/shopify) は、Claude がマーチャントのオンラインストアをエンドツーエンドで設計・更新できるよう支援します。
- [HubSpot](https://claude.com/marketplace/connectors/hubspot) は、顧客のオンボーディングを行い、Claude 上でのセットアップを完了させます。
- [Atlassian](https://claude.com/marketplace/connectors/atlassian) は、Claude が組織の深いコンテキストを活用してインサイトを得たり、業務分析を行ったりできるよう支援します。
- [Carta](https://claude.com/marketplace/connectors/carta) は、アップロードされたドキュメントをもとに Claude がエクイティ（株式）の起案と発行を行えるよう支援する予定です（近日公開）。

Skills over MCP は Claude と Claude Code でパブリックベータとして提供中です。Pro、Max、Ultra プランではデフォルトで有効になっており、Team プランでは管理者が有効にすると利用できます。Enterprise にも近日対応予定です。

![Skills over MCP（ベータ）：MCP サーバーは 3 つのレイヤーを Claude に提供します。スキルは各ユーザーや組織に合わせたドメイン知識を、ツールは Claude が実行できるアクションを、リソースは Claude が取り込めるコンテキストを担います。スキルは必要なときにだけ読み込まれ、サーバーとともに更新されます。](https://assets.claude.com/c801d50355ebd35519eb1d82598a4c903298e966.png)

## MCP サーバーが Claude とともに長時間かつインタラクティブな作業を担えるように

本番環境のエージェントは、より長く、より重要な仕事を担うようになっています。サーバーはこうした作業を支えるために、処理をバックグラウンドで実行したり、ユーザーに確認を取ったり、Claude からファイルを受け取ったりできるようになりました。

**[Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) で長時間の作業を引き渡す。** これまでツール呼び出しは、完了するまで Claude が次に進めませんでした。Tasks を使えば、サーバーは時間のかかる処理や、場合によってはエージェントループ全体を実行でき、その間も Claude は作業を続け、結果の準備ができた時点で受け取ります。[ZoomInfo](https://claude.com/marketplace/connectors/zoominfo) は Tasks を使い、以前は複数のプロンプトを要していたアカウントや連絡先のより深いリサーチを実行しています。

![Tasks：Claude は長時間のジョブを MCP サーバーに引き渡して作業を続け、結果の準備ができたら受け取ります。](https://assets.claude.com/e53adba43ded0a4377bdd900155891633b3edbc7.png)

**[Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) で呼び出しの途中に入力を求める。** お金を使う、データを削除するといった一部のアクションには、ユーザーの承認が必要です。Elicitation を使えば、サーバーは処理を一時停止してフォームやリンクを通じてユーザーに入力を求め、その後中断したところから再開できます。Elicitation の活用例は次のとおりです。

- [Supabase](https://claude.com/marketplace/connectors/supabase) は、有料プロジェクトを作成する前や破壊的な SQL を実行する前にコストを確認します。
- [Railway](https://claude.com/marketplace/connectors/railway) は、サービスの削除など、破壊的になりうる変更を行う前に確認を求めます。
- [GitHub](https://claude.com/marketplace/plugins/github) は、エージェントがリポジトリを削除する前に、ユーザーにそのリポジトリ名を入力させます。

Tasks と Elicitation は、Claude と Claude Code の Pro、Max、Ultra プランで一般提供が開始されており、Team および Enterprise 組織にも順次展開中です。

**[File Uploads](https://github.com/modelcontextprotocol/experimental-ext-file-uploads) でファイルを送受信する。** Claude はテキストだけでなく、ファイルも MCP サーバーに渡せるようになります。File Uploads 拡張は、PDF、スプレッドシート、画像を、コンテキストウィンドウを経由させずにサーバーへ送信します。

File Uploads は、Claude と Claude Code の Pro、Max、Ultra、および対象となる Team・Enterprise プラン向けにまもなく展開を開始します。

## 今すぐプラグインに対応を追加しましょう

これらの機能はオープンな MCP 仕様とその拡張の一部であるため、対応したサーバーは Claude に限らず、互換性のあるあらゆるクライアントで動作します。対応を追加するには、[Skills over MCP](https://code.claude.com/docs/en/mcp#use-skills-from-mcp-servers)、[Tasks](https://code.claude.com/docs/en/mcp#mcp-tasks-for-server-authors)、[Elicitation](https://code.claude.com/docs/en/mcp#respond-to-mcp-elicitation-requests)、[File Uploads](https://claude.com/docs/connectors/building/files?open_in_browser=1) の各ドキュメントを参照してください。

## 本番環境でエージェントを接続するための、より強固な基盤

AI エコシステム全体からの貢献のおかげで、MCP の SDK は月間 7 億回以上ダウンロードされ、Claude 向けの MCP コネクタは 10,000 を超えています。私たちは MCP コミュニティと協力して、Claude における MCP の動作を改善してきました。この 1 年で、MCP は次のように進化しました。

- **トークン効率の向上：** [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) はツール定義を必要なときにだけ読み込むため、複数サーバー構成ではツール定義が使うコンテキストを 85% 以上削減できます。
- **スケールしやすく：** [最新の MCP 仕様](https://claude.com/resources/articles/bringing-mcp-2026-07-28-to-claude)はステートレスで、Claude の各製品でサポートされています。これにより、サーバーの構築や、成長に伴う信頼性の維持が容易になります。
- **認可がよりシンプルに：** [Enterprise Managed Auth](https://claude.com/docs/connectors/building/enterprise-managed-auth) 拡張により、管理者が対応サーバーを一度認可するだけで、ユーザーは自動的に接続されます。
- **よりインタラクティブに：** [MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/quickstart) 拡張は、会話の横やフルスクリーンで、本格的なインターフェースを Claude に組み込みます。

これらの改善を合わせることで、MCP はより構築しやすく導入しやすいものとなり、本番環境のエージェントのニーズに合わせて標準が進化し続けるための強固な基盤が整います。

## MCP コミュニティへの感謝

MCP は [Agentic AI Foundation](https://aaif.io/) がホストするオープン標準であり、その上で開発を行う人々によって形づくられています。[2 年間の歩み](https://blog.modelcontextprotocol.io/posts/mcp-turns-two)は、仕様を書き、SDK を構築し、サーバーをリリースし、クライアント対応を追加してくれたメンテナー、コントリビューター、開発者の皆さんによるものです。MCP を今日の姿にしてくださったことに感謝します。
