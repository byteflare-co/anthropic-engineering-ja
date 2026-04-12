---
date: '2026-04-09'
final_url: https://claude.com/blog/cowork-for-enterprise
number: 18
selector_used: main
slug: cowork-for-enterprise
source_url: https://claude.com/blog/cowork-for-enterprise
title: Making Claude Cowork ready for enterprise
title_ja: Claude Cowork をエンタープライズ対応に
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

# Claude Cowork をエンタープライズ対応に

Claude Cowork がすべての有料プランで一般提供されました。企業内で Claude Cowork はチーム運営の重要な一部となっています：タスクの処理、プロジェクト成果物の下書き、チームの最新情報の共有などを担っています。

本日、チームが Claude Cowork を全社的に展開するための組織管理機能を導入します：Enterprise 向けのロールベースアクセス制御、グループ支出制限、拡張された OpenTelemetry オブザーバビリティ、管理者が Claude Cowork の導入状況を確認するための利用分析です。

## 初期のシグナル

Claude Code は開発者が Claude に質問を渡すことからタスク全体を渡すことへの移行を助けましたが、Claude Cowork でも組織全体で同じパターンが見られます：Claude Cowork の利用の大部分はエンジニアリングチーム以外から来ています。重要なのは、オペレーション、マーケティング、財務、法務などの部門が Claude にコア業務を渡しているのではなく、最も重要なタスクを取り巻く周辺作業——プロジェクトの進捗報告、コラボレーション用の資料、リサーチスプリントなど——を渡しているということです。

Claude Cowork の早期エンタープライズ導入企業がこのパターンを 1 つのチームで確認すると、より広範に展開したいと考えることが多く、誰がアクセスできるか、支出管理、チーム横断で何が起きているかの可視化といった課題が浮上します。

## 組織全体への展開のための管理機能

Claude Cowork の機能を備えたエージェントを組織全体に展開するには、管理チーム向けのガバナンスと可視性が必要です。本日、組織が必要とする管理機能をさらに追加します：

**ロールベースアクセス制御。** Claude Enterprise の管理者は、ユーザーをグループに整理——手動または ID プロバイダからの SCIM 経由——し、メンバーが使用できる Claude の機能を定義するカスタムロールを各グループに割り当てられるようになりました。特定のチームに Claude Cowork をオンにし、導入の進展に合わせて調整できます。

**グループ支出制限。** 管理コンソールからチームごとの予算を設定できます。予測可能なコストで、各チームのニーズに応じて調整可能です。

**利用分析。** Claude Cowork のアクティビティが管理ダッシュボードと Analytics API に表示されるようになりました。ダッシュボードでは、管理者がさまざまな期間にわたる Claude Cowork のセッション数とアクティブユーザー数を追跡できます。Analytics API ではさらに詳細に：ユーザーごとの Claude Cowork アクティビティ、Skills やコネクタの呼び出し、既存の Chat および Claude Code の数値と並んだ DAU/WAU/MAU を確認できます。どのチームが導入しているか、どのワークフローが定着しているか、次にどこに投資すべきかを把握できます。

**拡張された OpenTelemetry サポート。** Claude Cowork がツールやコネクタの呼び出し、ファイルの読み取りまたは変更、使用された Skills、各 AI 起動アクションが手動で承認されたか自動で承認されたかのイベントを発行するようになりました。イベントは Splunk や Cribl などの標準的な SIEM パイプラインと互換性があり、共有ユーザーアカウント識別子により OTEL イベントを Compliance API レコードと関連付けることができます。OpenTelemetry は Team および Enterprise プランで利用可能です。

**Zoom MCP コネクタ。** Claude Cowork はチームがすでに使用しているツールと統合されます。本日、Zoom がミーティングインテリジェンスを Cowork 体験に直接取り込むコネクタをローンチします。Zoom コネクタは AI Companion のミーティングサマリーとアクションアイテムをトランスクリプトやスマートレコーディングとともに提供し、チームが Zoom での会話を Cowork でのエージェンティックワークフローの作成に活用できるようにします。Zoom は Claude の設定のコネクタディレクトリから追加できます。

**ツールごとのコネクタ制御。** 管理者は、組織全体にわたる各 MCP コネクタ内で利用可能なアクションを制限できるようになりました——たとえば、読み取りアクセスは許可しつつ書き込み操作は無効にするといった設定が可能です。パーミッションは組織全体に適用され、管理コンソールから設定します。

## 組織での Claude Cowork の活用事例

[Zapier](https://claude.com/customers/zapier-cowork-qa) は Cowork を組織のデータベース、Slack、Jira に接続してエンジニアリングのボトルネックを可視化しました——ダッシュボード、チームごとの分析、優先順位付けされたロードマップが返され、Product チームと Design Ops チームがそれを自分たちのために複製しました。[Jamf](https://claude.com/customers/jamf) は 7 つの側面を持つパフォーマンスレビューを 45 分のガイド付き自己評価に変換し、その後ベンダーレビューやインシデント対応にも同様のワークフローを構築しました。ベンチャーファームの [Airtree](https://claude.com/customers/airtree) は、ポートフォリオ企業の Drive、Slack の更新情報、競合ニュースから情報を取得し、前回の準備資料と照合するボード準備ワークフローを構築しました。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba1577e91d8296653388ca_Group%202055245285.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba157c0117254341bed811_Group%202055245285-1.svg)

「Claude Cowork は、以前は正当化しにくかった規模の仕事をチームができるよう支援します。人間の役割は検証、改善、意思決定になります。繰り返しの手直し作業ではなく。」

Joel Hron、CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aedd1d4ccaa7aaecee72_zapier_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aed89af0a9a659d820f0_zapier_dark.svg)

「"アイデアを思いつく"ことと"何かを出荷する"ことの間の壁が崩壊しました。今重要なスキルは、すべてのステップのやり方を知っていることではありません。自分が何を達成しようとしているかを明確に理解し、その成果に向けて指揮できることです。実行は依然として本当の仕事ですが、一人が出荷できるものの上限は劇的に引き上げられました。正直なところ、これなしで仕事をしていた頃のことを思い出せません。」

Larisa Cavallaro、AI オートメーションエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b45499ebd143bd2c52765a_logo_jamf-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b454a6ceaa3ebddb228495_logo_jamf-dark.svg)

「組織全体の人々が Cowork をデータブレンディング、分析、ダッシュボード構築に使っています。ビスポーク（カスタム）のダッシュボード作成は非常に大きな効果がありました。以前は BI ツールやエンジニアの助けが必要だったタスクを、今では各自が数分でこなしています。」

Nick Benyo、ソフトウェアエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4c1998c3401934f20e29f_logo_airtree-light-mode.png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c4c19b37fe50b8853f38b3_logo_airtree-dark-mode.png)

「チーム横断で Claude Cowork を使うことで、その価値が何倍にもなりました。一人が作った Skills を全員が使えるようになりました。Claude Cowork は個人の生産性ツールではなく、ファーム共通のインフラストラクチャになったのです。」

Jackie Vullinghs、パートナー
