---
date: '2026-10-27'
final_url: https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
number: 160
selector_used: article
slug: how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
source_url: https://claude.com/blog/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
title: Manage costs and demonstrate ROI for Claude Code on Google Cloud
title_ja: Google Cloud 上の Claude Code でコストを管理し ROI を示す
---

組織が Claude Code に任せる仕事が増えるにつれて支出も増え、プラットフォームチームにはコストを管理しつつその効果を把握する手段が必要になります。Google Cloud と共同で開催した[最近のウェビナー](https://www.anthropic.com/webinars/how-to-control-costs-and-show-roi-for-claude-code-on-google-cloud)をもとに、Claude Code を利用する組織が Google Cloud 上でこれらをより適切に追跡・最適化する方法を、3 つの中核的なレバー「コントロール（control）」「追跡（track）」「証明（prove）」とあわせてご紹介します。

## Claude Code の支出を管理するためのコントロール

Google Cloud 上の Claude は従量課金制なので、請求額は開発者が Google Cloud 環境でどれだけ Claude を使っているかを示す指標になります。導入が利用を生み、利用に対して料金を支払います。そして価値が生まれるのも、まさにその利用の中です。

Claude Code の請求額は、タスクが消費するトークン数と、それを処理するモデルの掛け合わせで決まります。トークン消費量はタスクの複雑さと会話の長さに応じて増えます。チャットは一問一答の会話です。一方、Claude Code のようなエージェント型ツールは、ファイルを読み、ツールを実行し、タスク全体にわたって推論するというマルチステップの作業を行うため、チャットに比べてタスクあたりのトークン消費が多くなります。また、モデルごとにトークン単価が異なるため、[タスクに合ったモデルを選ぶこと](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)がもう 1 つの主要なコスト管理手段になります。

毎月の請求額に影響するトークンとモデル選択は、[Claude apps gateway](https://claude.com/blog/introducing-the-claude-apps-gateway) と Google Cloud のサービスを通じて可視化できます。支出のガバナンスとコスト管理は、3 つの独立したレバーで行えます。

- **コントロール**：アクセスを過度に制限して意図せず人々をブロックすることなく、利用を導くガードレールを設ける。
- **追跡**：請求書が届く前に、どこで支出が発生していて今後どこに向かうのかを細かく把握する。
- **証明**：トークンへの支出から組織がどのような価値を得ているのかを特定し、それがどこから生まれているのかを正確に結び付ける。

ここからは、この「コントロール → 追跡 → 証明」のフレームワークを、自社の Google Cloud 上の Claude Code 環境に適用する方法を説明します。

![graphic showing control - track - prove categories and the tools used in each](https://assets.claude.com/50faca60a22f422f7c0f5e9d2f4177a1ea483448.png)

### **ガバナンスのツールボックス**

Google Cloud 上の Claude には、支出のコントロール、追跡、価値の証明のためのツールと機能が備わっています。

![Graphic showing Google Cloud native and Claude Code + Claude apps gateway add](https://assets.claude.com/b3266f5cebd6e2613593339d21200b3a7c034b9a.png)

Google Cloud にはすでに、Claude の支出の追跡とコントロールに活用できるネイティブ機能が数多くあります。

- **プロジェクト単位の課金**：Claude Code 専用のプロジェクトを用意することで、コストをすっきりと追跡できます。
- **課金予算とアラート**：予算アラートを設定し、実際の支出が定義したしきい値を超えたときに通知を受け取れます。
- **支出上限（プレビュー）**：サービスレベルで Google Cloud の支出予算を強制でき、上限は手動で解除できます。
- **BigQuery エクスポート**：Claude の支出を、ほかのクラウドコストとあわせて分析できます。
- **割り当て（Quotas）**：Google Cloud 上の Claude モデルには、モデルファミリーとエンドポイントのロケーションごとに、リクエスト数、入力トークン数、出力トークン数の分単位の上限があります。
- **プロビジョンドスループット**：従量課金ではなく、予約済みキャパシティに対して固定料金を支払います。

Claude Code と Claude apps gateway は、独自の追跡・コントロール機能を追加します。gateway はセルフホスト型のサービスで、開発者がすでに使っている `claude` バイナリに同梱されており、Google Cloud プロジェクト内で Claude Code と Google Cloud 上の Claude の間で動作します。開発者は Google Workspace などの ID プロバイダー（IdP）経由でサインインするため、すべてのリクエストに検証済みの ID が付与されます。これにより、IdP グループごとのモデル許可リストや、ユーザー・IdP グループ・組織ごとの日次・週次・月次の支出上限を設定できます。

ここからは、Google Cloud 上の Claude への AI 投資のコストと ROI を測る 3 つのレバーを管理するために、各機能をどう選び、組み合わせればよいかを説明します。

#### レバー 1：コントロール

コントロールのレバーは、恣意的な上限で開発者を制限するのではなく、Claude Code の利用を導くガードレールを提供することがすべてです。

制限ではなく導くことが重要なのは、コストの高いセッションが必ずしも悪いわけではないからです。むしろ、特に Claude Code では価値の高いセッションであることが多いのです。そうしたセッションの主は、たいてい最前線にいるパワーユーザーで、新しいワークフローを使い、Claude から多くの価値を引き出し、大量の仕事をこなしています。

無駄は、ヘビーユーザーのうち中間層の広いすそ野に潜んでいることが多いものです。たとえば、Sonnet で十分にこなせる日常的なルーティンに Fable を使っているケースです。あるいは、もう必要なくなったスケジュールタスクの存在を忘れていて、それが自動で動き続けているケースもあるでしょう。

ユーザーを制限するのではなく導くためのガードレールとなる機能が 4 つあります。

- **[支出上限](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)**：Claude apps gateway では、ユーザーごと、IdP グループごと、または組織全体で、日次・週次・月次の支出上限を設定できます。グループや組織の上限は、各メンバーが継承する開発者ごとのデフォルト値であり、共有のプールではありません。
- **しきい値アラート**：Claude apps gateway と組み合わせて使うと、Google Cloud 上の Claude Code は、開発者が上限に近づいたときに、まず 75% を超えた時点で、さらに 95% を超えた時点で警告します。これは開発者向けの CLI 内の警告であり、管理者向けの Google Cloud Billing のアラートとは別物です。上限に達すると、期間がリセットされるか管理者が上限を引き上げるまで、gateway は 429 を返します。上限の引き上げは gateway の Admin API を使ってスクリプト化できます。
- **モデルのデフォルトと許可リスト**：Claude apps gateway を通じて、IdP グループごとに利用可能なモデルを指定できます。gateway はすべてのリクエストに対して許可リストをサーバー側で強制します。私たちの経験では、モデルのデフォルトを設定するのが非常に効果的です。ほとんどの人はデフォルトのモデルをそのまま使い、モデルを切り替える人には通常それなりの理由があるからです。モデルのデフォルトは、許可リストに加えて、あるいは許可リストの代わりに使えます。
- **Gateway Admin API**：gateway は[支出上限用の Admin API](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits) を提供しているため、たとえばチケット管理のワークフローを使って、上限をプログラムから設定・変更できます。

![Graphic showing the phases of a spend-cap lifecycle](https://assets.claude.com/d1ded8cd5410c90e62905f650bf2a4e09df4cdce.png)

これらの機能を組み合わせて全体の請求額をコントロールしましょう。ただし、コントロールは最初のレバーにすぎないことを忘れないでください。トークン単価だけでは全体像はつかめません。最も重要な指標はタスクあたりのコストであり、これは利用状況を追跡することで監視・分析できます。

#### レバー 2：追跡

このレバーは、支出がどこに向かい、どのように使われているかを把握するためのものです。うれしいことに、組織全体の Claude Code の利用状況、コスト、ツールのアクティビティを追跡できます。主な追跡戦略は次のとおりです。

- **利用状況とコストのオブザーバビリティ**：[Claude Code の OpenTelemetry メトリクスとイベント](https://code.claude.com/docs/en/monitoring-usage)は、利用状況と推定コストを、スキル、プラグイン、エージェント、MCP サーバーごとに分けて報告します。これらは OpenTelemetry Protocol（OTLP）経由で、Google Cloud Monitoring など既存のツールに送信できます。送信は OpenTelemetry コレクター経由でも、Claude apps gateway による中継（OpenTelemetry の設定を一元化する場合）でも可能です。
- **エンドユーザー向けの利用状況ビュー**：開発者は自分の支出を確認でき、上限に達する前に Claude Code 上で直接利用状況の警告を受け取れます。
- **既存システムへのデータエクスポート**：Google Cloud Billing の BigQuery エクスポートでは、モデルやトークン種別で Claude の SKU に絞り込み、Claude の支出をほかのクラウドや AI の支出と並べて確認できます。OTel のデータはオブザーバビリティ（O11y）スタックに流れ、gateway の Admin API は支出上限のステータスをチケット管理システムに直接送り込めます。

![Graphic showing Claude Code telemetry on Google Cloud](https://assets.claude.com/f2ab59204d683994ef32ddc5b4e6f1167389a800.png)

Claude Code は、開発者のマシン上で動いていてもクラウドワークステーション上で動いていても、有効化すれば OpenTelemetry をエクスポートできます。対象には、セッション、アクティブ時間、コード行数、コミット、プルリクエスト、トークン、コストが含まれ、ユーザー、チーム、モデルごとに分けて確認できます。最新の Claude Code のリリースでは、利用状況をスキル、プラグイン、エージェント、MCP サーバーごとにも分けて確認できるため、Claude Code 全体の利用状況だけでなく、組織内のどのスキルやプラグインが採用されているかもわかります。Claude apps gateway を使えば、マシンごとに設定する必要はありません。gateway にテレメトリーの送信先を設定すれば、サインインした開発者のテレメトリーが有効になります。また、すべてのエクスポートには、クライアント側で設定された値ではなく、サインイン時の開発者の検証済みメールアドレスと IdP グループがタグ付けされます。

利用状況を自社のコストセンターや部門に結び付けるには、OTEL\_RESOURCE\_ATTRIBUTES 環境変数を設定します（例：department=engineering,cost\_center=eng-123）。Claude Code はこれらのタグをすべてのメトリクスとイベントに付与するため、タグで絞り込んだり集計したりできます。メトリクスは、これらのカスタム属性付きで Google Cloud Monitoring（あるいは Grafana や Splunk などのほかの監視ソリューション）に届きます。

![A screenshot of a dashboard](https://assets.claude.com/201a89049ce753ac7e42f8518d1db7908b40a91a.png)

Claude Code の OpenTelemetry メトリクスから構築した、Cloud Monitoring 上の Claude Code 利用状況ダッシュボード。サンプルデータを用いた再現イメージです。

一般的な導入状況のビューには、アクティブな開発者数、過去 24 時間のセッション数、消費トークンの合計が表示されます。オレンジ色の枠は、開発者が gateway で強制される支出上限に達したことでブロックされたリクエストを示しています。このメトリクスは、開発者が上限の引き上げを申請できるワークフローとして、既存のチケット管理システムと組み合わせると効果的です。

すぐに使える Cloud Monitoring のダッシュボードとしては、[Claude Code Monitoring テンプレート](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/dashboards/claude-code)を参照してください。このテンプレートは Claude Code の OpenTelemetry メトリクスを、導入状況、コーディングアクティビティ、トークン使用量と推定支出をまとめた単一のビューに変換するため、Google Cloud 上で Claude Code を展開する際に、ユーザーやモデルごとの利用状況とコストを追跡できます。このテンプレートは Cloud Monitoring コンソールから直接コピーできます。

Google Cloud 上でカスタムの Claude Code テレメトリーをセットアップするには、まず [Claude Code OTel クイックスタート](https://github.com/Google-Cloud-AI/partner-ai-anthropic/tree/main/01-quickstart/otlp-to-telemetry-api)から始めましょう。これを使うと、Claude Code から Cloud Logging や Cloud Monitoring を含む Google Cloud Observability スイートに OpenTelemetry を直接エクスポートするよう設定できます。このクイックスタートは、ログをイベント種別（API リクエスト、ツールの判断、ツールの結果、アシスタントの応答、完了したフックの実行）ごとにパーティション分割された BigQuery テーブルにも振り分け、開発者・モデルごとの支出、ツールの成功率とレイテンシ、フックの待ち時間、ターン単位・セッション単位の分析のための SQL クエリも同梱しています。

#### レバー 3：証明

コントロールのレバーは利用とコストを統制・配分し、追跡のレバーはその支出を可視化します。証明のレバーは、Google Cloud 上の Claude Code の利用を ROI に結び付けるためのものです。

プラットフォームエンジニアが Claude Code で最も測定したい指標は、利用状況、開発者の満足度、インパクトという 3 つの軸に収まります。

**導入と利用状況**の指標は、組織内で Claude がどのように使われているかを測るもので、アクティブ化したユーザー数や、その週次・日次の利用状況が含まれます。これにより、利用の深さ、時間の経過に伴うユーザーの定着率、Claude Code のパワーユーザーが誰かといった情報がわかります。これらの指標はすべて Claude Code の OTel データから導き出されます。

**満足度**の指標は、エンジニアのユーザー体験を把握するもので、Claude Code への満足度、体感的な時間の節約、出力への信頼度、感じている摩擦などが含まれます。満足度の指標は、展開の前後に実施する短いアンケートと、その後の継続的なユーザーへのヒアリングから得られます。

**インパクト**の指標は、Claude が測定可能なエンジニアリング成果をどのように生み出しているかを評価するもので、スループット、サイクルタイム、レビュー速度をベースラインと比較するほか、特定の作業成果に関する定性的な測定も含みます。

### **最初に押さえたいインパクト指標**

ここでは、時間、労力、量の 3 つの領域に分けた、最初に押さえたいインパクト指標を紹介します。

**時間**は、作業がどれだけ早くリリースされるかを測ります。オープンからマージまでの PR サイクルタイムや、コードレビューの所要時間などです。

**労力**は、1 つの変更にどれだけの作業がかかるかを測ります。PR あたりのレビューの往復回数、PR あたりのレビューコメント数や手戻りなどです。

**量**は、空いたキャパシティで何が実現されたかを測ります。エンジニアあたりの PR 数、デプロイ頻度、そして名前の付いた作業成果、つまりチームが空いたキャパシティでリリースした具体的なバックログ項目です。これらは件数に加えて、定性的な視点ももたらします。

これらはルールではなく方向性を示す参考値ですが、組織における Claude Code のインパクトを測る出発点として適しています。必要なベースラインはすでに手元にあります。ソース管理やチケットに残っている、これまでのデリバリーの履歴です。

### **作業の単位を定義する**

これらの指標の多くは PR を数えるものですが、タイポの修正も機能リリースも同じ 1 つの PR です。そこで、定義したクラスに該当するマージ済み PR を数えるようにします。Claude が PR を作成し、それをリリースするかどうかを人が判断する、という形です。hotfix や feature release といったラベル、チケット ID、Claude が関与したかどうかを付けておけば、既存のシステムでそうした PR を簡単に見つけられます。すべての作業単位が PR というわけではありません。サービスの切り替えや、根本原因まで解決したインシデントなどがその例です。考え方は同じで、完了した 1 つの成果を、それが記録される場所で数えます。

## Claude Code のネイティブテレメトリー

コストガバナンスと利用状況の追跡を整えたら、次はそれらを ROI に結び付ける段階です。Claude Code のネイティブテレメトリーは、組織が得ている価値を裏付ける貢献度や生産性の指標を捉えるのに役立ちます。

![Graphic showing Claude Code native telemetry with three columns: Usage, Cost, Contribution / Productivity.](https://assets.claude.com/5d1a4e740237e04f4524c9ff169e0f70def7c5ab.png)

Claude Code の OTel メトリクスを使うと、コード提案の採用率、変更されたコード行数、作成されたコミット数、作成された PR 数、出力単位あたりのコスト、ユーザーあたりの PR 数を追跡または算出できます。

これらのネイティブメトリクスはどれも有用で、行動につなげられる情報を提供します。さらに、[Google Cloud 上の Claude Code テレメトリー](https://docs.google.com/document/d/1LezclyuvbRQ9tInAet0loCEPiNIITB8eLHvzNik9IBs/edit?tab=t.nr7gi1cdf1oi#heading=h.vdcj39wwyv9f)で取得できる、ユーザーのプロンプトやツールの判断といったログイベントと組み合わせると、その価値はいっそう高まります。たとえばユーザーのプロンプトを記録することは、すべての作業単位が PR になるわけではない以上、ユーザー全体が何を作ろうとしているのかを理解するよい方法です。なお、ユーザーのプロンプトは機密性の高い内容を含む可能性があるため自動では記録されず、明示的にオプトインする必要があります。

たとえば、SRE がインシデントのトラブルシューティングに Claude Code を使ったり、セールスエンジニアがライブデモ用のサンプルデータを生成したりするケースです。こうしたセッションは PR にはつながりませんが、それらのチームのワークフローを加速させています。また、Claude Code の PR メトリクスは Claude Code が*作成した* PR の数であり、最終的にマージされた数ではない点に注意してください。何がリリースされたかの記録はあくまでソース管理システムとチケット管理システムにあるため、全体像を把握するには、Claude Code のテレメトリーを GitHub や GitLab、チケットトラッカーと突き合わせてください。

Google Cloud 上で Claude を利用している顧客が Claude Code で実現した、測定可能なインパクトの例を紹介します。

- [Delivery Hero](https://claude.com/customers/delivery-hero) では、あるチームが 100 個の UI コンポーネントにわたるデザインシステムを全面的に刷新しました。通常ならエンジニア 1 人で 1 週間かかる作業を、Claude Code は数分でこなしました。
- [Shopify](https://claude.com/customers/shopify) では、エンジニアが Claude Code でより速く開発しているだけでなく、エンジニア以外のメンバーも、数日かかっていた社内ツールを数分で構築しています。Claude Code は、すでに開発している人を速くするだけでなく、Shopify で開発できる人の幅を広げています。
- [Fifth Dimension](https://cloud.google.com/customers/fifth-dimension-anthropic) では、エンジニア全員が Google Cloud 上の Claude Code を利用しています。合計で月に 30 万行以上のコードを書いており、採用率は 98% に達しています。

## はじめに

本記事の目的は、Google Cloud 上の Claude Code のコストを管理し、ROI を示すために用意されているツールや機能に慣れていただくことです。プラットフォームエンジニアにとって、この仕組みはユーザーの行動に気づき観察するためだけのものではありません。ガバナンスや設定を柔軟に調整するために必要な知見も与えてくれます。

これは継続的なループです。組織全体の支出上限、デフォルトモデル、モデルの許可リストといった妥当なデフォルトから始め、利用データが集まるにつれて役割やチームごとに調整していきます。実際の利用状況を追跡し、Claude Code から得ている価値とメトリクスを結び付けることで、Claude Code 活用の ROI とビジネスインパクトを分析する必要があるステークホルダーに、それらを届けられるようになります。

![Graphic showing a continuous loop for Control - Track - Prove framework](https://assets.claude.com/9a83ef407d2df018b107f8108d1955ad70702d7f.png)

Claude に任せる仕事の量と種類がますます深く多様になるにつれ、組織が Google Cloud 上で Claude Code をどう使い、その利用からどんな価値を得るかも変化していくでしょう。ここで紹介した**コントロール → 追跡 → 証明**のフレームワークは、Claude Code 導入のあらゆる側面と成果を測定するための、揺るぎない出発点となります。

始めるためのリソースは次のとおりです。

- [コストを効果的に管理する](https://code.claude.com/docs/en/costs)
- [利用状況とコストの監視](https://code.claude.com/docs/en/monitoring-usage)
- [Claude apps gateway の支出上限](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)
- [Google Cloud への Claude apps gateway のデプロイ](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp)
- [予算と予算アラートの作成、編集、削除](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp)
- [支出上限予算の管理 | Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps)
