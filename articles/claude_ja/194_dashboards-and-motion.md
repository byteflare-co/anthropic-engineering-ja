---
date: '2026-10-08'
final_url: https://claude.com/resources/articles/dashboards-and-motion
number: 194
selector_used: article
slug: dashboards-and-motion
source_url: https://claude.com/blog/dashboards-and-motion
title: Build live dashboards and animate explainers with Claude
title_ja: Claude でライブダッシュボードを構築し、アニメーションで解説する（Build live dashboards and animate explainers with Claude）
---

# Claude でライブダッシュボードを構築し、アニメーションで解説する（Build live dashboards and animate explainers with Claude）

本日より、Claude はあなたのデータを常に最新の状態に保たれるダッシュボードに、そしてあなたのアイデアを次のプレゼンテーション向けのアニメーション解説動画に変えられるようになりました。Claude Dashboards は BigQuery、Databricks、Snowflake などのデータプラットフォームや、Salesforce などの CRM ツールに接続でき、有料プランでベータ版として提供されます。Claude Motion は Team および Enterprise プランでベータ版として提供されます。Claude Docs、Slides、Design はベータ版を終了し、Free を含むすべてのプランでご利用いただけます。

[社内データについて質問する](https://claude.com/resources/articles/how-anthropic-enables-self-service-data-analytics-with-claude)には、通常はチケットを起票するか SQL を書く必要があります。また、動きで見せたほうが伝わるアイデアも、たいていは静的なスライドがまた 1 枚増えるだけで終わってしまいます。その結果、人々は待たされるか、諦めてしまいます。これまでも Claude はその一部をお手伝いできました。これからは、ダッシュボードやアニメーションそのものを依頼でき、Claude がそれをどのように作ったのかも確認できます。各チャートにはその背後にあるクエリが表示され、各アニメーションは編集可能なコードとして構築されます。最初のバージョンは Claude が作り、何を共有するかはあなたが決めます。

## Claude Dashboards：社内データにすばやく質問する

Amazon Redshift、BigQuery、ClickHouse、Databricks、Snowflake などの社内データプラットフォームを接続し、普段の言葉で質問してください。Claude はデータから答えを引き出してダッシュボードを構築し、データの変化に合わせて最新の状態に保ちます。他のコネクタとも連携できます。たとえば、Salesforce の商談（opportunities）のダッシュボードを依頼することもできます。Dashboards は、今週のサインアップ数が先月と比べてどうかといった、すばやく探索的な質問に適しています。任意の数値をクリックするとその背後のクエリを確認でき、Claude に説明を求めることもできます。各チャートには、データが最後に更新された日時が表示されます。

![Claude が 1 年分の乗車データからバイクシェアのダッシュボードを構築し、利用回数の合計と、日別・時間帯別の乗車数のチャートを表示している。](https://assets.claude.com/7688d4d3b888c17cf4b3553f537f291882a92656.png)

Dashboards は、お使いの BI ツールや分析ツールと並行して機能します。より深い分析が必要な質問の場合は、Claude からダッシュボードを Amplitude、Grafana、Hex、Mixpanel、Omni、Perplexity、PostHog、Sigma に直接送り、そこから分析を続けることができます。Databricks Genie、Looker、monday.com、Tableau にも近日対応予定です。

## Claude Motion：アイデアをアニメーションで説明する

四半期レポートを全社ミーティング向けの 30 秒の解説動画にする、取締役会資料のチャートに動きを加える、顧客オンボーディング用の製品ウォークスルーを作る、といったことを Claude に依頼できます。Claude はプロンプトからアニメーションを構築し、それは短い動画のように再生されます。エディタで調整したり、Claude に変更を依頼したりしたうえで、MP4 ファイルとしてダウンロードできます。

![Claude のメッセージ入力欄に「/motion」と入力すると、Motion のオプションが表示される。](https://assets.claude.com/46f88e8de631c732fa245ad453262e6ef35c0e73.png)

Claude Motion は、あなた自身の仕事を説明するために作られています。Claude はテキスト、チャート、図形、画像をアニメーション化するコードを書くため、どの単語、数値、タイミングでも変更できます。動画生成モデルは使用していないため、生成された映像や AI が生成した人物は含まれません。さらに作り込みたい場合は、Adobe、Descript、HeyGen、Higgsfield、invideo、Luma AI、Runway で開くことができます。Canva と Captions にも近日対応予定です。

## Docs、Slides、Design が日常業務で使える準備が整いました

[すべての Claude の会話に Docs、Slides、Design を導入して以来（新しいタブで開きます）](https://claude.com/resources/articles/cowork-is-now-claude)、Claude で作成された[ドキュメント、資料、デザイン](https://claude.com/resources/articles/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them)は 4,500 万件を超えました。それ以降にリリースした機能の多くは皆さまのフィードバックから生まれたもので、日々の使いやすさを高めています。そこで、ベータ版のラベルを外すことにしました。

- **エンタープライズ対応。** Artifacts が CMEK に対応し、管理者は組織で使用するアーティファクトのテンプレートを選択できるようになりました。
- **チームで編集。** チームと Claude が、同じドキュメント、資料、デザイン、ダッシュボードで共同作業できます。
- **チームの外にも共有。** 管理者が許可していれば、スライド、デザイン、ダッシュボード、アニメーションを組織外の人や、リンクを知っている誰とでも共有できます。
- **書式を保ったエクスポート。** PowerPoint や PDF でダウンロードしても、エディタで作ったとおりの見た目になります。また、資料は編集可能なファイルとして[Google Slides に直接送れます](https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides)。
- **スマートフォンで編集。** Claude モバイルアプリから、ドキュメント、資料、デザインを変更できます。

## Claude Design は Claude の中に移りました

Claude Design は、独自の URL である claude.ai/design で始まりました。9 月 16 日以降、Design はすべての Claude の会話の中でも動作するようになり、あなたのコンテキスト、ファイル、コネクタを活用できます。2 つのバージョンを運用していると両方の修正が遅くなるため、スタンドアロンのサイトを Claude に統合します。移行の時間を確保できるよう、[claude.ai/design（新しいタブで開きます）](http://claude.ai/redirect/claudedotcom.v1.bf0b37e9-4395-48a9-a56e-a963a6c21dea/design) は 12 月 14 日まで引き続き利用できます。

- **今すぐデザインシステムを移行しましょう。** Claude の Artifacts ページで「Migrate team design systems」をクリックしてください。1 回の移行で組織内のすべてのデザインシステムが移され、元のデザインシステムはスタンドアロン版が終了するまで変更されずに残ります。
- **プロジェクトについては、現時点で対応は不要です。** スタンドアロン版が終了するまで、引き続きそちらで動作します。
- **チャットとコメントを保存しましょう。** Claude とのチャットやプロジェクトへのコメントはスタンドアロン版に残り、終了後は利用できなくなります。スタンドアロンのプロジェクトへの公開リンクも、その時点で機能しなくなります。

詳しくは[移行ガイド（新しいタブで開きます）](https://support.claude.com/en/articles/17440474)をご覧ください。

## はじめに

Claude を開き、「この四半期の地域別売上のダッシュボードを作って」「セールスキックオフ向けに、料金プランの比較をアニメーションにして」「このメモを月曜日用の資料にして」のように、必要なものを依頼してください。まずは、いつも待たされているダッシュボードや、スライド 1 枚では伝えきれないレポートから始めてみましょう。

**Enterprise 管理者の方へ：** Dashboards と Motion はデフォルトでオフになっており、「組織設定 > Artifacts」からオンにできます。Docs、Slides、Design は 10 月 15 日にデフォルトでオンになりますが、今すぐオンにすることもできます。
