---
date: '2026-09-08'
final_url: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
number: 135
selector_used: main
slug: reducing-cost-and-improving-performance-with-claude-platform
source_url: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
title: Reducing cost and improving performance with Claude Platform
title_ja: Claude Platform でコストを削減しパフォーマンスを向上させる
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# Claude Platform でコストを削減しパフォーマンスを向上させる
- 著者

  Lance Martin

パフォーマンスとコストはトレードオフの関係にあると見なされがちです。支出を減らせば、結果は悪化するというものです。しかし実際には、Claude Platform を利用する多くのアプリケーションは、パフォーマンスを犠牲にすることなく、3 つの改善によってコストを削減できることがわかっています。すなわち、プロンプトキャッシュのヒット率を最大化すること、フロンティア Claude モデルへアップグレードする際にプロンプトからアンチパターンを取り除くこと、そしてタスクに応じて effort を調整することです。私たちはこのガイダンスを [claude-api スキル](https://github.com/anthropics/skills/tree/main/skills/claude-api)にまとめました。この記事では、claude-api を使った Claude Code が、パフォーマンスを維持または向上させながらコストを削減する方法をどのように見つけられるかを紹介します。

## **プロンプトキャッシュ**

Claude が応答を生成する前に、まずプロンプトを内部の作業状態へと処理します。このステップは *プリフィル (prefill)* と呼ばれ、入力処理の中でコストがかかる部分です。プロンプトキャッシュはこの状態(キー・バリュー、すなわち KV キャッシュ)を保存します。リクエストが同じプレフィックスで始まる場合、Claude は再計算する代わりにそれを読み戻します。キャッシュの読み取りは、フル入力価格の[ごく一部の価格で課金されます](https://platform.claude.com/docs/en/about-claude/pricing)。

プロンプトキャッシュを効果的に利用するためには、いくつか実務上の考慮事項があります。第一に、プロンプトキャッシュは特定のモデルに紐づいています。第二に、プロンプトキャッシュの読み取りはプロンプト全体にわたって *バイト単位で完全に一致*していなければなりません。最後に、プロンプトキャッシュには[限られた生存時間](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#ttl-support) (TTL) があります。

これらを踏まえた、実務上のヒントをいくつか挙げます。

- **会話の途中で effort や thinking の設定を変更しない**。これらの設定はコンテンツより前にプロンプトへレンダリングされるため、キャッシュされるプレフィックスの一部になります。特に Claude Opus 5 と Fable 5.1 では、キャッシュを壊さずに[会話の途中で effort を更新](https://platform.claude.com/docs/en/build-with-claude/effort#changing-effort-mid-conversation)できます。

- **揮発性の値をプレフィックスから外す**。システムプロンプト内の動的なタイムスタンプや ID は、モデル呼び出しごとに変化し、キャッシュを壊す可能性があります。

- **順序が入れ替わるツール定義を避ける**。Claude Messages API を使う場合、[プロンプトは固定順序で組み立てられ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#structuring-your-prompt)、ツール定義は先頭にレンダリングされます。ツール定義への変更はいずれもキャッシュを壊します。

- **会話をフォークするときは注意する**。サブエージェントやブランチは、フォーク元のプレフィックスがバイト単位で同一であり、同じモデル、同じ effort を使っている場合にのみ、親のキャッシュを共有します。

- **キャッシュの TTL より長く続く同期的なツール呼び出しやサブエージェントを避ける**。エージェントが長時間実行されるツール呼び出しやサブエージェントをブロッキングで待つ場合、結果が返ってくる前にキャッシュが失効することがあります。次のターンではキャッシュを書き直す必要があり、安価な読み取り価格ではなく通常の入力価格の 1.25 倍(1 時間キャッシュでは 2 倍)がかかります。

### 対処方法

私たちはプロンプトキャッシュ管理について、いくつかの教訓を[蓄積してきました](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)。

- **プロンプトキャッシュのヒット率を注意深くモニタリングする**。[Claude Console](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) はプロンプトキャッシュの診断機能を提供しており、キャッシュミスの理由も確認できます(図 1)。ヒット率が予期せず低下した場合、[キャッシュ診断 API](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) を使えば、2 つのリクエストがどこで分岐したかを正確に把握できます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8d87cec69dcbb7d97cb2_image3.png)

図 1。Claude Console は連続するリクエストを比較し、プロンプトのプレフィックスがどこで分岐したかを特定することで、予期しないプロンプトキャッシュミスを診断できます。

- **めったに使わないツールの読み込みを遅延させる**。すべてのツールを事前に宣言しつつ、めったに使わないものには [defer_loading](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#defer-loading-and-cache-preservation) を指定します。これによりキャッシュされるプレフィックスから外れ、Claude がツール検索で参照したときにのみ会話に追加されるため、キャッシュが保持されます。

- **システムプロンプトの更新はメッセージとして適用する**。[Claude Platform](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#when-to-use-a-mid-conversation-system-message) では、システムプロンプトを編集する代わりに、会話の途中でシステム指示をメッセージとして追加でき、これによりキャッシュが保持されます。

- **安定した部分が安定したままになるようリクエストを構成する**。静的なコンテキスト(ツール定義とシステムプロンプト)を先頭に置き、増え続ける会話をその後ろに配置します(図 2)。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8e173f4924ebf13397e3_image5.png)

図 2。動的なコンテンツが安定したプレフィックスの末尾に追加されるようにプロンプトを構成します。

- **プロンプトキャッシュがどのみち壊れるタイミングでモデルや effort を変更する**。[compaction (圧縮)](https://platform.claude.com/docs/en/build-with-claude/compaction) のような一部の操作は、すでにキャッシュ(会話)の大部分を書き直します。どちらにせよキャッシュミスの代償を払うことになるため、これはモデルや effort を切り替える[良いタイミング](https://cognition.com/blog/devin-fusion)です。

- **会話が伸びるにつれてキャッシュのブレークポイントを移動させる**。Claude Platform では、[automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) を設定することで、キャッシュのブレークポイントを最後のキャッシュ可能なブロックへ自動的に適用できます。

- **キャッシュを事前にウォームアップする**。レイテンシを削減するには、max_tokens: 0 と明示的なキャッシュブレークポイントを指定してリクエストを送信します。これによりプロンプトは処理されキャッシュに書き込まれますが、何も生成はされません。セッション開始時(たとえばユーザーが入力している間)にこれを実行しておけば、最初の実際のリクエストはウォームなキャッシュにヒットします。

- **プロンプトキャッシュの TTL を超えないようにする**。5 分間のキャッシュ TTL は、リクエスト開始時点からカウントされます。エージェントが 5 分を超えて実行されるツール呼び出しやサブエージェントのリクエストをブロッキングで待っている場合、結果が返ってくる前に親のキャッシュが失効します。このような場合は、代わりにプレフィックスに[1 時間の TTL を設定する](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)ことを検討してください。

## **指示**

プロンプトには、モデルの弱点を補うための指示が積み重なっていきがちです。こうした指示は、[最新の Claude モデル](https://x.com/trq212/status/2080710971228918066)の能力に対して次第にずれていく可能性があります。以下は、フロンティア Claude モデルの足かせとなり、意図せずコストを増加させうる、よくあるプロンプティングの「アンチパターン」です。

- **検証儀式**。「*作業内容を二重チェックしてください*」や「*回答前に 2 回検証してください*」といった指示は、フロンティアモデルによって文字通りに実行されることが多く、トークンを浪費する可能性があります。

- **徹底性・強調のブースター**。「*最大限徹底的に行ってください*」「*重要: あなたは常に…しなければなりません*」といった表現は、フロンティアモデルで作業する際に冗長さや余計なツール呼び出しにつながることがあります。

- **必須手続きとスクラッチパッドの足場**。固定された手順プロセス(例:「*スクラッチパッドで段階的に考えてください*」)や推論テンプレートは、フロンティアモデルには不要な儀式です。こうした足場は、モデルがネイティブに持つ推論の上に積み重なり、不要なトークンを消費することがあります。

- **古びた例**。古いモデルの失敗パターンに合わせて調整された few-shot の例は、フロンティアモデルに対して、必要のないリクエストでも長い推論チェーンを模倣させてしまうことがあります。

- **矛盾するルール**。フロンティアモデルは指示追従の能力が高くなっています。矛盾する指示(「常にポリシーの範囲内で返金する」と「エスカレーションなしに返金を行ってはならない」など)は、フロンティアモデルによってより文字通りに従われる可能性があり、結果としてパフォーマンスが低下することがあります。

- **古い設定**。古い世代の Claude 向けに書かれた設定(例:手動の thinking budget)は、フロンティアモデルへアップグレードした際に Claude Platform に拒否されることがあります。

### **対処方法**

私たちは claude-api スキルを更新し、これらのアンチパターンを検出する新しいコマンドを追加しました。Claude Code で `/claude-api prompt-audit` を実行すると、プロンプト、スキル、ツールの説明文をチェックできます。この監査は、作業ディレクトリ内のあらゆるもの(Claude API を呼び出すアプリケーションコードや、Claude Code 自身の設定([CLAUDE.md](http://claude.md) やスキルなど)を含む)を対象とします。

たとえば、カスタマーサポートのベンチマークで Opus 4.8 から Opus 5 へのモデル移行をテストしました。クリーンなプロンプトから始め、アンチパターンを 1 つずつ植え付けていきました(廃止された thinking 設定、矛盾する 2 つの返金ルール、手動のスクラッチパッド、「2 回検証する」、「最大限徹底的に行う」、必須の 6 ステップ手順)。これにより 6 つのレガシープロンプトができました。

それぞれを Opus 4.8 上で、モデル ID のみを変更した Opus 5 上で、そして各プロンプトに対して `/claude-api prompt-audit` を 1 回実行した後の Opus 5 上で実行しました(図 3 は 6 つの平均を示しています)。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8f03f76b0fe7cad36789_image7.png)

図 3。Opus 4.8 から Opus 5 へのモデル移行時における、プロンプティングのアンチパターンの影響。

図 3 | Opus 4.8 から Opus 5 へのモデル移行時における、プロンプティングのアンチパターンの影響。

Opus 5 では、検証儀式(「*2 回検証する*」)によって、返金のたびに注文検索が重複して実行され、不要なトークンが消費されました。強調ブースター(「*最大限徹底的に行う*」)は、数十回もの不要なナレッジベース検索につながりました。

`/claude-api prompt-audit` を実行してアンチパターンを取り除くと、コストは平均で 14.6% 低下し、精度は平均で 5.3% 向上しました。余計なツール呼び出しや重複した推論が排除されたことでコストが下がりました。精度が上がった理由は 3 つあります。廃止された thinking 設定は、すべてのルーティングリクエストを API 側で問答無用に拒否していました。矛盾する返金ルールは、Opus 5 に、顧客に確認を求めさせながら本来支払うべき 4 件の返金を保留させていました。そして手動のスクラッチパッドは Opus 5 の組み込み thinking と衝突し、3 件のチケットではツール呼び出しを推論の中に書いたまま、実際には実行しないという事態を引き起こしていました。

## **Effort**

[Effort](https://platform.claude.com/docs/en/build-with-claude/effort) は、Claude に「どれだけ懸命に取り組むか」を伝えるものです。effort が低いと、Claude は概して速く結論に達します。effort が高いと、Claude は熟考し、検証し、回答前に複数の選択肢を検討します。

同一モデルにおける effort レベル間のコストとパフォーマンスの関係は、タスクによって大きく異なります。たとえば、Claude Fable 5 は FrontierCode Diamond(最も難しい 50 タスク)において、低 effort ではタスクあたり $5.35 で 11.5% のスコアです。最大 effort では、Fable 5 はタスクあたり $19.00 で 30.9% のスコアとなり、effort を変更するとコストが約 3.5 倍になる代わりにスコアが約 2.7 倍(+19 ポイント)になります(図 4)。

Claude Fable 5.1 では、Humanity's Last Exam(ツールなし)において、最後のステップで効果が逓減する急な曲線が見られます。低 effort では質問あたり約 $0.30 で約 53% のスコア、最大 effort では約 $2.23 で約 61% のスコアとなり、最大 effort への最後の一段は、コストを 46% 増やす代わりにスコアを 0.5 ポイントほどしか押し上げません。この上昇幅はベンチマークの実行ごとのばらつきの範囲内にあり、実質的には測定可能な向上のないままコストだけを多く支払うことになります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8f79e11f87d01ba88ea0_image4.png)

図 4。FrontierCode Diamond における、effort レベルごとの Fable 5 のパフォーマンスとコスト。

effort はどちらの方向にも誤って調整されうるものです。

- **高いほど常に良いと考えてしまう**。effort が高すぎると、*考えすぎ*が生じることがあります。Claude はタスクが要求する以上の時間をかけて熟考するようになり、コストやレイテンシが増し、回答の質が下がることさえあります。熟考は、まだ見つけるべき根拠が残っている間しか役に立ちません。

- **低い effort に偏ってしまう**。低く設定しすぎると、Claude は十分な根拠を得る前に止まってしまいます。ツール呼び出しの回数が減るため、3 番目ではなく最初の検索結果から回答してしまうことがあります。難しいステップでの思考量も減り、通常であれば自発的に行うはずのチェックを省略します。回答は完成しているように見えても、実際には不完全な情報の上に組み立てられています。

### **対処方法**

effort を調整するための有効な方法がいくつかあります。

- **より低い effort でより強力なモデルを試す**。低い effort のより強力なモデルは、高い effort で懸命に取り組む弱いモデルよりも安価になることがあります。たとえば、CursorBench 3.2 では、Claude Fable 5.1 が低 effort で、Fable 5 が高 effort のときの[パフォーマンスに匹敵し](https://www-cdn.anthropic.com/0339e6a7c5c7b87f5c07798616dc32c215d14235/Claude%20Fable%205.1%20&%20Claude%20Mythos%205.1%20System%20Card.pdf)ながら、コストは 3 分の 1 に抑えられます(図 5)。新しいモデルの方が安価になる理由は 2 つあります。低 effort ではタスクあたりの作業量が少なくなること、そして Fable 5.1 のプロンプトキャッシュ読み取りが 100 万トークンあたり $0.25 であるのに対し Fable 5 は $1.00 であることです。Fable 5 の価格のままだとしても、低 effort の Fable 5.1 は約 40% 安くなります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8fa48d8330985eb9d300_image1.png)

図 5。CursorBench 3.2 における、effort レベルごとの Fable 5 と Fable 5.1 の比較。

- **自分のタスクの形状を理解する。** [effort レベルを一通り変化させながら](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)アプリケーションのパフォーマンスを計測することは、自分の特定のタスクにおけるコストとパフォーマンスのトレードオフを理解する有効な方法です。飽和していない評価において、effort レベル間でパフォーマンス・コスト曲線が平坦であれば、そのタスクは thinking の計算量に律速されておらず、effort を増やしても有益ではないことを示唆しています。

この調整には、多くの場合、モデルと effort レベルを横断した評価の実行が伴います。Claude Code では、`/claude-api hillclimb` がこの探索を代わりに行います。評価を訓練セットとテストセットに分割し、設定変更を提案し、失敗した訓練例を読んで問題を修正します。

私たちはこれを、Opus 4.8 のデフォルト(高)effort をベースラインとして、カスタマーサポートのベンチマークで実行しました。hillclimber はまず、必須のツール呼び出し儀式やスクラッチパッドのステップ、矛盾するルールを取り除く prompt-audit を適用しつつ、低 effort の Opus 5 を試しました。これにより、訓練精度 98.9% で Opus 4.8 のベースラインを上回り、コストは 1 チケットあたり 2.6 セントまで下がりました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f8fd5bc0d13015256b1f5_image6.png)

図 6。Hillclimbing は、モデル選択、effort、プロンプトを更新することでコストとパフォーマンスを改善します。

続いて、さらに安価な低 effort の Sonnet 5 まで段階を下げ、1 チケットあたり 1 セントとよりコストが下がりましたが、精度は 88.9% まで低下しました。失敗した訓練チケットを読み込み、Claude はルーティングルールと返金上限のクロスリファレンスをプロンプトに追加し、同じコストのまま Sonnet 5 を 98.9% まで引き上げました。

探索が一度も見ていなかった 14 件の保留チケットでは、最終的な構成は元の設定の 78.6% に対して 90.5% のスコアを記録し、コストは約 5 分の 1 に抑えられました。

## **コスト削減の自動化**

プロンプトキャッシュ、指示、effort は、コストを削減するための一般的なレバーです。私たちの[ドキュメント](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cut-spend-without-losing-quality)ではさらに多くの手法を取り上げています。Claude API を利用するアプリケーションコードの包括的なコスト監査を行うために、`/claude-api cost-optimize` を追加しました。これは支出の内訳を明らかにし、コスト削減策を適用し、評価を提供すれば、節約分がパフォーマンスとどうトレードオフになるかを示してくれます。

cost-optimize は、まずトークンがどこに使われているかを突き止めるところから始まります。Claude Admin API キーを持っていれば組織の[利用状況・コストレポート](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)から、アプリケーションが記録していれば各 API レスポンスの usage オブジェクトから、そのどちらもなければリクエスト構築コードを読み取って見積もることで把握します。

その後、利用可能な節約策を、プロンプトキャッシュを筆頭に、各リクエストが運ぶ内容の削減(prompt-audit を含む)、出力の上限設定、そして無人で実行される作業の[バッチ処理](https://platform.claude.com/docs/en/build-with-claude/batch-processing)の順にランク付けします。評価を提供すると、さらに一歩進んで effort レベルとモデル選択にわたるコストとパフォーマンスを算出します。

これを 4 つの公開ベンチマークで、Sonnet 5 をベースラインとして実行しました(図 7)。

- **LegalBench(コスト約 58% 削減)**: cost-optimize は、タスク間で共有されるプレフィックスのキャッシュ、低 effort の設定、Batch API 経由でのタスク処理を提案しました。thinking トークンは 102,779 から 8,284 まで減少しましたが、正答率はばらつきの範囲内にとどまり、コストは約 58% 削減されました。

- **tau2-bench retail(コスト約 73% 削減)**: 明示的なブレークポイント配置によるプロンプトキャッシュの実装により、cost-optimize は正答率を横ばいに保ちながら支出を 73% 削減しました。

- **OfficeQA Pro(コスト約 52% 削減)**: cost-optimize はバッチ処理とドキュメントキャッシュを追加し、コストは $136.20 から $64.87 まで下がりました。

- **SWE-bench Verified(コスト約 55% 削減)**: cost-optimize は、デフォルト構成がすでに正しくキャッシュを行っていることを発見しました。節約は effort を medium に設定し、エージェントの出力を数文の簡潔なものに制限することで得られました。タスクあたりのステップ数の中央値は 29 から 17 に、プロンプトトークンは 75.2M から 33.7M まで減少しました。

‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a9f9120b5999192bd5d7463_d41ebc95.png)

図 7。`/claude-api cost-optimize` によるベンチマーク間のコストとパフォーマンスの変化。

## **はじめ方**

フロンティア Claude モデルへ移行し、既存のプロンプトをそれに照らしてチェックしたい場合は `/claude-api prompt-audit` から始めてください。作業ディレクトリ内のプロンプト、スキル、ツールの説明文をスキャンします。これには、Claude API を呼び出すアプリケーションコードや、Claude Code の設定(CLAUDE.md、スキル)が含まれます。フロンティアモデルの足かせとなる一般的なアンチパターンを取り除きます。

アプリケーションが Claude API を使っていて、コスト監査を行いたい場合は `/claude-api cost-optimize` を使ってください。トークンの支出内訳を分析したうえで、さまざまなレバーを検証します。prompt-audit を適用するだけでなく、プロンプトキャッシュ、無人作業のバッチ処理、出力の上限設定によるコスト削減の方法もチェックします。評価を提供すれば、effort とモデル選択のトレードオフも計測します。

最後に、コストとパフォーマンスの反復的な探索には `/claude-api hillclimb` を使ってください。評価が与えられると、Claude はそれを訓練セットとテストセットに分割し、ベースラインのパフォーマンスを維持しながらコストを削減することを目指してアプリケーションへの更新を提案します。Claude は失敗した訓練ケースを読んで探索の指針とし、最終的な構成は保留にしておいたテストセットで採点されます。

詳しくは以下をご覧ください。

- ドキュメントは[こちら](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cut-spend-without-losing-quality)
- クックブックは[こちら](https://platform.claude.com/cookbook/cost-optimization-cost-optimization#prompt-caching)
