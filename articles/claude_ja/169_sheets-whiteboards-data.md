---
date: '2026-11-10'
final_url: https://claude.com/resources/articles/sheets-whiteboards-data
number: 169
selector_used: article
slug: sheets-whiteboards-data
source_url: https://claude.com/blog/sheets-whiteboards-data
title: Introducing Claude Whiteboards, Claude Sheets, and Claude Data
title_ja: Claude Whiteboards、Claude Sheets、Claude Data のご紹介
---

本日、Claude Whiteboards と Claude Sheets をベータ版としてリリースし、[Claude Dashboards](https://claude.com/resources/articles/dashboards-and-motion) は Claude Data として一般提供（GA）になります。Whiteboards はチームが Claude と一緒にブレインストーミングできる共有ボード、Sheets は Claude があなたと一緒に作成・編集するスプレッドシート、そして Claude Data にはデータストーリー、認定クエリ、ライブ共有が加わります。これらはすべての有料プランでご利用いただけます。

これまで Claude とプロジェクトを進める際には、出力を別のツールやプログラムに移す必要があることが多く、移した先では Claude が進捗や変更をリアルタイムに追うことができませんでした。これからは、ドキュメント、ボード、シート、ダッシュボードを Claude の中に置いたまま、チームで共同編集を続けられます。準備が整ったら、成果物をパートナーのツールに直接取り込み、そこで作業を続けることもできます。

## Claude Whiteboards

多くの人が Claude を思考のパートナーとして使っていますが、Claude とのブレインストーミングでは、その結果を別の場所にコピー＆ペーストしてから、同僚とのブレインストーミングや共同作業を始めるのが一般的でした。これからは、まだまとまっていない計画を Claude と声に出して話し合うだけで、Claude がそれを担当者と日付付きのタイムラインを含むボードに変換してくれるため、チームとリアルタイムで共同作業できます。たとえば振り返りミーティングでは、全員がメモを追加し、Claude がそれをテーマごとにグループ化して、各メンバーのアクションアイテムを下書きできます。ボード上の任意の部分をボックスで囲むようにドラッグすれば、その部分に焦点を当てて Claude に質問することもできます。ブレインストーミングが終わったら、Claude がボードをドキュメントやスライドに変換したり、Lucid、Miro、Vani by Zoho などのツールに取り込んだりできるので、そこでチームと作業を続けられます。

## Claude Sheets

Claude は、タブ、数式、書式設定、ドロップダウンを備えたスプレッドシートを生成できるようになりました。多くの場合、キャンペーントラッカーや採用予算を依頼するようなプロンプト 1 つで作成できます。Claude はセルを直接編集でき、新しい編集箇所はそれぞれ枠で示されるため、変更を追跡できます。シートはチームと共有できるので、あなたと Claude が一緒に作業できます。

現時点では、シートはシンプルなスプレッドシート機能のみを備えていますが、さらに機能を追加すべく取り組んでいます。Excel のフル機能が必要な場合は、ファイルを .xlsx や CSV にエクスポートするか、[Claude for Excel](https://claude.com/claude-for-microsoft-365) をご利用ください。また、Airtable、Asana、monday.com、Smartsheet などのパートナーツールで作業を続けることもできます。

## Claude Data

[Claude Dashboards](https://claude.com/resources/articles/dashboards-and-motion) は 10 月にベータ版としてリリースされ、Amazon Redshift、BigQuery、ClickHouse などのツールにある自社データについて、チームが手軽に質問できるようにしました。本日より、Claude Data として一般提供を開始します。名称を変更したのは、企業によるデータの活用方法はダッシュボードよりも幅広く、製品も今ではより広い働き方をカバーしているためです。認定クエリとライブ共有はベータ版です。Claude Data のチームでの活用例を紹介します。

- **指標の認定済み定義を作成する。** データチームが全員の使うべきクエリを認定できるため、矛盾したデータに基づくダッシュボードを作ったり、それをもとに作業したりすることがなくなります。これらの指標に基づいて作られたチャートには、認定済みであることを示す「certified」バッジが付きます。
- **データからストーリーを作る。** Claude Data で Claude と一緒に、指標からデータストーリーやナレーション付き動画の下書きを作成し、共有前に確認できます。
- **最新の数値を全員と共有する。** ライブ共有を使えば、同僚は共有ダッシュボードを開いたときに最新の数値を確認できます。データを最新に保つコネクタへのアクセス権を持っていなくても問題ありません。閲覧者が見られるのはあなたが承認したクエリの結果だけで、あなたのアクセス権で別のクエリを実行することはできません。
- **ルック＆フィールを揃える。** Claude Data でデザインシステムがサポートされるようになりました。
- **キャッシュで読み込みを高速化する。** これまではダッシュボードを開くたびに毎回再読み込みが行われていました。今後はダッシュボードがキャッシュに対応し、更新頻度をダッシュボードごとに設定できます。
- **変更履歴を追跡する。** Claude Data に変更履歴の機能が加わり、誰が編集したかを確認し、必要に応じて特定のバージョンにロールバックできます。

Claude Data のパートナーには、Amplitude、Mixpanel、Omni、PostHog、Sigma、ThoughtSpot が含まれます。

## 他のツールでも作業できる

本日より、[インタラクティブコネクタ](https://claude.com/resources/articles/interactive-connectors-full-tool) を会話の横やフルスクリーンでフル機能のアプリとして開けるようになりました。Adobe、Atlassian、Box、Notion などのツールで自ら作業することも、Claude に一緒に変更を加えてもらうこともできます。

## はじめに

Claude Whiteboards、Sheets、Data は、Web、デスクトップ、モバイルで利用できます。Claude Data を使うには、データウェアハウスや CRM などのデータコネクタが必要です。

**管理者の方へ：** Team プランでは、3 つすべてがデフォルトで有効です。Enterprise プランでは、Claude Whiteboards と Sheets はデフォルトで無効で、Claude Data は 2026 年 11 月 20 日にデフォルトで有効になります。これらの設定は「組織設定 > アーティファクト」からいつでも変更できます。
