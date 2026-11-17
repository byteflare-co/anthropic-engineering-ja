---
date: '2026-11-17'
final_url: https://claude.com/resources/articles/linked-billing-on-claude-platform
number: 181
selector_used: article
slug: linked-billing-on-claude-platform
source_url: https://claude.com/blog/linked-billing-on-claude-platform
title: Linked billing on the Claude Platform
title_ja: Claude Platform のリンク課金
---

本日、Claude Platform のリンク課金（linked billing）をベータ版として提供開始します。コーディングエージェントやワークフロー自動化ツールなどのサードパーティプラットフォームは、API キーを共有することなく、エンドカスタマーに Claude API の利用料金を支払ってもらえるようになります。エンドカスタマーは既存の Anthropic の請求契約をそのまま維持し、自分で利用上限額を設定できます。一方プラットフォーム側は、よりシンプルかつ安全な方法で Claude を提供できるようになります。

## API キーの共有に代わる、より安全な選択肢

サードパーティプラットフォーム上で Claude API の利用料金を支払うには、通常 API キーを共有する必要があります。API キーはパスワードのように機能します。キーを持っている人は誰でも、そのカスタマーに課金されるリクエストを送れてしまうため、プラットフォームはキーを安全に保管しなければなりません。

リンク課金では、カスタマーは API キーの代わりに自分の Claude Platform の組織をリンクし、利用料金はその組織に直接請求されます。API キーの受け渡しが発生しないため、プラットフォームはカスタマーのキーを保管・暗号化・ローテーションする必要がなく、カスタマーの API キーが組織の外に出ることもありません。

プラットフォームは、リンクされた各カスタマーの利用状況を確認できます。カスタマーはリンクする各プラットフォームを承認し、利用上限額を設定でき、いつでもリンクを解除できます。

