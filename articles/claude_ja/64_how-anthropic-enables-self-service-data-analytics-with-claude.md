---
date: '2026-06-03'
final_url: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
number: 64
selector_used: main
slug: how-anthropic-enables-self-service-data-analytics-with-claude
source_url: https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude
title: How Anthropic enables self-service data analytics with Claude
title_ja: Anthropic が Claude でセルフサービスのデータ分析を可能にする方法
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# Anthropic が Claude でセルフサービスのデータ分析を可能にする方法

多くのデータサイエンスチームやデータエンジニアリングチームが実感しているとおり、セルフサービスのビジネス分析を実現するというのは、伝統的に泥沼の作業でした。

ワイドで非正規化されたテーブルを使って、技術寄りでない同僚にもデータモデルにアクセスしやすくすると、ビジネスがスケールするにつれて、定義の食い違ったビューが重なり合うことになりがちです（そして、SQL を学ぶ気のない従業員との橋渡しには、ほとんど役に立ちません）。一方で、ユーザー向けにより閉じられた環境を用意するアプローチを取れば、ビジネス上の問いのロングテールを取りこぼし、チームが個別に作業を抱え込むことで、メトリクスやダッシュボードが膨張する結果に陥りやすいものです。

LLM の登場は、こうした課題を回避する、セルフサービス分析へのもうひとつの道を提供してくれます。とはいえ、Claude を単純にウェアハウスに向けてエージェントに実行させるだけでは、精度に対して誤った安心感を生み出しかねません。

アドホックな依頼から解放された当初の高揚感は、やがて不安に変わっていきます。このセットアップでは、ステークホルダーが、これまで彼らを慎重にキュレートされたデータセットへと導いていた、基盤となるインフラやドキュメント、専門知識から切り離されてしまうのだと気付くからです。

Anthropic では、ビジネス分析クエリの 95% が Claude によって自動化されており、集計レベルでの精度はおよそ 95% に達しています。こうしたしばしば単調で繰り返しの多い作業を Claude に任せることで、私たちのデータサイエンスチームは、因果モデリング、予測、機械学習といった、より戦略的な仕事に集中できるようになりました。

Anthropic 社内の Claude Code ヘビーユーザー数十名と話をし、分析エージェントについて無数の設計パターンを見てきた結果、私たちは、LLM と一緒に働く他のデータチームに向けたベストプラクティスを蓄積してきました。本記事では、Claude にセルフサーブなビジネスインサイトを最大限引き出させるための、これらのヒントとアプローチを共有します。具体的には次のとおりです:

- なぜ分析の精度はコード生成の問題ではなく、コンテキストと検証の問題なのか
- ほとんどのエラーを引き起こす 3 つの失敗モード
- それらに対処するために構築した、エージェント型の分析スタック
- 効果をどう測定するか
- スキルの大半を作る際に使う基本テンプレート（付録参照）

## **データはソフトウェアではない**

LLM の生成能力は両刃の剣です。複雑な問題に対する創造的な解を生み出す仕組みが、同時に誤った出力をハルシネートする原因にもなりえます。分析エージェントの難しさを正しく理解するには、コーディングエージェントと比較してみるのが有用です。

コーディングはオープンエンドな解空間であり、モデルの創造性が報われる領域です。一方で、ドキュメントとテストがハルシネーションに対する自然なガードレールとして働きます。これに対して分析のユースケースでは、多くの場合、唯一の正しい情報源を使った唯一の正解しかなく、しかもその正しさを決定論的に証明する方法はありません。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a20480bedac32484c00d6b9_4a7645b6.png)

セルフサービスでエージェント型のビジネス分析における複雑さは、主にデータの曖昧さに起因しています。中心的な問題は、***ユーザーの問いを、データモデル内の特定かつ最新のエンティティへとマッピングし、それを正しく扱う方法を知る能力*** に行き着きます。これさえできれば、そこから先の実行や SQL の生成はささいなことになります。

私たちは、不正確な応答の圧倒的多数を占める、この問題の 3 つの属性を特定しました:

1. **コンセプトとエンティティの曖昧性**: データモデルには（潜在的には数百万のフィールドのうち）数百もの妥当な選択肢があり、エージェントはユーザーの問いに最も適したフィールドを選びきれません。たとえば、アクティブユーザー数を測るとき、どんなアクションをもって「アクティブ」とみなすのか？ 不正ユーザーは含めるのか？ どのルックバックウィンドウを使うのか？

