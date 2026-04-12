---
date: '2026-01-26'
final_url: https://claude.com/blog/interactive-tools-in-claude
number: 7
selector_used: main
slug: interactive-tools-in-claude
source_url: https://claude.com/blog/interactive-tools-in-claude
title: Your favorite work tools are now interactive connectors inside Claude
title_ja: お気に入りの仕事ツールが Claude 内のインタラクティブコネクタになりました
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a8c18ce1b5adef7e9_6b1470e7fa2fb7280502291f204b88c412690076-1000x1000.svg)

# お気に入りの仕事ツールが Claude 内のインタラクティブコネクタになりました

本日より、MCP Apps によるインタラクティブコネクタを Claude に導入します。Claude の中でツールを開いて操作できるようになります。Asana でプロジェクトのタイムラインを構築・更新する。Slack メッセージをフォーマットされたプレビューでドラフト・編集・送信する。Figma でアイデアをダイアグラムとして視覚化する——すべてタブを切り替えることなく実現できます。

Claude はすでにあなたのツールに接続し、あなたに代わってアクションを実行しています。MCP Apps により、それらのツールが会話の中にインタラクティブコネクタとして直接表示されるようになり、何が起きているかを確認しながらリアルタイムでコラボレーションできます。

Claude で直接できるようになったことは以下の通りです:

- [Amplitude](https://claude.com/connectors/amplitude) -- 分析チャートを作成し、トレンドを探索してパラメータをインタラクティブに調整し、隠れたインサイトを発見します。
- [Asana](https://claude.com/connectors/asana) -- チャットをプロジェクト、タスク、タイムラインに変換し、チームが Asana で確認・実行できるようにします。
- [Box](https://claude.com/connectors/box) - ファイルを検索し、ドキュメントをインラインでプレビューし、コンテンツからインサイトを抽出して質問できます。

- [Canva](https://claude.com/connectors/canva) - プレゼンテーションのアウトラインを作成し、ブランディングとデザインをリアルタイムでカスタマイズして、クライアント向けのデッキを制作します。
- [Clay](https://claude.com/connectors/clay) - 企業を調査し、メールや電話番号付きの連絡先を検索し、企業規模や資金調達などのデータを取得して、会話の中で直接パーソナライズされたアウトリーチを作成します。

- [Figma](https://claude.com/connectors/figma) -- プロンプトでテキストや画像をフローチャート、ガントチャート、その他のビジュアルダイアグラムとして FigJam に描画します。
- [Hex](https://claude.com/connectors/hex) - データに関する質問をすると、インタラクティブなチャート、テーブル、引用付きの回答が得られます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6977320ae3916b6e1531390f_hex-mcp-apps.png)

- [monday.com](https://claude.com/connectors/monday) - 業務を管理し、プロジェクトを実行し、ボードを更新し、タスクをスマートに割り当て、インサイトで進捗を可視化します。
- [Slack](https://claude.com/connectors/slack) (Salesforce 提供) -- Slack の会話を検索・取得してコンテキストを得て、メッセージのドラフトを生成し、好みのフォーマットに整え、投稿前に確認できます。

近日公開: **Salesforce** - Agentforce 360 でエンタープライズコンテキストを Claude に取り込み、チームが単一の接続されたインターフェースから推論、コラボレーション、アクションを実行できるようにします。

## **MCP Apps: オープンスタンダード上に構築**

基盤となる技術は、ツールを AI アプリケーションに接続するためのオープンスタンダードである [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) 上に構築されています。MCP Apps は MCP の新しい拡張で、任意の MCP サーバーが Claude だけでなく、対応するあらゆる AI プロダクト内でリッチなユーザーインターフェースを備えたインタラクティブコネクタを提供できるようにします。

私たちは、エコシステムにツールを AI に接続するための普遍的な方法を提供するために MCP をオープンソース化しました。今回、開発者がその上にインタラクティブな UI を構築できるよう、ユーザーがいる場所を問わず MCP をさらに拡張しています。

詳しくは、[MCP Apps - The First Official MCP Extension](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps) の発表をご覧ください。

## **始め方**

今すぐ Claude でインタラクティブコネクタ (MCP Apps) を使い始めましょう。[claude.ai/directory](http://claude.ai/redirect/claudedotcom.v1.5a5f03a7-dd3a-485a-930c-3899a45f74d7/directory) にアクセスし、「featured」セクションのアプリに接続して始めてください。Free、Pro、Max、Team、Enterprise プランの Claude のモバイル、ウェブ、デスクトップで利用可能です。[Claude Cowork](http://claude.com/product/cowork) でも利用できるようになりました。
