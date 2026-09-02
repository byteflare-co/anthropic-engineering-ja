---
date: '2026-09-02'
final_url: https://claude.com/blog/claude-for-commerce-agents
number: 134
selector_used: main
slug: claude-for-commerce-agents
source_url: https://claude.com/blog/claude-for-commerce-agents
title: Building commerce agents with Claude
title_ja: "Claude でコマースエージェントを構築する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

# Claude でコマースエージェントを構築する

世界最大級の小売業者、マーケットプレイス、EC プラットフォーム、旅行会社の多くが、Claude を使って買い物をより簡単にするエージェントを構築しています。Shopify や Priceline をはじめとするエンタープライズ顧客は、消費者が自然言語で欲しいものを検索し、見つけ、比較し、購入できるエージェントを備えています。

本日、Claude 上でコマースエージェントを構築するためのブループリントを公開します。これには、エンジニアリングチームが数日でコマースエージェントを稼働させるために必要なハーネス、パターン、ガードレールが含まれており、小売、旅行、通信、チケット販売の各プラットフォーム向けにショッピングエージェントとマーチャントエージェントのリファレンス実装も用意されています。すぐに使い始められる Claude Code プラグインも含まれています。

コードは、Claude API、Amazon Bedrock、Microsoft Foundry、Google Cloud Vertex AI など、すでに Claude で構築している環境にそのままデプロイできます。また、Accenture、Mastercard、Visa といったソリューションおよびエコシステムパートナーと連携することもでき、これらのパートナーはクライアントやマーチャントコミュニティがこのブループリントを活用できるよう、私たちと協力しています。

[本日から利用可能](https://github.com/anthropics/commerce-agents)で、各業種向けの[ライブデモ](https://claude.com/solutions/commerce)と、どのように構築したかを解説する[エンジニアリング詳細記事](http://claude.com/blog/the-anatomy-of-effective-commerce-agents)もあわせて公開しました。ホリデーシーズンの計画に間に合うタイミングです。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95f44f1757be75a0616bd0_demo-retail.webp)

*ACME の* [*小売業向けサンプル*](https://claude.com/solutions/commerce) *で稼働するショッピングエージェント。*

## ブループリントの内容

このリポジトリには、[Messages API](https://platform.claude.com/docs/en/intro)、[Agent SDK](https://code.claude.com/docs/en/agent-sdk)、[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview)(ベータ版)のいずれを使っても構築できる、ショッピングエージェントとマーチャントエージェントの完全な実装が含まれています。コードを書く前に、セルフガイド型のデモでその動作を確認でき、その後 Claude Code と協力して自社のカタログ、ポリシー、ブランドなどに合わせてカスタマイズできます。

### ショッピングエージェント

ショッピングエージェントは、あなたのアプリやウェブサイトの中で動作します。ブループリントには、カタログ、カート、チェックアウト、顧客の好み、注文履歴との連携ポイントが含まれており、決済については既存のチェックアウトを使うか、エージェント型決済プロバイダーを使うかをあなた自身で選べます。

顧客が「週末に子供2人と出かけるためのテント、寝袋、コンロが欲しい」と言えば、あとはエージェントに任せられます。以下のようなことができます。

- カタログを検索し、複数商品にまたがるリクエストも含めて適切な組み合わせを揃える。
- 顧客の好みを記憶し、提案内容をそれに合わせて調整する。
- 商品、比較、カートを、テキストだけでなく会話の中でそのまま表示する。
- カートを組み立て、チェックアウトへと引き渡す。
- 注文状況の確認、返品・交換の方法、返金ポリシーの説明など、カスタマーサービスに関する質問にも同じ会話の中で答える。サポートページへ誘導する必要はない。

このエージェントには、価格や商品を実際のカタログデータに限定するガードレールが組み込まれており、押し付けがましいアップセルを避けるよう設計されています。リポジトリ内では、これらはカタログ検索、複数商品プランニング、詳細調査、パーソナライゼーション、カスタマーケア、会話内 UI のためのスキルとツールとして実装されています。

### マーチャントエージェント

マーチャントエージェントは、店舗を運営する人たちをサポートします。ユーザーが「前シーズンの在庫を一掃するには何を値引きすればいいか」と尋ねると、自社のデータに基づいた答えが返ってきます。以下のようなことができます。

- 何が売れていて何が売れていないかなど、売上実績に関する質問に答える。
- 在庫を追跡し、プロモーション開始前に商品が売り切れそうといった問題を積極的に知らせる。
- 店舗自身の販売履歴に基づいて価格やプロモーションを提案する。
- 動かす必要がある商品を動かすためのマーケティングキャンペーンを起案する。

エージェントが変更を積極的に提案する場合でも、実際に反映される前に必ず人が承認します。つまり、エージェントが店舗を見守る一方で、最終判断はユーザーに委ねられます。リポジトリ内では、これらの機能は売上分析、カタログ・在庫管理、マーケティング・プロモーション、チャートやダッシュボードといったポータル内 UI のためのスキルとして提供されています。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a972d45795f7bbae7ce272f_Retail%20%E2%80%94%20Merchant%20workspace.png)

## 業界全体からの信頼

買い物客、旅行者、サブスクリプション利用者、マーチャントにサービスを提供する企業各社が、Claude 上でエージェントを構築・運用しています。Claude でコマースエージェントを構築することについて、各社から寄せられた声を紹介します。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ae674813a930db5dcaf7_Visa_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ae6d39727b14adbf7631_Visa_dark.svg)

「AI はコマースの姿を根本から変えていきますが、あらゆる取引の中心には信頼がなければなりません。マーチャントからは、AI が顧客とどう関わるかについてもっとコントロールしたいという声が寄せられています。Anthropic のコマースブループリントとの協業により、Claude の知性と Visa ネットワークが持つ信頼性、セキュリティ、グローバルなリーチを組み合わせることで、マーチャントが顧客との関係を維持しながら、より良い顧客体験を提供できるようになります。」

Jack Forestell 氏、Chief Product and Strategy Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a96d51f43f5c41132ff29ed_mastercard-logo.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a96d51f43f5c41132ff29ed_mastercard-logo.svg)

