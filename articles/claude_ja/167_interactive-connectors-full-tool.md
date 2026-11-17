---
date: '2026-11-10'
final_url: https://claude.com/resources/articles/interactive-connectors-full-tool
number: 167
selector_used: article
slug: interactive-connectors-full-tool
source_url: https://claude.com/blog/interactive-connectors-full-tool
title: Your apps can now open in Claude, and Claude can work in them
title_ja: アプリを Claude の中で開けるように、そして Claude がアプリの中で作業できるように
---

今年初め、ツールの小さなライブビューを Claude に取り込む[インタラクティブコネクタ](https://claude.com/resources/articles/interactive-tools-in-claude)をリリースしました。本日から、コネクタが対応している場合には、ツールを会話の横に開いたり全画面に拡大したりして、Claude に一緒に作業してもらい、直接変更を加えてもらえるようになります。

この機能は、チャットと Cowork を統合した[新しい Claude 体験](https://claude.com/resources/articles/cowork-is-now-claude)の一環として、Web 版と Claude デスクトップアプリの全プランで順次提供されます。アカウントが新しい Claude に更新されるか、組織で有効化されると、これらの機能が表示されるようになります。

新機能は次のとおりです。

- **開いているツールの中で Claude が作業できます。** 開いているページ、行、ファイルに変更を加えるよう Claude に依頼でき、その操作はコネクタの操作と同じ方法で承認できます。変更は Claude が行うそばからツールに反映されるため、Claude と並んで作業を続けられます。
- **ツール全体が会話の横に開きます。** ツールの中で作業しながら、スペースが必要なときはチャットを非表示にしたり全画面表示にしたりできます。Confluence や Notion のようなツールでは、限定的なプレビューではなく、ご自身のアカウントでサインインした状態のフル機能のエディタを使えます。
- **Claude へのプロンプトを書かなくても、接続済みのツールを直接開けます。** Claude の手助けが欲しくなったら、同じ画面から依頼できます。
- **よく使うツールをピン留めできます。** ツールを[アーティファクト](https://claude.com/resources/articles/sheets-whiteboards-data)と並べて配置し、サイドバーや + メニューからワンクリックでアクセスできます。

## 普段使っているツールの中で Claude と作業する

まずは、ディレクトリ内の一部のツールから提供を開始します。Asana、Canva、Carta、Dropbox、monday.com、Smartsheet、Vercel、Webflow などです。

現在 Claude で利用できるツールの一部で、次のようなことができます。

- **Adobe.** 写真のレタッチ、編集、エフェクトの追加を Claude に依頼できます。PDF のハイライト、編集、墨消しも可能です。
- **Atlassian.** Confluence のページをチャットの横に開き、Claude に執筆や編集を依頼して、その変更をページ上でリアルタイムに確認できます。
- **Box.** Box のファイルをチャットの横に開いて Claude に修正を依頼し、変更を確定する前に各バージョンを並べて比較できます。
- **HubSpot.** パイプラインのタスクやフォローアップに優先順位を付け、そのまま Claude の中で対応できます。
- **Notion.** Notion のドキュメントやデータベースの作成を Claude に依頼できます。Claude から離れることなく、チャットしながら作り上げることも、自分で編集することもできます。

![Claude でインタラクティブコネクタに対応している 13 のツールのロゴ](https://assets.claude.com/98d2cbf9c0392a81da0d53ea7666bf08528db80e.png)

Figma、Harvey、Shopify も連携機能を開発中です。ほかの開発者の皆さんにも、ぜひ同様の取り組みをお勧めします。

## 開発者向け：MCP Apps を基盤に構築

インタラクティブコネクタは MCP Apps 上で動作します。MCP Apps は [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) のオープンな拡張機能で、MCP サーバーが独自のインターフェースを AI アプリケーションに持ち込めるようにするものです。構築した MCP App は Claude 専用ではなく、この[拡張機能](https://modelcontextprotocol.io/extensions/apps/overview)をサポートするあらゆる AI アプリケーションで動作します。

これまで Claude における MCP Apps は、主に会話内のインタラクティブなビューとして表示されていました。今回、Claude はアプリツールなど拡張機能のより多くの部分や埋め込みサイトをサポートするようになり、開発者のアプリ全体を Claude の中で実行できるようになりました。

これらの機能のサポートは、開発者向けにパブリックプレビューとして提供されています。開発者は今日から構築を始められます。構築を始めるには[ドキュメント](https://claude.com/docs/connectors/building/mcp-apps/getting-started)をご覧ください。

## はじめに

上記のツールは[ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.f56c3437-4d6d-43c5-8692-96e7261d14d8/directory/featured/interactive-connectors)から接続でき、チャットから任意のツールを開いたり、サイドバーにピン留めしたりできます。

**管理者の方へ：** 組織でコネクタのすべてのツールをすでに許可している場合、新機能は提供開始に合わせて表示されます。管理者は、これまでと同じ方法でコネクタのツールを制限できます。
