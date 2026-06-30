---
date: '2026-06-30'
final_url: https://claude.com/blog/getting-started-with-loops
number: 82
selector_used: main
slug: getting-started-with-loops
source_url: https://claude.com/blog/getting-started-with-loops
title: Getting started with loops
title_ja: "ループを使い始める"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229e73ca2d0d73d78f7_682ac293884c9d4ee4ebe2355a2f6c4ecfdd9c1b-1000x1000.svg)

# ループを使い始める

最近、コーディングエージェントへのプロンプトを書く代わりに「ループを設計する」ことについて、多くの議論が交わされています。X (Twitter) で実際にループとは何なのかを突き止めようとすると、いくつもの異なる答えに出くわすはずです。

Claude Code チームでは、**ループとは、停止条件が満たされるまでエージェントが作業のサイクルを繰り返すこと** と定義しています。私たちは以下の観点でループをいくつかのタイプに分類しています。

- どのようにトリガーされるか
- どのように停止するか
- どの Claude Code のプリミティブを使うか
- どんなタスクに最も向いているか

本稿では主なループのタイプ、それぞれをいつ使うべきか、そしてコード品質を保ちつつトークン使用量を管理する方法を解説します。すべてのタスクに複雑なループが必要なわけではありません。まずは最もシンプルな解決策から始め、これらのパターンは選択的に使ってください。

## **ターンベースのループ**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d98c_8ace2295.png)

- **トリガー**: ユーザーのプロンプト。
- **停止条件**: Claude がタスクを完了した、あるいは追加のコンテキストが必要だと判断したとき。
- **向いている用途**: 定期的なプロセスやスケジュールに組み込まれていない、短めのタスク。
- **使用量の管理方法**: 具体的なプロンプトを書き、skill を使って検証を改善することでターン数を減らす。

あなたが送るすべてのプロンプトは、各ターンをあなたが指示する手動のループを開始します。Claude はコンテキストを収集し、アクションを実行し、自分の作業をチェックし、必要なら繰り返し、応答を返します。私たちはこれを「エージェントループ」と呼んでいます。

たとえば Claude に「いいねボタンを作って」と頼んでみてください。Claude はあなたのコードを読み、編集を加え、テストを実行し、自分が *動くと信じている* ものを返してきます。あなたはそれから手動で作業を確認し、次のプロンプトを書きます。

検証のステップを改善するには、あなたが手動で行っている手順を `SKILL.md` としてエンコードしておけば、Claude が自分の作業をエンドツーエンドでより多くチェックできるようになります。ここには、Claude が結果を *見たり*、*計測したり*、*操作したり* するためのツールやコネクタも含めるべきです。チェックが定量的であればあるほど、Claude が自己検証しやすくなります。

たとえば、`SKILL.md` ファイルに次のように指定できます。

```
---
name: verify-frontend-change
description: Verify any UI change end-to-end before declaring it done.
---

# Verifying frontend changes
Never report a UI change as complete based on a successful edit alone. Verify it the way a human reviewer would:

1. Start the dev server and open the edited page in the browser.

2. Interact with the change directly. For a new control (button, input, toggle): click it, confirm the expected state change, and screenshot before/after.

3. Check the browser console: zero new errors or warnings.

4. Use the Chrome Devtools MCP, run a performance trace and audit Core Web Vitals.

If any step fails, fix the issue and rerun from step 1 — do not hand back partially verified work.
```

## **ゴールベースのループ (/goal)**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d98f_c6fa9ae5.png)

- **トリガー**: リアルタイムの手動プロンプト。
- **停止条件**: ゴールが達成される、または上限ターン数に達する。
- **向いている用途**: 検証可能な終了条件があるタスク。
- **使用量の管理方法**: 完了条件を具体的に設定し、ターン数の上限を明示する (例: 「5 回試したら止める」)。

ときに 1 ターンでは不十分なことがあります。特に複雑なタスクではそうです。エージェントは反復できるとパフォーマンスがよくなります。`/goal` で「完了」とは何かを定義することで、Claude が反復する時間を延ばすことができます。

成功条件を定義しておくと、Claude は「十分よい」かどうかを自分で判断してループを早めに終わらせる必要がなくなります。Claude が止まろうとするたびに、評価モデルがあなたの条件をチェックし、ゴールが達成されるか、指定したターン数に達するまで Claude を作業に戻します。

これこそ、合格したテストの数や一定のスコア閾値の突破といった、決定論的な条件が非常に効果的である理由です。

たとえば次のように書きます。

```
/goal get the homepage Lighthouse score to 90 or above, stop after 5 tries.
```

## **時間ベースのループ (/loop と /schedule)**

- **トリガー**: 指定した時間間隔。
- **停止条件**: あなたがキャンセルする、または作業が完了する (PR がマージされる、キューが空になる、など)。
- **向いている用途**: 定期的な作業、または外部の環境やシステムとのインタフェース。
- **使用量の管理方法**: 間隔を長くする、または時間ではなくイベントに反応させる。

エージェント的な作業の中には、定期的なものもあります。タスクは同じで、入力だけが変わるパターンです。たとえば毎朝 Slack のメッセージを要約するようなものです。一方、外部システムに依存する作業もあり、それと連携する簡単な方法は、一定間隔でチェックして変化に反応することです。たとえば、コードレビューが付くかもしれない PR や、CI が失敗するかもしれない PR を見張るような場合です。

このようなケースでは、`/loop` を使って一定間隔でプロンプトを再実行することで、Claude が走るタイミングを制御できます。たとえば次のようにします。

```
/loop 5m check my PR, address review comments, and fix failing CI
```