2. **データの陳腐化**: データソース、ビジネス定義、スキーマは絶えず変化します。アセットやエージェントの知識は古びていき、微妙に間違った答えを返し始めます。

3. **検索の失敗**: 正しい情報が実際にデータモデル内にあり、きちんと注釈までついているのに、検索空間があまりに広いせいで、エージェントがそれを見つけられない、ということです。

## **私たちのエージェント型分析スタック**

Anthropic でこの 3 つのエラーを最小化する主な手段は、エージェント型のデータスタックです。各レイヤーは、これらの問題のうちひとつ以上に対処することを主目的に存在しています:

1. **エンティティの曖昧性**: data foundations と sources of truth が、もっともらしいエンティティの空間を、単一のガバナンスされた答えに絞り込みます。

2. **陳腐化**: メンテナンスと検証プロセスが、ビジネスの変化に応じて、すべてが腐ってしまうのを防ぎます。

3. **検索の失敗**: スキルが、エージェントがその答えを確実に見つけ、正しく使うことを担保します。

このセクションでは、各レイヤーをどう構築したかを順に見ていきます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2049920443016925a3ef72_74528df2.png)

### **Data foundations**

分析エージェントを正確に保つうえで最も重要なのは、強固な data foundations を整えることです。ここにはデータモデル、変換、テスト、データウェアハウス内のテーブル、そしてそれらを記述するメタデータが含まれます。[ディメンショナルモデリング](https://en.wikipedia.org/wiki/Dimensional_modeling)、シフトレフトのテスト、重要なパイプラインの鮮度・完全性チェックといった、標準的なデータエンジニアリングおよびデータ品質のプラクティスは、依然としてすべて当てはまります（ここではそれらを蒸し返しません）。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2049920443016925a3ef75_98412372.png)

ディメンショナルモデリングのような標準的なデータエンジニアリングのプラクティスは、これまでと同じくらい重要です。

変わるのは、データモデルのエンドユーザーがもはやデータ専門家（例: データサイエンティスト）ではなく、データ専門性や基盤インフラへの理解度がまちまちなユーザーに代わって動くエージェントになる、という点です。これは、結果の正しさをユーザーが検証することを要求できなくなる、という挑戦を突きつけます。なぜなら、エンドユーザーは検証する術を持たないからです。

data foundations レイヤーが主に狙うのは曖昧性の解消です。たとえば *revenue* が 40 もの候補テーブルではなく、ひとつのガバナンスされたデータセットに解決されるのであれば、エージェントが検索を始める前に、問題の大半は消えてなくなります。また、ここは陳腐化に対する最初の防衛線でもあります。同じリポジトリでカノニカルモデルを定義することが、それを常に最新に保つルールを強制する自然な場所だからです。

私たちが特にうまくいくと感じているプラクティスはいくつかあります:

- **カノニカルなデータセットを作る**: 圧倒的に多い失敗パターンは、エージェントがコンセプト（「product X の revenue」）を、単一の正しいテーブル・カラム・メトリクス定義にマッピングできないことで、たいていはサブリミナルに実装が異なる複数の妥当な候補が存在することに起因します。解決策は、より少なく、よりヘビーにガバナンスされた論理モデルを置くことです。すなわち、明確にオーナーがついていて、消費可能で、発見しやすい、少数のカノニカルかつ唯一の真実となるデータセットを整え、ニア重複のものは積極的に非推奨にしていきます。物理的なロールアップやキャッシュもコストやパフォーマンスの観点では依然として重要ですが、これらはカノニカルモデルから機械的に派生させるべきものであり、代替候補として併存させるべきではありません。エージェントがコンセプトを検索したとき、ガバナンスされた答えがひとつだけ見つかる、というのが理想形です。
- **標準を強制する**: 私たちが学んだのは、foundations は、カノニカルモデルとメトリクス定義が *ツール* によって（エージェントが構造的にまずそこにルーティングされる。後述）、*CI* によって（それらをバイパスする変更はレビューで落ちる）、*マンデート* によって（下流チームはガバナンスされたレイヤーの上に構築するか、そうしない理由を説明する）強制されたときにしか維持されない、ということです。強制のないガバナンスは、結局は「複数候補問題」へと急速に退化します。
- **アーティファクトを同居させる（colocate）**: 絶えず変わるデータモデルやビジネスロジックに対する私たちの主な防衛策は、コロケーションです。データコードのほぼすべて（モデリング、セマンティックレイヤー、リファレンスドキュメント、カノニカルなダッシュボード定義など）は、単一のリポジトリ内にあり、レイヤー間の整合性を守る CI チェックが入っています。モデリングの変更が下流のダッシュボードを壊したり、ドキュメント化されたメトリクスを無効化したりするなら、CI がそれを検知し、同じ PR の中で修正まで進めます。（このメカニズムについては、**Skills** セクションで改めて取り上げます）
- **メタデータをファーストクラスのプロダクトとして扱う**: コーディングエージェントがうまく動く理由の一部は、コードベースが *読みやすい（legible）* ことにあります。README、型シグネチャ、docstring などです。あなたのウェアハウスも同じくらい読みやすくできますが、それにはカラム・テーブルの説明、カノニカルなメトリクス定義、グレインのドキュメント、有効値レンジ、リネージ、オーナーシップ、モデルティアリングを、変換コードそのものと同じ厳密さで保守する必要があります。これは新しい知見ではありませんが、良いガバナンスは、エージェントが正しいデータセットを選ぶための決定的な文脈を与えてくれます。

### **Sources of truth**

data foundations がデータウェアハウスそのものだとすれば、sources of truth は、エージェントがそれを航行するために参照する基準面のようなものです。このレイヤーはコンセプトとエンティティの曖昧性を減らし、ステークホルダーの質問の中の「weekly active users」を、データモデル内の特定かつガバナンスされたエンティティに変換します。信頼度の高い順に、おおむね次のとおりです:

- **セマンティックレイヤー:** コンパイルされたメトリクスとディメンションの定義。質問が定義済みメトリクスにきれいに対応していれば、エージェントは関数を呼び、ひとつの数値を得ます。そしてそれは、社内の他のあらゆる出口が出すのと同じ数値です。私たちのエージェントは、（スキル指示によって）*構造的に* セマンティックレイヤーを最初に使うことが求められています（付録参照）。試してみたものの *うまくいかなかった* アイデアもあります。生のテーブルやクエリログから LLM にメトリクス定義を自動生成させて、セマンティックレイヤーをブートストラップしようとしたケースです。それはもっともらしく見える定義を生み出しましたが、私たちが排除しようとしていた当の曖昧性を埋め込んでしまい、より小規模で人手によるレイヤーと比べて、評価において純粋に逆効果でした。したがって、*ドキュメント* は Claude に生成させても、*定義* は人間がオーナーとして持つことを推奨します。
- **リネージと変換グラフ:** セマンティックレイヤーが質問をカバーしていない場合、リネージと（参照回数に基づく）テーブルのランキングが、エージェントに対して、どの上流モデルがそのコンセプトに繋がっているか、どれが非推奨か、どれが同じグレインを共有しているかを推論させる手がかりになります。これにより「メトリクスを知らない」が「どのガバナンスされたモデルから集計すれば良いかは分かる」へと変わります。これは後述の **オンライン検証** で表面化させる鮮度・出所シグナルのバックボーンでもあります。
- **クエリコーパス:** ダッシュボード、ノートブック、過去の分析からの、過去の SQL。直感的にはこれは高価値であるはずです——すでに正しく答えられたあらゆる質問の記録なのですから。*ところが実際には、何千もの過去クエリへの生の検索アクセスをエージェントに与えても、精度は 1 ポイント未満しか変わりませんでした*（このアブレーションは後のセクションで詳しく取り上げます）。構造化されていない検索では、新しい質問を正しい先例に対応付けることができなかったのです。うまくいくのは、そのコーパスをドメインごとの構造化されたリファレンスドキュメントや、再利用可能な分析パターンへと蒸留して、**スキル** に組み込むことです。クエリ履歴は、エージェントが直接読む真実の源としてではなく、キュレーションのための素材として扱うべきものです。
- **ビジネスコンテキスト:** 多くのチームが見落とす層で、私たちが最も長く過小評価していた層でもあります。あなたのビジネスを理解していないエージェントは、ユーザーが *聞いた* ことには答えますが、ユーザーが *意図した* ことには答えません。「Q2 のローンチ」が特定のプロダクトを指していること、ふたつのチームで同じ用語が違う意味で使われていること、ある質問が木曜のボードミーティングのために投げられていること——こうしたことをエージェントは知りません。そこで私たちは、インデックス化されたドキュメント、ロードマップ、意思決定ログ、組織構造から成る企業ナレッジグラフを流し込み、エージェントが暗黙の参照を解決し、より良い確認質問ができるようにしています。

この 4 つに共通する典型的な失敗パターンは、data foundations レイヤーと同じ——**ドキュメントが乏しい、または古い** ことです。Claude はこのギャップを埋めるのに非常に有用です（カラム説明の下書き、クエリパターンからのメトリクスドキュメント提案、CI 上での未文書化モデルのフラグ立てなど）。しかし、キュレーションとオーナーシップは人間が担います。

次の 2 つのセクションでは、そのオーナーシップを「実際に実行に移される程度に安価にする方法」を議論します。

### **Skills**

sources of truth がエージェントの *宣言的な* 知識（あるメトリクスが何を意味するか）だとすれば、スキルはその *手続き的な* 知識——どのソースをどの順番で参照するか、曖昧なデータをどう航行するか、完成した分析はどんな姿か——です。

Claude Code において、[skill](https://code.claude.com/docs/en/skills) はエージェントがオンデマンドで読み込む markdown のフォルダです。Anthropic では、私たちが開発したスキルが大きな付加価値を生んでいます。スキルなしでは、分析の質問に正しく答える Claude の能力は、私たちの評価で 21% を超えませんでした。スキルを加えると、集計でこれらの数値は常に 95% を超え、特定ドメインでは 99% 前後に達することもあります。私たちがスキルの大半を作るときに使うスケルトンは、付録に掲載しています。

いくつかのベストプラクティスを挙げます:

**ペアのスキルを作る**: ***knowledge*** スキルは、追加のドメイン詳細をオンデマンドで読み込めるようにする、薄いトップレベルのルーターとして機能します。「まずセマンティックレイヤーを試す。カバーされていなければ、このドメインの関連するテーブル・カラム・JOIN・落とし穴を記述した、約 30 個のリファレンスファイルがある」と告げる役目です。このルーターは、事実上、検索失敗への私たちの答えです。エージェントに数百万フィールドのウェアハウスを検索させる代わりに、クエリが書かれるよりも前に空間を数十のキュレートされたファイルに絞り込みます。***unbook*** スキルは、シニアアナリストが踏むプロセスをエンコードしたものです。質問を明確化し、（knowledge スキル経由で）ソースを見つけ、クエリを実行し、結果を敵対的レビューサブエージェントに通す。さらに、リテンションカーブ、レートの分解、ファネル分析といった一ダースほどの再利用可能な分析パターンも同梱しているので、よくあるリクエストごとに作り直さずに済みます。

**適切なリファレンスドキュメントを作る**: LLM による検索を念頭に書かれたものです。私たちのリファレンスドキュメントは、テーブルを記述し（グレイン、スコープ、除外）、落とし穴の仕組みを記述し（例: 「既知のフリーメールドメインは除外する。ただし anthropic.com のようなカスタムドメインは残す」）、明示的なルーティングトリガーを示します（例: 「IF 質問が実験の lift について…DO NOT 生のイベントカウントには使わない」）。陳腐化しがちな処方的なレシピは含めません。リファレンスドキュメントを作るのに使うスケルトンを以下に示します。

```
# [Domain] Tables

## Quick Reference
### Business Context — [what this domain means in plain words]
### Entity Grain — [what one row represents]
### Standard Hygiene Filter — [the filter every query in this domain applies]

## Dimensions
- [How the key dimensions are encoded, and how the same concept is named
  differently across tables]

## Key Tables
### [table_name]
- **Grain**: [...] · **Scope/exclusions**: [...]
- **Usage**: [when to use it, when NOT to, join keys, required filters]
[... one short section per governed table ...]

## Gotchas
- [The wrong-answer modes a senior analyst would warn you about]

## Best Practices / Common Query Patterns
- [Default choices, standard cuts, worked patterns where the exact query
  form is the hard part]

## Cross-References
- [Neighboring domain docs that own adjacent questions]
```

**スキルの保守をファーストクラスの市民として扱う**: スキルドキュメントは日々変わるデータモデルを記述しているので、アクティブな保守がなければ数週間で間違ったものになります。私たちはこれをエンジニアリング上の問題として扱うようになる前に、オフライン精度がリリース時の約 95% から 1 ヶ月で約 65% まで漂流するのを目の当たりにしました。具体的には、スキルの markdown ファイルを変換モデルと同じリポジトリにコロケートし、モデルを変更する PR がそれを記述するドキュメントを更新する PR と同じになるようにしました。レポーティングモデルの変更でスキルファイルに触れない PR を、コードレビューフックが警告します。今では、私たちのデータモデル PR のおよそ 90% が、同じ diff にスキルの変更を含んでいます。モデルが改善され、過去の失敗モードがもはや当てはまらなくなったスキルの足場は、定期的に剪定もしています。

**すべてのサーフェスで一貫したシームレスな体験を作る**: 同じスキルは、Slack、IDE、ダッシュボードツール、スタンドアロンのエージェントセッションのいずれにおける問いに対しても、*同じ* 答えを返さなければなりません。私たちはこれを、カノニカルなソースをひとつ（データリポジトリ）に揃え、スキルの変更を自動同期することで実現しました。マージ時に、スキルはプラグインマーケットプレイス（IDE ユーザー向け）、クラウドストレージ blob（1 ファイルを読むホスト型アプリ向け）に同期され、さらに MCP 経由でリソースとして直接配信されます。最初からポータビリティを意識して設計し、ハードコードされたリポジトリパスやサーフェス固有のネームスペースは避けました。

### **検証**

最後に、検証は、3 つの失敗モードのどれが依然として漏れているかを突き止める方法です。

#### **オフライン評価**

私たちがよく見るパターンとして、データチームは凝った分析環境を構築する一方で、自分たちの分析エージェントの精度を理解するプロセスを何も持っていない、というものがあります。

このギャップを埋めるひとつの方法が、シンプルな question / answer のペアによるオフライン評価です。オフライン評価は、ML モデルにとってのオフラインテストに似ていると考えてください——オンラインのエージェントの性能を教えてくれるわけではありませんが、致命的なギャップが存在するかどうかについて、良い感覚を与えてくれます。

Anthropic では 2 種類のオフライン評価を運用しています。**ダッシュボードベース評価** は Claude によって自動生成され（その後、人間が検証します）、最もよくあるステークホルダー質問をカバーします。**ロングテール評価** は、Claude にビジネスコンテキスト（ロードマップ、テーブルドキュメント）を与え、ドメインの残りの部分にわたるもっともらしい質問を生成させるものです。さらに、ステークホルダーがスレッドの中でエージェントを修正したケースを継続的に収集しています。その修正は、評価候補だからです。

その他のベストプラクティスとして、次のようなものがあります:

- **グラウンドトゥルースをアンカーしてドリフトしないようにする**: ライブデータに対して書かれた評価は、根底にある数値が動いた瞬間に陳腐化します。すべての評価はスナップショット日付に固定するか、安定したファクトテーブルに対して書くか、グレーダーがエージェントの *数値* ではなく *クエリ* を判定するようにします。依存先に触る PR で関連評価が再実行されるよう、スイートを CI に組み込みます。
- **結果をテストログではなくテレメトリのように保存する:** すべての実行は、スキルのバージョン、git SHA、モデル ID、アサーションごとの pass/fail、トークン数、ウォールクロックを添えて、ウェアハウスのテーブルに着地します。「あの変更は効いたか？」がクエリになり、単発の CI ランでは捕まらない緩やかなリグレッションを捉える時系列データが得られます。
- **ドメインごとにローンチをゲートする**: ドメインオーナーは、彼らの評価セットのスライスが一定の閾値を超えるまで（私たちは当初 90% 程度を使いました）、自身のステークホルダーにエージェントをアナウンスできません。これにより、ユーザーが失敗を目にする *前* に、リファレンスドキュメントの修正が強制されます。
- **適切な数の評価を用意する**: 必要な評価の数は、ビジネスエリアの複雑さと、基盤となるデータモデルの複雑さによって決まります。オフライン精度がオンライン精度をどれだけ予測するかを追跡してキャリブレートしてください。私たちが見てきたところでは、トピックごと（例: 「growth」）に数十を超えると効果は逓減し、その天井は新しいモデル世代ごとに下がっていきます。
- **オフライン評価の精度は ~100% を狙うべき**: そして、すべての正解は（セマンティックレイヤーがあるなら）セマンティックレイヤーにヒットしているべきです。繰り返しになりますが、この水準の精度は、システムが間違った答えを出さないことを保証するものではなく、適切な評価カバレッジを前提に「目に見えるギャップがない」ことを示すにすぎません。

#### **アブレーション手法**

スキルに関するあらゆる構造的な意思決定（例: どのソースを露出させるか、サブエージェントがそのレイテンシに見合う価値を生むか、ふたつのスキルをひとつに統合すべきか）は、オフライン評価セットを固定したうえで判断します。

ひとつだけコンポーネントを変えて、合格率を比較します。各ランは 1 時間しかかからず、多くの主観的な議論を置き換えてくれます。単発の結果よりも、方法論そのものが重要です:

- **ヌル結果を前提に設計する**。私たちのアブレーションのうち最も有用だったのは、ネガティブなものでした。エージェントに、私たちのダッシュボード、変換、アナリストのノートブック SQL（数千ファイル）への直接の grep アクセスを与えました。続いて、回答前にエージェントが実際にそれらを読んでいることをトランスクリプトで確認しました。精度はどちらの方向にも 1 ポイント未満しか動きませんでした。続いて、明らかな交絡を確かめました——間違えた質問の答えは実際にコーパスの中にあったか？ 約 80% のケースで、はい。「答えが存在すること」は「いまそれが正解できること」を予測したか？ いいえ、フリップ率はフラットでした。情報はそこにあり、エージェントもそれを見ていたのに、それを使えなかったのです。この単一の実験が私たちに告げたのは、ボトルネックは過去の仕事への *アクセス* ではなく *構造*（つまり、質問を正しいエンティティにマッピングすること）だ、ということでした。この洞察は、その後数ヶ月のロードマップの方向を変えました。
- **PR 粒度でアブレートする**。意味のあるスキル編集には、関連する評価スライス上で前後のラン結果と差分を取り、その delta を PR の説明に書きます。これは「ドキュメントを改善しました」を正直に保ち、善意の追加がかえって悪化させる、という意外と頻繁に起こるケースを捉えます。
- **うまくいかなかったことの短いリストを保つ**。私たちの例を 2 つ: あるポイントを超えてドキュメント精緻化のラウンドを重ねること（私たちは 3 回連続でネガティブな反復に当たりました——ドキュメントは長くなり、より良くはなりませんでした）、そして、レイテンシ削減のために敵対的レビュアーをより安価なモデルに置き換えること（精度向上の大半を失い、本当のスピードアップにはなりませんでした）。ネガティブな結果は記録コストが低く、次の人が同じ実験をやり直すのを防いでくれます。

#### **オンライン検証**

最後のステップは、実際のオンラインシステムのパフォーマンスを可能な限り正確に保つことです。私たちが取っている手立てとして、次のようなものがあります:

- **敵対的レビュー**: 潜在的な最終回答の基となるすべての仮定を積極的に挑戦するための Claude スキルを採用することで、評価セット内で精度を 6% 向上させられることを確認しました。ただし、トークンが 32% 増、レイテンシが 72% 増というコストを伴います。
- **出所フッター（Provenance footer）:** すべての応答には、その答えがどのソース階層から来たか（セマンティックレイヤー › キュレートされたリファレンス › 生テーブル）、基となるデータがどれくらい新鮮か、誰がそのモデルのオーナーかを含むフッターが付きます。これは答えをより正しくはしませんが、消費者が応答をどれくらい信頼してよいかを判断するのには役立ちます。「raw table, freshness unknown」というフッターは、上流に転送する前に検証せよ、というシグナルであり、サイレント障害に対する数少ない緩和策のひとつです。
- **データ品質チェック**: あなたのエージェントが正しいフィールドを適切な方法で使っているのに、データそのものが正しくない、ということもありえます。参照されるフィールドが最新で、完全で、異常値を含まないことを保証するための基本的なデータ品質チェックを加えるのは、一般的に良い衛生習慣です。
- **パッシブモニタリング:** 私たちが継続的に追っているプロダクションシグナルが 2 つあります。エージェントクエリのうちセマンティックレイヤー経由で解決されたものの割合と、応答に修正用語（「そのテーブルは違う」「fraud フィルタが抜けている」など）が使われた割合です。両者はダッシュボードに供給され、オフラインの合格率と並べて毎週レビューされます。
- **アクティブな修正収集**: ループを閉じる部分です。スケジュールされたエージェントが、数時間ごとにステークホルダーチャンネルを走査して同様の修正用語を探し、該当するリファレンスドキュメントへの 1 行修正を下書きし、ドメインオーナーにタグ付けした PR を開きます。修正パスは意図的に退屈なものにしてあります——markdown ファイルを編集し、マージし、どこにでも自動同期する——のでドメインオーナーは多くの時間を費やさずに済みます。同じ修正は、オフライン評価セットにもフィードバックされます。

このどれをもってしても完全には捕まえられない失敗モードが、**サイレント** なものです。答えは間違っているのに、もっともらしく見えてしまい、異議なく使われてしまうケースです。私たちの緩和策は、出所フッター、リーダーシップ向けの内容に対する明示的な人間のサインオフ、そして各ドメインのトップ KPI に対して、祝福されたダッシュボードと毎日突き合わせる常設の評価です。とはいえ、堅牢な解はまだ持っていません。

## **始め方**

ゼロから始めるなら、少数のカノニカルデータセット、いくつかの数十件のオフライン評価、薄い knowledge スキルがあれば、アップサイドの大半を捕まえられます。本記事の残りはすべて、それらが構築されたあとに私たちが付け加えてきたものです。

私たちは多くのベストプラクティスを共有しましたが、そのすべてがすべてのデータチームにとって適切とは限りません。アプローチに影響する数個の原則について、組織内ですり合わせるために、次のような問いを投げてみてください:

- **正しい答えは、いま重要なのか、それとも将来重要なのか**？ AI モデルは急速なペースで進歩しています。現在のモデルの不足を補うために大量のインフラを構築している企業をよく見かけますが、それらの不足はモデルが改善されれば無用のものになります。モデルが今どこで不足しているのかを把握しつつ、モデル改善がそのギャップを埋めるのを待つ方が、はるかにオーバーヘッドが小さく済みます。もっとも、それがあなたの会社のリスク許容度に合うとは限りません。
- **時間とともにビジネスの複雑さがどう変わると見ていますか**？ 私たちが議論したプロセスの一部は、たとえばあなたがあまり大量のデータを生み出していない、出力の消費者が少数しかいない、データモデルがシンプルなままにとどまる見込みである、といった場合には過剰かもしれません。
- **出力のオーディエンスはどれくらい技術寄りですか**？ 言い換えれば、答えが間違っていることを認識できるデータサイエンティスト向けに分析システムを構築しているのであれば、エラーへの寛容度は、基盤データモデルへの理解がないオーディエンス向けに作る場合より高くて済むかもしれません。
- **精度向上にどれくらい支払う意思がありますか**？ 敵対的検証のようなプロセスは、精度を大きく押し上げてくれることが分かっていますが、しばしばコストとレイテンシが上がります。
- **アクセス制御と社内データプライバシーに対するスタンスはどの程度ですか**？ エージェントは、より多くのコンテキストを持つほど大きく性能を上げます。一方で、広範なデータアクセスはほとんどの企業のガバナンス姿勢に逆らいます。これは、エージェントをひとつ構築するのか、スコープを切ったものを複数構築するのかを決める観点になります。

どの道を取るにせよ、私たちにとって最大の成果は、3 つの失敗モードそれぞれに対処することから来ました。曖昧性を単一のガバナンスされた答えに畳み込むこと、答えを発見しやすくすること、そしてどちらかが古びたときにフラグを立てること——です。

*この記事は、Data Science および Data Engineering チームのメンバーである Chen Chang、Clement Peng、Justin Leder、Johanne Jiao、Josh Cherry によって書かれました。著者らは、貢献してくれた Michael Segner に感謝します。*

## **付録**

#### **スキルファイルのスケルトン**

以下に示すのは、私たちのメインのウェアハウススキルのスケルトンです——実ファイルの構造を、社内固有の内容は [bracketed placeholders] に置き換えたものです。逐語的にコピーすることを意図したものではなく、私たちが書き留める価値があると感じた節の種類を示すものです。

```
---
name: [warehouse-skill]
version: [x.y.z]
description: "IF the user asks to query [the company]'s data warehouse for any
  [list of business domains] question — THEN invoke this skill. DO NOT invoke
  for [adjacent engineering tasks] or questions with no data-warehouse component."
---

# [Warehouse] Skill Instructions

## Description
The single source of truth for safe and effective [warehouse] querying.
Referenced by other skills [listed] for query execution guidance.

Act as a Data Analyst, providing strategic insights and data-driven
recommendations but seek guidance along the way.

**Out-of-scope decisions**: [product areas, etc.] → surface data only,
state "decision is [owning team]'s call", do NOT take a position or author
code fixes.

## Executing queries
Priority:
1. **[Managed connection]** (if available): [query tool] / [schema tool]
2. **[CLI fallback]** (if installed): [default project, fallback project]
3. **Neither** — ask the user to authenticate, then stop

---

# Semantic Layer (REQUIRED first step)

The governed semantic layer is the **mandatory default path** for every data
question — same numbers as [the BI tool], joins/grain/filters baked in. Raw SQL
via the reference docs below is the **fallback**, used only after the
semantic-layer path is shown not to cover the ask.

## Required workflow
1. **Load** — [how to load the semantic layer in each runtime, with fallbacks]
2. **Discover** — search measures/dimensions by keyword; **always check
   segments** (the named canonical population filters — hand-rolled WHERE
   clauses for these are the dominant wrong-answer mode)
3. **Compile + run** — build the spec → compile to SQL → execute
4. **Fallback** — only if discovery finds no relevant metric or compile fails
   → raw SQL via `references/*.md` (PART 3 below)

> **Don't bail early.** Do NOT fall back to raw SQL on these grounds:
> - "[custom date filtering / cohorts]" → [covered by time-dimension specs]
> - "[needs a join]" → [the metric layer already encapsulates its joins]
> - [3–4 more pre-rebutted excuses agents use to skip the semantic layer]

### Date windows & timezone — decide before you query
- **As-of date vs trailing-N days**: [convention for each]
- **"Last week/month"** → the last *complete* calendar week/month, not trailing-7/30
- **Timezone default**: [TZ]; [exception for certain reporting rollups]
- **Freshness lag**: [some] tables settle late — anchor on MAX(date), not "yesterday"

---

# PART 1: MUST KNOW (Read First for Every Request)

## 🚀 Quick Start Workflow
1. **Check for red flags first**: [restricted/PII requests, gated domains,
   high-stakes asks that need extra validation]
2. **Out of scope — escalate, don't guess**: [access requests, pipeline
   troubleshooting, stale dashboards, root-cause assertions, product/pricing
   recommendations] → redirect to [the owning team], don't answer
3. **Clarify the request**: time period, segment, the business decision it informs
4. **Check for existing dashboards**: [per-domain dashboard catalogs]
5. **Identify the data source**: [navigation map below; prefer governed/aggregated tables]
6. **Execute the analysis**: [required filters + adversarial review]
7. **Deliver insights**: show methodology, differentiate observations from interpretations

## 🏢 Business Context

### Entity Disambiguation (MUST CLARIFY)
- **"[Term A]" can mean**: [entity 1] or [entity 2] — always clarify which
- **"[Term B]" can mean**: [entity 1] → [entity 2] → [entity 3] (one-to-many chain)
- **"Users"**: [which identifier gives accurate counts, and which ones inflate them]

### Business Terminology
- [Current product names vs deprecated aliases that still appear as frozen
  values in the data layer — write with the new names, filter with the old]
- [Key internal acronyms]
- **[Headline metric] calculations**: [monthly / default window / leading indicator]
- **Unfamiliar terms — search [internal docs], don't guess**

### Data Integrity Requirements ⚠️
- **NEVER**: make up data/columns; make speculative assertions beyond what data shows
- **ALWAYS**: use safe division; differentiate observations ("data shows X")
  from interpretations ("this suggests Y"); flag limitations

---

# PART 2: HOW TO DO (Follow During Execution)

## 🔧 Technical Execution Guide
- [Managed-connection tools and CLI invocation details]
- **PII protection**: for restricted data, return the SQL for the user to run
  themselves — do not return results

## 📊 Analysis Best Practices Guide
1. Clarify the ask before querying
2. Show your work (filters, inclusions/exclusions, freshness)
3. Clarify denominators
4. Consider sample bias
5. Connect to business impact
6. **Adversarial SQL review (MANDATORY)** — spawn the [sql-reviewer] sub-agent
   for every query before the final answer; blocking findings must be fixed
   and re-reviewed; do not self-certify
7. **Report with provenance** — every answer ends with a footer:
   > **Source:** [semantic layer | governed table | raw exploration] ·
   > **Confidence:** [tier] · **Reviewed:** [reviewer ✓, round N] ·
   > **Freshness:** [max date in the data] · **Owner:** [owning team]

---

# PART 3: DATA REFERENCES & RESOURCES

## 📚 Knowledge Base Navigation
### [Domain A] → `references/[domain_a].md`
- **Use for**: [kinds of questions]
- **Key tables**: [...]
- **Dashboards**: `references/[domain_a]_dashboards.json`

### [Domain B] → `references/[domain_b].md`
- **Use for**: [...]

[... one entry per business domain — a few dozen in total ...]

## ⚠️ Troubleshooting Guide

### When Information Is Missing
- [missing tables / access denied / outdated docs / unknown enum values → what to do]

### Field Naming Gotchas
- Use `[field_x_v2]` NOT `[field_x]`
- [Two similarly-named tables report the same metric at different grains — which to use]
- [Which of two plausible sources is canonical for the headline metric]
- [… a dozen more hard-won one-liners …]
```
