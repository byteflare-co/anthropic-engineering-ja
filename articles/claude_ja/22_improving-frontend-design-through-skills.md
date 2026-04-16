---
date: '2025-11-12'
final_url: https://claude.com/blog/improving-frontend-design-through-skills
number: 22
selector_used: main
slug: improving-frontend-design-through-skills
source_url: https://claude.com/blog/improving-frontend-design-through-skills
title: Improving frontend design through Skills
title_ja: Skills でフロントエンドデザインを改善する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22dc2ead61fff4f6e1d_589b94b913c4cee1c3c1ce2cb04f638d09c465b1-1000x1000.svg)

# Skills でフロントエンドデザインを改善する

何の指示もないまま LLM にランディングページを作らせると、ほとんどの場合 Inter フォント、白背景に紫のグラデーション、控えめなアニメーションに落ち着くことにお気づきかもしれません。

原因は何でしょうか。[分布収束 (distributional convergence)](https://en.wikipedia.org/wiki/Convergence_of_random_variables) です。サンプリング時、モデルは学習データ中の統計的パターンに基づいてトークンを予測します。どこでも通用し誰の気分も害さない「安全な」デザイン選択は、ウェブの学習データにおいて支配的です。方向付けがなければ、Claude はこの高確率な中心からサンプリングしてしまいます。

顧客向けプロダクトを開発している開発者にとって、このありきたりな美学はブランドアイデンティティを損ない、AI が生成したインターフェースを一目で見分けられ、そして一蹴できるものにしてしまいます。

### ステアラビリティの課題

幸い、Claude は適切なプロンプトを与えればステアラビリティが非常に高いモデルです。Claude に「Inter と Roboto を避けて」とか「ベタ塗りの色ではなく雰囲気のある背景を使って」と伝えるだけで、結果はすぐに改善します。この指示への感度の高さは機能の一部であり、Claude が異なるデザインコンテキスト、制約、美的嗜好に適応できることを意味します。

しかし、ここには現実的な課題があります。タスクが専門的になるほど、提供すべきコンテキストも増えていきます。フロントエンドデザインにおいて効果的なガイダンスは、タイポグラフィの原則、カラーセオリー、アニメーションパターン、背景の扱いにまたがります。どのデフォルトを避け、どの代替を好むのかを、複数の次元にわたって指定する必要があります。

これらすべてをシステムプロンプトに詰め込むこともできますが、そうすると Python のデバッグでも、データ分析でも、メール作成でも、あらゆるリクエストにフロントエンドデザインのコンテキストが付いて回ります。問うべきは、無関係なタスクに対する恒久的なコンテキストオーバーヘッドを発生させることなく、ドメイン固有のガイダンスを必要なときにだけ Claude に与えるにはどうすればよいか、ということです。

## **Skills: コンテキストを動的にロードする**

これこそ、[Skills](https://www.anthropic.com/news/skills) が設計された目的です。恒久的なオーバーヘッドなしに、専門的なコンテキストをオンデマンドで届けることです。skill とは、指示・制約・ドメイン知識を含むドキュメント (多くは Markdown) で、Claude がシンプルなファイル読み取りツール経由でアクセスできる専用のディレクトリに保存されます。Claude はこれらの skills を活用し、必要な情報を実行時に動的にロードして、最初にすべてを読み込むのではなくコンテキストを段階的に拡張できます。

これらの skills と必要なツールが与えられると、Claude は手元のタスクに基づいて関連する skills を自律的に特定し、ロードできます。たとえば、ランディングページを作ったり、React コンポーネントを作ったりするよう依頼された場合、Claude はフロントエンドデザイン skill をロードして、その指示をジャストインタイムで適用できます。これが本質的なメンタルモデルです。skills はオンデマンドで起動するプロンプトとコンテキストリソースであり、恒久的なコンテキストオーバーヘッドを発生させずに、特定のタスクタイプ向けの専門的なガイダンスを提供します。

これにより開発者は、ばらばらな指示を多数のタスク向けにシステムプロンプトに詰め込むことでコンテキストウィンドウを過負荷にすることなく、Claude のステアラビリティの恩恵を享受できます。[以前説明したとおり](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、コンテキストウィンドウ内のトークン数が増えすぎるとパフォーマンスが低下するおそれがあるため、コンテキストウィンドウの中身をスリムに保ち、焦点を絞ることはモデルから最良のパフォーマンスを引き出すうえで極めて重要です。Skills は、効果的なプロンプトを再利用可能かつコンテキスト依存にすることで、この問題を解決します。

## **より良いフロントエンド出力のためのプロンプティング**

フロントエンドデザイン skill を作ることで、恒久的なコンテキストオーバーヘッドなしに、Claude から大幅に質の高い UI 生成を引き出せるようになります。核心にある洞察は、フロントエンドデザインをフロントエンドエンジニアの視点で考えることです。美的な改善を実装可能なフロントエンドコードにマッピングできればできるほど、Claude はうまく実行できます。

この洞察を活かして、狙いを定めたプロンプトが効く領域をいくつか特定しました。タイポグラフィ、アニメーション、背景エフェクト、テーマです。これらはいずれも Claude が書けるコードにきれいに変換されます。プロンプトに組み込むのに、細かい技術的指示は必要ありません。これらのデザイン軸についてモデルがより批判的に考えるように促す、狙いを定めた表現を使うだけで十分に強力な出力を引き出せます。これは、私たちが [コンテキストエンジニアリング](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) のブログ記事で示したガイダンスと近いものです。つまり、正しい「高度 (altitude)」でモデルにプロンプトを与えること、具体的な HEX コードを指定するような低高度のハードコード的ロジックと、共有コンテキストを前提にした曖昧な高高度の指示という 2 つの極端を避けることです。

### **タイポグラフィ**

実例を見るために、まずはプロンプトで影響を与えられる次元の一つとしてタイポグラフィから始めましょう。以下のプロンプトは、Claude に対してより興味深いフォントを使うよう特化して誘導します。

```
<use_interesting_fonts>
Typography instantly signals quality. Avoid using boring, generic fonts.

Never use: Inter, Roboto, Open Sans, Lato, default system fonts

Here are some examples of good, impactful choices:
- Code aesthetic: JetBrains Mono, Fira Code, Space Grotesk
- Editorial: Playfair Display, Crimson Pro
- Technical: IBM Plex family, Source Sans 3
- Distinctive: Bricolage Grotesque, Newsreader

Pairing principle: High contrast = interesting. Display + monospace, serif + geometric sans, variable font across weights.

Use extremes: 100/200 weight vs 800/900, not 400 vs 600. Size jumps of 3x+, not 1.5x.

Pick one distinctive font, use it decisively. Load from Google Fonts.
</use_interesting_fonts>
```

**ベースプロンプトで生成した出力:**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691366f388193282b0213316_image11.png)

**ベースプロンプト + タイポグラフィセクションで生成した出力**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913679c9a202c88b680873b_image13.png)

‍

興味深いことに、より興味深いフォントを使うよう指示するだけで、モデルはデザインの他の側面も改善するよう促されるようです。

タイポグラフィだけでも大きく改善されますが、フォントは一つの次元に過ぎません。インターフェース全体にわたる統一感のある美学についてはどうでしょうか。

### **テーマ**

プロンプトで誘導できるもう一つの次元は、よく知られたテーマや美学からインスピレーションを得たデザインです。Claude はポピュラーなテーマについて豊富な理解を持っているため、フロントエンドに落とし込みたい具体的な美学を伝えるためにこれを活用できます。例を挙げます。

```
<always_use_rpg_theme>
Always design with RPG aesthetic:
- Fantasy-inspired color palettes with rich, dramatic tones
- Ornate borders and decorative frame elements
- Parchment textures, leather-bound styling, and weathered materials
- Epic, adventurous atmosphere with dramatic lighting
- Medieval-inspired serif typography with embellished headers
</always_use_rpg_theme>
```

これによって次のような RPG テーマの UI が得られます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913cec4181329835d1da27f_image2.png)