![Linked billing on the Claude Platform](https://assets.claude.com/d5dce5584f3e356c5938201534cd671ac1c50687.png)

Claude Platform のリンク課金

## プラットフォームは課金の仕組みを構築せずに Claude を提供できる

リンク課金は、プラットフォームがカスタマーに Claude を提供するための新しい方法です。プラットフォームがリクエストを送信し、Anthropic がエンドカスタマーに直接請求します。リンク課金により、プラットフォームは次のことができます。

- **より早くローンチできる。** 承認フローと課金は Anthropic がホストするため、従量計測や請求書発行の仕組みを構築する必要はありません。
- **カスタマーごとの利用状況を把握できる。** リンクされた各カスタマーのリクエスト数、トークン使用量、使用モデルを Console で、または [Usage and Cost Analytics API](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api)（ベータ版）を通じてプログラムから取得できます。
- **誰が支払うかを選べる。** リクエストごとにプラットフォームとエンドカスタマーのどちらが支払うかを決められるため、Claude API のコストをカスタマーに転嫁したり、プロダクトやインスタンス単位で一部の機能のコストをプラットフォーム側で負担したりできます。

## カスタマーは可視性とコントロールを得られる

カスタマーは、Anthropic がホストするフローを使って簡単にプラットフォームとリンクできます。その後は、既存の Anthropic のコミットメントから消化することも、従量課金で支払うこともできます。さらにリンク課金では、カスタマーは次のことも可能です。

- **組織全体で一度リンクするだけでよい。** Owner、Admin、Billing のいずれかのロールを持つ Console ユーザーがリンクを承認するため、個人の開発者でも大規模なチームでも同じように機能します。
- **プラットフォームごとに上限を設定できる。** プラットフォームごとに月間の利用上限額を設定することも、すべてのプラットフォームに適用されるデフォルト値を設定することもできます。
- **API の支出先を確認できる。** Console には、リンクされた各プラットフォームでの支出が表示されます。
- **いつでもリンクを解除できる。** Console から直接リンクを解除できます。

リクエストはプラットフォーム側の組織で実行されるため、IP 許可リスト、暗号化キー、データ保持など、カスタマーの組織での設定は適用されません。

現在リンク課金に対応しているプラットフォームは、Asana、ClickHouse、Factory、Gumloop、Harness、Higgsfield AI、Kilo Code、Linear、Major、Mintlify、Omni、OpenArt、Niteshift、Railway、Ramp、Runlayer、Tessera、Tines、Warp です。

## はじめ方

リンク課金は本日より、Claude Platform 上でベータ版として利用可能です。サードパーティプラットフォームは、[Console](https://platform.claude.com/settings/oauth-apps) でアプリを作成し、[ドキュメント](https://platform.claude.com/docs/en/manage-claude/oauth-apps/organization-billing-connections)の手順に従うことで対応を追加できます。Claude Platform のカスタマーは、対応しているどのプラットフォームからでも自分の組織をリンクでき、リンク課金に対応したプラットフォームは [Claude Marketplace](https://claude.com/marketplace/agents-products?howYouPay=linkedBilling) で探せます。

![Tessera AI](https://assets.claude.com/6d781cd38e4d23ff513cc6f163a4177e56ef9895.svg)

> 「私たちのカスタマーには、世界有数の大企業も含まれています。リンク課金により、新たにキーを管理することなく、自社の Claude の組織を Tessera で使えるようになります。」

Anirudh Sriram 氏、CTO、Tessera

![Tines](https://assets.claude.com/9a3c4cfd245bebefdf4bbef1944dd9d7fb32cfec.svg)

> 「Claude は AI で可能なことを広げており、Tines は、IT やセキュリティ部門が必要とする可視性とコントロールを備えたうえで、ビジネス全体のチームがその取り組みを安全に構築・デプロイ・運用できるよう支援しています。リンク課金によって、カスタマーは API キーを共有することなく、既存の Claude Platform の組織を通じて Claude と Tines をよりシンプルに組み合わせられるようになり、支出のコントロールやビジネス全体での AI 活用の拡大が容易になります。」

Charlie Ardagh 氏、Vice President, Strategic Partnerships、Tines

![Warp](https://assets.claude.com/399915ee2f0b3513a52ff63e61b1da17ed7eb078.svg)

> 「エンジニアリングチームは、自分たちが選んだモデルやインフラでソフトウェアファクトリーを構築できる柔軟性を持つべきです。リンク課金はそれをより簡単かつ安全にし、API キーや複雑な課金の取り決めを管理することなく、カスタマーが自分の Claude Platform の組織を Warp にシームレスにリンクできるようにします。この体験を Warp に導入できることを楽しみにしています。」

Zach Lloyd 氏、Founder and CEO、Warp

![Linear](https://assets.claude.com/02794cae131d86ae8d46e3238f14d1a7ad685181.svg)

> 「API キーを手作業でコピーすることは、本質的に安全ではありません。リンク課金により、管理者はコミット済みの Claude の支出を、ワンクリックで Linear のクラウドコーディングエージェントに直接使えるようになりました。」

Tom Moor 氏、Member of Technical Staff、Linear

![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)

> 「Ramp では、カスタマーがどこで働いていても、時間とお金を節約できるようにしたいと考えています。リンク課金により、カスタマーは API キーを共有する手間なく、既存の Claude Platform アカウントを Ramp Router 経由で簡単に使えるようになります。」

Amanda Carroccio 氏、Director of AI Partnerships、Ramp

![Railway](https://assets.claude.com/2dea27bb68e069958a1993a8ed54b8671ad4fddd.svg)

> 「Claude Platform のリンク課金により、Railway Agent を使う開発者は API キーを手作業で管理するのではなく、アプリケーションの構築とデプロイに集中できます。Claude Platform の組織を Railway にリンクすることで、開発者はより安全な方法でモデルや利用上限にアクセスできます。」

Cody De Arkland 氏、GM, Agent Experience、Railway

![Asana](https://assets.claude.com/b8ffecd4a133f2860151d51156002816a54772e7.svg)

> 「カスタマーは、IT や財務部門の負担を増やすことなく、より多くの業務に AI を取り入れたいと考えています。リンク課金により、既存の Claude のコミットメントを使って、AI Studio や AI Teammates を含む Asana の Agentic Work Management を動かせます。セットアップの手間も少なく、活用が広がるにつれて自分で管理できる利用上限も備えています。」

Arnab Bose 氏、Chief Product Officer、Asana

![ClickHouse](https://assets.claude.com/002d4e2a6b94d0409b6dd64c8e91ac1e1fac0bd8.svg)

> 「リンク課金によって、ClickHouse Cloud での Claude の課金はすぐに使える状態になります。Claude Platform の組織をリンクするだけで、管理すべきキーはなく、Claude API の利用料金は既存の契約条件のまま組織に請求されます。」

Ryadh Dahimene 氏、Director of Product Management, AI/ML、ClickHouse

![Factory](https://assets.claude.com/87ed06e3a5284cc3cc54b2e40051da1d15a205af.svg)

> 「リンク課金は、エンタープライズのカスタマーのオンボーディングプロセスを簡素化します。Anthropic の API キーを作成して私たちと共有する代わりに、管理者が Claude Platform の組織を一度リンクするだけです。私たちがキーを保持する必要がないため、インテグレーションのセキュリティがさらに高まります。」

Leo Tchourakov 氏、Member of Technical Staff、Factory

![Gumloop (Marketplace)](https://assets.claude.com/51533a1bef90ecc07f125f337a40048af6f77368.svg)

> 「Gumloop はセキュリティを非常に重視しており、リンク課金によって、カスタマーはもう API キーを第三者に渡す必要がなくなりました。Claude Platform の組織を一度 Gumloop にリンクすれば、Claude API の利用料金はその組織に直接請求されます。」

Rahul Behal 氏、Chief Technology Officer、Gumloop

![Harness](https://assets.claude.com/d459c27c7d38eb7c8c7b5cdcd39c05ac5bb97873.svg)

> 「ソフトウェアファクトリーはエンジニアリングの次の章であり、多くのカスタマーが Claude を使ってそれを構築しています。リンク課金を使えば、Claude Platform の組織を Cosmos by Harness にリンクでき、Cosmos での Claude API の利用料金はその組織に請求されます。Claude Platform のリンク課金をサポートできることを嬉しく思います。」

Sanjay Nagaraj 氏、SVP of Engineering、Harness

![Higgsfield](https://assets.claude.com/89a7f4137c4cc871d03fdf313ee00edceb773b8e.png)

> 「カスタマーは、創作に使うツールでのエージェント機能を Claude に期待しています。リンク課金により、Claude Platform の組織を Higgsfield にリンクでき、Claude API の利用料金は組織に直接請求されます。運用がシンプルになることで、クリエイティブチームは自分たちが最も得意なことに集中できます。」

Alex Mashrabov 氏、CEO、Higgsfield AI

![Mintlify](https://assets.claude.com/17e354acbdb212465bbff93d971f04b1e480b324.svg)

> 「リンク課金なら、カスタマーが Claude Platform の組織をリンクするだけで、すべてがそのまま動きます。私たちは認証情報の管理ではなく、開発に時間を使えるようになります。」

Kyle Finken 氏、Engineer Manager、Mintlify

![Niteshift](https://assets.claude.com/b52f6e78c14b8ca19d3970f16e1c9bd2b8b152f3.svg)

> 「Niteshift は、フルスタックの開発環境を備えたクラウドコーディングエージェントをオーケストレーションしています。エージェントの利用量と範囲が拡大するにつれ、カスタマーはコスト管理とセキュリティの両方をますます重視するようになっています。リンク課金により、長期間有効な API キーを共有することなく、月間の利用上限額を設定し、Anthropic との請求関係を維持できます。」

Sajid Mehmood 氏、CEO & Co-Founder、Niteshift

![Omni](https://assets.claude.com/ade4bc4e76a4151d0e0ba0e7c78fa7eaf24f39c3.svg)

> 「Claude Platform のリンク課金により、カスタマーは API キーを共有することなく Claude の組織を Omni にリンクできます。Omni 独自の利用状況トラッキングと組み合わせることで、Claude のトークン使用量を Omni まで遡って追跡でき、監査性が向上します。」

Marc Dupuis 氏、Director of Product、Omni

![Runlayer](https://assets.claude.com/8fb16c1ab5b1ddf0c974e424f3630431c0e15aac.svg)

> 「Runlayer は AI の最前線にいるエンタープライズと協業しており、Claude Platform のリンク課金をサポートできることを嬉しく思います。共有する API キーがないということは、攻撃経路が 1 つ減るということです。」

Andy Berman 氏、CEO、Runlayer
