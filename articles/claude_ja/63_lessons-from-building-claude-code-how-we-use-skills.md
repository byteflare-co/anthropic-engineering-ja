---
date: '2026-06-03'
final_url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
number: 63
selector_used: main
slug: lessons-from-building-claude-code-how-we-use-skills
source_url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
title: 'Lessons from building Claude Code: How we use skills'
title_ja: "Claude Code を作って学んだこと: 私たちは skills をこう使っている"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# Claude Code を作って学んだこと: 私たちは skills をこう使っている

Skills は Claude Code でもっともよく使われる拡張ポイントのひとつになりました。柔軟で、作りやすく、配布しやすいからです。

しかし、この柔軟さゆえに、何がいちばんうまく機能するのかが見えにくくもなっています。どんなタイプの skill を作る価値があるのか。skill はどう構造化すればよいのか。他の人と共有すべきタイミングはいつなのか。

私たち Anthropic では Claude Code で skills を広範に使っており、現在も数百もの skill が稼働しています。本稿はそうした skills を開発の加速に活かすなかで学んだことをまとめたものです。

## skills とは何か

Skills は、指示・スクリプト・リソースを束ねたフォルダで、エージェントがそれを発見して使うことで、より正確で効率的に物事を進められるようにするものです。本稿は skills の基本に馴染みがある前提で書かれています。初めての方は、まず [Skilljar 上の Introduction to agent skills コース](https://anthropic.skilljar.com/introduction-to-agent-skills) から始めてください。

skills についてよくある誤解として、「単なる markdown ファイルでしょ」というものがあります。実際には skills はフォルダであり、スクリプト、アセット、データなどを含めることができ、エージェントはそれらを発見し、調べ、操作できます。

Claude Code では skills に対して [幅広い設定オプション](https://code.claude.com/docs/en/skills#frontmatter-reference) が用意されており、動的な hooks を登録することもできます。

私たちの経験では、Claude Code でもっとも効果的な skills は、これらの設定オプションとフォルダ構造を効果的に活用しています。

## skills の種類

Anthropic 社内のすべての skills をカタログ化してみたところ、それらは 9 つのカテゴリに整理できることに気づきました。最良の skills はそのうち 1 つにきれいに収まり、欲張りすぎている skills は複数のカテゴリをまたいでエージェントを混乱させてしまいます。これは決定版のリストというわけではありませんが、自分たちの skills ライブラリの抜けを見つけるためのフレームワークとして役立ちます。

![The Claude Code team categorized our internal skills and found that they could be bucketed into nine distinct categories.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f026439c_b7942952.png)

Claude Code チームは社内の skills を分類し、9 つの明確なカテゴリに振り分けられることを発見しました。

### **1. ライブラリと API リファレンス**

ライブラリや CLI、SDK の正しい使い方を説明する skills です。社内ライブラリ向けにも、Claude Code が時々苦手としがちな一般的なライブラリ向けにも作れます。こうした skills には、参考用コードスニペットのフォルダや、スクリプトを書く際に Claude が避けるべき落とし穴のリストが含まれることが多いです。

例:

- `billing-lib` — 社内の請求ライブラリ: エッジケース、落とし穴、その他もろもろ。
- `internal-platform-cli` — 社内 CLI ラッパーのすべてのサブコマンドと、それぞれをいつ使うかの例。
- `sandbox-proxy` — 開発作業向けの組織のエグレスゲートウェイ設定: どのホストに到達できるか、「connection refused」エラーをどうデバッグするか、許可リストにエントリを追加する方法。

### **2. プロダクト検証**

コードが正しく動いているかをテスト・検証する手順を記述した skills です。検証のために、playwright、tmux、その他の外部ツールと組み合わせて使われることが多いです。

検証用 skills は、社内で見るかぎり Claude の出力品質に対してもっとも測定可能なインパクトがありました。エンジニアが 1 週間まるごと費やして検証用 skills を磨き上げる価値があるほどです。

たとえば、Claude に出力を動画で記録させ何をテストしたかを正確に確認できるようにする、各ステップで状態に対するプログラム的なアサーションを強制する、といったテクニックを検討してみてください。これらはたいてい、さまざまなスクリプトを skill に含めることで実現します。

例:

- `signup-flow-driver` — ヘッドレスブラウザでサインアップ → メール認証 → オンボーディングを実行し、各ステップで状態をアサートするフックを備える
- `checkout-verifier` — Stripe テストカードでチェックアウト UI を動かし、請求が正しい状態で実際に着地することを検証する
- `tmux-cli-driver` — TTY が必要なインタラクティブな CLI の検証用

### **3. データ取得と分析**

データや監視スタックに接続する skills です。資格情報付きでデータを取得するためのライブラリ、特定のダッシュボード ID、よくあるワークフローやデータ取得方法の手順などを含むことがあります。

例:

- `funnel-query` — 「サインアップ → 活性化 → 課金 を見るにはどのイベントを join すればよいか」と、正規の user\_id が実際に入っているテーブル
- `cohort-compare` — 2 つのコホートの継続率やコンバージョン率を比較し、統計的に有意な差分をフラグ立てし、セグメント定義へのリンクを示す
- `grafana` — datasource UID、クラスタ名、問題 → ダッシュボードの引き当て表
- `datadog` — フィールドリファレンス (@request\_id と trace\_id)、サービス一覧、メトリクスのプレフィックス規約

### **4. 業務プロセスとチーム自動化**

繰り返しのワークフローを 1 コマンドに自動化する skills です。指示はわりとシンプルですが、他の skills や MCP に対してより複雑な依存を持つこともあります。こうした skills では、過去の結果をログファイルに保存しておくと、モデルが一貫性を保ちつつ、過去の実行を振り返るのに役立ちます。

例:

- `standup-post` — チケットトラッカー、GitHub アクティビティ、直前の Slack を集約し、差分のみのフォーマット済みスタンドアップにする
- `create-<ticket-system>-ticket` — スキーマ (有効な enum 値、必須フィールド) を強制し、作成後のワークフロー (レビュアーへの呼びかけ、Slack へのリンク投稿) も実施する
- `weekly-recap` — マージ済み PR、クローズ済みチケット、デプロイをまとめてフォーマット済みのリキャップ投稿にする

### **5. コードのスキャフォールディングとテンプレート**

コードベース内の特定の用途向けにフレームワークのボイラープレートを生成する skills です。組み合わせ可能なスクリプトと併用することもできます。スキャフォールディングが、純粋にコードでカバーできない自然言語の要件を含むときに特に有用です。

例:

- `new-<framework>-workflow` — 独自のアノテーション付きで新しいサービス/ワークフロー/ハンドラをスキャフォールドする
- `new-migration` — マイグレーションファイルのテンプレートとよくある落とし穴
- `create-app` — 認証、ロギング、デプロイ設定があらかじめ組み込まれた新しい社内アプリ

### **6. コード品質とレビュー**

組織内のコード品質を強制し、コードレビューを助ける skills です。堅牢性を最大化するために、決定論的なスクリプトやツールを含めることもできます。hooks の一部として、あるいは GitHub Action 内で自動的に走らせたい skills です。

- `adversarial-review` — 新鮮な目線のサブエージェントを起動して批評させ、修正を実装し、指摘が些末なものになるまで反復する
- `code-style` — コードスタイルを強制する。特に Claude がデフォルトでうまく扱えないスタイルに有効
- `testing-practices` — テストの書き方と何をテストすべきかの指示

### **7. CI/CD とデプロイ**

コードベース内でのコードの取得、プッシュ、デプロイを助ける skills です。データ収集のために他の skills を参照することもあります。

例:

- `babysit-pr` — PR を監視し、フレーキーな CI をリトライし、マージコンフリクトを解消し、自動マージを有効化する
- `deploy-<service>` — ビルド → スモークテスト → エラー率比較を伴う段階的なトラフィックロールアウト → リグレッション時の自動ロールバック
- `cherry-pick-prod` — 独立した worktree → cherry-pick → コンフリクト解消 → テンプレ付き PR

### **8. Runbooks**

症状 (Slack スレッド、アラート、エラーシグネチャなど) を起点に、複数のツールを使った調査を順に進め、構造化されたレポートを出す skills です。

例:

- `<service>-debugging` — もっともトラフィックの多いサービスについて、症状 → ツール → クエリパターンの対応関係をまとめたもの
- `oncall-runner` — アラートを取得し、定番の疑い箇所を確認し、所見をフォーマットする
- `log-correlator` — リクエスト ID を渡されると、そのリクエストに触れた可能性のあるすべてのシステムから合致するログを引いてくる

### **9. インフラ運用**

定型的なメンテナンスや運用手順を実行する skills です。ガードレールがあると助かる破壊的な操作を含むものもあります。クリティカルな運用の場面でエンジニアがベストプラクティスに沿いやすくなります。

例:

- `<resource>-orphans` — 孤児になった pod/volume を見つけて Slack に投稿し、待機期間を置き、ユーザーの確認を受けてから連鎖的にクリーンアップする
- `dependency-management` — 組織の依存パッケージ承認ワークフロー
- `cost-investigation` — 「なぜストレージ/egress 料金が跳ね上がったのか」を、対象のバケットやクエリパターンを指定して調査する

## skills を作るときのコツ

作るべき skill が決まったら、どう書けばよいでしょうか。ここからは、skills を作るうえでの Claude Code チームのベストプラクティスとコツ・ヒントを紹介します。

### 当たり前のことを書かない

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643a2_6f109d87.png)

Claude はすでにコーディングのやり方を知っており、あなたのコードベースも読めます。Claude がデフォルトでやることをそのまま書いた skill は、コンテキストを増やすだけで価値を足してくれません。知識を主目的にした skill を出すなら、Claude をその通常の思考パターンから押し出すような情報に集中してください。

[frontend design skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) はその好例です。Anthropic のエンジニアが顧客と反復しながら Claude のデザイン感覚を改善する形で作ったもので、Inter フォントや紫グラデといった定番パターンを避けるようになっています。

### 落とし穴セクションを育てる

どんな skill であっても、もっとも情報量の高い部分は Gotchas (落とし穴) セクションです。このセクションは、Claude がその skill を使うときによくぶつかる失敗ポイントを積み上げていく形で育てるべきです。理想的には、こうした落とし穴を捕まえるたびに skill を更新していきます。

たとえば:

「`subscriptions` テーブルは append-only です。欲しい行は `created_at` がもっとも新しい行ではなく、version がもっとも大きい行です。」「このフィールドは API gateway では `@request_id`、billing service では `trace_id` という名前ですが、同じ値です。」「Stripe webhook が実際には処理されていなくても、staging は 200 を返します。本当の状態は `payment_events` で確認してください。」

### ファイルシステムと段階的開示 (progressive disclosure) を使う

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f026439f_0e0f23c0.png)