タイポグラフィとテーマは、狙いを定めたプロンプトが効くことを示しています。しかし、各次元を毎回手作業で指定するのは面倒です。これらの改善をすべて、再利用可能な一つのアセットにまとめられたらどうでしょうか。

### **汎用プロンプト**

同じ原理は、他のデザイン次元にも拡張できます。モーション (アニメーションとマイクロインタラクション) を指示すれば、静的なデザインには欠けている洗練が加わりますし、モデルをより興味深い背景選択へと誘導すれば、奥行きと視覚的な面白さが生まれます。包括的な skill が輝くのは、こういうところです。

これらすべてをまとめ、私たちは約 400 トークンのプロンプトを作りました。(skill としてロードしてもコンテキストを肥大化させない) 十分にコンパクトなサイズで、タイポグラフィ、カラー、モーション、背景にわたってフロントエンド出力を劇的に改善します。

```
<frontend_aesthetics>
You tend to converge toward generic, "on distribution" outputs. In frontend design,this creates what users call the "AI slop" aesthetic. Avoid this: make creative,distinctive frontends that surprise and delight.

Focus on:
- Typography: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics.
- Color & Theme: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes. Draw from IDE themes and cultural aesthetics for inspiration.
- Motion: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions.
- Backgrounds: Create atmosphere and depth rather than defaulting to solid colors. Layer CSS gradients, use geometric patterns, or add contextual effects that match the overall aesthetic.

Avoid generic AI-generated aesthetics:
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (particularly purple gradients on white backgrounds)
- Predictable layouts and component patterns
- Cookie-cutter design that lacks context-specific character

Interpret creatively and make unexpected choices that feel genuinely designed for the context. Vary between light and dark themes, different fonts, different aesthetics. You still tend to converge on common choices (Space Grotesk, for example) across generations. Avoid this: it is critical that you think outside the box!
</frontend_aesthetics>
```