「信頼はコマースの通貨であり、エージェントの時代においてはそれがさらに重要になります。Anthropic のコマースブループリントによって、私たちはマーチャントが Claude で自社のエージェントを構築し、成長を推進できるよう支援しています。AI のイノベーションと信頼性の高い決済・コマースインフラを組み合わせることで、消費者、マーチャント、AI エージェントを安全かつシームレスに、そして大規模につなげる手助けをしています。」

Sherri Haymond 氏、Executive Vice President, Global Head of Digital Commercialization

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f679a0b07cb25d6830bc76_accenture_logo.svg.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f679a262980d8650836fd9_accenture_logo.svg-1.svg)

「コマースエージェントは、今日の消費者が期待するパーソナライズされた知的な顧客体験を提供しようとする組織にとって、急速に不可欠な能力となりつつあります。私たちの最新の調査によると、85% の消費者が AI エージェントとの協働に前向きであり、およそ4人に3人が、購入を代行してもらう相手として親友よりも AI エージェントを信頼すると回答しています。これは単なる買い物の仕方の変化にとどまりません。エージェント型コマースはブランド価値のルールそのものを書き換えつつあり、何が、いつ、どこで、誰によって購入されるかを根本から形作っています。Anthropic のコマースエージェントブループリントは実証済みの出発点となり、組織がデプロイを加速し、顧客満足度、ロイヤルティ、成長を高める差別化された体験を構築する助けとなります。Accenture の小売・消費財分野での深い専門知識と組み合わせることで、クライアントが構想から本番稼働へと移行し、エージェント型 AI からより早く価値を実現できるよう支援できます。」

Kath Gramling 氏、Global Consumer Goods, Retail and Travel lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7dc912b141697da7a0c_priceline-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7de9410fba39a2cfc8d_priceline-white.svg)

「旅行は、人が購入するものの中でも特に複雑なものの一つです。航空券、ホテル、レンタカーなど、比較検討すべき選択肢が数多くあります。私たちの AI アシスタントである Penny は、その複雑さを一つの会話の中でさばき、最良の選択肢と最良の価値を提示します。最新世代の Penny を Claude 上に構築したのは、そうした推論こそまさに Claude モデルが得意とすることだからです。」

Cobus Kok 氏、Vice President, AI Experiences

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9771254c4225f0bc16623e_intuit-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9771288cd6fb2332ebeabe_intuit-white.svg)

「数百万人の消費者、企業、会計士が Intuit の上で財務を管理しています。Anthropic のようなパートナーと協力しながら、私たちは顧客が自社ビジネスで何が変化しているのか、なぜそうなっているのかを明確に理解し、確信を持って行動できるような、高度にパーソナライズされた体験を構築しています。Claude を含むフロンティア AI の推論能力と、Intuit独自のデータ、機能、インテリジェンス、人間の専門知識を組み合わせることで、顧客の次なる繁栄を支える金融インテリジェンスシステムを作り上げています。」

Chris Kasten 氏、Intuit’s Chief Architect and SVP of Engineering, Platform and Development Xceleration Group

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68da9368f2bd228e7080695d_logo_shopify-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68da936caa7913237c0589f4_logo_shopify-dark.svg)

