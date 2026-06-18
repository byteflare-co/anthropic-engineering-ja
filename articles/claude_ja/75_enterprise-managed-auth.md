---
date: '2026-06-18'
final_url: https://claude.com/blog/enterprise-managed-auth
number: 75
selector_used: main
slug: enterprise-managed-auth
source_url: https://claude.com/blog/enterprise-managed-auth
title: Centrally manage authorization for MCP connectors
title_ja: "MCP コネクタの認可を一元管理する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

# MCP コネクタの認可を一元管理する

管理者は、組織で利用する MCP コネクタを ID プロバイダ経由で組織全体にプロビジョニングできるようになりました。手始めとして Okta に対応しています。ユーザーは初回ログイン時にコネクタへのアクセスを自動的に得られ、認可は組織が中央で構成します。

コネクタは Claude を業務でより役立つものにしてくれます。チームがすでに使っているツールから、Claude が必要とするコンテキストを与えてくれるからです。これまでは、コネクタを有効にするのに 2 段階のアクションが必要でした。管理者が組織に対してコネクタを有効化し、その後で個々のユーザーが各自で認可する必要があったのです。

エンタープライズ管理型の認可は、この 2 段階目を効率化します。管理者がコネクタを一度認可すれば、ユーザーはすでに持っている IdP のグループとロールを通じてアクセスを継承し、初めて Claude を開いたときにコネクタがそこにある状態になります。その結果、エンドユーザーにとってはゼロタッチでのコネクタ設定が実現します。

エンタープライズ管理型認可は、Model Context Protocol の [Enterprise-Managed Authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) の最初の実装です。オープンな標準の上に構築されているため、任意のコネクタが — 各社のチームが自前で構築するカスタムコネクタも含めて — これをサポートでき、すべての Claude のお客様に対してどれも同じように動作します。

### 仕組み

ID プロバイダを Claude に接続し、組織で有効にする MCP コネクタを選びます。従業員がログインすると、コネクタはすでにそこにある状態です。アクセスは Claude チャット、Claude Code、Cowork のすべてで一貫して保たれます。

管理者にとっては、これにより MCP のアクセス管理が、スタックの他の部分を統制しているのと同じワークフローに統合されます。プロビジョニングは一度だけ、グループ単位でスコープを設定し、失効は IdP を通じて管理します。IdP でのアクセスチェックは摩擦がないため、管理者は生産性を損なうことなくアクセストークンの有効期間を短くできます。これにより、誰かのプロビジョニングが解除されたとき、コネクタのアクセスは古いトークンとして残り続けることなく、すぐに失効します。アクセスはすでに信頼している ID プロバイダを通じて行われるため、コネクタは別途モニタリングすべき独立した領域ではなく、他のすべてと同じセキュリティ・アクセス制御の対象となります。

管理者はまた、コネクタが IdP 経由でのみ接続するよう強制することもできます。これにより、業務と個人の利用がきれいに分離され、誰かが個人アカウントを業務用ツールにうっかり紐付けてしまうことを防げます。

### エコシステムとともに構築

エンタープライズ管理型認可は、アクセスを統制する ID プロバイダ、その標準をサポートする MCP プロバイダ、そして管理対象の接続をチーム全体に展開する Claude のお客様という 3 つのグループにまたがって機能します。

**ID プロバイダ。** ローンチ時点では Okta をサポートしており、その他の ID プロバイダのサポートも近日中に追加されます。

**MCP プロバイダ。** Asana、Atlassian、Canva、Figma、Granola、Linear、Supabase がローンチ時点でエンタープライズ管理型認可をサポートしており、Slack も近日対応予定です。

**Claude のお客様。** Hubspot、Ramp、Webflow が、チーム全体にエンタープライズ管理型認可を展開している組織の一部です。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e70a75001b66e8d27f_asana-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e7f48cd2308583c215_asana-light.svg)

「エンタープライズ管理型認可は、Asana が描く『人間とエージェントのチームのためのオペレーティングシステム』というビジョンを実現するうえでの基盤となるマイルストーンです。Claude を組織のもっとも重要なワークフローに、安全に、コントロールされた形で接続する方法を提供することで、私たちはエンタープライズ全体にわたって AI 主導の価値をスケールさせる力を解き放っています — それも、大規模なデプロイメントが要求する絶対的なガバナンス、コンプライアンス、信頼に裏打ちされた形で。」

Arnab Bose, CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)

「エンタープライズ管理型認可は、Atlassian Rovo MCP を Claude Enterprise のお客様が大規模に採用しやすくします。従業員には、Jira、Confluence、Teamwork Graph の各所で日々頼っている Atlassian の業務に Claude をつなぐシンプルな方法を提供します。同じくらい重要なのは、管理者には MCP クライアントのアクセスを管理する中央拠点が提供されることです。これにより、組織は期待しているガバナンスを維持しながら、AI でより速く動けるようになります。」

Brendan Haire, VP of Engineering, Rovo and AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

