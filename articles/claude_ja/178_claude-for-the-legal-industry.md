---
date: '2026-05-12'
final_url: https://claude.com/resources/articles/claude-for-the-legal-industry
number: 178
selector_used: article
slug: claude-for-the-legal-industry
source_url: https://claude.com/blog/claude-for-the-legal-industry
title: Claude for the legal industry
title_ja: 法務業界のための Claude
---

***アップデート:** Claude for Legal に、[法務業務向けのすぐに使えるアーティファクト](/resources/articles/introducing-artifacts-for-legal-work)が追加されました。*

今年初めに私たちは最初の法務向けプラグインをリリースしました。それから数か月で、法務プロフェッショナルは、あらゆるナレッジワーク職種の中で最も Claude Cowork を積極的に利用するユーザーとなりました。そして今回、その成果をもとに、はるかに大規模なツール群を構築しています。

法務業務は、特有のテクノロジースタックの上に成り立っています。契約ライフサイクル管理システム、[リサーチプラットフォーム](https://claude.com/resources/articles/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work)、文書管理、e ディスカバリー、データルーム、事務所固有のひな形（プレシデント）など、挙げればきりがありません。Claude は現在、いくつかの重要な構成要素を通じて、これらすべてと接続できます。第一に、[MCP コネクタ](https://claude.ai/redirect/claudedotcom.v1.ed6dfcd1-401a-4a8f-b0aa-1d5548aeb472/directory/connectors)が、法務業務（特定の案件に紐づく文書、コミュニケーション、記録）を Claude に取り込みます。第二に、業務分野別のプラグインが、弁護士が最も頻繁に行うタスクをパッケージ化します。そして最後に、どちらもオープンなプロトコル上に構築されているため、法律事務所や企業の法務部門は、実際の業務のやり方に合わせて Claude をカスタマイズできます。[Anthropic 自身の法務チームが Claude をどのように活用しているかはこちら](/resources/articles/how-anthropic-uses-claude-legal)

本日、法務業界がすでに頼りにしているソフトウェアと Claude をつなぐ 20 以上の新しい MCP コネクタと、特定の法務業務や業務分野に合わせた 12 の新しいプラグインを発表します。さらに、Free Law Project や Justice Technology Association をはじめ、現在リーガルサービスを利用できない人々にも法的支援を届けようと取り組む団体と提携します。

## Claude は法務チームが働く場所で働く

Claude は法務チームの今いる場所で力を発揮します。Microsoft Word、Outlook、Excel、PowerPoint の中で直接動作し、4 つのアプリ間でコンテキストを引き継ぎます。Word で仕上げた修正履歴（レッドライン）が Outlook のカバーノート、Excel のクロージングチェックリスト、PowerPoint の取締役会向けサマリーになるときも、改めて説明し直す必要はありません。

**Word** では、Claude のスキル（チームのプレイブックや基準を落とし込んだ再利用可能な指示）が、起草、レッドライン、プレイブックに照らした条項ごとの比較を担い、すべての変更を追跡してその理由を説明します。また、各工程の合間にある定型作業も引き受けます。ドラフトを相手方に送る前に社内コメントを削除したり、署名用版の最終的な書式チェックを行ったり、承認済みのプレイブックから代替条項の文言を引き出したりといった作業です。

**Outlook** では、Claude が届いた案件業務を振り分けます。契約依頼にフラグを立て、返信やカバーノートを起草し、フォローアップを予定に組み込むことで、作業が溜まらないようにします。

**Claude Cowork** では、多数の文書にまたがる業務に同じコネクタとプラグインを利用できます。一連の契約書のトリアージ、製品機能のローンチ前のクリアランス、規制動向に関する取締役会向けメモの起草などです。スケジュールタスクを使えば、週次の規制アップデートの確認や受付案件のトリアージといった定期業務を自動化できます。

そして **Projects** を使えば、案件チームは永続的なワークスペースを持つことができ、ひな形や過去のドラフトがすべての会話にわたって保持されます。

## 法務スタック全体にわたる新しいコネクタ

新しい MCP コネクタにより、Claude は法務チームがすでに頼りにしているシステムとやり取りできるようになります。

**契約ライフサイクルと起草**

- **Definely**：レビューのために契約構造へのライブかつ決定論的なアクセスを提供します。定義の解決、相互参照の検証、依存関係のマッピング、構造的な差分の実行により、修正が契約全体にどう波及するかを確認できます。
- **Docusign**：Claude を契約データに接続し、更新日や義務といった重要条項をすばやく抽出できるようにするとともに、起草から署名、署名後の管理まで、契約ライフサイクル全体にわたる契約ワークフローを統合的に管理します。
- **Ironclad**：Claude が契約リポジトリとワークフローにアクセスし、契約について平易な言葉で質問できるようにします。結果は各ユーザーの権限に応じて自動的に範囲が限定されます。

**ディールルームと取引文書**

- **Box**：Box に保存されたコンテンツに Claude を接続し、ファイルの検索やアクセス、文書への問い合わせ、コンテンツの作成・更新、メタデータフィールドの抽出を可能にします。その際、Box の既存のセキュリティおよびアクセスポリシーは維持されます。
- **Datasite**：毎年数千件の M&A 取引が行われるセキュアなワークスペースである Datasite のバーチャルデータルームに Claude を接続し、フォルダ構成の設定、ユーザーの招待、文書の検索、買い手からの Q&A の追跡、データルームの準備状況の監査を行えるようにします。

**文書管理**

- **iManage**：ナレッジワークプラットフォームである iManage は、案件履歴、文書、組織のナレッジなど、ガバナンス下にある iManage コンテンツへの、権限に基づいた監査可能なアクセスを Claude に提供します。一括エクスポートやカスタム統合は不要です。
- **NetDocuments**：Claude が NetDocuments リポジトリから文書を検索・取得し、組織のひな形に基づいて新しい文書を起草できるようにします。組織の権限とガバナンスポリシーは完全に尊重されます。

**エキスパートネットワークとスキル**

- **Lawve AI**：実務弁護士、企業内弁護士、リーガルテクノロジストが作成した法務 AI スキルの厳選ライブラリを提供し、Claude の中から検索できます。
- **The L Suite**：企業内弁護士の有力コミュニティである同社から、2 つの MCP コネクタが提供されます。(1) Lloyd は、The L Suite のメンバーが Claude を Braintrust メンバープラットフォームに接続できるようにします。(2) TopCounsel は、The L Suite 独自のデータセットとランキングアルゴリズムに基づき、あらゆる企業内弁護士が特定の案件に適した外部弁護士を見つけられるよう支援します。

**e ディスカバリーとレビュー**

- **Consilio**：クライアント自身の進行中の案件と Consilio の Aurora Legal AI を Claude からすぐに利用できるようにします。すべての応答は、ユーザーがすでに閲覧権限を持つ範囲に限定されます。
- **Everlaw**：訴訟プラットフォームを提供する同社のコネクタにより、Claude はメタデータ、キーワード、文書の種類を使って Everlaw プロジェクトの文書を検索・整理・取得でき、レビューへの直接リンクも得られます。
- **Relativity**：法務データインテリジェンスのための AI プラットフォームである RelativityOne において、Claude が案件の立ち上げ、ワークスペーススキーマの設計、アクセス管理、利用状況の分析を行えるようにします。

**フィデューシャリーグレードのワークフロー**

- **Thomson Reuters**：Claude を CoCounsel Legal に接続します。CoCounsel Legal は、主要なすべての業務分野にわたって起草、リサーチ、レビュー、検証をエンドツーエンドで行うフィデューシャリーグレード（受託者責任に耐える水準）のシステムであり、リスクの高い法務業務のための AI アシスタントとして機能します。Westlaw の一次法源、Practical Law のガイダンス、KeyCite、そしてお客様自身の文書に基づき、透明で検証可能なアウトプットを提供します。

**リーガルリサーチと判例法**

- **Legal Data Hunter**：世界で最も急成長している法務コーパスへのアクセスを Claude に提供します。EU の統合法令、最高裁判所や憲法裁判所の判例、公式の学説など、160 以上の法域にわたる 3,100 万件以上の文書を収録しています。
- **Midpage**：複雑なリーガルリサーチ、判決のレビュー、成果物の作成のために、Claude を判例データベースに接続します。すべてが実際の出典にハイパーリンクされているため、容易に検証できます。
- **Trellis**：ドケット、判決、評決、提出書類など、米国最大の州の第一審裁判所データセットへの直接アクセスを Claude に提供し、裁判官や相手方弁護士の分析、申立書の起草に活用できます。

**法務 AI アシスタント**

- **Harvey**：Harvey のリーガルインテリジェンスを Claude にもたらし、一般的な法律上の問い合わせ、Vault プロジェクトを対象とした分析、特定のナレッジソースに関するリサーチの質問をサポートします。
- **Solve Intelligence**：先行技術調査、クレームマッピング、特許の起草のために、Claude を特許文献および非特許文献、法令、SEP の技術標準、オープンウェブに接続します。

**公共サービス**

- **BoardWise**：州の資格委員会の案件に直面している有資格の専門職を支援します。期限の把握、状況への対処、そして法域に合わせた構造化された回答書の起草をサポートします。
- **Courtroom5**：弁護士をつけずに出廷する民事訴訟当事者（全体の約 80%）に法的なガイダンスを提供します。全 50 州にわたり、法域を考慮した案件受付、期限の計算、次のステップの案内を行います。
- **Descrybe**：一次法源を扱うためのリーガルリサーチツールを Claude に提供します。概念や引用による判例検索、判例の取り扱い状況の確認、引用元となる典拠の検索、引用文言の検証が可能です。
- **Free Law Project**：CourtListener が保有する数百万件の米国裁判所の判決、PACER のドケット、裁判官のプロフィール、口頭弁論、引用データに Claude を接続します。

## 業務分野別プラグイン

法務業務の姿は、担う役割によって異なります。私たちは、それぞれ特定の法務ロールを中心に構築された 12 の業務分野別プラグインをリリースします（[こちら](https://github.com/anthropics/claude-for-legal)の Legal Marketplace からダウンロードできます）。各プラグインは、まず短いセットアップインタビューを行い、あなたの業務を学習します。プレイブック、エスカレーションの経路、リスク判断の基準、事務所のスタイルなどです。これにより Claude の回答は汎用的なものではなく、チームに合わせて調整されたものになります。プラグインには次のものがあります。

- **Commercial Legal**：ベンダー契約や NDA をプレイブックに照らしてレビューし、ビジネス側の関係者向けに平易な言葉でまとめたサマリーとともにエスカレーションを振り分けます。
- **Corporate Legal**：M&A を扱います。データルーム全体にわたるデューデリジェンス、開示別紙、取締役会の同意書、クロージングチェックリストなどです。取締役会業務、上場企業のガバナンス、法人のコンプライアンス向けにも設定できます。
- **Employment Legal**：採用、解雇、労働者の分類、休暇に関する期限、社内調査をカバーし、州ごとのルールを組み込んだポリシーを起草します。
- **Privacy Legal**：DPA をプレイブックに照らしてレビューし、PIA や DPIA をトリアージし、法定期限内に DSAR への回答を準備し、文書化されたポリシーと実際の運用とのギャップを指摘します。
- **Product Legal**：社内フレームワークに照らしてローンチレビューを行い、マーケティング上の主張の裏付けを確認し、社内の各チームからのリスクに関する質問に答えます。
- **Regulatory Legal**：規制動向を監視し、重要性の閾値に基づいて絞り込み、新しい規則をポリシーライブラリと比較し、ギャップやパブリックコメントの期限を追跡します。
- **AI Governance Legal**：AI のユースケースをガバナンスの階層に照らしてトリアージし、影響評価を実施し、ベンダーの AI 関連条項をレビューし、AI ポリシーのたたき台を起草できます。
- **IP Legal**：商標クリアランスや FTO（Freedom to Operate）のトリアージを行い、警告書の起草と対応、DMCA 削除要請やオープンソースコンプライアンスへの対応、発明開示のスクリーニングを行います。
- **Litigation Legal**：案件の受付とポートフォリオの追跡、訴訟ホールド、請求書（デマンドレター）、召喚令状のトリアージ、時系列表、証言録取の準備、秘匿特権ログ、準備書面の起草を管理します。
- **Law Student**：ソクラテス式の問答練習、判例要約、IRAC の採点、法域ごとの違いを踏まえた司法試験対策を提供します。
- **Legal Clinic**：クライアントの受付、期限の追跡、案件メモ、指導担当者によるレビューキューを管理します。
- **Legal Builder Hub**：公開レジストリからコミュニティ製の法務スキルを見つけてインストールします。インストールやアップデートのたびに、セキュリティレビュー、ライセンスチェック、鮮度チェックを実行します。

各エージェントテンプレートは、Cowork または Claude Code にワンクリックでインストールでき、組織の起草基準に沿ったアウトプットを生成します。[その一部](https://github.com/anthropics/claude-for-legal)（Commercial Legal、Corporate Legal、Litigation Legal、Product Legal、Litigation Legal）は、Claude Platform 上で Managed Agents としてデプロイし、プログラムから利用できるクックブックとしても提供されています。チームは独自のひな形やプレイブックを重ねて、スキルをカスタマイズできます。

法務組織の働き方はそれぞれ異なり、どんなプラグインのセットでもあらゆる業務を網羅することはできません。プラグインとスキルのエコシステムはオープンなプロトコルであり、**Box、Legal Quants、Lawve AI**、**Thomson Reuters** をはじめとする初期のコントリビューターは、すでに独自のスキル、プラグイン、スタイル規約を公開しています。どのパートナーも、[Directory](https://claude.ai/redirect/claudedotcom.v1.ed6dfcd1-401a-4a8f-b0aa-1d5548aeb472/directory) を通じてコネクタやスキルを提出できます。

## AI でリーガルサービスへのアクセスを民主化する

リーガルサービスは多くの個人や中小企業にとって手の届かないものであり、その格差は広がりつつあります。私たちは **Free Law Project**、**Justice Technology Association**、その他の法律扶助団体や公共サービス団体と協力し、リーガルサービスをより手頃で利用しやすいものにする取り組みを進めています。

要件を満たす法律扶助クリニック、公設弁護人、非営利のリーガルサービス団体は、[Claude for Nonprofits プログラム](https://claude.com/solutions/nonprofits)を通じて大幅な割引価格で利用できます。BoardWise、Courtroom5、Descrybe、Free Law Project が提供する無料または低価格のツールも、MCP コネクタを通じて Claude ユーザーが利用できます。

> 「ほとんどの人は、自分に法的な権利があることを、それを行使するには手遅れになるまで知りません。Claude は今や、人々が不安を抱えて答えを探しているまさにその瞬間に、その人のいる場所で寄り添うことができます。」 - Sonja Ebron, CEO & Co-Founder, Courtroom5

## 法務業界全体からの信頼

法律事務所や企業の法務部門は、Claude を試す段階から、Claude の上で業務を運営する段階へと移行しています。そして、彼らが頼りにする法務ツールも、ますます Claude の上に構築されるようになっています。2 月に開催した [Briefing: Enterprise Agents](https://www.anthropic.com/events/the-briefing-enterprise-agents-virtual-event) では、Thomson Reuters が Claude Agent SDK 上で再構築した CoCounsel を披露しました。今回のリリースにより、その統合は双方向になります。Harvey、Solve Intelligence をはじめ、以下に紹介する各社も同様の取り組みを進めています。

これらのアップデートは、法的推論と長文書の処理において一般公開されている中で最も高性能なモデルである Claude Opus 4.7 を基盤としています。

法務チームやエコシステムのパートナーが、Claude との取り組みについて語ってくれた声を紹介します。

![EvenUp](https://assets.claude.com/466446f5f59635a264efe3e688a42b51c0e88976.svg)

> 「PI（人身傷害）法は AI にとって最も困難な課題のいくつかを突きつけます。大量の医療記録や請求データにわたって推論し、重要な事実を特定し、複雑なワークフローを一貫性と正確性をもって実行することです。Claude Opus 4.8 は、推論、信頼性、ロングコンテキスト性能において新たな水準を実現しています。EvenUp はその上に、独自の PI データ、専門領域の知見、そして目的に特化したワークフローを加えています。」

Rami Karabibar, CEO and CoFounder

![Solve Intelligence](https://assets.claude.com/2819327500f71d308c553acac2e114468c0e86fa.svg)

> 「Claude Opus 4.7 のマルチモーダル理解には、化学構造の読み取りから複雑な技術図面の解釈に至るまで、大きな向上が見られます。より高い解像度のサポートは、Solve Intelligence がライフサイエンス分野の特許ワークフロー（起草や権利化手続きから侵害検出、無効資料チャートの作成まで）向けにクラス最高のツールを構築するのに役立っています。」

Sanj Ahilan, Chief Research Officer

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> 「私たちはすべてのモデルを、引用の正確性、根拠のない判例引用、メモリリーク、拒否の適切性など、24 以上の法務特化型スコアラーで評価しています。訴訟においては、権威ありげなハルシネーションは回答がないことよりも悪いからです。法務業務にとって重要な指標、特にグラウンディングと引用の忠実性において、Claude は社内の比較評価で毎回勝っています。だからこそ、私たちのパイプラインで最もリスクの高い部分は Anthropic 上で動いているのです。」

Jay Madheswaran, CEO and Co-Founder

![Freshfields](https://assets.claude.com/631c9f975e09f01ae344ef9004351099cc0d918b.svg)

> 「Freshfields Lab における私たちのアプローチは、常に入手可能な最良のテクノロジーの上に構築することでした。Claude の能力は、当事務所独自の AI ソリューションに欠かせない要素となっています。今回の協業で私たちはさらに踏み込み、複数ステップにわたる法務タスクをエンドツーエンドで処理できるエージェント型ワークフローを Anthropic と共同開発しています。クライアントにとって、それはより速く、より精緻で、よりスケーラブルなリーガルサービスを意味します。」

Gerrit Beckhaus, Partner and Co-Head

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> 「Accenture の私の法務チームは日常的な法務案件に Claude を活用しており、どのように生産性向上を実現できるかを目の当たりにして、大いに期待を寄せています。」

Mindy Lok, Global IP Legal Lead and Legal Chief Technology Officer

![Thomson Reuters](https://assets.claude.com/3c80d8dc7dbf6556d1137977873dee26eaffae1d.svg)

> 「AI の未来は、作業がどこで行われるかではなく、その結果を信頼できるかどうかによって定義されるでしょう。プロフェッショナルの現場において、それは権威あるコンテンツに基づき、正確性が検証され、セキュリティを中核に据えて構築された AI を意味します。それこそが信頼できる AI の次なるフロンティアであり、Thomson Reuters は Anthropic との取り組みを通じてその最前線をリードしています。」

Joel Hron, CTO

![Quinn Emanuel Urquhart & Sullivan](https://assets.claude.com/9a319a911bf5466e2baf48bd08ee6bb10df98427.png)

> 「コーディングの経験がほとんどないまま、私は Claude 上に当事務所の訴訟プラットフォームを構築しました。実際の公判のために必要だったのです。突破口となったのは、Claude を訴訟チームの一員として扱うことでした。途中から案件に加わるパートナーを迎え入れるときと同じように、時系列、重要な抜粋、主要なテーマを渡してオンボーディングするのです。その成果物は、私ひとりでは到底（おそらく永遠に）成し得なかった水準をはるかに超えています。」

Christopher D. Kercher, Partner, Founder & Head of AI & Data Analytics

![Harvey](https://assets.claude.com/9447073367b83132335cb2c191c36bef275f48e6.svg)

> 「法務は AI による変革において最も有望な業界のひとつであり、だからこそ Anthropic とのパートナーシップを深めることに大きな期待を寄せています。Claude Opus 4.7 は Harvey の BigLaw Bench で 90.9% を記録し、Claude モデルとして過去最高のスコアとなりました。そして Harvey for Claude コネクタは、私たちのリーガルインテリジェンスを Claude の中に直接届けます。」

Winston Weinberg, CEO & Co-Founder

![Crosby](https://assets.claude.com/9815d36508ab5cbef0ba2782bc26371f19356894.svg)

> 「Claude for Word は、Claude のエージェントの力を弁護士の重要な日常ワークフローの中にもたらします。これによりチームは最も重要なことに集中できるようになります。つまり、弁護士は複雑なエッジケースに専門的判断を下し、エンジニアは豊富なコンテキストを活用してクライアントのために自己改善するシステムを構築するのです。」

Ryan Daniels, Co-Founder & CEO

![Legora](https://assets.claude.com/666fbd8fbde356286a5ac8370b994f246c08fb10.svg)

> 「Opus 4.7 は、複雑な法務業務における推論の前進です。長い文書にわたる一貫性が高まり、ニュアンスのある指示をより適切に扱い、リスクの高いワークフローでの信頼性も向上しています。Anthropic が基盤となるインテリジェンスを構築し、Legora はそれを本番運用可能なシステムへと仕上げ、弁護士が実務で信頼できるワークフロー、安全策、インターフェースに Claude を組み込みます。この組み合わせこそが、法務プロフェッショナルに真のインパクトをもたらすのです。」

Jake Lauritzen, CTO

![Holland & Knight](https://assets.claude.com/b8faaa7f6a90ceca02b29e39d7376ccd7dedda75.svg)

> 「Holland & Knight では、Everlaw が Anthropic と連携し、MCP を通じて同社のツールへのアクセスを提供していることを高く評価しています。私たちは多くの訴訟ワークフローに Claude の能力を適用しており、適切なコンテキストのもとでそれを実現することに大きな可能性を見出しています。Everlaw によって適切な証拠を検討に取り込めるようになり、さらなる力が引き出されます。」

Manfred Gabriel, Partner

![EvenUp](https://assets.claude.com/466446f5f59635a264efe3e688a42b51c0e88976.svg)

> 「PI（人身傷害）法は AI にとって最も困難な課題のいくつかを突きつけます。大量の医療記録や請求データにわたって推論し、重要な事実を特定し、複雑なワークフローを一貫性と正確性をもって実行することです。Claude Opus 4.8 は、推論、信頼性、ロングコンテキスト性能において新たな水準を実現しています。EvenUp はその上に、独自の PI データ、専門領域の知見、そして目的に特化したワークフローを加えています。」

Rami Karabibar, CEO and CoFounder

![Solve Intelligence](https://assets.claude.com/2819327500f71d308c553acac2e114468c0e86fa.svg)

> 「Claude Opus 4.7 のマルチモーダル理解には、化学構造の読み取りから複雑な技術図面の解釈に至るまで、大きな向上が見られます。より高い解像度のサポートは、Solve Intelligence がライフサイエンス分野の特許ワークフロー（起草や権利化手続きから侵害検出、無効資料チャートの作成まで）向けにクラス最高のツールを構築するのに役立っています。」

Sanj Ahilan, Chief Research Officer

![Eve Legal](https://assets.claude.com/f1efc487a08ab700dd2f0a0d09e717745da3e2d0.svg)

> 「私たちはすべてのモデルを、引用の正確性、根拠のない判例引用、メモリリーク、拒否の適切性など、24 以上の法務特化型スコアラーで評価しています。訴訟においては、権威ありげなハルシネーションは回答がないことよりも悪いからです。法務業務にとって重要な指標、特にグラウンディングと引用の忠実性において、Claude は社内の比較評価で毎回勝っています。だからこそ、私たちのパイプラインで最もリスクの高い部分は Anthropic 上で動いているのです。」

Jay Madheswaran, CEO and Co-Founder

![Freshfields](https://assets.claude.com/631c9f975e09f01ae344ef9004351099cc0d918b.svg)

> 「Freshfields Lab における私たちのアプローチは、常に入手可能な最良のテクノロジーの上に構築することでした。Claude の能力は、当事務所独自の AI ソリューションに欠かせない要素となっています。今回の協業で私たちはさらに踏み込み、複数ステップにわたる法務タスクをエンドツーエンドで処理できるエージェント型ワークフローを Anthropic と共同開発しています。クライアントにとって、それはより速く、より精緻で、よりスケーラブルなリーガルサービスを意味します。」

Gerrit Beckhaus, Partner and Co-Head

![Accenture](https://assets.claude.com/eef8a51d4b99d31d65fa28d41f247f85bc363b45.svg)

> 「Accenture の私の法務チームは日常的な法務案件に Claude を活用しており、どのように生産性向上を実現できるかを目の当たりにして、大いに期待を寄せています。」

Mindy Lok, Global IP Legal Lead and Legal Chief Technology Officer

![Thomson Reuters](https://assets.claude.com/3c80d8dc7dbf6556d1137977873dee26eaffae1d.svg)

> 「AI の未来は、作業がどこで行われるかではなく、その結果を信頼できるかどうかによって定義されるでしょう。プロフェッショナルの現場において、それは権威あるコンテンツに基づき、正確性が検証され、セキュリティを中核に据えて構築された AI を意味します。それこそが信頼できる AI の次なるフロンティアであり、Thomson Reuters は Anthropic との取り組みを通じてその最前線をリードしています。」

Joel Hron, CTO

1/11

## はじめに

[新しいコネクタ](https://claude.ai/redirect/claudedotcom.v1.ed6dfcd1-401a-4a8f-b0aa-1d5548aeb472/directory/connectors)と[業務分野別プラグイン](https://github.com/anthropics/claude-for-legal)はオープンソースであり、Claude Cowork で利用できます。Enterprise の管理者はワークスペースの設定から有効化できます。詳しくは[こちら](http://www.claude.com/solutions/legal)をご覧いただくか、[営業チームにお問い合わせください](https://claude.com/contact-sales)。

[ローンチウェビナー](http://website.anthropic.com/webinars/how-legal-teams-put-claude-to-work)に登録して、新機能の実際の動作をご覧ください。ライブでの製品ウォークスルーをお見せするとともに、法律事務所や企業の法務部門が Claude と接続されたエコシステムを最大限に活用する方法を紹介します。ビルダーの方は、Legal Quants や Lawvable を通じてコミュニティが管理するスキルを探すこともできます。

法律扶助や司法アクセスに取り組む団体で、パートナーシップに関心のある方は、[Nonprofits プログラム](https://claude.com/solutions/nonprofits)からご連絡ください。
