---
date: '2026-11-23'
final_url: https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards
number: 204
selector_used: article
slug: zero-data-retention-with-enterprise-frontier-safeguards
source_url: https://claude.com/blog/zero-data-retention-with-enterprise-frontier-safeguards
title: Zero data retention with Enterprise Frontier Safeguards is now in beta
title_ja: "Enterprise Frontier Safeguards によるゼロデータ保持がベータ版で利用可能に（Zero data retention with Enterprise Frontier Safeguards is now in beta）"
---

ここ数か月、私たちはビジネス顧客向けに Enterprise Frontier Safeguards（EFS）の開発を進めてきました。EFS は、高度な悪用を最先端の精度で検出しながら、ゼロデータ保持（ZDR）とも両立します。つまり、Anthropic もクラウドプロバイダーも、企業のデータを保持しません。

[9 月に EFS を発表](https://www.anthropic.com/news/enterprise-frontier-safeguards)して以来、私たちは 100 社を超える顧客とともに EFS の開発をさらに進めてきました。その中には Fortune 100 企業の 4 分の 1 や、データの可視性に厳格なルールがある業界（ヘルスケア、金融サービス、法務など）の多くの企業が含まれています。Bridgewater、Salesforce、Stripe といった先進的な企業が、プライベートベータで EFS を評価してきました。

![Comcast](https://assets.claude.com/f0caec900385c80cdaddb5e06e70d0c207863316.svg)

> 「重要インフラを運営する企業として、私たちにとって安全性はモデルの能力と同じくらい重要です。強力なセーフガードを得ながら、データを自社のアカウント内に保持できるソリューションが必要でした。Enterprise Frontier Safeguards はまさにそれを実現してくれます。」

Noopur Davis 氏、EVP, Chief Information Security and Product Privacy Officer

![Stripe](https://assets.claude.com/0e2493b60dbe1a71a144ca649e1916bade399bf7.svg)

> 「Stripe にとって、顧客データの保護は事業運営の根幹です。Anthropic の Enterprise Frontier Safeguards により、悪用に対する保護を強化したうえでフロンティアモデルを利用できるようになります。また、会話ログを Stripe の AWS 環境内に保持し、そのアクセスとレビューを Stripe のセキュリティ管理のもとで統制することも可能になります。」

Matthew Kemelhar 氏、Head of Security

![Cisco](https://assets.claude.com/49dd4517ec32bf73cf3b4c159439f4ea5a4692f3.svg)

> 「EFS を使えば、顧客は機密データを自社の環境内に置き、自社の暗号鍵で保護しながら、フロンティアの能力に求められる専門的な安全メカニズムも維持できます。フロンティアモデルの安全性を手放すことなく、企業が自社データの管理権を保てるというこのバランスこそが、Cisco のようにセキュリティに敏感な組織で高度な AI が広く採用されるために不可欠です。」

Omar Santos 氏、Distinguished Engineer

![Wells Fargo](https://assets.claude.com/18e8dec2ece0d685715d94078c742b0a4c2eaa20.svg)

> 「Enterprise Frontier Safeguards は、まさに私たちが求めていたものを提供してくれます。ログは Wells が管理する鍵のもと、Wells が管理する環境に保存されます。データの管理権は私たちが持ち、検出は Anthropic が担います。この役割分担があるからこそ、私たちのチームはフロンティアモデルを安全に活用し、顧客、従業員、規制当局に対する義務を果たすことができます。業界がこうしたセーフガードを必要としているからこそ、私たちはその形成に協力しました。」

Munish Kumar Sharma 氏、Chief Information Security Officer

![KPMG](https://assets.claude.com/b2a943197cdf8a11b2ac7b63ecee2763fe5cc652.svg)

> 「規制対象のデータや機密性の高いデータを扱う場面で、ゼロデータ保持に対応した Enterprise Frontier Safeguards があれば、規制が厳しく機密性の高いクライアント案件全体にわたって、自信を持って AI の展開を加速できるようになります。」

Todd Lohr 氏、US Vice Chair and Head of Client Technology & Innovation

そして今回、EFS をパブリックベータとして公開します。本記事では、EFS の仕組み、ZDR との両立方法、そして企業がベータプログラムに参加する方法について詳しく説明します。

## EFS が ZDR のもとで自動安全モニタリングを提供する仕組み

従来の ZDR を利用している顧客は、Claude の[分類器](https://www.anthropic.com/research/next-generation-constitutional-classifiers)によって保護されています。これは個々のリクエストをスクリーニングし、害を引き起こす可能性があるかどうかを評価するリアルタイムの[セーフガード](https://www.anthropic.com/news/building-safeguards-for-claude)です。しかし、高度な攻撃は一般に複数のクエリにまたがって行われ、個々のリクエストは単独で見ると無害に見えることがあります。

たとえば、9 月の[脅威インテリジェンスレポート](https://www.anthropic.com/threat-intelligence-report-september-2026#cyber-operations-sep-26)では、約 50 の組織を標的とした作戦について説明しています。この作戦では、ある AI エージェントが攻撃の作業を、並列に動作する多数の他のエージェントに分割していました。収集した認証情報はセッション間で保存され、攻撃者が容易にキャンペーンを再開できるようになっていました。リクエストを 1 件ずつ見ると、この攻撃は個別の、より無害なタスクに見えていたはずです。

こうした攻撃を捕捉するために、私たちは自動安全モニタリングと呼ばれる第 2 の防御層を使用しています。この層は、多数のリクエストにまたがる悪用のパターンを探します。EFS を通じて、Anthropic は顧客データを一切保存することなく自動安全モニタリングを提供できます。自動安全モニタリングシステムは、完全に顧客が管理するインフラストラクチャ上に保存されたデータを分析します。

![従来の ZDR と EFS ZDR の比較。どちらも Claude のアラインメントとリアルタイム分類器を使用しますが、EFS ZDR のみが自動安全モニタリングを追加します。これはリクエストに分割された攻撃を検出し、レビュー用のケースを作成します。](https://assets.claude.com/407895af12324a5800318809efd87eda92ff500d.webp)

自動安全モニタリングがリスクを発見すると、レビュー用の Safety Case が作成されます。これらのケースはクラウドストレージから、または API 経由で読み取ることができ、セキュリティ情報イベント管理（SIEM）システムと統合することもできます。ケースには入力と出力は含まれません。

![Safety Case の例を 2 つの視点から示した図。ケース ID、危害カテゴリ、ステータス、フラグが付いたトランスクリプト ID はお客様のチームと Anthropic の双方が閲覧できますが、入力と出力を読めるのはお客様のチームだけです。説明用の例であり、詳細はすべて架空のものです。](https://assets.claude.com/debb29b66026bd3e0a55de89f8884d8ffe903570.webp)

設定が完了すると、自動安全モニタリングは、深刻な害につながりうる意図的な悪用（攻撃的なサイバー作戦など）の検出に役立ちます。また、ユーザーの意図を超えた行動をとるエージェント、たとえば極端なケースではソフトウェアのエクスプロイトを使って社内データベースや外部システムにアクセスするようなエージェントの検出にも役立ちます。

## ゼロデータ保持と EFS

EFS では、入力と出力を保存するためのストレージをお客様自身が用意します。お客様が管理するストレージにデータが届けられた後は、Anthropic もクラウドプロバイダーもデータのコピーを保持しません。これにより、次のことが保証されます。

- **ゼロデータ保持**：Anthropic もクラウドプロバイダーもお客様のデータを保持しません。お客様は自身のストレージを用意し、自身のデータを保存します。入力と出力は、お客様のストレージに書き込まれた後、速やかに削除されます。アクセスポリシーと監査ログはお客様自身が設定し、安全データはお客様自身の鍵で暗号化します。
- **運営者による人手でのレビューなし**：Anthropic とクラウドプロバイダーのいずれの担当者も、お客様の入力と出力にアクセスしません。このデータにアクセスできるのは自動安全モニタリングのみです。
- **お客様のデータでトレーニングは一切行いません**：入力と出力は自動安全モニタリングにのみ使用され、モデルや分類器のトレーニングに使われることは決してありません。

![EFS のアーキテクチャ。自動安全システムは、お客様のクラウドアカウント内のストレージに安全データを書き込み、モニタリングのためにそれを読み取ります。Anthropic が受け取るのは安全に関する連絡とモニタリングのメタデータのみで、入力、出力、その抜粋を受け取ることはありません。](https://assets.claude.com/e1deaac362da2eb9fac5d8dc38feebc89b80ec00.webp)

EFS は、Claude Platform、Claude Platform on AWS、Amazon Bedrock、Claude on Google Cloud を通じて利用できます。Amazon Bedrock または Claude on Google Cloud（Google Managed）経由で EFS を利用する場合、EFS はお客様のクラウドプロバイダーによって運用され、エンドツーエンドのデータフローはそのクラウドの境界内にとどまります。

ストレージには、Claude を利用する場所に応じて、お客様自身のアカウントの Amazon S3 または Google Cloud Storage を使用できます。ストレージ料金は、読み取り、書き込み、鍵操作（および該当するネットワーク転送）を含め、通常どおりクラウドプロバイダーから請求されます。

## はじめに

EFS は、Claude Platform、Claude Platform on AWS、Amazon Bedrock、Claude on Google Cloud で利用できます。Microsoft Foundry での EFS サポートも近日提供予定です。

対象となるお客様には、利用開始の手順をご案内します。設定方法については[開発者ドキュメント](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview)を、アーキテクチャの仕組みについては[セキュリティホワイトペーパー](https://trust.anthropic.com/resources?s=a7lwkeieqk3ggz29k954j&name=enterprise-frontier-safeguards:-technical-overview)をご覧ください。また、Accenture、Deloitte、KPMG、PwC などの[コンサルティングパートナー](https://partnerhub.claude.com/directory/)を通じて導入することもできます。