「Canva はすでに Fortune 500 企業の 95% に信頼されており、私たちの MCP サーバーは、より多くのチームが Canva の AI とデザインツールを使って、同じワークフローのなかでオンブランドのデザインを作成・編集・公開できるようにします。Okta とのエンタープライズ管理型認可によって、エンタープライズはすでに信頼しているシステムで AI アクセスを明快かつシンプルに管理できるようになり、チームは AI とともに、安全に、そして大規模に創作できるようになります。」

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee4cb7c69d15a44ec7d6_Figma%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee481c19e67f332ef755_Figma%20Light.svg)

「Figma MCP は、コードとキャンバスの力をひとつに結びつけ、チームがより速く動き、より多くを探索し、際立つプロダクトを世に出せるようにします。MCP の採用が広がるなかで、エンタープライズ管理型認可は、エンタープライズがチームのスピードを落とさずに MCP のデプロイメントを安全にスケールさせやすくしてくれます。」

Devdatta Akhawe, VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a341e95b3dc7be545d7a477_granola-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a341e93bb7e7bd486f93263_granola-light.svg)

「Anthropic と Okta が、エンタープライズが MCP サーバーへ安全に、中央集権的に、そして大規模に接続することを容易にしてくれたのは素晴らしいことです。Granola はチームが業務で得るもっとも重要なコンテキストの一部 — 決定事項、詳細、フォローアップ — を、起きたその場で捉える手助けをします。MCP はこれをチームのツール全体で役立つものにしてくれ、エンタープライズ管理型認可はそれをチームをまたいで摩擦なく利用可能にしてくれます。」

Chris Pedregal, CEO & co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6989420bd171609a4d78b31e_logo_hubspot-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6989420ff5d1708aeefc4396_logo_hubspot-dark-mode.svg)

「エンタープライズ管理型認可は、私たちが MCP 接続に求めてきたセキュリティとユーザー体験そのものです。みんなが Okta への標準的なログインを行うだけで、ソフトウェアエコシステム内のすべての MCP ホストに、自分のパーソナルなコンテキストとともに接続されます。パーソナル ID は引き継がれますが、誰も OAuth の認可承認の山につまずくことはありません。これはエンタープライズ管理にとって大きな勝利であり、それらの MCP ホストが公開する個々のツールを選別的に制御できることと組み合わさると、その価値はさらに大きくなります。」

Andrew Meinert, Director, System Operations & AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6f1fdcf6881c9918dd0e_Linear_Logo_0%202%20(1).svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6f187456bf5ca9c27129_Linear_Logo_0%201%20(1).svg)

「一度ログインするだけで、すべての MCP コネクタが自動的にセットアップされているというのは、なかなか魔法のような体験です。」

Tom Moor, Head of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3407a0610055531404ba06_okta-logo-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a34079e0e3beac5523dc868_okta-logo-white.svg)

「MCP をめぐる勢いは目覚ましいものがありますが、相互接続された AI ワークフォースへと向かっていくなかで、セキュリティは後付けで考えるわけにはいきません。Cross App Access プロトコルを Enterprise-Managed Authorization extension として MCP に組み込み、それを Claude のエコシステムに実装することで、私たちは ID を中央集権的なガバナンスのプレーンに変え、セキュリティチームに厳密なコンプライアンス制御を、そしてユーザーにシームレスでセキュアな体験を提供します。」

Aaron Parecki, Director of Identity Standards

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

「エンタープライズ管理型認可が登場する前は、新入社員にフルセットのツールキットをオンボーディングするということは、コネクタごとに OAuth 承認の行列を消化することを意味していました。今では、入社初日に Claude にログインすればすでに接続が完了しています — 2,000 人の従業員が Okta 経由でプロビジョニングされ、追加の手間はゼロです。」

Cameron Leavenworth, Staff IT Engineer, AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68db36ce5254656fdbac3c90_SLA-Slack-from-Salesforce-logo%201.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68db36d1588af40e62128f8f_SLA-Slack-from-Salesforce-logo-inverse%201.svg)

「Slack は、人間とエージェントが同じ会話、同じコンテキスト、同じ目標に向かって肩を並べて働く場所です。Slack MCP サーバーを通じて、それらすべてが Claude からアクセス可能になります。読むだけではなく、行動するためにも。エンタープライズ管理型認可は、組織が摩擦なくすべてのユーザーへアクセスを展開できることを意味します。セキュリティチームは既存の ID プロバイダから一度設定するだけで、ユーザーはシームレスにアクセスを得られます。」

Rod García, VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413cc60038a6b9254745b_supabase-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413ca2450bd8db73b97f3_supabase-dark-light.svg)

「これまで Claude から Supabase を使う唯一の方法は、組織のオーナーになるか、チーム全員に Personal Access Token を配るかでした。エンタープライズ管理型認可はそれを解決します。アクセスとロールはあなたの IdP が制御するので、ビルダーは IT 部門がセキュリティで妥協することなく、Claude を使ってデータを探索しクエリできます。」

Bil Harmer, CISO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413a64096a140ea0118d8_webflow-logo-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413a24969057e976d25c4_webflow-logo-white.svg)

「私たちのチームは Claude を開けば、IT がすでに運用している ID グループでスコープされた、自分が利用を許可されているすべてのツールがそこにあります。エンタープライズ管理型認可は、AI を申請して使うものから、ただ使うものへと変えてくれました。私たちはこれを Webflow 全体に広げていきます。」

Reed Shackelford, Senior Manager, Enterprise AI Operations
