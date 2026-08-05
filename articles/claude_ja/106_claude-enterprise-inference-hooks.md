---
date: '2026-08-05'
final_url: https://claude.com/blog/claude-enterprise-inference-hooks
number: 106
selector_used: main
slug: claude-enterprise-inference-hooks
source_url: https://claude.com/blog/claude-enterprise-inference-hooks
title: 'Inference hooks: inline data loss prevention for Claude Enterprise'
title_ja: "推論フック: Claude Enterprise 向けのインラインなデータ漏洩防止機能"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

# 推論フック: Claude Enterprise 向けのインラインなデータ漏洩防止機能

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a737642f52b1b4fc4aaec1a_260805-PromptHooks-Blog-960x540-ZT-v008.gif)

推論フック(inference hooks)を使うと、コンプライアンスチームは、チャットや Claude Code、Claude Cowork をはじめとする Claude Enterprise の各サーフェスにおいて、あらゆるプロンプトとツール呼び出しのレスポンスが Claude に届く前に、それらを検査してポリシーを適用できるようになります。ブロックするか許可するかの判断を下すのはお客様の DLP サーバーであり、Claude はその判断をリアルタイムで実行に移して、承認されていないコンテンツが Claude に届く前にブロックします。

セキュリティチームは、従業員が機微なデータを移動させうるすべてのチャネルが、自分たちのチームが管理する検査ポイントを必ず通過するよう求めています。これまで、ネイティブなインラインの実行制御は Claude Code のクライアント側フックに限られていました。推論フックは、製品ごとに個別の統合作業やエージェントを用意することなく、Claude Enterprise のあらゆるサーフェスをカバーする単一の実行制御レイヤーによって、このギャップを埋めます。

## 推論フックの仕組み

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7362314ccf1158f2bffe5f_Claude-blog-prompt-hooks-DLP%20(1).png)

組織が推論フックを有効にすると、すべての推論リクエストは署名付きの WebSocket 接続を通じてセキュリティサーバーへとルーティングされます。モデルが生成を開始する前に、Claude はプロンプトとその周辺のコンテキストをお客様のサーバーに送信します。サーバーは許可か拒否かの判定を返し、Claude はその判定を受け取ってはじめて処理を進めます。同じチェックはツール呼び出しに対しても実行されます。Claude が(MCP・スキル・プラグインを通じて接続されたツールを含む)ツールを呼び出すと、そのレスポンスはモデルに返される前に検査されます。

## 推論フックの活用方法

既存の DLP プログラムを Claude にも拡張できます。推論フックは、公開されたスキーマを持つオープンな Webhook ベースのプロトコルを採用しています。そのため導入は容易で、Netskope、Palo Alto Networks、Proofpoint、Zscaler など、他のツールがすでに情報を送っているのと同じサーバー、あるいは自社で構築した AI セキュリティサーバーを指定するだけで済みます。

チャット、Claude Code、Cowork、その他の Claude Enterprise 製品を、1 つの設定でカバーできます。組織レベルで一度推論フックを有効にすれば、MCP コネクタ、スキル、プラグインを通じて行われるツール呼び出しを含め、Claude Enterprise のサーフェス全体に適用されます。

シャドーモード(常に許可)、ロールベースの除外設定、割合ベースの段階的ロールアウトによって、展開をシンプルに進められます。失敗時のポリシー許容度、タイムアウトなどの各種設定は、組織のリスク許容度に合わせてカスタマイズできます。

## はじめに

推論フックは現在、Claude Enterprise のお客様向けにベータ版として提供されています。[ドキュメント](https://platform.claude.com/docs/en/manage-claude/inference-hooks)を参照して組織の DLP サーバーを設定し、Claude Enterprise のサーフェス全体でポリシーの適用を開始してください。

セキュリティベンダーの方々にとっても、推論フックはドキュメント化されたスキーマを持つ Webhook ベースのプロトコル上に構築されているため、統合を構築することができ、Claude Enterprise のお客様は自組織の設定先として御社のプラットフォームを指定できるようになります。