上記の例では、まず問題とその解決目的についての一般的なコンテキストを Claude に与えています。こうした高レベルのコンテキストをモデルに与えることが、出力をキャリブレーションするうえで有効なプロンプティング戦術であることが分かっています。次に、先ほど議論した改善すべきデザインの軸を特定し、これらすべての次元にわたってモデルがより創造的に考えるよう促す、狙いを定めた助言を与えています。

また、Claude が別のローカルマキシマムに収束してしまうのを防ぐために、追加のガイダンスを末尾に加えています。特定のパターンを避けるよう明示的に指示しても、モデルは別のよくある選択 (タイポグラフィでは Space Grotesk など) に落ち着いてしまうことがあるからです。最後の "think outside the box" というリマインダーが、創造的なバリエーションを強化してくれます。

### **フロントエンドデザインへの影響**

この skill を有効にすると、Claude の出力はさまざまなタイプのフロントエンドデザインで改善されます。例えば次のようなものです。

**例 1: SaaS のランディングページ**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77b_6d547f28.png)

**キャプション:** ありきたりな Inter フォント、紫のグラデーション、標準的なレイアウトで AI が生成した SaaS ランディングページ。skills は使用していません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f790_c47f37ab.png)

**キャプション:** 同じプロンプトに加えてフロントエンド skill を使って AI が生成したフロントエンド。特徴あるタイポグラフィ、統一感のある配色、レイヤー構造のある背景を備えています。

**例 2: ブログレイアウト**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78d_f7040147.png)

デフォルトのシステムフォントとフラットな白背景で AI が生成したブログレイアウト。skills は使用していません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77e_0ce357ff.png)

同じプロンプトに加えてフロントエンド skill を使って AI が生成したブログレイアウト。エディトリアル向けの書体、雰囲気のある奥行き、洗練されたスペーシングが特徴です。

**例 3: 管理ダッシュボード**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f784_7beb17d0.png)

標準的な UI コンポーネントで、視覚的な階層がほぼない AI 生成の管理ダッシュボード。skills は使用していません。

‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f781_3705adad.png)

同じプロンプトに加えてフロントエンド skill を使って AI が生成した管理ダッシュボード。大胆なタイポグラフィ、統一感のあるダークテーマ、意図のあるモーションを備えています。

## **Skills で** [**claude.ai**](http://claude.ai/redirect/claudedotcom.v1.ae42297c-4607-4039-98b1-7ecbb39733d4) **の artifact 品質を改善する**

限界はデザインセンスだけではありません。Claude は artifact を構築する際にアーキテクチャ上の制約にも直面します。[Artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) は Claude が作成し、チャットと並べて表示する、インタラクティブで編集可能なコンテンツ (コードやドキュメントなど) です。