「私たちは、顧客が買い物をするあらゆる場所にマーチャントが存在できるようにしたいと考えており、それは今やエージェントとの会話を意味することが増えています。私たちは Anthropic のブループリントを基盤に、Catalog、UCP、Shop Sign-in を通じてマーチャントのストアと接続するリファレンスストアフロント実装を構築しています。マーチャントは Claude を使って、顧客が商品を見つけ、チェックアウトし、注文に関する質問に答えるエージェントを構築できます。」

Vanessa Lee 氏、VP Product

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a906156d04a91e09ce93cb7_klaviyo-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90615393673a5ea036d6b2_klaviyo-white.svg)

「コマースと優れた顧客体験にはパーソナライゼーションが欠かせませんが、Klaviyo 上のあらゆるブランドは、どんなチームでも手作業では処理しきれないほどの顧客データと意思決定を抱えています。Claude はそのギャップを埋め、消費者の好みやパフォーマンスデータを、収益を生み出すインサイト、キャンペーン、パーソナライゼーションへと変換します。だからこそ私たちは Anthropic との協業を続けています。エージェントが複雑な分析、デザイン、意思決定を担い、企業は顧客を喜ばせることに集中できるのです。」

Andrew Bialecki 氏、Founder and Co-CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a97717810bbbdeb232b1861_wix-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a97717a1ece7880de88876a_wix-white.svg)

「Wix の使命は、複雑なテクノロジーをシンプルでアクセスしやすいものにすることです。マーチャントにとってそれは、運用の複雑さを増やすことなく強力なコマース機能を提供することを意味し、エージェントはその自然な次のステップです。私たちのエンジニアは、15分で稼働するコマースエージェントを作り上げ、このパイロットは Anthropic の AI 機能と、Wix の中小企業向けコマースプラットフォームおよび深い専門知識を組み合わせることの可能性を示しました。」

Dror Zalika 氏、Head of Commerce at Wix

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a7436f6227c5015996a7_zomato-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a95a74649d16140f5e9939f_zomato-white.svg)

「私たちのエンジニアは、何のつまずきもなくこのブループリントを稼働させることができ、セットアップはドキュメント通りに機能しました。ツールの反復回数の制限やプロンプトキャッシングなど、そこに組み込まれているプラクティスは、私たちが Zomato 自身のエージェントを構築する中で見覚えのあるものばかりです。Claude 上で初めてエージェントを立ち上げるチームは、これによって何週間もの試行錯誤を省けるでしょう。」

Akhil Bansal 氏、Senior Engineering Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90644256c9ac773063e8e6_fetch-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a906441c42656e199477abf_fetch-white.svg)

「私たちのエンジニアは、Anthropic のブループリントにある両方のコマースエージェントを1時間もかからずにローカルで稼働させ、初回の試行で実際の会話が動作しました。Claude Code のワークフローを2回実行したところ、それぞれの要望に合わせて設計された、異なる2つのアーキテクチャが得られました。ゼロから始めるチームにとって、これはエージェントの土台作りに要する日数を数時間に短縮することを意味します。」

Ashley Nader 氏、Staff Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aded6c2824c6159c1795_Square_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ade71ac3dc1f534d924d_Square_dark.svg)

「Square での取り組みの多くは、販売者に時間を取り戻してもらうことであり、エージェントはそれを実現する大きな飛躍です。私たちは、売上、人員配置、在庫を監視し、単なる答えではなく実際に取るべき次のステップを返しつつ、販売者がコントロールを保てるエージェント型ツールを構築しています。この取り組みの中で最も難しいのは信頼であり、Claude は私たちが高い基準を満たす助けとなっています。」

Willem Avé 氏、Head of Product

## 始め方

このブループリントは本日から利用できます。詳細を知りたい方、デモのスケジュールを組みたい方、自社への導入方法について相談したい方は、[営業チームにお問い合わせ](https://claude.com/contact-sales)ください。

1. [github.com/anthropics/commerce-agents](https://github.com/anthropics/commerce-agents) のリポジトリをフォークする。
2. [claude.com/blog/the-anatomy-of-effective-commerce-agents](http://claude.com/blog/the-anatomy-of-effective-commerce-agents) でエンジニアリング詳細記事を読む。
3. [claude.com/solutions/commerce](https://claude.com/solutions/commerce) で各業種のデモを見て、ワーキングセッションをリクエストする。

ライブウォークスルーやデモ、コマースを構築するチームが Claude を最大限に活用する方法について解説する[ウェビナー](http://anthropic.com/webinars/building-claude-commerce-agents)にもぜひご登録ください。
