---
date: '2026-09-25'
final_url: https://claude.com/blog/build-plugins-for-claude
number: 150
selector_used: main
slug: build-plugins-for-claude
source_url: https://claude.com/blog/build-plugins-for-claude
title: Build plugins for Claude
title_ja: "Claude 向けプラグインを開発する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Claude 向けプラグインを開発する

毎日、何百万人もの人々が Claude を自分のアプリや業務ツール、データに接続しています。本日、開発者がこうしたユーザーにより簡単にリーチできるようにする取り組みを発表します。

プラグインは MCP コネクタや Agent Skills、あるいはその両方をパッケージ化したもので、サードパーティが Claude 向けの拡張機能を作る主な方法です。プラグインを作成し、新しいディレクトリ提出ポータルから申請すると、承認後に[Claude ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory)に掲載されます。

## ‍**ディレクトリ提出ポータルでプラグインを提出・管理する**

[ディレクトリ提出ポータル](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory/manage/new)は、Claude の有料プランを利用している開発者に公開されています。プラグインを提出し、Claude ディレクトリに公開する方法は2通りあります。

- **単体の MCP コネクタ:** リモートの MCP サーバーを指定します。
- **プラグインバンドル:** MCP サーバーとスキルを組み合わせ、GitHub 上でホストし、そのリポジトリを提出します。Claude Code では、プラグインに LSP、コマンド、フック、エージェントを含めることもできます。

どちらの方法を選んでも、ポータルが提出からリリースまでをガイドします。以下のことが可能です。

- **プラグインを自動検証する。** 提出するとすぐに各申請がチェックされ、安全性がスキャンされるため、問題を早期に発見できます。
- **ステータスとフィードバックを確認する。** レビュープロセスの進捗状況、安全性スキャンの結果、推奨される変更点を確認できます。
- **準備ができたら公開する。** 承認されたら、Claude 上でプラグインをいつ公開するかは自分で決められます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab6a76f77cf7911a03be1bd_d852ff4a.png)

プラグインのレビューステータスと推奨される変更点のスタイライズ表示。データはイメージです。

## **公開後もプラグインをモニタリングし改善する**

プラグインが公開されると、利用状況の分析によって製品面・バージョン別のインストール数が分かるため、ユーザーのために優先すべき修正や機能を判断できます。ディスカバリー面では、自分のリスティングがどれだけ閲覧されているか、どのような検索から人々がたどり着いているかが分かるので、より多くの新規ユーザーにリーチできるよう改善できます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab6a76f77cf7911a03be1c0_ec09f8b2.png)

公開済みプラグインの利用状況指標のスタイライズ表示。データはイメージです。

## **MCP 2.0 とその拡張機能でリッチな体験を届ける**

Claude は最新の MCP 仕様、一般に[MCP 2.0](https://modelcontextprotocol.io/specification/2026-07-28)と呼ばれるものをサポートしており、ステートレスなコアを含んでいます。2つの[MCP 拡張機能](https://modelcontextprotocol.io/extensions/overview)を使うことで、プラグインの利用体験を向上させることができます。チャット内でのインタラクティブな UI のための[MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/getting-started)と、エンタープライズユーザー向けのゼロタッチ OAuth のための[Enterprise Managed Auth](https://claude.com/docs/connectors/building/enterprise-managed-auth)です。今後さらに多くの MCP 機能・拡張機能のサポートが追加される予定です。

## **Claude 向けプラグインの開発を始める**

プラグインは、サードパーティ開発者が Claude 向けの拡張機能を作る主な方法です。今後数週間かけて、Claude と Claude Code にまたがる単一のディスカバリー体験が展開されていきます。

スキルと MCP コネクタは引き続きビルディングブロックとして存在し、Claude ディレクトリでの掲載も継続されます。将来的には、開発者は自分のコネクタのリスティングをプラグインに変換できるようになる予定です。すでに Claude ディレクトリにスキル、コネクタ、プラグインを掲載している場合、変更を加える必要はありません。

プラグイン開発を始めるには、[プラグインの作り方](https://claude.com/docs/build/overview)に関するドキュメントを参照し、[こちら](https://claude.ai/redirect/claudedotcom.v1.60bbe5e0-cac1-4d3f-bd29-fce3837769bd/directory/manage/new)からプラグインを提出してください。