SKILL.md ファイルは、特定の状況で Claude が参照できる別ファイルをいくつも指し示しています。たとえばジョブが pending なら stuck-jobs.md を参照する、といった具合です。

先にも触れたとおり、skill は単なる markdown ファイルではなくフォルダです。ファイルシステム全体を、コンテキストエンジニアリングと段階的開示の手段だと捉えてください。skill にどんなファイルがあるかを Claude に伝えておけば、Claude は適切なタイミングでそれを読んでくれます。

段階的開示のもっともシンプルな形は、Claude に使ってもらう別の markdown ファイルへのポインタを置くことです。たとえば、詳しい関数シグネチャや利用例を `references/api.md` に分けておくといった具合です。

別の例として、最終アウトプットが markdown ファイルなら、`assets/` の中にテンプレートファイルを置いてコピーして使えるようにすることもできます。

references、scripts、examples などのフォルダ群を持たせることで、Claude がより効果的に作業できるようになります。

### Claude をレールに乗せすぎない

Claude は基本的にあなたの指示を守ろうとしますし、skills は再利用性が高いので、指示を過度に具体的にしないよう注意したいところです。Claude が必要とする情報は与えつつ、状況に適応する余地を残してあげてください。

たとえば:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643ae_3c108f2c.png)

### セットアップをよく考える

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643a8_d5e89124.png)

