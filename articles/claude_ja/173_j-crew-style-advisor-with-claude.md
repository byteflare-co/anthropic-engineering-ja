---
date: '2026-11-12'
final_url: https://claude.com/resources/articles/j-crew-style-advisor-with-claude
number: 173
selector_used: article
slug: j-crew-style-advisor-with-claude
source_url: https://claude.com/blog/j-crew-style-advisor-with-claude
title: J. Crew brings its signature approach to styling to life with Claude
title_ja: J.Crew、Claude で独自のスタイリング手法をオンラインで実現
---

オンラインでの買い物は通常、商品を 1 点ずつ探す形で進みます。そのため、セーターを見つけた顧客は、それに合うパンツや靴をあらためて探さなければなりません。この状況を変えるため、J.Crew は本日、[JCrew.com](https://www.jcrew.com/) 上で AI スタイリスト「Style Advisor」をローンチしました。顧客がコーディネート一式単位で買い物できるよう支援するものです。J.Crew のチームは [Claude Code](https://claude.com/product/claude-code) を使い、Fable から Haiku まで複数の Claude モデルを、それぞれが最も得意とする仕事に割り当てて Style Advisor を構築しました。現在、米国で女性向け・男性向けスタイルに対応して利用可能です。

J.Crew のスタイリストたちは 40 年以上にわたり、プロポーション、色、レイヤリングのバランスを取り、意外性のあるアイテムの組み合わせによってコーディネート一式を作り上げてきました。Style Advisor はその専門知識をオンラインにもたらします。顧客が「ビーチウェディング用のコーディネート」や「初めての就職面接用の服装」など必要なものを伝えると、Style Advisor は J.Crew 自身の撮影から引き出したコーディネート一式で応えます。顧客はそこからさらに絞り込みを続けられるため、買い物がビジュアルな対話になります。

## **構築方法**

J.Crew のプロダクトチームは、複雑で自由度の高い仕事向けの Anthropic のモデルである [Claude Fable](https://www.anthropic.com/claude/fable) 5.1 を使って、Style Advisor がスタイリストのように推論する仕組みを設計し、その後 Claude Code で [Claude Opus](https://www.anthropic.com/claude/opus) 5.5 を使って動作するプロトタイプを構築しました。J.Crew のエンジニアがそのプロトタイプを本番環境へと仕上げました。各会話では、[Claude Sonnet](https://www.anthropic.com/claude/sonnet) 5.5 がスタイリストとして振る舞い、応答の各ステップを判断します。一方、[Claude Haiku](https://www.anthropic.com/claude/haiku) 5.5 は素早く的を絞ったタスクを担当し、Style Advisor が迅速に応答できるようにしています。すべてのコーディネートは J.Crew のスタイリストが手がけたものなので、推奨内容は J.Crew のスタイリングの視点と一貫性を保ちます。

### **顧客による Style Advisor の使い方**

- **コーディネート一式で買い物する。** すべての推奨は、J.Crew のスタイリストがブランドのカタログ撮影のために作ったコーディネートを起点としています。Style Advisor はそれを写真で表示するため、顧客はコーディネート全体を確認できます。
- **1 点のアイテムから組み立てる。** 顧客は 1 つのアイテムから始めて、コーディネートを完成させるアイテムの提案を受けられます。
- **シーンに合わせて装う。** 休暇、ホリデーパーティー、結婚式など、出かける先を伝えると、それに合った推奨を受けられます。
- **J.Crew の視点を得る。** Style Advisor は、J.Crew のスタイリストが店舗で用いるのと同じスタイリングの原則を適用します。

## **今後の展開**

ローンチ時点で、Style Advisor は顧客が新しいコーディネートのアイデアを見つけ、より自信を持って買い物できるよう支援します。J.Crew は今後、各顧客の好みや過去の購入履歴に合わせて提案を調整することでよりパーソナルなものにし、さらに多くの市場や製品ラインへ展開していく計画です。

「消費者の期待が変化し、AI が小売に新たな可能性を開くなかで、J.Crew は従来のオンラインショッピングのモデルに挑戦し、個々の商品検索を超えて、よりつながりがありインスピレーションを起点とした体験へと移行しようとしています」と、J.Crew Group の Chief Executive Officer である Libby Wadle 氏は述べています。「私たちは長い間、顧客が将来どのように買い物をしたいと考えるか、そしてその進化に受け身で対応するのではなく、どうすれば主導できるかを考えてきました。ショッピング体験を根本から再考する機会があると考えています。Anthropic との取り組みを通じて、J.Crew が数十年にわたって培ってきたスタイリング、マーチャンダイジング、クリエイティブの専門知識を結集し、これからの顧客行動を形づくる手助けをしていきます。」

「J.Crew はファッション界で最も認知度の高い独自の視点を持つブランドの 1 つであり、そのチームは Claude を使ってその専門知識を新しい形で顧客に届けました」と、Anthropic の Chief Commercial Officer である Paul Smith 氏は述べています。「彼らはフロンティアモデルを使って体験を構築し、より高速で効率的なモデルでそれを運用しています。そのため顧客は、ブランドのスタイリングに忠実な回答を素早く得られます。」

***今すぐ [Claude Code](https://claude.com/product/claude-code) で構築を始めましょう。***
