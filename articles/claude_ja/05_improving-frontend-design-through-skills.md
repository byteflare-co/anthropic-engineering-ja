---
date: '2025-11-12'
final_url: https://claude.com/blog/improving-frontend-design-through-skills
number: 4
selector_used: main
slug: improving-frontend-design-through-skills
source_url: https://claude.com/blog/improving-frontend-design-through-skills
title: Improving frontend design through Skills
title_ja: Skills で Claude のフロントエンドデザインを改善する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22dc2ead61fff4f6e1d_589b94b913c4cee1c3c1ce2cb04f638d09c465b1-1000x1000.svg)

# Skills で Claude のフロントエンドデザインを改善する

LLM にガイダンスなしでランディングページを作らせると、ほぼ必ず Inter フォント、白背景に紫のグラデーション、最小限のアニメーションというスタイルに収束することに気づくかもしれません。

問題は何でしょうか? それは[分布の収束 (distributional convergence)](https://en.wikipedia.org/wiki/Convergence_of_random_variables) です。サンプリング中、モデルは訓練データ内の統計パターンに基づいてトークンを予測します。安全なデザイン選択——誰に対しても無難で、誰も気分を害さないもの——はウェブの訓練データを支配しており、方向づけがなければ Claude はこの確率の高い中央付近からサンプリングしてしまうのです。

顧客向けプロダクトを作る開発者にとって、この汎用的な美意識はブランドのアイデンティティを弱体化させ、AI が生成したインターフェースを一目でそれと分からせ——そして切り捨てられる対象にしてしまいます。

### 舵取りの難しさという課題

良いニュースは、Claude が適切なプロンプトで高度に「ステアラブル (steerable)」であるということです。「Inter と Roboto を避ける」「無地の色の代わりに大気感のある背景を使う」と Claude に伝えれば、出力は即座に改善します。この指示への感度は機能でもあります——Claude が異なるデザイン文脈、制約、美学的な好みに適応できることを意味するからです。

しかしこれは実務上の課題を生みます。タスクが専門的になるほど、提供すべきコンテキストも増えるのです。フロントエンドデザインにおいて有効なガイダンスは、タイポグラフィの原則、カラー理論、アニメーションパターン、背景処理にまたがります。複数の次元にわたって、どのデフォルトを避けるべきか、どの代替を好むべきかを指定する必要があります。

これらをすべてシステムプロンプトに詰め込むこともできますが、そうすると Python デバッグ、データ分析、メール作成——あらゆるリクエストがフロントエンドデザインのコンテキストを引きずることになります。問題はこう変わります——「無関係なタスクに恒久的なコンテキストオーバーヘッドをかけずに、必要なときにピンポイントでドメイン特有のガイダンスを Claude に提供するには、どうすればよいのか?」

## Skills: 動的なコンテキストの読み込み

まさにこれこそ、[Skills](https://www.anthropic.com/news/skills) が設計された目的です。恒久的なオーバーヘッドなしに、専門的なコンテキストをオンデマンドで届けるということです。スキルはドキュメント (多くの場合 Markdown) で、指示、制約、ドメイン知識を含んでおり、Claude がシンプルなファイル読み取りツールを通じてアクセスできる指定ディレクトリに格納されます。Claude はこれらのスキルを活用して、実行時に必要な情報を動的に読み込み、最初からすべてを読み込むのではなく、段階的にコンテキストを強化できます。

これらのスキルと読み取りに必要なツールを装備すると、Claude は目の前のタスクに基づいて自律的に関連スキルを特定して読み込めます。たとえばランディングページの構築や React コンポーネントの作成を頼まれたとき、Claude はフロントエンドデザインのスキルを読み込み、その指示をジャストインタイムで適用できます。これこそが本質的なメンタルモデルです——スキルは、特定のタスクタイプに対して専門的なガイダンスを、恒久的なコンテキストオーバーヘッドなしに提供する、オンデマンドで有効化されるプロンプトおよびコンテキストリソースなのです。

これにより、開発者は Claude のステアラブルさの恩恵を受けられるようになります——コンテキストウィンドウを、多くのタスクにまたがる雑多な指示でシステムプロンプトを膨らませることなく、です。[以前説明した](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)ように、コンテキストウィンドウにトークンが多すぎるとパフォーマンスの低下を招くため、コンテキストウィンドウの中身をリーンかつ焦点を絞った状態に保つことは、モデルから最高のパフォーマンスを引き出すうえで極めて重要です。Skills は、効果的なプロンプトを再利用可能かつコンテキスト依存にすることで、この問題を解決します。

## よりよいフロントエンド出力のためのプロンプティング

フロントエンドデザインのスキルを作ることで、恒久的なコンテキストオーバーヘッドなしに、Claude からはるかによい UI 生成を引き出せます。核となる洞察は、フロントエンドデザインをフロントエンドエンジニアが考えるように考えることです。美学的な改善を実装可能なフロントエンドコードにマッピングできればできるほど、Claude はよりよく実行できます。

この洞察を活用し、私たちはターゲットを絞ったプロンプトがうまく働く領域をいくつか特定しました——タイポグラフィ、アニメーション、背景効果、テーマです。これらはすべて Claude が書けるコードにきれいにマッピングできます。これをプロンプトに実装するには、詳細な技術指示は必要ありません——モデルにこれらのデザイン軸についてより批判的に考えるよう促す、ターゲットを絞った言葉遣いだけで、より強力な出力を引き出すには十分です。これは、私たちの[コンテキストエンジニアリング](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)のブログ記事で示した、モデルに対する「適切な高度」でプロンプトを与えるべきであるというガイダンスと密接に対応しています。具体的な 16 進カラーコードを指定するような低すぎる高度のハードコード指示と、共有のコンテキストを前提とした曖昧な高すぎる高度のガイダンスという 2 つの極端を避けよ、というものです。

### タイポグラフィ

この考え方を実際に見るために、タイポグラフィをプロンプトで影響を与えられる 1 次元としてとらえるところから始めましょう。以下のプロンプトは、Claude をより興味深いフォントへと具体的に誘導します。

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

**ベースプロンプトのみで生成された出力:**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/691366f388193282b0213316_image11.png)

**ベースプロンプト + タイポグラフィセクションで生成された出力:**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913679c9a202c88b680873b_image13.png)

