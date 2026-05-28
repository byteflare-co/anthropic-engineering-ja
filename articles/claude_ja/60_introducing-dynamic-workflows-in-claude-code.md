---
date: '2026-05-28'
final_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
number: 60
selector_used: main
slug: introducing-dynamic-workflows-in-claude-code
source_url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
title: Introducing dynamic workflows in Claude Code
title_ja: Claude Code の動的ワークフローを発表
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

# Claude Code の動的ワークフローを発表

本日、Claude Code に動的ワークフロー（dynamic workflows）を導入します。これにより、Claude は最も難しいタスクをエンドツーエンドで引き受けられるようになります。通常であれば四半期単位で計画するような仕事が、数日で片付くようになるのです。Claude は、数十から数百の並列サブエージェントを 1 つのセッションで走らせるオーケストレーションスクリプトを動的に書き、結果があなたの手元に届く前に自ら検算します。

問題のなかには、単一のエージェントが一回で扱うには大きすぎるものがあります。特に複雑でレガシーなコードベースではそうです。サービス全体にまたがるバグ探し、数百のファイルに及ぶマイグレーション、コミットする前にあらゆる角度からストレステストしたいプラン——動的ワークフローは、こうした仕事をエンドツーエンドで扱えます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186b2e070156fbb2df90ad_166befe7.png)

動的ワークフローは本日からリサーチプレビューとして、Claude Code の CLI、Desktop、VS Code 拡張機能で、Max、Team、Enterprise プラン（管理者が有効化している場合）向けに利用できます。加えて、Claude API、Amazon Bedrock、Vertex AI、Microsoft Foundry でも利用可能です。

注意: 動的ワークフローは、通常の Claude Code セッションよりも大幅に多くのトークンを消費する可能性があります。そのため、自分の仕事における使用感をつかむには、スコープを絞ったタスクから始めることをおすすめします。

最良の体験のためには、動的ワークフローを使うときに auto モードを有効にしてください。そのうえで、ワークフローを開始する方法は 2 つあります。

1. Claude に動的ワークフローを作るよう直接お願いする（たとえば「ワークフローを作って」）。
2. Claude Code 固有の新しい設定 `ultracode` をオンにする。これは effort メニューからアクセスでき、エフォートレベルを xhigh に設定すると同時に、タスクの処理にワークフローを使うべきかどうかを Claude が自動で判断するようにします。

## **動的ワークフローの実例**

早期アクセスユーザーや Anthropic 社内のチームは、動的ワークフローを以下のような幅広いユースケースで活用してきました。

- **コードベース全体のバグ探し、プロファイラに基づく最適化監査、セキュリティ監査:** Claude はサービスやリポジトリを並列に調べ、見つかった指摘ごとに独立した検証を走らせるため、レポートには本当の問題が浮かび上がります。同じかたちは、認証チェック、入力バリデーション、コードベース全体にわたる安全でないパターンといった、ハードニングの一連のパスにも当てはまります。
- **大規模なマイグレーションとモダナイゼーション:** Claude は、フレームワークの入れ替え、API のデプリケーション、数千のファイルにまたがる言語ポートを、エンドツーエンドで扱えます。
- **二重チェックが必要な重要な仕事:** 誤答のコストが高いとき、ワークフローは Claude に同じ問題への独立した試行を与え、結果があなたに届く前に、結果を崩そうとする敵対的なエージェントを働かせます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186eb7c527a0f35719a37b_Klarna-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186eb3a5f68864d977de69_Klarna-dark.svg)

「動的ワークフローは、大規模コードベース上での調査・レビュー系のタスクで特に価値を発揮してきました。デッドコードを特定したり、従来の静的解析では見逃されていたクリーンアップの機会を浮かび上がらせたりするのに使い、強い成果を見ています。これはエンジニアがメンテナンスやリファクタリングの仕事を進める速度を上げるのに役立っています」

Alessio Vallero, Senior Engineering Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186fa3128d757bc62363f8_cyberagent-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a186faafd2bd2ff345e25ec_cyberagent-dark.svg)

「動的ワークフローは、単一のサブエージェントを投げて走らせるのと、フルのエージェントチームを組み上げるのとの間のすき間を埋めてくれます。プランから実装までがそのまま流れるので、可視性を失うことなく、より長い実行も信頼できるようになっています」

Ken Takao, Lead Systems Engineer
