---
date: '2026-05-07'
final_url: https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
number: 42
selector_used: main
slug: collaborate-with-claude-across-excel-powerpoint-word-and-outlook
source_url: https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook
title: Collaborate with Claude across Excel, PowerPoint, Word and Outlook
title_ja: Excel、PowerPoint、Word、Outlook で Claude とコラボレーションする
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

# Excel、PowerPoint、Word、Outlook で Claude とコラボレーションする

本日より、Claude for Excel、PowerPoint、Word が一般提供（GA）となり、Claude for Outlook はすべての有料プラン向けにパブリックベータとして提供を開始します。Claude は Microsoft アプリ間でタスクを移っていく際にも、会話のコンテキストを丸ごと保ち続けます。

## **4 つのアプリをまたぐひとつの会話**

ほとんどの仕事は単一のアプリケーションでは完結しません。だから Claude も、あなたと一緒にアプリを移っていきます。Outlook でメールをトリアージし、添付ファイルを Word で開いてチームのテンプレートに沿ってメモを書き、Excel で裏付けとなる分析を組み立て、PowerPoint でデッキに仕上げる — そのいずれの場面でも、いま何の作業をしているかを説明し直す必要はありません。Excel で前提を変えると、PowerPoint のチャートも Word のメモの中の数字も自動で更新されます。

Claude は開いているファイルをまたいで動作するので、スプレッドシート、デッキ、メモを並べて開いておけば、変更がそのあいだを流れていきます。

会話はファイルごとに永続化されるため、サイドバーを閉じて翌日に開き直しても、キーボードや音声で前回の続きから作業を再開できます。

## **Claude for Outlook**

Claude for Outlook は、Claude をあなたの受信トレイに連れてきます。受信トレイをトリアージするように Claude に頼むと、返信が必要なもの、Claude が下書きできるもの、ノイズの 3 つにメッセージを分類します。返信は宛先・件名・本文があらかじめ埋まった状態で、Outlook の作成ペインに下書きとして並びます。カレンダー招待は出席者の空き状況をチェックし、Outlook 標準のイベントフォームで開かれます。

添付ファイルを Word や Excel で開けば、Claude は送信者が何を求めていたかをすでに把握しています。すべての返信とカレンダー招待は送信前にあなたが確認します。あなたが送信ボタンをクリックするまで、何も外には出ていきません。

## **組織全体への Claude for Microsoft 365 のデプロイ**

Claude for Excel、PowerPoint、Word は、IT 管理者と組織が必要とするコントロールを備えて一般提供（GA）となりました。ひとつの AppSource リスティングで Excel、PowerPoint、Word をカバーし、別のリスティングでベータ版の Outlook が追加されます。管理者はどちらも Microsoft 管理センターからデプロイできます。

エンタープライズ管理者は [OpenTelemetry](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents) を構成して、プロンプト、ツール呼び出し、ドキュメント参照を自社のコレクターにストリームできます。これにより、セキュリティチームは Claude が各アプリで何をしているかを正確に把握できます。[Analytics API](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide) は、ユーザー単位・アプリ単位・日単位でアクティビティを内訳表示します。

組織は Claude アカウントで 4 つのアドインすべてにアクセスすることもできますし、既存の LLM ゲートウェイ経由で、Amazon Bedrock、Google Cloud の Vertex AI、Microsoft Foundry 上で動作する Claude モデルにトラフィックをルーティングすることもできます。

Microsoft 365 Copilot のお客様は、[Excel](https://support.microsoft.com/en-gb/topic/choose-your-model-when-editing-with-copilot-in-excel-b2c3b3ec-154b-484b-84d0-914a80df395a) と [PowerPoint](https://support.microsoft.com/en-gb/topic/choose-your-model-in-agent-mode-25ba645b-2932-4f10-a910-fea4ae76d65c) のなかで Claude AI モデルを直接利用することもできます。

## **各組織での Claude for Microsoft 365 の使われ方**

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2be95a402ad3cb9e5ef1_bain-co-logo.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2c0085999666b31fe241_bain-co-logo-dark-mode.svg)

「Claude in Excel のおかげで、私のチームは複雑なモデルの初版をより速く構築できるようになり、モデルの磨き込み、入力と前提のプレッシャーテスト、さらに多くのシナリオやトレードオフの探索に集中できるようになりました。これにより、クライアントとより豊かで深い議論を、より早い段階で交わせるようになっています。」

Gene Rapoport, Head of Private Equity AI Practice

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2c7e3b559bfaa084ac5e_BCI-logo-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2c80dba35f3eb780b917_BCI-logo-dark-mode.svg)

「私たちは Claude に、エグゼクティブの過去のライティングからスタイルガイドを構築するよう指示できます。これにより、EA はそのエグゼクティブの声で自分のメールを下書きできるようになります。チームが手作業で組み立てる時間を取れないような、レバレッジの高い仕事です。」

Ben Letalik, Sr. Director, Digital Transformation & Innovation

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2cf24bd8c16a849d017c_servicenow-dark-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fa2cf434dfc8599b43d17c_servicenow-light-mode.svg)

「Claude for M365 は ServiceNow で急速に普及しています。Claude はツール間でコンテンツを移すよう私たちに頼むのではなく、Excel のなかで自ら作業を進めてくれるので、生産性に段階的な変化をもたらしています。」

Rajeev Sethi, GVP Enterprise Technologies

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f9164fe390163f4c6c6fc9_citadel-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f91652ec3e6676dd8330b8_citadel-dark.svg)

「私たちの投資プロフェッショナルはデータと分析モデルのなかで生きており、Claude for Excel はまさにその場で彼らに寄り添います。アナリストは、カバレッジモデルの構築・更新、シグナルとノイズの分離、そして自分の作業のプレッシャーテストに Claude を活用しており、いずれも効率に段階的な変化をもたらしています。」

Atte Lahtiranta, Head of Core Engineering
