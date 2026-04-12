---
date: '2026-04-08'
final_url: https://claude.com/blog/claude-managed-agents
number: 8
selector_used: main
slug: claude-managed-agents
source_url: https://claude.com/blog/claude-managed-agents
title: 'Claude Managed Agents: get to production 10x faster'
title_ja: "Claude Managed Agents: 本番投入を 10 倍速く"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d227246bc2b5a3cc3626_9f6a378a1e3592cf8d27447457409ba12284faef-1000x1000.svg)

# Claude Managed Agents: 本番投入を 10 倍速く

本日、クラウドホスト型エージェントをスケールさせながら構築・デプロイするためのコンポーザブル API 群、Claude Managed Agents をローンチします。

これまで、エージェントを作るということは、セキュアなインフラ、状態管理、権限設定、そしてモデルアップグレードのたびにエージェントループを書き直すことに開発サイクルを費やすことを意味していました。Managed Agents は、パフォーマンス向けにチューニングされたエージェントハーネスと、本番インフラを組み合わせることで、プロトタイプからローンチまでを数か月ではなく数日に短縮します。

シングルタスクランナーを作っているのか、複雑なマルチエージェントパイプラインを作っているのかを問わず、運用オーバーヘッドではなくユーザー体験に集中できるようになります。

Managed Agents は本日、Claude Platform でパブリックベータとして提供開始します。

## エージェントを 10 倍速く構築してデプロイする

本番エージェントを出荷するには、サンドボックス化されたコード実行、チェックポイント、認証情報管理、スコープ付き権限、エンドツーエンドのトレーシングが必要です。ユーザーが目にするものを 1 つ出す前に、数か月分のインフラ仕事が発生するのです。

Managed Agents はその複雑さを肩代わりします。あなたはエージェントのタスク、ツール、ガードレールを定義し、私たちは自社のインフラ上でそれを動かします。組み込みのオーケストレーションハーネスは、いつツールを呼ぶか、コンテキストをどう管理するか、エラーからどう回復するかを判断します。

Managed Agents には次のものが含まれます。