上で見たデザインセンスの問題に加えて、Claude には [claude.ai](http://claude.ai/redirect/claudedotcom.v1.ae42297c-4607-4039-98b1-7ecbb39733d4) で優れたフロントエンド artifact を生成する能力を制限している別のデフォルト挙動があります。現状、フロントエンドを作るよう依頼されると、Claude は CSS と JS を含む単一の HTML ファイルを作るだけです。これは、artifact として適切にレンダリングされるにはフロントエンドが単一の HTML ファイルでなければならないと Claude が理解しているためです。

人間の開発者でも、HTML/CSS/JS を単一ファイルにしか書けないとしたらごく基本的なフロントエンドしか作れないでしょう。それと同じ理屈で、より豊富なツールを使うよう指示すれば、Claude はより印象的なフロントエンド artifact を生成できるのではないかと仮説を立てました。

そこで私たちは [web-artifacts-builder skill](https://github.com/anthropics/skills/blob/main/web-artifacts-builder/SKILL.md) を作成しました。これは Claude の [コンピュータを使う](https://www.claude.com/blog/create-files) 能力を活用し、複数ファイルと [React](https://react.dev/)、[Tailwind CSS](https://tailwindcss.com/)、[shadcn/ui](https://ui.shadcn.com/) といったモダンなウェブ技術を用いて artifact を構築するよう Claude を導きます。内部的には、この skill が (1) Claude が基本的な React リポジトリを効率的にセットアップする、(2) 編集後に単一 HTML ファイル要件を満たすために [Parcel](https://parceljs.org/) ですべてを単一ファイルにバンドルする、ためのスクリプトを公開します。これは skills の中核的な利点の一つです。定型的なアクションを実行するスクリプトへのアクセスを Claude に与えることで、Claude はトークン使用量を最小化しつつ信頼性とパフォーマンスを高められます。

web-artifacts-builder skill を使うと、Claude は shadcn/ui のフォームコンポーネントと Tailwind のレスポンシブグリッドシステムを活用して、より包括的な artifact を作成できます。

**例 1: ホワイトボードアプリ**

たとえば、web-artifacts-builder skill なしでホワイトボードアプリを作るように促すと、Claude はごく基本的なインターフェースを出力しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f787_b07e5190.png)

一方、新しい web-artifacts-builder skill を使った場合、Claude は、異なる図形の描画やテキスト機能を含む、はるかに洗練され機能豊富なアプリケーションを最初から生成しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78a_57c49993.png)

‍

**例 2: タスク管理アプリ**

同様に、タスク管理アプリを作るよう依頼した場合、skill なしでは Claude は動作はするものの非常にミニマルなアプリケーションを生成しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f793_875d1eef.png)

skill を使うと、Claude は最初からより機能豊富なアプリを生成しました。たとえば、タスクに関連付けるカテゴリと期日を設定できる "Create New Task" フォームコンポーネントが含まれていました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7c9_7ae52606.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7a1_4c4951af.png)

‍

[Claude.ai](http://claude.ai/redirect/claudedotcom.v1.ae42297c-4607-4039-98b1-7ecbb39733d4) でこの新しい skill を試すには、skill を有効にして、artifact を作る際に Claude に「web-artifacts-builder skill を使って」と依頼するだけです。

## **Skills で Claude のフロントエンドデザイン能力を最適化する**

このフロントエンドデザイン skill は、言語モデルの能力に関するより広い原理を示しています。モデルはしばしば、デフォルトで表現する以上のことを行う能力を持っているのです。Claude はデザインへの深い理解を備えていますが、ガイダンスがなければ分布収束がそれを覆い隠します。これらの指示をシステムプロンプトに加えることもできますが、そうするとタスクに関係ないリクエストにまでフロントエンドデザインのコンテキストが付きまといます。代わりに Skills を使えば、Claude は絶えずガイダンスを必要とするツールから、あらゆるタスクにドメイン専門性を持ち込む存在へと変貌します。

Skills はまた、高度にカスタマイズ可能です。自分のニーズに合わせて独自の skill を作ることができます。これにより、skill に焼き込みたい基本単位 — 自社のデザインシステム、特定のコンポーネントパターン、業界固有の UI 慣習など — を自分で定義できます。これらの意思決定を Skill にエンコードすれば、エージェントの思考の構成要素を、開発チーム全体で活用できる再利用可能なアセットに変えられます。skill は組織的な知識となって、持続し、スケールし、プロジェクト間で一貫した品質を保証します。

このパターンはフロントエンド作業の枠を超えて広がります。Claude がより広範な理解を持っているにもかかわらず汎用的な出力を生成してしまうドメインはすべて、Skill 開発の候補です。方法は一貫しています。収束しがちなデフォルトを特定し、具体的な代替を提示し、ガイダンスを適切な「高度」で構造化し、Skills によって再利用可能にすることです。

フロントエンド開発にとっては、これは Claude がリクエストごとのプロンプトエンジニアリングなしに、特徴あるインターフェースを生成できるようになることを意味します。はじめるには、[フロントエンドデザインクックブック](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb) を探索するか、[Claude Code の新しいフロントエンドデザインプラグイン](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) を試してみてください。

**インスピレーションを受けましたか？ 自分のフロントエンド skill を作るには、** [**skill-creator**](https://github.com/anthropics/skills/tree/main/skill-creator) **をご覧ください。**

‍

**謝辞**
執筆: Anthropic の Applied AI チーム Prithvi Rajasekaran、Justin Wei、Alexander Bricken、ならびにマーケティングパートナーの Molly Vorwerck、Ryan Whitehead。

‍
