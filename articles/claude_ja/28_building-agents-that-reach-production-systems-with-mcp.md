---
date: '2026-04-22'
final_url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
number: 28
selector_used: main
slug: building-agents-that-reach-production-systems-with-mcp
source_url: https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
title: Building agents that reach production systems with MCP
title_ja: "MCP で本番システムに到達するエージェントを構築する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

# MCP で本番システムに到達するエージェントを構築する

エージェントは、到達できるシステムの範囲でしか役に立ちません。エージェントを外部システムに接続する方法として、各チームは直接 API 呼び出し、CLI、MCP の 3 つのアプローチに収束する傾向があります。本記事では、それぞれが適する場面、本番のエージェントが MCP に行き着く理由、そしてそうした統合を効果的に構築するためのパターンを整理します。

## エージェントを外部システムに接続する

エージェントを外部システムに接続する経路として、私たちは一般に 3 つを目にします。直接 API 呼び出し、CLI、そして MCP です。それぞれ、何を構築しているかに応じてどこかで意味をなします。重要な違いは、エージェントとサービスの間に共通の層があるかどうか、そしてその層がどこまで届くかです。

### 直接 API 呼び出し

エージェントが API を直接呼び出します。コード実行サンドボックス内で HTTP リクエストを発行するコードを書くか、汎用のファンクションコール用ツールを介して行います。多くのチームはここから始め、1 つのエージェントが 1 つのサービスと対話する場合や、エージェントプラットフォーム間で再利用する必要のない少数の統合であれば問題なく機能します。

課題はスケールするにつれて出てきます。エージェントとサービスの間に共通の層がないため、エージェントとサービスのペアそれぞれが、独自の認証処理・ツール記述・エッジケースを持つ一点物の統合になります——M×N 統合問題です。

### コマンドラインインターフェース（CLI）

エージェントがシェル上でコマンドラインツールを実行します。高速かつ軽量で、既存のツールに乗っかれます。ローカル環境やサンドボックス化されたコンテナ——ファイルシステムとシェルがある場所ならどこでも——でうまく機能します。これは共通の層を提供しますが、薄い層です。

CLI は、コンテナを公開していないモバイル、Web、クラウドホスト型プラットフォームに届かないという厳しい制約に当たりますし、認証は CLI 自身の仕組み——通常はディスク上の認証情報ファイル——で処理されます。ローカル環境における素早く許容度の高い統合に最も適しています。

### Model Context Protocol（MCP）

MCP は、共通の層をプロトコルとして提供します。エージェントは、システムのケーパビリティを公開するサーバーに接続し、認証・ディスカバリ・豊かなセマンティクスが標準化されています。1 つのリモートサーバーが、あらゆるデプロイ環境で、あらゆる互換クライアント（Claude、ChatGPT、Cursor、VS Code など）に届きます。

先行投資が少しだけ必要になります。見返りとして統合はポータブルになり、機能豊富なエージェント統合に必要なセマンティクスが得られます。

## 本番のエージェントはクラウドで動く

スケールし継続的に稼働させるため、本番のエージェントはますますクラウドで動くようになっています。エージェントが到達すべきシステム——データが置かれ、作業が追跡され、インフラが走っている場所——もクラウドホストです。これらのシステムはリモートで認証の背後にあることが多く、そこで MCP が共通の層を提供します。