`/loop` はあなたのコンピュータ上で動くので、コンピュータをオフにすれば止まります。クラウドにループを移したい場合は、`/schedule` でルーチンを作成すればよいです。

## **プロアクティブなループ**

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a43eb603762e725a739d989_eb9e496a.png)

- **トリガー**: イベント、またはスケジュール。リアルタイムには人間が関与しない。
- **停止条件**: 個々のタスクはゴールが達成されたときに終了する。ルーチン自体はあなたがオフにするまで動き続ける。
- **向いている用途**: 定義のはっきりした、繰り返し発生する作業のストリーム: バグレポート、issue のトリアージ、マイグレーション、依存関係のアップグレードなど。
- **使用量の管理方法**: ルーチンはより小さく速いモデルへルーティングし、判断が必要なところだけ最も能力の高いモデルを使う。

上で挙げたプリミティブは、Claude Code の他の機能 — **auto mode** や **動的ワークフロー (dynamic workflows)** (research preview) — と組み合わせて、長時間走り続けるループを構成できます。

たとえば、受信するフィードバックを処理するには次のように組み立てられます。

1. **`/schedule`** (research preview) で、新しいレポートをチェックするルーチンを実行する
2. **`/goal`** で完了の定義を、**skills** で検証方法を文書化する
3. **動的ワークフロー (Dynamic workflows)** で、各レポートをトリアージし、修正し、修正をレビューするエージェント群をオーケストレーションする
4. **Auto mode** で、許可を求めて止まらずにルーチンが動くようにする

これらをまとめると、プロンプトはたとえば次のようになります。

```
/schedule every hour: check #project-feedback for bug reports. /goal: don't stop until every report found this run is triaged, actioned, and responded to. When fixing a bug, use a workflow to explore three solutions in parallel worktrees and have a judge adversarially review them.
```

## **コード品質を保つ**

ループの出力の品質は、その周囲のシステムに左右されます。システムを設計するときは次の点を意識しましょう。

- **コードベース自体をきれいに保つ**: Claude はコードベースに既に存在するパターンや規約に従います。
- **Claude が自分の作業を検証する手段を与える**: あなたとあなたのチームにとって「良い」とは何かを [skills](https://code.claude.com/docs/en/skills) でエンコードしましょう。
- **ドキュメントへのアクセスを容易にする**: フレームワークやライブラリのドキュメントには、最新のベストプラクティスがあります。
- **コードレビューには別のエージェントを使う**: 新鮮なコンテキストを持つレビュアーはバイアスが少なく、メインエージェントの推論に影響されません。組み込みの `/code-review` skill を使うか、GitHub 向けに [Code Review](https://code.claude.com/docs/en/code-review) を利用できます。

個々の結果が基準を満たさないとき、その問題を直すだけで止めないでください。それを今後すべての反復のためにシステムへエンコードするよう試みましょう。

## **トークン使用量を管理する**

トークン使用量を管理するために、ループには明確な境界を持たせるべきです。

- **適切なプリミティブとモデルをジョブに合わせて選ぶ**: 小さなタスクに複数のエージェントやループは要りません。タスクによっては、より安く速いモデルでも問題ありません。
- **明確な成功条件と停止条件を定義する**: 完了とは何かを具体的にすることで、Claude が解にたどり着くのが早くなります (ただし早すぎないように)。
- **大規模実行の前にパイロット実行する**: 動的ワークフローは数百のエージェントを起動できます。まずは小さなスライスで使用量を見積もりましょう。
- **決定論的な作業にはスクリプトを使う**: スクリプトを実行するほうが、ステップを推論するより安く済みます。たとえば PDF skill では、毎回コードを再導出するのではなく、Claude が毎回実行するフォーム入力スクリプトを同梱できます。
- **必要以上にルーチンを頻繁に実行しない**: 監視している対象が変化する頻度に間隔を合わせましょう。
- **使用状況をレビューする**: `/usage` コマンドは直近の使用量を skill・subagent・MCP ごとに分解して表示します。`/goal` を引数なしで実行すると、これまでのターン数とトークン使用量が見られます。`/workflows` では各エージェントのトークン使用量を表示でき、いつでもエージェントを停止できます。

## **使い始める**

まとめると次のようになります。

| ループ | 引き渡すもの | 使うべき場面 | 手に取るもの |
| --- | --- | --- | --- |
| ターンベース | チェック | 探索や意思決定をしているとき | カスタム検証 skill |
| ゴールベース | 停止条件 | 完了の姿が分かっているとき | `/goal` |
| 時間ベース | トリガー | 作業がプロジェクトの外でスケジュールに沿って発生するとき | `/loop`、`/schedule` |
| プロアクティブ | プロンプト | 作業が定期的で、定義がはっきりしているとき | 上記すべてに加えて動的ワークフロー |

ループを使い始めるには、まずあなたが既に行っている作業を見渡してみてください。あなたがボトルネックになっているタスクを 1 つ選び、どの部分を引き渡せるかを問いかけてみましょう。検証チェックを書けるか? ゴールは十分に明確か? その作業はスケジュールに沿って到来するか?

アイデアが固まったら、ループを走らせ、どこで詰まり、どこで行き過ぎたかといった結果を観察し、ためらわずに反復してください。

詳しくは、Claude Code の [並列にエージェントを動かす](https://code.claude.com/docs/en/agents) ドキュメントと、[loop](https://code.claude.com/docs/en/goal)、[schedule](https://code.claude.com/docs/en/routines)、[goal](https://code.claude.com/docs/en/goal)、[動的ワークフロー](https://code.claude.com/docs/en/workflows#orchestrate-subagents-at-scale-with-dynamic-workflows) の各ページをご覧ください。

*この記事は Delba de Oliveira と Michael Segner によって書かれました*