興味深いことに、「より興味深いフォントを使え」という指示は、モデルがデザインの他の側面も改善するよう促しているようです。

タイポグラフィだけでも大きな改善をもたらしますが、フォントはあくまで 1 次元にすぎません。インターフェース全体にわたる一貫した美学についてはどうでしょうか?

### テーマ

プロンプトで狙えるもう 1 つの次元は、よく知られたテーマや美学に着想を得たデザインです。Claude は人気のあるテーマについて豊かな理解を持っているので、これを使って、フロントエンドが体現してほしい具体的な美学を伝えられます。次はその例です。

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

これは次のような RPG テーマの UI を生み出します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913cec4181329835d1da27f_image2.png)

タイポグラフィとテーマは、ターゲットを絞ったプロンプティングが機能することを示しています。しかし手動で各次元を指定するのは面倒です。これらの改善すべてを 1 つの再利用可能な資産にまとめられたら、どうでしょうか?

### 汎用プロンプト

同じ原則は他のデザイン次元にも広がります。モーション (アニメーションとマイクロインタラクション) のためにプロンプトすれば、静的なデザインに欠けている洗練が加わります。またより興味深い背景の選択へとモデルを誘導すれば、奥行きと視覚的な興味を生み出せます。ここで、包括的なスキルの真価が発揮されます。

これらをすべてまとめて、約 400 トークンのプロンプト——コンテキストを膨らませずに読み込める (スキルとして読み込んでも) コンパクトさでありながら、タイポグラフィ、カラー、モーション、背景にわたって劇的にフロントエンド出力を改善するもの——を開発しました。

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

