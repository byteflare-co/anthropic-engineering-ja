---
date: '2026-05-12'
final_url: https://claude.com/blog/code-w-claude-sf-2026-sf
number: 45
selector_used: main
slug: code-w-claude-sf-2026-sf
source_url: https://claude.com/blog/code-w-claude-sf-2026-sf
title: 'Code w/ Claude SF 2026: Building on the AI exponential'
title_ja: "Code w/ Claude SF 2026: AI の指数関数の上に作る"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

# Code w/ Claude SF 2026: AI の指数関数の上に作る

今週、サンフランシスコで毎年恒例の開発者カンファレンス [Code w/ Claude](https://claude.com/code-with-claude/san-francisco#agenda) を開催しました。このイベントには開発者、エンジニア、創業者が集まり、Claude を作っているチームと共に、二日間にわたるキーノート、ブレイクアウトセッション、ワークショップに参加しました。

プロンプティングと[モデル選定](https://www.youtube.com/watch?v=OXJO4LldSnc&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=12)から、skill の設計、[AI ネイティブなエンジニアリングチームのスケール](https://www.youtube.com/watch?v=igO8iyca2_g&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=11)まで、どのセッションも同じ変化を中心に展開しました。アイデアからプロダクションのソフトウェアまでの距離は縮まっており、最大の手応えを得ているチームは、AI の指数関数に反応するのではなく、それを前提に設計しているのです。

今がどのような状況なのかを、[ライブコーディングセッション](https://www.youtube.com/watch?v=DlTCu_pNDHE&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=5)、[顧客とのディープダイブ](https://www.youtube.com/watch?v=EdmuYPBt_EM&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=2)、ハンズオンチュートリアルを通じてお見せしました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02b62b0fd6f5b85ee0bea3_CwC.jpeg)

共同創業者兼プレジデントの Daniela Amodei と、共同創業者兼 CEO の Dario Amodei が、CPO の Ami Vora がモデレートするファイヤーサイドチャットに参加しました。

## 発表内容

カンファレンスでは、[Claude Code のレートリミットを 2 倍に引き上げ](https://www.anthropic.com/news/higher-limits-spacex)、Claude Opus の API レートリミットも引き上げました。これにより、開発者、スタートアップ、エンタープライズは、より信頼性高くスケールしながら構築できるようになります。どちらも本日より有効です。

さらに、Claude Platform 上の [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) に、クラウドホスト型のエージェントを大規模に構築・デプロイすることを支援する新機能を導入しました。4 つの[新機能](https://claude.com/blog/new-in-claude-managed-agents)が、すべての開発者に向けて提供開始されています。

- **ドリーミング (Dreaming)。** 過去のエージェントセッションを振り返り、パターンを浮かび上がらせ、メモリーをキュレーションするスケジュールド処理です。これによってエージェントは、実行と実行の合間に改善されていきます。繰り返し起きるミス、共有されたワークフロー、チームの好みが、より有用なメモリーストアへと取り込まれます。
- **マルチエージェントオーケストレーション。** リードエージェントが、共有ファイルシステム上で並列に作業するスペシャリストのサブエージェントに作業を委任できます。各サブエージェントは、独自のモデル、プロンプト、ツールを持ちます。フロー全体は Claude Console でトレース可能です。
- **アウトカム (Outcomes)。** 開発者は「良い出力とはどういうものか」をルーブリックとして定義します。別途用意されたグレーダーが、各結果を独立したコンテキストウィンドウで評価し、基準を満たすまでエージェントを再修正に戻します。社内ベンチマークでは、最も難しい問題でアウトカムによってタスク成功率が最大 10 ポイント向上しました。
- **Webhook。** アウトカムを定義してエージェントを走らせ、完了時に Webhook で通知を受け取ることができます。

## 見逃した方へ

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02b5708e141ac8abcd4968_Exec%20Boris%20Cherny.jpg)

Claude Code の生みの親である Boris Cherny が、サンフランシスコの Code w/ Claude 2026 で発表しています。

ライブストリームを見逃した方は、[こちら](https://www.youtube.com/playlist?list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR)からキーノートとブレイクアウトセッションの録画をご覧いただけます。

私たちのトークでは、Anthropic のチームによる Claude 開発の裏側に加えて、[Asana](https://www.youtube.com/watch?v=BrpB-h1e--k&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=10)、[Cursor](https://www.youtube.com/watch?v=BbYSGxtsMic&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=15)、[GitHub](https://www.youtube.com/watch?v=y5TmF_6o6xk&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=7)、[Replit](https://www.youtube.com/watch?v=snroDwX1-JU&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=14)、[Vercel](https://www.youtube.com/watch?v=bJKdXhnw7NU&list=PLmWCw1CzcFim2obQ-w3ohbULOfwp5lApR&index=3&pp=iAQB0gcJCQMLAYcqIYzv) といった顧客が、プロダクション対応のエージェントをどう設計し、エージェント開発の境界をどう押し広げているのかを共有しています。

Code w/ Claude は、[ロンドン](https://claude.com/code-with-claude/london)（5 月 19〜18 日）と[東京](https://claude.com/code-with-claude/tokyo)（6 月 5〜6 日）でも開催します。Day 1 のキーノートとブレイクアウトセッションはすべてライブ配信されます。

*トークから着想を得たテクニカルチュートリアル、ガイド、顧客事例にもご期待ください。*

‍