上記の skill は、設定に Slack チャンネルが含まれていない場合にユーザーに尋ねるよう書かれています。

skill によっては、ユーザーからのコンテキストを使ったセットアップが必要になることがあります。たとえば、スタンドアップを Slack に投稿する skill を作るなら、どのチャンネルに投稿するかを Claude に尋ねさせたくなるかもしれません。

これを実現する良いパターンは、上の例のように skill ディレクトリ内の config.json にこうしたセットアップ情報を保存することです。設定が未セットアップなら、エージェントがユーザーに情報を尋ねればよいわけです。

エージェントに構造化された選択式の質問を出させたい場合は、AskUserQuestion ツールを使うよう Claude に指示できます。

### description は人間ではなくモデル向けに書く

Claude Code はセッション開始時に、利用可能なすべての skill とその description のリストを作ります。Claude はこのリストを見て「このリクエストに使える skill はあるか?」を判断します。つまり description フィールドは要約ではなく、いつこの skill をトリガーすべきかの記述だということです。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f0264399_a60f7943.png)

description には「babysit」のような、その skill のトリガーになりそうな語を含めておくと役に立ちます。

### Claude に記憶を持たせる

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643b1_9159a9b1.png)

このテキストログファイルは、「Sarah の認証 PR をレビューした」といった過去の出来事を Claude が思い出せるようにしてくれます。

skill の中にデータを保存しておくことで、ある種のメモリを持たせることもできます。append-only のテキストログや JSON ファイルといった単純なものでも、SQLite データベースのような複雑なものでも構いません。