上記の例では、まず Claude に問題と解こうとしていることに関する一般的なコンテキストを与えることから始めています。私たちは、この種のハイレベルなコンテキストをモデルに与えることが、出力をキャリブレーションするのに役立つプロンプトの戦術であることを見てきました。その後、前に議論した改善のベクトルを特定し、モデルがこれらの次元すべてにわたってより創造的に考えるよう促す、ターゲットを絞ったアドバイスを与えます。

加えて、Claude が別の局所最適解へと収束してしまわないように、末尾に追加のガイダンスを含めています。特定のパターンを避けるよう明示的に指示しても、モデルは他のよくある選択 (たとえばタイポグラフィの Space Grotesk) をデフォルトにしてしまうことがあります。最後の「think outside the box」のリマインダーは、創造的な変化を強化します。

### フロントエンドデザインへの影響

このスキルを有効にすると、Claude の出力はいくつかのタイプのフロントエンドデザインにわたって改善されます。

**例 1: SaaS ランディングページ**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77b_6d547f28.png)

**キャプション:** 汎用的な Inter フォント、紫のグラデーション、標準的なレイアウトを使った AI 生成の SaaS ランディングページ。スキルは使用していません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f790_c47f37ab.png)

**キャプション:** 上と同じプロンプトにフロントエンドスキルを加えて生成された AI ランディングページ。特徴的なタイポグラフィ、一貫した配色、レイヤード背景を備えています。

**例 2: ブログレイアウト**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78d_f7040147.png)

デフォルトのシステムフォントとフラットな白背景の AI 生成ブログレイアウト。スキルは使用していません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f77e_0ce357ff.png)

上と同じプロンプトにフロントエンドスキルを加えた AI 生成ブログレイアウト。エディトリアルな書体、大気感のある奥行き、洗練された余白を備えています。

**例 3: 管理ダッシュボード**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f784_7beb17d0.png)

標準的な UI コンポーネントを使った、視覚的階層の弱い AI 生成の管理ダッシュボード。スキルは使用していません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f781_3705adad.png)

上と同じプロンプトにフロントエンドスキルを加えて生成された、力強いタイポグラフィ、一貫したダークテーマ、意図的なモーションを備えた AI 生成の管理ダッシュボード。

## Skills で [claude.ai](http://claude.ai) のアーティファクト品質を改善する

デザインの趣味だけが限界ではありません。Claude はアーティファクトを作るときにアーキテクチャ上の制約にも直面します。[アーティファクト](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)は、Claude が作成してチャットの横に表示する、インタラクティブで編集可能なコンテンツ (コードやドキュメントなど) です。

上で探ったデザインの趣味の問題に加えて、Claude には [claude.ai](http://claude.ai) で素晴らしいフロントエンドアーティファクトを生成する能力を制限する、もう 1 つのデフォルトの振る舞いがあります。現在、フロントエンドを作るよう頼まれたとき、Claude は CSS と JS を含んだ単一の HTML ファイルを作るだけです。これは、アーティファクトとして正しくレンダリングされるためにはフロントエンドが単一の HTML ファイルでなければならない、と Claude が理解しているからです。

人間の開発者が単一ファイル内でしか HTML/CSS/JS を書けないとしたら非常に基本的なフロントエンドしか作れないだろうと期待されるのと同じように、私たちは「Claude により豊かなツールを使う指示を与えれば、より印象的なフロントエンドアーティファクトを生成できるはず」と仮説を立てました。

これが、[web-artifacts-builder スキル](https://github.com/anthropics/skills/blob/main/web-artifacts-builder/SKILL.md)を作るきっかけになりました。このスキルは、Claude の[コンピュータ使用](https://www.claude.com/blog/create-files)能力を活用し、[React](https://react.dev/)、[Tailwind CSS](https://tailwindcss.com/)、[shadcn/ui](https://ui.shadcn.com/) のようなモダンなウェブ技術と複数ファイルを使ってアーティファクトを構築するよう Claude を導きます。内部では、このスキルは (1) Claude が効率的に基本的な React リポジトリをセットアップするのを助け、(2) 編集が終わったあとに [Parcel](https://parceljs.org/) ですべてを単一ファイルにバンドルし、単一 HTML ファイル要件を満たす——そのようなスクリプトを公開しています。これはスキルのコアとなる利点の 1 つです——Claude にボイラープレートのアクションを実行するスクリプトへのアクセスを与えることで、Claude はトークン使用を最小化しつつ信頼性とパフォーマンスを向上させられます。

web-artifacts-builder スキルを使えば、Claude は shadcn/ui のフォームコンポーネントと Tailwind のレスポンシブグリッドシステムを活用して、より包括的なアーティファクトを作れるようになります。

**例 1: ホワイトボードアプリ**

たとえば web-artifacts-builder スキルなしでホワイトボードアプリを作るようプロンプトしたとき、Claude は非常に基本的なインターフェースを出力しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f787_b07e5190.png)

一方で、新しい web-artifacts-builder スキルを使ったときには、さまざまな図形とテキストの描画を含む、はるかに洗練された機能豊富なアプリケーションが初期状態で生成されました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f78a_57c49993.png)