これはすでに採用動向に表れています。[MCP SDK](https://modelcontextprotocol.io/docs/sdk) のダウンロード数は、今年の初めの月間 1 億から最近 3 億を突破し、エンタープライズや主要なエージェンティックプラットフォームで強い採用が進んでいます。何百万人もの人々が日々 Claude で MCP を利用しており、このプロトコルは [Claude Cowork](https://claude.com/product/cowork)、[Claude Managed Agents](https://claude.com/blog/claude-managed-agents)、[Claude Code の channels](https://code.claude.com/docs/en/channels) など、最近私たちが出荷した多くの機能を支えています。

MCP が本番のエージェンティックシステムを支え続けるなかで、私たちはこうした統合を適切に構築するためのパターンを共有します。高度なサーバーの構築から、コンテキスト効率の良いクライアント、そして skills がプロトコルを補完する場所まで取り上げます。

## 効果的な MCP サーバーを構築する

私たちの[ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.2c1987ee-b62f-4279-900c-f2285fc3ed34/directory/connectors)には 200 を超える MCP サーバーがあり、毎日何百万人もの人々に利用されています。プロトコル上で構築するエンタープライズや開発者と密に仕事をするなかで、サーバーをエージェントがどれだけ確実に使えるかを決める、いくつかの設計パターンが見えてきました。

### 最大のリーチのためにリモートサーバーを構築する

リモートサーバーこそが配布を可能にします——Web、モバイル、クラウドホスト型エージェントをまたいで動作する唯一の構成であり、主要なクライアントが消費するように最適化されているのはこれです。エージェントがどこで動いていてもあなたのシステムを使えるよう、リモートサーバーを構築してください。

### エンドポイントではなく意図を軸にツールをまとめる

少数でよく記述されたツールは、網羅的な API のミラーを安定して凌駕します。API を MCP サーバーに 1 対 1 で包むのではなく、意図を軸にツールをまとめましょう。そうすればエージェントは、多くのプリミティブを継ぎ合わせる代わりに、数回の呼び出しでタスクを達成できます。1 つの create\_issue\_from\_thread ツールは、get\_thread + parse\_messages + create\_issue + link\_attachment を上回ります。パターン全体の詳細は [writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents) を参照してください。

### 表面積が広い場合はコードオーケストレーション向けに設計する

Cloudflare、AWS、Kubernetes のように、サービスが数百の個別操作を必要とする場合、意図でまとめたツールセットでは恐らくカバーしきれません。代わりに、コードを受け取る薄いツール表面を公開します——エージェントが短いスクリプトを書き、サーバーはそれをサンドボックスであなたの API に対して実行し、結果だけがコンテキストに返ります。[Cloudflare の MCP サーバー](https://github.com/cloudflare/mcp)がリファレンス例で、2 つのツール（search と execute）が約 2,500 のエンドポイントを約 1K トークンでカバーします。

### 役に立つ場所では豊かなセマンティクスを出荷する

[MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview) は最初の公式プロトコル拡張で、ツールがチャートやフォーム、ダッシュボードのようなインタラクティブなインターフェースを返し、チャット画面内にインラインでレンダリングできるようにします。MCP apps を出荷するサーバーは、テキストだけを返すサーバーに比べて採用と定着が有意に高くなる傾向があります。肝心な瞬間にエージェントやエンドユーザーの前に製品の UI を差し出すために使ってください——この拡張は Claude.ai、Claude Cowork、その他多くの主要な AI ツールでサポートされています。

‍[Elicitation](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation) は、サーバーがツール呼び出しの途中で一時停止してユーザーに入力を求められるようにします。[Form mode](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation#form-mode-elicitation-requests) はシンプルなスキーマを送ると、クライアントがネイティブのフォームをレンダリングします——欠けているパラメータの要求、破壊的な操作の確認、選択肢の曖昧さ解消に使えます。[URL mode](https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation#url-mode-elicitation-requests) はユーザーをブラウザに渡します——下流の OAuth の完了、決済の処理、MCP クライアントを経由させるべきでない資格情報の収集に使えます。どちらもユーザーを設定ページに送り出さず、フローに留めておけます。Form mode は広範にサポートされ、URL mode は Claude Code でサポートされており、他のクライアントでも対応が進んでいます。

### 標準化された認証に乗る

標準化された認証こそが、クラウドホスト型エージェントにとって MCP を実用的なものにします。サーバーが OAuth を必要とする場合、最新の [MCP 仕様](https://modelcontextprotocol.io/specification/2025-11-25)はクライアント登録向けに [CIMD](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#client-id-metadata-documents)（Client ID Metadata Documents）をサポートします——これによりユーザーは初回認証フローが高速になり、予期せぬ再認証プロンプトも大幅に減ります。これは私たちが推奨する認証方式であり、MCP SDK、Claude.ai、Claude Code でサポートされ、業界全体で広く採用されつつあります。

ユーザーが一度認可した後、次の問いはクラウドホスト型エージェントがそれらのトークンを実行時にどう保持し再利用するかです。[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) の [Vaults](https://platform.claude.com/docs/en/managed-agents/vaults#mcp-oauth-credential) がこれをカバーします。ユーザーの OAuth トークンを一度登録し、セッション作成時に ID で vault を参照すれば、プラットフォームが各 MCP 接続に適切な資格情報を注入し、リフレッシュもあなたの代わりに行います——独自のシークレットストアを構築する必要も、呼び出しごとにトークンを取り回す必要もありません。

## MCP クライアントをコンテキスト効率良くする

MCP は、AI エージェント（[*クライアント*](https://modelcontextprotocol.io/docs/develop/build-client#python)）が必要なツールやデータソース（[*サーバー*](https://modelcontextprotocol.io/docs/develop/build-server)）に接続して動作する方法を標準化します。サーバーは一連のケーパビリティを安全に公開し、クライアントはそれらをオーケストレーションしコンテキストを管理します。MCP クライアントを構築しているなら、progressive disclosure（段階的開示）のパターンでコンテキスト効率を高めましょう。

### tool search でツール定義を必要に応じてロードする

[Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) は、すべてのツールをあらかじめコンテキストにロードするのではなく、ロードを後回しにします。これによりエージェントは実行時にカタログを検索し、必要なときに関連するツールを引き込めます。私たちの[テスト](https://www.anthropic.com/engineering/advanced-tool-use)では、tool search は高い選択精度を保ちつつ、ツール定義のトークンを 85% 以上削減する傾向があります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e920e636fbec575e46319c_context-usage.webp)

tool search によるコンテキスト使用量の削減。出典: [advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use)

### programmatic tool calling でツール結果をコード内で処理する

[Programmatic tool calling](https://www.anthropic.com/engineering/code-execution-with-mcp) は、ツール結果を生のままモデルに返すのではなく、コード実行サンドボックス内で処理します。これによりエージェントはコード内で呼び出しをまたいでループ・フィルタ・集約でき、最終的な出力だけがコンテキストに到達します。私たちのテストでは、複雑な多段階ワークフローで使用トークン量を約 [37%](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) 削減します。

これらのパターンは複数のサーバーをまたいで自然に組み合わせられます——より軽いコンテキスト、より少ないラウンドトリップ、より速い応答です。全体の内訳は [*advanced tool use*](https://www.anthropic.com/engineering/advanced-tool-use) を参照してください。

## MCP サーバーと skills を組み合わせる

[Skills と MCP は相補的な関係です](https://claude.com/blog/skills-explained)。MCP はエージェントに外部システムのツールとデータへのアクセスを与え、skills はそれらのツールを使って実際の仕事を達成する *手順知識* をエージェントに教えます。最も有能なエージェントは両方を使い、skills によって MCP サーバーは一握りの接続を超えてスケールします。両者を組み合わせる一般的なパターンは 2 つあります。

### skills と MCP サーバーをプラグインとしてバンドルする

Claude の[プラグイン](https://code.claude.com/docs/en/plugins-reference#plugin-components-reference)は、skills、MCP サーバー、hooks、LSP サーバー、専用のサブエージェントを、簡単に消費できる 1 つの配布方式にまとめられる便利な抽象化です。このアプローチは、最小限の摩擦で複数のコンテキストプロバイダを統合する最良の方法です。

MCP サーバーと skills を組み合わせると、Claude はよりドメインスペシャリストのように振る舞えるようになります。MCP を介してツールを掴み、Claude にワークフローをエンドツーエンドでオーケストレーションする skills を与えてください。Cowork 向けの[データプラグイン](https://claude.ai/redirect/claudedotcom.v1.2c1987ee-b62f-4279-900c-f2285fc3ed34/directory/plugins/data%40knowledge-work-plugins)がその例で、Snowflake、Databricks、BigQuery、Hex などのアプリ向けに 10 の skills と 8 つの MCP サーバーで構成されています。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6945b3dfa8f134d0104e4e23_How%20Skills%20and%20MCP%20work%20together%20-%20v3B%402x%20(2).png)

skills と MCP の組み合わせ。出典: [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers)

### MCP サーバーから skills を配布する

プロバイダが MCP サーバーと並んで skill を公開することがますます一般的になっており、エージェントは生のケーパビリティと、それらを適切に使うための意見の入ったプレイブックの両方を受け取れます。[Canva](https://claude.com/connectors/atlassian)、[Notion](https://claude.com/connectors/notion)、[Sentry](https://claude.com/connectors/sentry) などは今日 Claude でこれを行っており、私たちの [Web ディレクトリ](https://claude.com/connectors)でコネクタの隣に skill を掲載しています。

このペアリングをあらゆるクライアント間でポータブルにするため、MCP コミュニティはサーバーから直接 skills を届けるための[拡張](https://github.com/modelcontextprotocol/experimental-ext-skills)を活発に進めています。このやり方なら、クライアントは依存する API とバージョンが合った関連する専門知識を自動的に継承します。この拡張が安定するにつれて、このパターンは広く採用されるようになると見ています。

## 積み上がる層

冒頭ではエージェントを外部システムに接続する 3 つの経路を挙げました。実際には、成熟した統合は 3 つすべてを出荷するでしょう——基盤としての API、ローカルファーストな環境向けの CLI、そしてクラウド基盤のエージェント向けの MCP です。

本番のエージェントがクラウドへ移行するにつれて、MCP は極めて重要な層になります——そして積み上げ効果のある層です。今日、1 つのリモートサーバーがあらゆるデプロイ環境の互換クライアントすべてに届き、認証・双方向性・豊かなセマンティクスはプロトコル側で処理されます。より多くのクライアントが仕様を採用し、より多くの拡張が投入されるにつれて、あなたは何も新たに出荷しなくても、同じサーバーがより高機能になっていきます。

統合を構築するとき、クラウド上の本番エージェントに自分のシステムに到達させることがゴールなら、MCP サーバーを構築し、上記のパターンで卓越したものに仕上げてください。MCP 上に構築されたすべての統合は、エコシステムを強化します——孤独に解決すべきエッジケースは減り、メンテナンスすべき一点物の統合も減ります。

### Acknowledgements

本ブログへの貢献に対し、Den Delimarsky、David Soria Parra、Henry Shi、Felix Rieseberg、Conor Kelly、Molly Vorwerck、Andy Schumeister、Kevin Garcia、Amie Rotherham、Matt Samuels、Angela Jiang、Katelyn Lesse、AJ Rebeiro、Jess Yan に感謝します。