たとえば `standup-post` skill は、書いた投稿をすべて standups.log に積んでおくことができます。次に走らせたとき、Claude が自分自身の履歴を読んで、昨日からの差分を把握できるようになります。

データを保存するための安定したディレクトリは、環境変数 `${CLAUDE_PLUGIN_DATA}` で取得できます。skills でのデータ永続化については、こちらを参照してください: <https://code.claude.com/docs/en/plugins-reference#persistent-data-directory>

### スクリプトを置き、コードを生成させる

Claude に与えられるツールのなかで、もっとも強力なものの 1 つがコードです。スクリプトやライブラリを Claude に持たせると、Claude はターンをボイラープレートの再構築ではなく、合成 — 次に何をするかを決めること — に使えるようになります。

たとえば `data-science` skill には、イベントソースからデータを取得する関数群のライブラリを入れておくことができます。複雑な分析を Claude にさせるために、次のようなヘルパー関数群を与えるイメージです:

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643ab_00319576.png)

すると Claude は、「火曜日に何があった?」のようなプロンプトに対して、この機能を組み合わせるスクリプトをその場で生成し、より高度な分析をこなせるようになります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1f3a763cec27e2f02643a5_32329bf3.png)

### オンデマンド hooks を使う

skills には、その skill が呼ばれたときにだけ有効化され、セッションの間だけ持続する hooks を含めることができます。常時動かしたくはないが、ときどき非常に役に立つような、より意見の強い hooks に向いた仕組みです。

たとえば:

- `/`**`careful`** — Bash の PreToolUse マッチャーで rm -rf、DROP TABLE、force-push、kubectl delete をブロックします。本番に触れているとわかっているときだけ使いたいタイプで、常にオンだと正気を失います。
- `/`**`freeze`** — 特定のディレクトリ外への Edit/Write をすべてブロックします。デバッグ中に「ログを追加したいだけなのに、つい無関係なコードを『修正』してしまう」のを防ぐのに有用です。

## skills を配布する

skills の最大の利点の 1 つは、チームの他のメンバーと共有できることです。

skills を他の人と共有する方法は 2 つあります:

- skills をリポジトリにチェックインする (`./.claude/skills` 配下)
- **plugin** にして、Claude Code Plugin marketplace でアップロード/インストールできるようにする (詳細は [こちらのドキュメント](https://code.claude.com/docs/en/plugin-marketplaces) を参照)

比較的少数のリポジトリで作業する小規模チームには、skills をリポジトリにチェックインする方法がよく合います。とはいえ、チェックインされた skill はモデルのコンテキストをわずかに増やします。スケールに伴って、社内の plugin marketplace を用意すれば、skills を配布しつつ、どれをインストールするかをチームに委ね、セットアップフローも組み込めるようになります。

## skills marketplace を運営する

どの skills を marketplace に入れるかは、どう決めるのでしょうか。提出のしかたはどうするのでしょうか。

Anthropic では、決定する中央集権的なチームはありません。代わりに、もっとも有用な skills を有機的に見つけようとしています。試してほしい skill を持っている人は、GitHub のサンドボックスフォルダにアップロードして、Slack やほかのフォーラムで誰かに案内します。

skill がある程度の支持を得たら (どのくらいかは skill のオーナーが判断します)、それを marketplace に移す PR を送ります。

## skills を合成する

互いに依存する skills を持ちたくなることもあるでしょう。たとえば、ファイルアップロード skill と、CSV を作ってアップロードする CSV 生成 skill といった具合です。この種の依存関係管理は、marketplace や skills にネイティブに組み込まれているわけではありませんが、他の skills を名前で参照しておけば、それがインストールされていればモデルが呼び出してくれます。

## skills を計測する

skill の状況を把握するために、私たちは社内で skill 使用をロギングする PreToolUse hook を使っています ([サンプルコードはこちら](https://gist.github.com/ThariqS/24defad423d701746e23dc19aace4de5))。これにより、人気のある skill や、期待に対して発火しすぎていない skill を見つけられます。

## 始めてみよう

skills のベストプラクティスは現在も進化の途中にあります。私たちの良い skills の多くは、最初は数行と落とし穴がひとつあるだけのものから始まり、Claude が新しいエッジケースに当たるたびに人が書き足していくことで良くなってきました。

skills を理解するための一番の方法は、まず始めてみて、実験し、自分にとって何がうまくいくかを見ることです。

- [skills のドキュメント](https://code.claude.com/docs/en/skills) を見てみる
- [カスタマイズ用のサンプル skills を探す](https://github.com/anthropics/skills)

*本記事は、Claude Code に取り組んでいる Anthropic の technical staff の一員、Thariq Shihipar によって執筆されました。*