**例 2: タスク管理アプリ**

同様に、タスク管理アプリを作るよう依頼したとき、スキルなしでは Claude は機能的だが非常にミニマルなアプリケーションを生成しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f793_875d1eef.png)

スキルありでは、Claude はより機能豊富なアプリを初期状態で生成しました。たとえば Claude は、タスクに関連するカテゴリや期日を設定できる「Create New Task」フォームコンポーネントを含めていました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7c9_7ae52606.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6913d5b728dcecc13bc1f7a1_4c4951af.png)

[Claude.ai](http://claude.ai) でこの新しいスキルを試すには、スキルを有効にした上で、アーティファクトを作るときに「use the web-artifacts-builder skill」と Claude に伝えるだけです。

## Skills で Claude のフロントエンドデザイン能力を最適化する

このフロントエンドデザインのスキルは、言語モデルの能力についてより広い原則を示しています——モデルはしばしば、デフォルトでは表現しないより多くのことができるのです。Claude は強いデザイン理解を持っていますが、分布の収束がガイダンスなしではそれを覆い隠してしまいます。これらの指示をシステムプロンプトに追加することもできますが、そうするとすべてのリクエストがフロントエンドデザインのコンテキストを背負うことになります——その知識が当のタスクに無関係であっても、です。代わりに Skills を使うことで、Claude は常にガイダンスを必要とするツールから、あらゆるタスクにドメイン専門性をもたらすツールへと変わります。

Skills は高度にカスタマイズ可能でもあります——あなた自身の具体的なニーズに合わせて作れます。これにより、社内のデザインシステム、特定のコンポーネントパターン、業界特有の UI 慣習など、スキルに組み込みたい正確なプリミティブを定義できます。これらの決定を Skill にエンコードすることで、エージェントの思考の一部を、開発チーム全体が活用できる再利用可能な資産へと変えられます。スキルは継続してスケールする組織の知識となり、プロジェクト横断で一貫した品質を保証します。

このパターンはフロントエンドの仕事を超えて広がります。より広い理解を持っているにもかかわらず Claude が汎用的な出力を生成するあらゆるドメインは、Skill 開発の候補になります。方法は一貫しています——収束的なデフォルトを特定し、具体的な代替を提供し、適切な高度でガイダンスを構造化し、Skills を通じて再利用可能にすることです。

フロントエンド開発においては、これは Claude がリクエストごとのプロンプトエンジニアリングなしに特徴的なインターフェースを生成できることを意味します。始めるには、私たちの[フロントエンドデザインのクックブック](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb)を探索するか、[Claude Code の新しい frontend design プラグイン](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design)を試してみてください。

**インスピレーションを感じましたか? 自分のフロントエンドスキルを作るには、[skill-creator](https://github.com/anthropics/skills/tree/main/skill-creator) をチェックしてください。**

**謝辞**
Anthropic の Applied AI チームによって執筆されました——Prithvi Rajasekaran、Justin Wei、Alexander Bricken、およびマーケティングパートナーの Molly Vorwerck と Ryan Whitehead。
