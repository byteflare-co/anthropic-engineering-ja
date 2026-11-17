---
date: '2026-09-15'
final_url: https://claude.com/resources/articles/salesforce-in-claude
number: 192
selector_used: article
slug: salesforce-in-claude
source_url: https://claude.com/blog/salesforce-in-claude
title: Bringing Salesforce into Claude
title_ja: Salesforce を Claude の中へ（Bringing Salesforce into Claude）
---

# Salesforce を Claude の中へ（Bringing Salesforce into Claude）

本日、Salesforce in Claude をベータ版としてリリースします。これは Salesforce と共同で構築したプラグインで、営業担当者のアカウント、商談、パイプラインを、既存の Salesforce の権限のまま Claude に取り込みます。アカウントリサーチ、商談準備、パイプラインレビュー、CRM の更新など、アカウントエグゼクティブが日々行う業務向けの 37 個の[スキル](https://claude.com/resources/articles/skills)が含まれています。

営業担当者は、Salesforce、メール、通話録音、Slack に散らばった情報を手作業で集め、顧客との打ち合わせの準備やフォローアップ作業に一日の何時間も費やしていることがよくあります。この新しいプラグインを使えば、Claude がそうした事務作業を引き受け、営業担当者が承認した時点で Salesforce を更新します。

プラグインには 2 つのコネクタも含まれており、管理者が Salesforce を接続し、営業担当者がサインインすればすぐに使い始められます。Salesforce コネクタにより、Claude は Salesforce のデータを読み取って操作できます。たとえば、アカウントの履歴の要約、商談の更新、通話の記録、フォローアップタスクの作成などです。Slack コネクタは、スキルが読み書きできる案件チャンネルの要約やアカウントチームのスレッドをカバーします。営業担当者が初めてプラグインを使うときには、セットアップ用のスキルが利用中のツールとコネクタを特定し、その人の役割と担当顧客に合わせた Claude Artifact を作成します。

## 営業担当者が今日から Salesforce in Claude を使う方法

**ブリーフィングで一日を始める。** Claude は毎朝、その日の打ち合わせ、間もなくクローズする案件、リスクのある商談、返信が必要な未読スレッドをまとめたパーソナライズされたブリーフィングを届けます。一度スケジュールを設定すればバックグラウンドで実行され、外出先の Claude アプリを含め、Claude が使えるところならどこからでもアクセスできます。ブリーフィングから、クローズ日の延期、ステージの変更、フォローアップタスクの追加を Claude に指示すれば、Claude が Salesforce を更新します。金曜日には、ブリーフィングが一週間を総括し、マネージャー向けの報告の下書きを作成します。

**通話の準備をする。** 営業担当者が次の打ち合わせの準備を Claude に頼むと、Claude は Salesforce、Slack、メールから情報を集めてブリーフィングを作成します。進行中の商談とそれぞれの状況、今週アカウントチームで話し合われた内容、未返信のスレッド、過去の通話から持ち越された未解決の質問などです。それらのスレッドの中にまだ Salesforce に登録されていない関係者が見つかれば、Claude はその人をアカウントの取引先責任者として追加します。

**案件をレビューし、クロージングプランを作る。** 商談を指定すると、Claude はチームの営業手法に照らしてその案件を評価し、クオリフィケーションの不足、まだ会っていない関係者、クローズ日を危うくしている要因を洗い出します。さらに続けるよう頼めば、ビジネスケースと日付入りの相互クロージングプラン（mutual close plan）を起草し、クオリフィケーション項目を埋め、不足している関係者を取引先責任者の役割として追加します。これらはすべて、承認された時点で商談に保存されます。

**すべての打ち合わせを、Salesforce が更新された状態で終える。** 各通話の後、Claude は文字起こしや営業担当者のメモをもとに、フォローアップメール、Slack の案件チャンネル向けの要約を作成し、次のステップ、ステージ、クローズ日といった商談の更新内容を下書きして、営業担当者のレビューに回します。

**パイプラインをレビューし、予測を共有する。** 営業担当者がパイプラインの表示を求めると、Claude はステージ別のカバレッジ、最も遅れそうな案件とその理由、アカウント単位のドリルダウンを示すインタラクティブなダッシュボードを構築します。ダッシュボードからクローズ日の変更やステージの変更を指示すれば、Claude が Salesforce のレコードを更新します。ダッシュボードはリーダー層やチームと共有でき、Claude はリーダー層が求める形式で予測の説明文を下書きすることもできます。営業リーダーは同じビューをチーム全体に対して実行できます。

**組織の既存の権限の上に構築**
Salesforce は引き続き記録システム（system of record）であり続けます。営業担当者は自分の Salesforce 認証情報でサインインし、Claude はその権限で許可された範囲のデータだけを読み取ります。デフォルトでは、Claude は提案した変更を書き込む前に、一つひとつ営業担当者に承認を求めます。Team プランと Enterprise プランでは、デフォルトでお客様のデータをモデルの学習に使用しません。

管理者は組織として一度 Salesforce を接続し、どのグループにプラグインを提供するかを選択します。

## **営業チームは Salesforce in Claude をどう活用しているか**

Anthropic の顧客である GitLab、Siemens、Legora は Salesforce in Claude を組織に導入しており、また 7,000 人の Salesforce の営業担当者が業務で使用しています。Salesforce in Claude の利用について、次のような声が寄せられています。

> 「Salesforce in Claude によって、当社の営業担当者はライブデータから打ち合わせのブリーフィングを、数時間ではなく数秒で作成できるようになりました。営業チームが拡大するなかでも、新しく加わる担当者は皆、当社がサービスを提供する法律事務所の全体像を把握した状態でスタートできます。」 — David Eckstein, Chief Financial Officer, Legora

> 「Salesforce in Claude があれば、営業担当者はパイプラインレビューがすでに済み、アカウントの履歴もすでに揃った状態で一日を始められます。その分の時間は、そのまま顧客との対話に充てられます。」 — Alexa Vignone, President and Chief Revenue Officer, Salesforce

## **はじめに**

Salesforce in Claude は、Claude のすべての有料プランでベータ版として利用できます。[Salesforce MCP](https://claude.ai/redirect/claudedotcom.v1.e99779ba-53b6-469f-9481-ce5276e9a73a/directory/bundles/salesforce#directory/connectors/salesforce-headless-360) は本日からマーケットプレイスで直接インストールできます。プラグインをインストールするには、管理者が [AgentExchange](https://agentexchange.salesforce.com/sales-cloud-in-claude-beta-access) からアクセスをリクエストし、組織全体に対して一度 Salesforce を接続します。管理者向けには、組織でこの機能を有効にする手順をまとめた[セットアップガイド](https://support.claude.com/en/articles/16952184)を用意しています。営業リーダー向けには、[Claude を使って効果的な営業組織を運営するためのガイド](https://claude.com/resources/articles/building-an-ai-native-revenue-organization)を用意しています。
