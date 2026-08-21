---
date: '2026-08-20'
final_url: https://claude.com/blog/computer-use-skills-api-files-api
number: 122
selector_used: main
slug: computer-use-skills-api-files-api
source_url: https://claude.com/blog/computer-use-skills-api-files-api
title: Build production agents with computer use, the Skills API, and the Files API
title_ja: computer use、Skills API、Files API で本番運用可能なエージェントを構築する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# computer use、Skills API、Files API で本番運用可能なエージェントを構築する

computer use、Skills API、Files API が本日、Claude Platform で一般提供開始となりました。computer use には、Web アプリケーションで動作するエージェント向けの新しい browser use ツールも追加されています。これらを組み合わせることで、ソフトウェアを操作し、チームの専門知識を適用し、完成したファイルを返すエージェントを構築できるようになります。

### **Claude Platform 上でのエージェント構築**

**computer use** を使うと、目に見えるソフトウェアを操作するエージェントを構築できます。スクリーンショットを与えられると、エージェントはキーボードの前にいる人と同じようにクリック、入力、スクロールを行います。これにより、自動化を想定して作られていないアプリケーションでも動作させることができます。新しい **browser use ツール** はこれを Web にまで拡張します。スクリーンショットに加えて、エージェントはページの構造を読み取り、画面上の位置ではなく特定のフィールドやボタンに対して操作を行います。

**Skills API** と **Files API** は、そのエージェントにあなたのチームの専門知識やドキュメントを与えるためのものです。スキルとは、Claude がタスクに応じて必要なときにだけ読み込む、指示・スクリプト・テンプレートのフォルダです。**Skills API** を使えば、自分自身のスキルをアップロードしてバージョン管理し、任意のリクエストに紐づけることができます。これらは Claude のコード実行サンドボックス内で実行されるため、ホスティングする必要はありません。**Files API** は、エージェントが読み書きするドキュメントのためのストレージです。PDF やスプレッドシートを一度アップロードすれば、以降のリクエストでは再送信する代わりに ID で参照でき、エージェントが作成したファイルをダウンロードすることもできます。

たとえば、保険金請求エージェントを構築しているとします。このエージェントは Files API から受付書類を読み込み、チームの申請手続きをエンコードしたスキルに従い、browser use ツールを使って保険会社の Web ポータルで申請を完了し、確認書をファイルとして保存し直します。すでに一般提供されているコード実行と Web 検索も、同じループに組み込まれます。

### **一般提供に伴う新機能**

- **computer use:** 更新された computer use ツールでは、モデル呼び出し 1 回につき 1 アクションではなく、1 ターンで複数のアクションを実行できるようになりました。これにより、より少ない呼び出し回数と時間でタスクが完了します。また、computer use は当社の BAA のもとで HIPAA 規制対象ワークロードにも利用可能になりました。
- **browser use ツール:** computer use に本日新しく追加されました。同じマルチアクションターンを利用し、ページ構造の情報を加えることで、ピクセル情報のみに頼る場合よりも Web 要素を確実にターゲットできます。
- **Skills API:** 自分自身のスキルをアップロードしバージョン管理するための、よりシンプルな API です。
- **Files API:** ファイルの自動失効、5 倍のレート制限引き上げ、組織あたり 1 TB のストレージが追加されました。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d86b69e80750cfefc646_Asteroid_Logo_Black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d83ff9fbb0abe47899c7_Asteroid_Logo_White.svg)

「私たちのエージェントは、API を持たないヘルスケアや保険のシステム内部で動作しています。新しい computer use ツールにより、最も時間のかかる保険金請求ワークフローは 32 分から 13 分に短縮され、テストしたすべてのワークフローでタスクあたりのコストが約 30% 削減され、完了率は 100% に達しました。プロンプトへの変更は一切ありませんでした。」

Davide Locatelli 氏、Research Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

「Skills API のおかげで、専門的なドキュメント作成機能を Box Agent に組み込む簡単な方法が得られました。銀行向けの場合、スキルがその企業の与信手法と承認済みのメモ形式を捉え、Box Agent はすでに Box にある財務諸表や取引関連書類にそれを適用して、根拠に基づいた与信メモをアナリストのレビュー用に作成します。銀行は、複雑なワークフロー用のエージェントをゼロから作ることなく手に入れられます。」

Matthew Midson 氏、Managing Director of Banking
