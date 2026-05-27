---
date: '2026-05-26'
final_url: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
number: 56
selector_used: main
slug: code-w-claude-london-2026-rethinking-how-we-build
source_url: https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build
title: 'Code w/ Claude London 2026: Rethinking how we build'
title_ja: "Code w/ Claude London 2026: 私たちの作り方を考え直す"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Code w/ Claude London 2026: 私たちの作り方を考え直す

今週、ロンドンで [Code w/ Claude](https://claude.com/code-with-claude/london) をヨーロッパに届けました。このイベントでは、ビルダー、開発者、創業者が一堂に会し、Claude を作っているチームと共に、二日間にわたるキーノート、ブレイクアウトセッション、ワークショップに参加しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a162288008621ab8a976251_image3.jpg)

*Claude Code のプロダクト責任者である Cat Wu が、セッションの合間に参加者と話をしているところ。*

Claude Code 責任者の Boris Cherny は、[キーノート](https://www.youtube.com/watch?v=6amLO7I9xdg)の冒頭で、初めてコーディングに「魔法」を感じた瞬間について語りました。中学生のころ、彼は数学の宿題やテストを解く TI-83 のプログラムを書き、自分の eBay 上のポケモンカード出品をより売れるようにするために独学で HTML を学びました。手を動かしながら学び、何かが動いたときには胸が躍ったのです。

その後どこかで、プログラミングは複雑になってしまった、と彼は指摘します。コンパイラ、型チェッカー、ビルドシステム、それぞれの層が「アイデアがある」と「動く」のあいだの距離を少しずつ押し広げていきました。エージェントによって、その距離は再び縮まろうとしています。問題を説明すれば、プログラムが現れる。電卓を使うときのあの感覚です。ただし、その電卓は分散システムを書くことができます。

Claude Code の[基本を超えていく](https://claude.com/code-with-claude/session/ldn-beyond-the-basics-with-claude-code)方法を扱ったワークショップから、私たちのモデル全体で[思考予算とエフォートレベル](https://claude.com/code-with-claude/session/ldn-the-thinking-lever)を最適化するセッションまで、Anthropic と、[Spotify](https://claude.com/code-with-claude/session/ldn-coding-is-no-longer-the-constraint-scaling-devex-to-teams-and-agents-at-spotify)、[Base44](https://claude.com/code-with-claude/session/ldn-from-one-person-to-80-scaling-a-hypergrowth-engineering-org-with-claude-code)、[Legora](https://claude.com/code-with-claude/session/ldn-what-legal-agents-inherit-from-coding-agents-lessons-from-legora) といった顧客が、この感覚をどう取り戻しているのかを紹介しました。

## 発表内容

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1623afcae08af4b3a9de5e_image1.jpg)

*Claude Developer Platform のエンジニアリング責任者である Katelyn Lesse と、同プラットフォームのプロダクト責任者である Angela Jiang が、Code w/ Claude London で Claude Managed Agents の新機能をデモする様子。*

カンファレンスで発表されたように、Claude Managed Agents は、あなたが管理するサンドボックスで動作させ、プライベートな Model Context Protocol (MCP) サーバーに接続できるようになりました。これにより、エージェントがツールを実行する環境と、エージェントが到達するサービスの両方が、エンタープライズで確立された境界の内側で動くようになります。これら 2 つの[新機能](https://claude.com/blog/claude-managed-agents-updates)は、Claude Platform で利用可能です。

- **セルフホストサンドボックス**（パブリックベータ）。ツールの実行は、自社インフラ、または Cloudflare、Daytona、Modal、Vercel のようなマネージドプロバイダーなど、あなたが構成した環境に移ります。一方で、オーケストレーション、コンテキスト管理、エラー復旧を担うエージェントループは Anthropic のインフラ上にとどまります。あなたのネットワークポリシー、監査ログ、セキュリティツールがそのまま適用され、ファイルやリポジトリは境界の外に出ません。また、計算負荷の高い処理に向けて、コンピュートサイズやランタイムイメージを自分でコントロールできます。
- **MCP トンネル**（リサーチプレビュー）。エージェントは、プライベートネットワーク内の MCP サーバーに、それらをパブリックインターネットに晒すことなく到達できます。あなたがデプロイする軽量なゲートウェイが、外向きの単一の接続を確立します。インバウンドのファイアウォールルールも、公開エンドポイントも不要で、通信はエンドツーエンドで暗号化されます。MCP トンネルは Managed Agents と Messages API でサポートされており、組織管理者が Claude Console から管理します。

Amplitude、Clay、Rogo を含むチームは、すでにセルフホストサンドボックスを使った Managed Agents 上で開発を進めています。まずは[ドキュメント](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)を読み、[クックブック](https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes)を試してみてください。あるいは、MCP トンネルへの[アクセスを申請](https://claude.com/form/claude-managed-agents)してください。

## 見逃した方へ

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1623c3214b8b8cf8f378e7_image2.jpg)

*リサーチプロダクトマネージャーの Lisa Crofoot が、Code w/ Claude London のキーノートで発表しているところ。*

ライブストリームを見逃した方は、キーノートとブレイクアウトセッションの[録画](https://claude.com/code-with-claude/london)をご覧ください。

Code w/ Claude は次に[東京](https://claude.com/code-with-claude/tokyo)（6 月 5〜6 日）に向かいます。Day 1 のキーノートとブレイクアウトセッションはすべてライブ配信されます。

*トークから着想を得たテクニカルチュートリアル、ガイド、顧客事例にもご期待ください。*
