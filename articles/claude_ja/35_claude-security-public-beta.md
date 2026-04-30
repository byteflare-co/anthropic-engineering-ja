---
date: '2026-04-30'
final_url: https://claude.com/blog/claude-security-public-beta
number: 35
selector_used: main
slug: claude-security-public-beta
source_url: https://claude.com/blog/claude-security-public-beta
title: Claude Security is now in public beta
title_ja: Claude Security のパブリックベータが始まりました
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Claude Security のパブリックベータが始まりました

Claude Security が、Claude Enterprise のお客様向けにパブリックベータとして利用可能になりました。

AI のサイバーセキュリティ能力は急速に進化しています。今日のモデルはすでにソフトウェアコードの欠陥を見つけ出すことに非常に長けており、次世代のモデルはさらに高い能力を持ち、特にこれらの欠陥を自律的に *悪用* することに優れているでしょう。動作するソフトウェアエクスプロイトの発見がはるかに容易になる世界に備えて、組織がセキュリティを強化するために行動を起こすべきは、まさに今です。

先日、私たちは Claude Mythos Preview——ソフトウェア脆弱性の発見と悪用の両面で、トップクラスの人間専門家に匹敵またはそれを凌駕しうるモデル——を、[Project Glasswing](https://www.anthropic.com/glasswing) の一環として一部のパートナーに提供開始しました。

しかし、私たちのサイバーセキュリティへの取り組みは Glasswing にとどまりません。Claude Security によって、これまでよりもはるかに多くの組織が、私たちが一般提供している最も強力なモデル Claude Opus 4.7 を、自社のコードベース全体に対して活用できるようになります。Opus 4.7 は、ソフトウェア脆弱性の発見とパッチ適用、そして見落とされがちな複雑で文脈依存の問題の発見において、現時点で最も強力なモデルの一つです。

Claude Security——以前は Claude Code Security と呼ばれていました——は、限定的なリサーチプレビューで、すでにあらゆる規模の数百の組織によってテストされてきました。各チームがコードベースの脆弱性をスキャンし、ピンポイントなパッチを生成するのを支援してきたのです。そこで得られたフィードバックが、今回のリリースを形作りました。本日のリリースでは、Claude Security がすべての Enterprise のお客様にご利用いただけるようになります。スケジュールスキャンとターゲットスキャン、監査システムとの容易な統合、トリアージ済みの発見事項の追跡改善といった機能が含まれています。API 統合やカスタムエージェントの構築は不要です。組織で Claude をお使いであれば、今日からスキャンを始められます。

Opus 4.7 の能力は、多くのエンタープライズがすでに使用しているソフトウェアツールへの Claude の統合を通じて、サイバー防御者にも届けられています。技術パートナーである [CrowdStrike](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-puts-claude-opus-4-7-to-work-across-falcon-platform-project-quiltworks/)、Microsoft Security、[Palo Alto Networks](https://www.paloaltonetworks.com/blog/2026/04/ai-driven-defense-anthropics-claude-opus/)、SentinelOne、[TrendAI](https://newsroom.trendmicro.com/2026-04-30-TrendAI-TM-and-Anthropic-Advance-AI-Powered-Vulnerability-Detection-and-Risk-Mitigation-with-Claude-Opus-4-7)、[Wiz](https://www.wiz.io/blog/red-agent-claude-opus) は、自社ツールに Opus 4.7 を組み込んでいます。さらに、Accenture、BCG、Deloitte、Infosys、PwC といったサービスパートナーも、Claude を統合したセキュリティソリューションの組織への導入を支援しています。

私たちは、サイバーセキュリティにとって極めて重要な時期に入りつつあります。AI は、脆弱性の発見から悪用までのタイムラインを圧縮しつつあります。これに対する正しい対応は、防御者がフロンティアの能力に、最もアクセスしやすい形で——Claude を直接通じて、またパートナーを通じて——届けられるようにすることだと、私たちは考えています。

## **Claude Security の仕組み**

[Claude Security](https://youtu.be/0SgCiUfoYo8) は、Claude.ai のサイドバーから直接、または [claude.ai/security](http://claude.ai/redirect/claudedotcom.v1.ec06f8c9-04ff-472c-b95a-05decd18f5eb/security) からアクセスできます。利用を始めるには、自分のリポジトリの一つを選び（あるいは特定のディレクトリやブランチに範囲を絞り）、スキャンを開始します。

スキャン中、Claude はセキュリティ研究者によく似た方法でコードについて推論します。既知のパターンを検索することで脆弱性を見つけるのではなく、Claude はコンポーネントがファイルやモジュールをまたいでどのように相互作用するかを理解しようとし、データフローを追跡し、ソースコードを読み込みます。

完了すると、Claude は各発見事項について、その脆弱性が本物であるという確信度、深刻度、想定される影響、再現方法を含む詳細な説明を提供します。また、ピンポイントなパッチの手順も生成し、Claude Code on the Web で開いて文脈の中で修正に取り組むこともできます。

## **当初プレビューから学んだこと**

過去 2 か月間、数百のエンタープライズでの本番利用から学んだことに沿って、Claude Security を磨き上げてきました。具体的には、以下のことが分かりました。

**検出品質が最も重要です。** 各チームから、セキュリティ業務を本当に加速させるのは高確信度の発見事項である、との声が寄せられました。Claude Security の多段階バリデーションパイプラインは、各発見事項がアナリストに届く前に独立して検証することで偽陽性を抑え、Claude はあらゆる結果に対して確信度評価を付与します。これにより、チームに届くシグナルは行動する価値のあるものになります。

**スキャンから修正までの時間こそが意味のある指標です。** 初期ユーザーから一貫して指摘されたのがこの点でした。複数のチームが、セキュリティチームとエンジニアリングチームの間で何日もやりとりを繰り返すのではなく、一度のセッションでスキャンからパッチ適用まで進めるようになっています。

**チームが求めているのは継続的なカバレッジであり、一度きりの監査ではありません。** スキャンをスケジュールできるオプションを追加し、各チームが定期的なペースで発見事項のレビューと対応を行えるようにしました。

今回のリリースでは、リポジトリ内の特定のディレクトリに絞ってスキャンする機能、文書化された理由とともに発見事項を却下する機能（後のレビュアーが過去のトリアージ判断を信頼できるようにするため）、既存のトラッキング・監査システム向けに発見事項を CSV または Markdown でエクスポートする機能、Webhook を介して Slack、Jira、その他のツールにスキャン結果を送信する機能も追加しました。

ここでは、Claude Security を使用した組織の方々にその経験を語っていただきます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa585b66f744445eaec7_Doordash_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa5e900d8af5fd782dd2_Doordash_dark.svg)

「私たちは Anthropic とのパートナーシップを通じて、プロアクティブなセキュリティの取り組みを進化させています。Claude Security は、DoorDash の規模とスピードに合わせて新しいコードを生成し、セキュリティを確保する方法を加速させてくれます——深い脆弱性を正確に浮かび上がらせ、発見事項を私たちのワークフローに直接流し込んでくれるので、エンジニアは文脈の中でそれに対応できます。」

Suha Can, Vice President and Chief Security Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ada683bb0532fc4582a3_Snowflake_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5adab7a0103ed60805b38_Snowflake_dark.svg)

「Claude Security は、リサーチプレビューの初期テストの段階で、新規かつ高品質な発見事項を浮かび上がらせ、私たちの環境やお客様に影響が出る前に潜在的なセキュリティ問題を特定して対処するのに役立ちました。利用範囲を広げていくにつれて、強い可能性を感じています。」

Krzysztof Katowicz-Kowalewski, Staff Product Security Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f37e9aa5aaf2be13e1fc87_column-logo-black.png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f38ff88ca62b8275c66f36_logo_column-dark-mode.png)

「Claude Security は、私たちのコードの背後にある実際のビジネスロジックを把握しています。私たちのセキュリティチームは今や、信頼できるツール群の中で、数クリックでスキャンから修正まで進めるようになりました。」

Greg Janowiak, Information Security Officer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f3877190da77141c92e1e5_684b70d717a5356f5a6f8793_yuno_wordmark_dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f390df66611aa841df95df_logo_yuno-dark-mode%20(1).svg)

「スキャンの品質こそ、私たちが Claude Security を脆弱性管理プログラムに直接組み込もうとしている理由です——本物の問題が、間に挟まるトリアージのオーバーヘッドを減らしつつ、より早くエンジニアリングに届くようにするためです。」

Chiara La Valle, Head of Security

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f3a87453ecfe9d53a39_Hebbia-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f3d5a2f38a808068b47_Hebbia-dark-theme.svg)

「脆弱性発見のペースが上がる中で、私たちにとって最も強いシグナルは、発見事項がチケットではなく、実際にマージできる PR にどれだけ早く変わるかです。Claude Security で生成したパッチを使って、本物の脆弱性を数日ではなく数分で塞いできました。」

Matt Aromatorio, Head of Security