- **本番グレードのエージェント**: セキュアなサンドボックス化、認証、ツール実行が代行されています。
- **長時間セッション**: 何時間も自律的に動作し、切断を乗り越えて進捗と出力が保持されます。
- **マルチエージェント協調**: エージェントが他のエージェントを立ち上げて指示し、複雑な作業を並列化できます (*リサーチプレビュー*として提供中——アクセス申請は[こちら](http://claude.com/form/claude-managed-agents))。
- **信頼できるガバナンス**: スコープ付き権限、ID 管理、実行トレーシングを組み込み、エージェントに実システムへのアクセスを与えられます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d53a1b570fa207204f0111_Claude-Blog-Managed-Agents-Diagram-NoBorder.png)

Claude Managed Agents のアーキテクチャ

## Claude を最大限活かすために設計されている

Claude のモデルはエージェント型の仕事向けに作られています。Managed Agents はその Claude のために目的特化で作られており、より少ない労力でよりよいエージェントの成果を得られるようにします。

Managed Agents を使えば、あなたは成果と成功基準を定義するだけで、Claude が自己評価して到達するまで反復します (*リサーチプレビュー*として提供中——アクセス申請は[こちら](http://claude.com/form/claude-managed-agents))。より厳しいコントロールが欲しい場合には、従来のプロンプト・レスポンス型のワークフローもサポートしています。

構造化ファイル生成に関する社内テストでは、Managed Agents は標準的なプロンプトループよりも最大で 10 ポイント、タスク成果の成功率を改善しました——もっとも難しい問題でとくに大きな伸びを見せました。

セッショントレーシング、統合アナリティクス、トラブルシューティングのガイダンスは Claude Console に直接組み込まれており、すべてのツール呼び出し、判断、失敗モードを確認できます。

## チームが作っているもの

チームはすでに Managed Agents で 10 倍速くリリースしており、幅広い本番ユースケースに対応しています。コードベースを読み、修正を計画し、PR を開くコーディングエージェント。プロジェクトに参加し、タスクをピックアップし、他のチームメンバーと並んで成果物を届ける生産性エージェント。ドキュメントを処理して重要な情報を抽出する財務・法務エージェント。いずれのケースでも、数日でリリースすることは、ユーザーに価値をより速く届けることを意味します。

- [**Notion**](https://claude.com/customers/notion-qa) は、ワークスペース内で直接チームが Claude に作業を委任できるようにしています (Notion Custom Agents 内のプライベートアルファで提供中)。エンジニアはコードを出荷するのに、ナレッジワーカーはウェブサイトやプレゼンテーションを生成するのに使っています。何十ものタスクが並列で実行でき、チーム全体が成果物について協働できます。
- [**Rakuten**](https://claude.com/customers/rakuten-qa) は、Slack や Teams に接続されるエンタープライズエージェントを、プロダクト・セールス・マーケティング・財務にまたがって出荷しました。従業員はタスクを割り当て、スプレッドシート、スライド、アプリといった成果物を受け取れます。専門エージェントはそれぞれ 1 週間以内にデプロイされました。
- [**Asana**](https://claude.com/customers/asana-qa) は Asana プロジェクト内で人間と並んで働く協働型 AI エージェント「AI Teammates」を構築しました。チームは高度な機能を追加するのに、そうでなければ到達できないほど劇的に速いスピードを実現しました。
- [**Vibecode**](https://claude.com/customers/vibecode) は、Managed Agents をデフォルトの統合として使い、顧客がプロンプトからデプロイ済みアプリまで進めるのを手助けしています。新世代の AI ネイティブアプリを支えているのです。ユーザーは同じインフラをこれまでより少なくとも 10 倍速くスピンアップできるようになりました。
- [**Sentry**](https://claude.com/customers/sentry) は、彼らのデバッグエージェント Seer を、Claude を活用したパッチ作成・PR 作成エージェントとペアにしました。開発者はフラグ立てされたバグから、レビュー可能な修正まで 1 つのフローで進めます。この統合は Managed Agents の上で、数か月ではなく数週間で出荷されました。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69813caf8d50645af3af864f_logo_vibecode-light-mode.svg)

「Claude Managed Agents が登場する前は、ユーザーは LLM をサンドボックス内で手動で実行し、そのライフサイクルを管理し、適切なツールを装備させ、実行を監督する必要がありました——セットアップに数週間から数か月かかることもあるプロセスです。今では数行のコードで、同じインフラを少なくとも 10 倍速くスピンアップできます。これは、開発者にも vibe コーダーにも、作れるものの可能性を広げます。ウェブとモバイルで AI ネイティブアプリケーションの急増を目にすることになるでしょう」

Ansh Nanda, Co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf57518a91cc645d08ae1a_sentry-light-mode.svg)

「コードの何が悪いかを開発者に伝えるだけでは不十分だと分かりました——彼らはあなたに直してほしいのです。今では顧客は、Seer の根本原因分析から、Claude を活用したエージェントによる修正と PR 作成へと、一直線に進めます。私たちが Claude Managed Agents を選んだのは、セキュアで完全に管理されたエージェントランタイムを提供してくれるからです。おかげで私たちはハンドオフ周りのシームレスな開発者体験の構築に集中できます。Managed Agents は、数か月ではなく数週間で初期統合を構築することを可能にしただけでなく、独自のエージェントインフラを維持する継続的な運用オーバーヘッドもなくしてくれました」

Indragie Karunaratne, Senior Director of Engineering, AI/ML

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)

「Atlassian は、人間とエージェントの両方にまたがる仕事をエンタープライズで調整する支援をしています。Claude Managed Agents のおかげで、チームがすでに頼っているワークフローに開発者向けエージェントを直接組み込むことが、数か月ではなく数週間でできるようになりました——お客様は Jira から直接タスクを割り当てられます。Managed Agents はサンドボックス化、セッション、スコープ付き権限といった難しい部分を引き受けてくれるので、私たちのエンジニアはインフラに費やす時間を減らし、エンドユーザーのために優れた機能を作ることに集中できます」

Sanchan Saxena, SVP, Head of Product, Teamwork Collection

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d54700357e01220a808b6e_general-legal-light-mode.svg)

「Claude Managed Agents を使って、ユーザーのドキュメントやコレスポンデンスから情報を引き出し、あらゆる問い合わせに答えられるシステムを構築しました——たとえそのデータを取得するための特定のツールを構築していなかったとしても、です。Managed Agents 以前は、ユーザーが聞きたがるかもしれないあらゆる質問を予測し、そのためのツールやプロンプトワークフローを作る必要がありました。今は Managed Agents を使えば、必要なツールをその場でコーディングできるので、実質的にあらゆるユーザーの問い合わせを処理できます。これによって開発時間が 10 分の 1 に短縮され、UX とより多くのデータソースの統合に集中できるようになりました」

Javed Qadrud-Din, CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d546e8750a5d04702cf69a_blockit-light-mode.svg)

「Claude Managed Agents のおかげで、本番品質のミーティング準備エージェントの構築が 3 倍速くなりました。アイデアから出荷までが数日です。私たちのエージェントはミーティング前にすべての参加者を調査し、会話を前に進めるために何が重要かを表面化させます。カスタムツールは私たち自身のカレンダーや連絡先データを取り込ませるのに使えますし、MCP はミーティング議事録ツールや CRM のような外部システムへの接続をシンプルにし、マネージドハーネスはサンドボックス実行や組み込みウェブ検索を含む重労働を引き受けてくれました。おかげで私たちはインフラではなくプロダクト構築に集中できます」

John Han, Co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)

「私たちは、Notion がチームがエージェントと一緒に仕事を進めて物事を成し遂げるベストな場所であってほしいと考えています。それを実現するために、長時間セッション、メモリ管理、継続的に高品質な出力を扱える Claude Managed Agents を統合しました。ユーザーはコードからスライドやスプレッドシートの生成まで、オープンエンドで複雑なタスクを、Notion を離れることなく委任できます」

Eric Liu, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)

「Claude Managed Agents を使うことで、私たちのパワーユーザーはガリレオのような存在になります——単一の専門や分野をはるかに超えて、さまざまなドメインに貢献できるのです。各専門エージェントを 1 週間以内にデプロイし、エンジニアリング、プロダクト、セールス、マーケティング、財務にまたがる長時間タスクを管理し、サンドボックス環境内でアプリ、提案書、スプレッドシートを生成しています。エージェントがより能力を高めるにつれ、Managed Agents は独自にエージェントインフラを構築することなく安全にスケールすることを可能にしてくれるので、私たちは会社全体でイノベーションの民主化に完全に集中できます」

Yusuke Kaji, General Manager of AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a7ba07d03afe57aaaf02_asana_light.svg)

「Claude Managed Agents は私たちの Asana AI Teammates の開発を劇的に加速してくれました——高度な機能をより速く出荷するのを助け、エンタープライズグレードのマルチプレイヤー体験の創造に集中できるようにしてくれました」

Amritansh Raghav, CTO

## 始め方

Managed Agents は消費ベースで課金されます。標準の Claude Platform トークンレートに加えて、アクティブなランタイムの場合は 1 セッション時間あたり 0.08 ドルが適用されます。料金の詳細は[ドキュメント](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)をご覧ください。

Managed Agents は今すぐ Claude Platform で利用できます。詳しくは[ドキュメント](https://platform.claude.com/docs/en/managed-agents/overview)をご覧いただくか、[Claude Console](https://platform.claude.com/workspaces/default/agent-quickstart) にアクセスするか、私たちの新しい CLI を使って最初のエージェントをデプロイしてみてください。

開発者は、最新の Claude Code と組み込みの claude-api スキルを使って Managed Agents と組み合わせて構築することもできます。「start onboarding for managed agents in Claude API」と尋ねるだけで始められます。
