---
date: '2026-07-02'
final_url: https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend
number: 83
selector_used: main
slug: giving-admins-more-visibility-and-control-over-claude-usage-and-spend
source_url: https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend
title: Giving admins more visibility and control over Claude spend
title_ja: "管理者に Claude の支出に対する可視性と制御をさらに提供する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# 管理者に Claude の支出に対する可視性と制御をさらに提供する

Claude Enterprise 向けに、より充実した管理者アナリティクス、モデル単位のエンタイトルメント、支出アラートを導入します。Claude が組織全体でますます難しく複雑なエージェント的作業を担うようになるにつれ、利用状況とコストのパターンは標準的なチャットツールとは違った様相を見せるようになっています。今回のコントロールにより、管理者は Claude がどのように使われているかを理解するための可視性と、コストを管理するためのツールを手にできます。

今回追加する機能は、Anthropic がすでに提供しているコントロール、つまりあらゆる階層での支出上限、アクセスとモデルのルーティング、エクスポート機能付きの利用状況アナリティクスダッシュボードと Analytics API、そして推論コストの制御の上に積み上がるものです。より充実したアナリティクスときめ細かなコスト制御は、私たちが数か月かけて構築してきたコントロール群への、最新の追加要素です。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a45ed484e5998965a180707_Cost-controls-admin-viz-thumbnail.png)

## 導入状況とコストを追跡する

[管理者向けのアナリティクスダッシュボード](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans) では、グループごと・ユーザーごとに利用状況とコストが表示されるようになり、作成された artifact、編集されたファイル、利用された skill やコネクタなどのアウトプットが、そのコストのすぐ隣に並ぶようになりました。管理者は IT チームがすでに管理している SCIM グループでフィルタリングでき、既存の組織図に沿った内訳を得られます。

Claude Code には、管理コンソール内に価値と利用状況にフォーカスした 2 つの新しいタブが追加され、より詳しいインサイトが得られるようになりました。Usage タブでは、組織全体のアクティブな開発者、セッション数、上位のコマンドが表示され、日次で更新されます。Value タブでは利用状況とコストのデータをまとめ、Claude Code の価値を一目で把握できるようにします。生産性の向上、コミットあたりのコスト、年間の価値を推定します。すべての計算式はタブ上で確認でき、入力値も調整可能です。

[Analytics chat](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage) は、はるかに幅広い質問に答え、深掘りできるより充実した artifact を生成できるようになりました。管理者は「今月 Claude の利用を倍増させたチームはどこ?」や「1 シートあたりの価値が最も高いのはどこ?」といった質問を自然言語で投げかけることができ、Claude はステークホルダーとエクスポートして共有できるチャートを返します。

利用状況とコストのデータは [Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api) を通じてプログラマブルに取得できるため、財務や IT は Datadog Cloud Cost Management や CloudZero のようなすでに運用しているツールに Claude の利用状況とコストデータを取り込み、他のクラウドや AI の支出と並べて確認できます。結果は日付範囲、チーム、プロダクト、モデルでフィルタできます。Skill はそれぞれの利用状況とコストを報告し、新しいエンドポイントではプラグインの導入状況や artifact の作成状況を追跡できます。

管理者は、コスト、プロダクトとモデル別の内訳、支出上限に対する進捗といった利用状況の可視性を個々のユーザーへ拡張でき、誰も突然の遮断に見舞われることがなくなります。ユーザー側でも自分の利用トレンドを時系列で確認でき、どのプロダクト・モデル・skill を最も使っているか、そしてその活動が支出としてどう積み上がっているかがわかります。

## 支出を管理するためのコントロール

[モデルのデフォルトとエンタイトルメント](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization) により、管理者はチャット・Cowork・Claude Code にわたって、新しい会話を開始するときのデフォルトの Claude モデルを設定できます。これにより、日常的な作業が必ずしも最も高価なオプションをデフォルトにしないようにできます。管理者は、特定の役割向け、あるいは組織全体向けにどのモデルを利用可能にするかを制御できます。

支出しきい値アラートは、組織レベルの支出上限の 75% と 90% で管理者に通知します。これにより、誰かが作業中に上限に引っかかって止められる前に、上限を引き上げる時間が確保できます。ユーザーは 75% と 95% のしきい値でアプリ内通知を受け取り、Claude を離れずに管理者へ上限引き上げをリクエストできます。

多数のグループにまたがって上限を管理している組織向けに、[Admin API](https://platform.claude.com/docs/en/manage-claude/spend-limits-api#example-workflows) はコスト制御のワークフローをスクリプトへ落とし込み、組織のスケールに合わせて制御をスケールさせます。上限引き上げリクエストのレビュー自動化、支出上限に近づいているメンバーの特定、急激に変化している利用状況のフラグ付けなどを、すべてスケールして行えます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c4898064ee45d6186056ab_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c4897e0ac296b8c65e5713_Frame-1.svg)

「コストの可視化は月に一度の作業ではありません。きめ細かな支出データとアラートがあれば、請求サイクルの終わりに驚くのではなく、Claude をどう使っているかをチームが定期的に見直すきっかけになります。Analytics API を使えば、そのデータを私たちが日常的に使っているツールへ取り込めます。」

Kyra Abbu, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a451ef104342d131f95adb1_Workato_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a451ef3b97d50cc14b9f880_Workato_dark.svg)

「私たちの最良の四半期をけん引している人たちに減速をかけるつもりはありませんし、CFO からそれを求められてもいません。彼が求めているのは ROI です。エンタープライズ MCP サーバに接続した Claude は、私たちの売上を 4% 押し上げました。チームごとにコストとビジネスインパクトを並べて見られることは、その主張を通すうえで欠かせません。」

Carter Busse, CIO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4691bbbc84cd40c4662c8c_nubank-color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4691b8d4901403602b533c_nubank-white.svg)

「トークンの使用量だけを見ていても、多くのことはわかりません。私が本当に見たいのは、組織全体で繰り返し実行されている skill はどれか、ということです。それこそが価値の本当のシグナルです。」

Ciro Yamada, Product Director

## 使い始める

組織全体で Claude を管理している管理者の方へ: 管理コンソールで利用状況とコストの内訳を確認し、グループごとにモデルのデフォルトと支出上限を設定し、支出しきい値アラートを設定して超過に先回りしましょう。利用状況データは管理ダッシュボードで確認でき、Analytics API により、財務や IT は同じメトリクスを既存のレポーティングシステムへ取り込めます。詳しくは [こちら](https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api) をご覧ください。
