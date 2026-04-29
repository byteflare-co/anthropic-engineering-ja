---
date: '2026-04-29'
final_url: https://claude.com/blog/claude-api-skill
number: 32
selector_used: main
slug: claude-api-skill
source_url: https://claude.com/blog/claude-api-skill
title: Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp
title_ja: "Claude API skill が CodeRabbit、JetBrains、Resolve AI、Warp で利用可能に"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

# Claude API skill が CodeRabbit、JetBrains、Resolve AI、Warp で利用可能に

本日、CodeRabbit、JetBrains、Resolve AI、Warp が [claude-api skill](https://github.com/anthropics/skills/tree/main/skills/claude-api) を同梱します。これにより、開発者は普段使っているツールのなかで、本番投入できる品質の Claude API コードをそのまま手にできるようになります。3 月に Claude Code で初めて導入されたこの skill は、開発者がすでに使っている、より多くのツールへと広がっています。

## Claude API skill で開発する

`claude-api` skill は、Claude API のコードがうまく動くために必要な細部を捉えています。たとえば、ある仕事にどのエージェントパターンが適しているか、モデル世代をまたいでどのパラメータが変わるか、いつプロンプトキャッシュを適用すべきか、といったことです。その結果、エラーは減り、キャッシュは効きやすくなり、エージェントパターンはより整い、モデル移行はよりなめらかになります。

skill は私たちの SDK の変化に追随し、常に最新の状態を保ちます。新しいモデルがリリースされたり API に新機能が加わったりしたとき、Claude はすでにそれを知っているのです。

skill が使える場所であればどこでも、Claude にこう頼めます。

- **「キャッシュヒット率を改善して」** 多くの開発者が見落としているプロンプトキャッシュのルールを skill が適用してくれます。
- **「自分のエージェントにコンテキスト圧縮を追加して」** ドキュメントに書かれている圧縮プリミティブとエージェントパターンを順に案内します。
- **「最新の Claude モデルにアップグレードして」** Claude があなたのコードをレビューし、[Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) のような新しいモデルに合わせて、モデル名・プロンプト・effort 設定の更新方法を案内します。Claude Code では、これを `/claude-api migrate` で直接実行することもできます。**‍**
- **「自分の業界向けのディープリサーチエージェントを作って」** Claude が [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) の構成を一通り案内してくれるので、長時間稼働のリサーチが、独自プロジェクトを立ち上げることなく、わずかなプロンプトで実現できます。Claude Code では、これを `/claude-api managed-agents-onboard` で直接実行することもできます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692481a076d768db9276c4d9_warp-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692481a493eb0f6f4ca5b90a_warp-white.svg)

「開発者が Claude API のパラメータやキャッシュのルールを調べるために Warp を離れる必要はないはずです。Claude API skill が組み込まれていることで、その知識はすでにそこにあり、エンジニアは集中を切らさず、より速くリリースできます」

Zach Lloyd, Founder and CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c02555494a06a2d8a9cbb0_logo-orange.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5e8c0ed40050ce0a934d_Code%20Rabbit-dark-theme.svg)

「CodeRabbit では週に何百万もの PR をレビューしており、API の古い知識が本番障害を引き起こすことがどれほど多いかを目にしてきました。Claude API skill は、私たちの SDK の変化に合わせて Claude を最新に保つので、エージェントを開発する人がレビュー時に直面する想定外のことが減ります」

Erik Thorelli, Developer Experience Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e543f9e6c0e1972c338437_logo_%5Bjetbrains%5D-%5Blight%5D.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e54425a3fe2aed4f88910e_logo_jetbrains_dark.svg)

「Claude API skill によって、JetBrains IDE と Junie 上の開発者は、Claude API のアップグレードをガイド付きの IDE ワークフローに変えられます。よい例が Claude Opus 4.7 への移行で、skill はモデル参照を更新し、手動の thinking 設定を adaptive thinking に置き換え、古くなったパラメータやベータヘッダを片付け、適切な effort レベルをインラインで提案できます。これにより、チームはより強い初回パスを得られ、通常はクリーンアップの段階で出てくるバージョン固有のミスを避けやすくなります」

Denis Shiryaev, Head of AI Dev Tools Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

「Claude API skill のおかげで、Resolve AI のエンジニアは新しいモデルの能力をより速く取り込めています。手作業で移行ガイドを読み解き、細かな API 変更を 1 つずつ追いかける代わりに、私たちのチームはモデルのリリースから実装までを、ガイド付きの 1 パスで進められます」

Mayank Agarwal, Founder & CTO
