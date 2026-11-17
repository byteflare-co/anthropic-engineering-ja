---
date: '2026-11-10'
final_url: https://claude.com/resources/articles/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors
number: 168
selector_used: article
slug: more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors
source_url: https://claude.com/blog/more-ways-to-work-with-claude-sheets-whiteboards-and-interactive-connectors
title: 'More ways to work with Claude: Sheets, Whiteboards, and Interactive Connectors'
title_ja: "Claude との新しい働き方: Sheets、Whiteboards、インタラクティブコネクタ"
---

私たちは、Claude Code が開発者の働き方を変えていく様子を見てきました。エンジニアは 1 行ずつ手作業でコードを書くことから、アイデアを説明して Claude が作ったものをレビューするスタイルへと移行しました。それは、ものづくりの喜びを彼らに取り戻させました。私たちの目標は、その魔法をあらゆるチームに届けることであり、本日、Claude で実現できることを広げます。新しいアーティファクトの種類として **Claude Sheets**、**Claude Whiteboards**、**Claude Data** を導入します。また、**インタラクティブコネクタ** のアップグレードにより、普段最もよく使うアプリでの作業がより簡単になります。**Claude Meetings** も近日公開予定です。

## すべてのコネクタとコンテキスト

Claude Code では、Claude が必要とするコンテキストはすでにコードベースの中にあります。しかし他のチームでは、コンテキストはメール、アプリ、ドライブに散らばっています。Claude はそうしたコンテキストに、[Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)（MCP）上に構築されたコネクタを通じてアクセスします。MCP は、AI を普段使っているツールと接続するために私たちが導入したオープン標準です。[Claude Marketplace](https://claude.com/resources/articles/claude-marketplace) には、コミュニティが構築したものを含め、9,000 を超えるコネクタとプラグインが掲載されています。

[**インタラクティブコネクタ**](https://claude.com/resources/articles/interactive-connectors-full-tool) は、これをさらに一歩進めます。本日から、パートナーは自社のアプリを Claude に直接埋め込めるようになり、タブを切り替えることなく Adobe や Atlassian などで作業できます。[Salesforce](https://claude.com/resources/articles/salesforce-in-claude)（ベータ）、NetSuite、Workday（ベータ）のプラグインにはスキルが組み込まれているため、営業担当者は商談の準備を、経理担当者は財務データの分析を、人事チームは休暇や経費の処理を行えます。

## チームで、より速くアイデアを形にする

本日から、Claude はチームと一緒にスプレッドシート、ホワイトボード、ダッシュボードを作成できるようになります。これらは、[ドキュメント、スライド、デザイン](https://www.youtube.com/watch?v=To5nrYqvR44) を作成する既存の機能や、コンテンツを短いアニメーションに変換できる [Claude Motion](https://support.claude.com/en/articles/17454997-get-started-with-claude-motion)（ベータ）と連携して動作します。いずれにおいても Claude は必要なことをすばやく汲み取るため、仕事のペースを決めるのはあなたの思考です。

- [**新しいアーティファクトの種類**](https://claude.com/resources/articles/sheets-whiteboards-data):
  - Claude Sheets では、チームと Claude が一緒にスプレッドシートを作成し、共同でデータを整理し、数式を作成・編集し、複数のタブにまたがって作業できます。
  - Claude Whiteboards はデジタルホワイトボードです。会議中にチームでアイデアを並べて整理し、その後 Claude に結果の要約を依頼できます。
  - Claude Data（旧 Dashboards）は Snowflake や Salesforce などのツールと接続し、データチームが認定した定義（ベータ）を使って、ダッシュボード、ビジュアルなデータストーリー、ナレーション付きの短い動画を作成できます。

また、アカウントトラッカー、デイリーブリーフィング、プロジェクトのステータスボード、契約レビュー表など、チームの働き方に合わせたカスタムアーティファクトを Claude に作ってもらうこともできます。Claude はすべてのステップで同じコンテキストを引き継ぐため、詳細を説明し直さなくても、アイデアをホワイトボードからスプレッドシート、さらにダッシュボードへとつなげていけます。

近日公開予定の **Claude Meetings** では、通話に Claude を参加させ、メモを取らせたり、会話中にチームが作業しているドキュメントを更新させたりできるようになります。

## すでにこの働き方を実践しているチーム

Anthropic 社内では、技術職ではないチームも、エンジニアと同じくらい Claude を活用し始めています。法務チームは Claude と協力して、チーム独自のプレイブックに基づいて自動的に修正提案（レッドライン）を作成する、Slack ベースの法務レビューツールを構築しました。これによりマーケティング関連のレビューは 3 日から 24 時間に短縮され、簡単な修正は弁護士がドラフトをレビューする前に済むようになりました。財務チームは、経営陣向けの長い事業報告ドキュメントをインタラクティブなページに作り替え、今ではチーム全員が Claude と一緒にそれを更新しています。

どちらのチームもコードは書きませんが、それぞれの分野のエキスパートです。彼らは Claude を使ってその知識をツールに変え、自分たちの時間を節約し、さらに他の人も使えるようにしました。私たちの顧客も、同じように働いています。

![Datadog](https://assets.claude.com/0a17621af2bfc623c9104a3dd9fba2e6ebfc89d5.svg)

> 「Datadog では、Claude の活用がコーディングからナレッジワークへと広がっています。プロダクトマネージャーは Claude を使って、アイデアから機能概要、PRD、テスト可能なプロトタイプまでをはるかに速く進めており、顧客のニーズ、プロダクトの判断、そして解くべき正しい課題に集中する時間が増えています。Datadog では、誰かが Claude で良いものを作ると、それがすぐに広まります。」

Yanbing Li 氏、Chief Product Officer、Datadog

![Gusto](https://assets.claude.com/8a33e695a4b145386eca05940de86cb5782b22c3.svg)

> Gusto では、商事法務チームの 1 人のメンバーが、交渉済みの条件を署名可能な契約書に変換するツールを数時間で構築しました。所要時間は 1 週間以上から数時間に短縮され、交渉された内容は引き続きその担当者がレビューしています。

Gusto

![Hubspot](https://assets.claude.com/d6f4aa0286766975a05548621fb66283ec2bfe32.svg)

> 「Claude と HubSpot はシームレスに連携するので、私たちの CSM はすべての商談に必要なコンテキストを揃えて臨めます。Claude のライブダッシュボードは HubSpot からデータを取得し、各商談で重要なことや次に連絡すべき顧客を表示します。フォローアップメールは通話終了から 30 分以内に下書きされます。かつて毎週何時間もかかっていた作業がバックグラウンドで動くようになり、チームは顧客がより良いソリューションを構築し、価値を実証し、より良く成長できるよう支援することに集中できます。」

Jon Dick 氏、Chief Customer Officer、Hubspot

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> 「Accenture では、Claude が法務チームの働き方の変革を後押ししています。法務ワークフローを再構想し、法務プロフェッショナルがビジネスを支援する新しい方法を切り拓く機会に、私たちは大きな期待を寄せています。」

Mindy Lok 氏、Legal Chief Technology Officer、Chief Intellectual Property Officer、Accenture

![Advantage Solutions](https://assets.claude.com/97c2cf17bb75ef2c4f1d0986904838b87ab4f8b5.svg)

> 「私たちの FP&A チームは、予測サイクルごとにスライド、コメント、検証に約 10 時間を費やしていました。その取りまとめ作業を Claude で自動化し、30 分未満にまで短縮しました。Claude がそのすべてを肩代わりしてくれたのです。今では、財務が本来やるべきこと、つまりインサイトを見つけて意思決定を推進することに取り組んでいます。これほどの規模のビジネスを支えるチームにとって、意味のある変化です。」

Ash Gupta 氏、Director of Financial Planning and Analysis、Advantage Solutions

## エンタープライズのために、エンタープライズとともに構築

Claude がより多くのツールと接続するようになるにつれ、企業にはそのアクセスやアクションを監督するためのより良い方法が必要になります。私たちは、企業が自社の要件を満たせるようセキュリティとコンプライアンスの制御を組み込んでおり、私たち自身の最も機密性の高い業務にも同じ Claude を使っています。Enterprise プランでは、管理者が誰がどのプロダクトやコネクタを使えるかを決め、組織の利用上限をきめ細かく設定できます。

その制御は、Claude が接続するツールにも適用されます。対象の Team プランおよび Enterprise プランでベータ提供中の [**Claude auto-connect**](https://support.claude.com/en/articles/15537633-auto-connect-your-organization-s-apps-to-claude) を使えば、Notion、Atlassian、Dropbox などのアプリの接続は一度設定するだけで済みます。従業員は各ツールを個別に接続する代わりに、Claude でそのツールを初めて使ったときに自動的に接続されます。

どのような方法でツールを接続しても、Claude は既存の権限の範囲内で動作します。管理者は各コネクタで可能な操作を制限することもでき、たとえば Claude が Slack を読むことはできても、あなたに代わってメッセージを送信することはできない、といった設定が可能です。

機密性の高いビジネスデータの保護は私たちの開発の中核であり、Claude がより長く複雑な作業を担うようになるにつれ、その保護を引き続き強化しています。

- [Enterprise 組織のデータ](https://claude.com/resources/articles/unified-claude-enterprise) は、転送中も保存時も暗号化されます。
- Enterprise プランでは、セキュリティチームが監査ログと Compliance API を通じて [Claude の利用状況を把握できます](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations)。Compliance API は、Splunk や CrowdStrike を含む 100 以上のセキュリティ・コンプライアンスツールと連携します。
- Enterprise 向けの新しい Claude エクスペリエンスでは、各クラウドセッションがそれぞれ独立した [隔離された仮想マシン](https://claude.com/resources/articles/unified-claude-enterprise) で実行され、コネクタの認証情報はその外部に保持されます。

## アイデアに追いつく仕事のかたち

現代の仕事はソフトウェアを中心に組み立てられていますが、Claude はあなたを中心に動きます。接続したツールを通じてチームの仕事を理解し、必要な形式でアイデアを形にする手助けをし、管理者が設定した制御の範囲内で動作します。その結果、集中して大きな目標に向けて前進するための時間が増えます。
