---
date: '2026-11-12'
final_url: https://claude.com/resources/articles/claude-for-manufacturing
number: 174
selector_used: article
slug: claude-for-manufacturing
source_url: https://claude.com/blog/claude-for-manufacturing
title: Introducing Claude for Manufacturing
title_ja: Claude for Manufacturing を発表
---

本日、[Claude for Manufacturing](http://claude.com/solutions/manufacturing) をローンチしました。新規案件の価格見積もりから停止した機械の診断まで、さまざまな業務に対応するスキルを備えたプラグインです。見積担当者は、顧客からの依頼内容を Claude に読ませ、類似案件のコストを比較させ、見積書の下書きを作成させることができるようになりました。このプラグインは、Autodesk Fusion、Infor、Microsoft 365、Oracle NetSuite へのコネクタを通じて、製造業者自身の記録をもとに動作します。Claude for Manufacturing は、成果物が顧客やサプライヤーに届く前に、責任者がその内容を確認・承認できるように設計されています。

製造業のチームは、1 日の多くの時間を情報収集に費やしがちです。Manufacturing Leadership Council が 2025 年に実施した調査では、製造業者の 79% が[データを手作業で入力している](https://manufacturingleadershipcouncil.com/survey-october/)と回答しました。Claude が各プロセスをレビューの段階まで進めることで、見積担当者は価格に、品質エンジニアは対策に、技術者はまず何を確認すべきかに集中できるようになります。

## **製造業者のために作られたスキル**

このプラグインには 17 のスキルが含まれており、営業、品質、オペレーション、サプライチェーン、設計、セットアップをカバーしています。単一のタスクを処理するスキルもあれば、複数のタスクを順に実行するスキルもあるため、Claude は人によるレビューが必要になるまで、複数のステップにわたって業務を進めることができます。スキルで実行できるプロセスには、次のようなものがあります。

- **新規案件の見積もり**: 見積担当者は Claude に、顧客の依頼内容を読み、不足している情報を洗い出し、類似案件のコストを比較し、発行用の見積書を下書きするよう依頼できます。
- **検査不合格の調査**: 品質エンジニアは Claude に、不合格の内容を記録し、同じ問題に関する過去の報告書を確認し、考えられる原因を順位付けし、是正処置報告書を下書きさせることができます。
- **故障の診断**: 技術者は Claude に、センサーのエクスポートデータ、修理記録、写真、マニュアルを読ませ、考えられる原因を順位付けさせたうえで、自ら確認して次の対応を判断できます。
- **別サプライヤーからの調達**: 購買担当者は Claude に見積依頼書を準備させ、返ってきた入札内容を比較させることができます。
- **Autodesk Fusion を使った設計比較**: エンジニアは Claude に、既存モデルからバリエーションを生成させ、エンジニアの目標値に照らして評価させ、意思決定メモを下書きさせることができます。
- **生産状況のレポート**: 工場長は Claude に生産データを 1 つのレポートにまとめさせ、目標に対する生産量、設備のダウンタイム、そしてダウンタイムや生産未達によるコストを示すことができます。

これらのスキルは出発点にすぎません。各組織はこれらをベースに、自社の業務に合わせて拡張できます。また、今後も製造業向けのスキルを追加していく予定です。

## **製造システムへのコネクタ**

Claude for Manufacturing は、製造業務の中核を担うソフトウェアと連携します。そして、それらのソフトウェアは引き続き、チームが事業を運営するうえでの中心であり続けます。

- **Autodesk Fusion**: Claude が既存モデルからバリエーションを生成するため、エンジニアは 1 つに決める前に、より多くの設計案を比較できます。
- **Infor**: Claude が Infor で発注書や在庫を照会するため、購買担当者や計画担当者は行動する前にそれらを確認できます。
- **Microsoft 365**: Claude が共有フォルダや受信トレイから手順書、サプライヤーとのメール、エクスポートされたレポートを見つけ出すため、品質エンジニアはそれらを 1 つの業務にまとめられます。
- **Oracle NetSuite**: Claude が見積書を下書きする際に実際の受注、在庫、生産工程、案件コストの記録を取得するため、見積担当者はそれらに基づいて新規案件の価格を設定できます。

製造業者は、コネクタのないシステムでもこのプラグインを利用できます。それらのシステムから定期的にエクスポートしたデータを Microsoft 365 に保存すれば、Claude がそのファイルをもとに見積書を下書きしたり、生産レポートをまとめたりします。

## **Claude から Infor を更新する**

製造業者向けの基幹ソフトウェアを手がける Infor も、[独自のプラグインをリリース](https://claude.ai/redirect/claudedotcom.v1.6c3e0985-e562-42c1-bdc3-827696b5657e/directory/infor)します。Claude for Manufacturing の Infor コネクタでは記録を照会できますが、Infor のプラグインを使えば、Claude から Infor 上のデータを変更することもできます。

たとえば、鋼材の納入が 2 週間遅れた場合、購買担当者は Claude に、影響を受ける顧客注文はどれか、他の拠点にどれだけの鋼材があるかを尋ねることができます。購買担当者が承認すれば、Claude は Infor 上で別のサプライヤーへの発注書を発行し、影響を受ける生産のスケジュールを組み直せます。Claude のアクセス権限は、購買担当者の Infor 上の権限に従います。

## **製造チームが主導権を握り続ける**

スキルはユーザーによるレビューで終わるように設計されています。見積担当者が見積書を確認して発行し、品質エンジニアが是正処置報告書に記載する対策を検証します。このレビューを支援するため、Claude は数値や主張を、その根拠となるデータや文書にリンクさせることができます。

Claude for Manufacturing は設備を操作しません。その領域に向けて、Anthropic は [Model Hardware Standard](https://www.anthropic.com/news/model-hardware-standard-research-preview) を開発しています。これはリサーチプレビューとして提供されており、プログラム可能な設備が自らの計測値、設定、安全上の制限を記述するための標準的な方法を提供するものです。

## **始め方**

Team プランまたは Enterprise プランをご利用の場合は、[プラグインをインストール](https://claude.ai/redirect/claudedotcom.v1.6c3e0985-e562-42c1-bdc3-827696b5657e/customize/plugins/id/45112ff2-6233-4954-b8ec-c448ef2d1e59%40anthropic-plugin-directory)し、Claude に「Set us up.」と伝えてください。Claude がチームで使用しているシステムを尋ね、コネクタをテストし、まだ完全には実行できないスキルを報告します。

プラグインの実際の動作をご覧になりたい方は、11 月 17 日午前 11 時（米国東部時間）開催の[技術ウェビナーにご登録ください](https://claude.com/resources/webinars/claude-for-manufacturing-put-your-plants-know-how-to-work)。自社の製造システムについてご相談されたい場合は、[営業チームにお問い合わせください](https://claude.com/contact-sales)。
