---
date: '2026-06-18'
final_url: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
number: 74
selector_used: main
slug: steering-claude-code-skills-hooks-rules-subagents-and-more
source_url: https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more
title: 'Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and
  more'
title_ja: "Claude Code を操る: CLAUDE.md ファイル、skills、hooks、rules、subagents など"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

# Claude Code を操る: CLAUDE.md ファイル、skills、hooks、rules、subagents など

Claude はあなたの働き方に寄り添うように作られており、Claude Code ではそれをカスタマイズできます。

Claude の振る舞いに指示を与える方法は 7 つあります。CLAUDE.md ファイル、rules、[**skills**](https://code.claude.com/docs/en/skills)、[**subagents**](https://code.claude.com/docs/en/sub-agents)、[**hooks**](https://code.claude.com/docs/en/hooks-guide)、output styles、そしてシステムプロンプトへの追記です。

それぞれの方法が制御するのは次の点です。

- 指示がいつコンテキストに読み込まれるか
- 長いセッションでも持続するかどうか (compaction 時の挙動)
- どれだけの強制力を持つか

以下の表は各方法の主な違いをざっくりまとめたものです。本稿ではさらに詳細を解説し、各 Claude の指示をどこに置くべきかの判断フレームワークも示します。

| 方法 | 読み込まれるタイミング | Compaction 時の挙動 | コンテキストコスト | 使うべき場面 |
| --- | --- | --- | --- | --- |
| CLAUDE.md (ルート) | セッション開始時に読み込まれ、セッション中はコンテキストに残り続ける | メモ化される。一度読まれてセッション中はキャッシュされる。compaction 後はキャッシュがクリアされ再読み込みされる | 高い。関連の有無にかかわらず、すべての行がトークンを消費する | ビルドコマンド、ディレクトリ構成、モノレポ構造、コーディング規約、チームの規範 |
| CLAUDE.md (サブディレクトリ) | オンデマンド。Claude がそのサブディレクトリ配下のファイルを読んだとき | そのサブディレクトリに再び触れるまで失われる | 低い。関連するサブディレクトリで作業しているときだけコンテキストを消費する | サブディレクトリ固有の規約 |
| Rules | セッション開始時 (ユーザーレベルの rule)、または該当ファイルに触れたときのみ (path-scoped) | compaction 時に再注入される | 中程度。path-scoped でない限り常時オン | 特定の制約や規約 (例: すべての API ハンドラは Zod で入力を検証すること) |
| Skills | name と description はセッション開始時に読み込まれ、本文は skill が呼び出されたときに読み込まれる | 呼び出し済み skill は共有予算の範囲で再注入され、古いものから先に削除される | 低い。本文は呼び出されたときだけ読み込まれ、呼び出し済み skill 全体で共有トークン予算がある | 手順を伴うワークフロー (デプロイやリリースのチェックリスト) |
| Subagents | name、description、ツール一覧はセッション開始時に読み込まれ、本文は Agent ツール経由で呼び出されたときだけ読み込まれる | 最終メッセージ (要約とメタデータ) のみがメインセッションに返る | 低い。呼び出されるまではメインコンテキストでのコストはゼロ。独自の隔離されたコンテキストウィンドウで動く | 並列実行する作業や、隔離して走らせ要約だけを返したいサイドタスク (深掘り調査、ログ解析、依存関係の監査) |
| Hooks | ライフサイクルイベントで発火 | compaction を完全にバイパスする | 低い。設定はメインコンテキストの外にあり、一部の出力 (例: ブロッキングエラー) のみが返ることがある | 決定論的な自動化: 編集後の linter 実行、完了時の Slack への投稿、コマンドのブロック、PreCompact 時のチャット履歴のバックアップ |
| Output styles | セッション開始時にシステムプロンプトへ注入される | compaction されない | 高い。コンテキストウィンドウを占めるが、デフォルトのシステムプロンプトを上書きする | 役割の大きな変更 (コーディングアシスタントから汎用アシスタントへ) |
| システムプロンプトへの追記 | セッション開始時に CLI フラグとして渡される | compaction されず、その起動にのみ適用される | 中程度。セッション内の最初のリクエスト以降はキャッシュされる | トーン、応答の長さ、フォーマットの好み |

## 指示を届ける 7 つの方法

### CLAUDE.md ファイル

CLAUDE.md はプロジェクトのルートに置かれる markdown ファイルです。セッション開始時にコンテキストへ読み込まれ、セッション中ずっとそこに居続けます。

ビルドコマンド、ディレクトリ構成、モノレポ構造、コーディング規約、チームの規範など、いずれもここに自然に収まります。

種類は 2 つあり、読み込まれ方が異なります。

- **常に読み込まれる**: 1 つ目は、ルートにある CLAUDE.md ファイルで、共有リポジトリにコミットされたものや、プロジェクト固有の個人的な設定としてローカルに保存したものです。これらはすべてセッション開始時に読み込まれ、長いセッションでも失われたり劣化したりしません。Claude Code が会話を compaction するときには、これらのファイルを再読み込みします。
- **オンデマンド:** セッションを起動したフォルダの下のサブディレクトリにある CLAUDE.md ファイルです。たとえば `app/api/CLAUDE.md` はセッション開始時ではなく、Claude が `app/api` 配下のファイルを読んだときに読み込まれます。compaction 時の挙動は path-scoped な rule と同じで、そのサブディレクトリに再び触れるまで消えています。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a340f852d1f938ab8675599_65a737a9.png)

cwd 配下のサブディレクトリ CLAUDE.md ファイルは、Claude がそのディレクトリ内のファイルを読んだときに読み込まれます。

共有リポジトリでは、CLAUDE.md は誰のものでもない設定ファイルがそうであるように肥大化していきます。各チームが自分たちの指示を書き足していき、削除されることはほぼありません。スケールするにつれて、そのコストは積み上がっていきます。

リポジトリで作業するすべてのエンジニアのすべてのセッションに、関係があるかどうかに関わらず、すべての行が読み込まれます。これはトークンを消費するうえに、本当に大事な指示への準拠を薄めてしまいます。ファイルが大きくなってきたら、チーム固有の規約は path-scoped な rule へ、手順は skill へ追い出しましょう。これらは関連するときだけ読み込まれます。

**Tip:** CLAUDE.md は 200 行未満に抑え、オーナーを決め、コードと同じようにレビューしてください。このファイルは Claude にコードベースの概要を渡すもの、あるいは Claude が必要なときにもっと詳しい情報を見つけにいけるよう、他のファイルへの索引として捉えるのがよいでしょう。

モノレポでは、各チームのディレクトリに専用のサブディレクトリ CLAUDE.md を置きましょう。そうすれば、チームは自分たちの規約だけを読み込むことができ、開発者は触れることのない他チームのコードについては `claudeMdExcludes` 設定でスキップできます。

組織内のすべてのリポジトリに適用すべき標準 (セキュリティポリシー、コンプライアンス要件など) には、中央管理された CLAUDE.md を用意し、MDM や構成管理を通じて開発者マシンに配布できます。これは個別の設定で除外することができません。

CLAUDE.md のセットアップについては、ブログ記事 [CLAUDE.md files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) を参照してください。

スコープのない rule は CLAUDE.md と同じように、常にセッション開始時に読み込まれ、compaction 時に再注入されます。これはタスクに関係なくコンテキストを読み込むため、トークンを浪費しがちです。

Path-scoped な rule は、`paths` フィールドを追加して読み込まれるタイミングを制御することで、指示が関連するときだけ読み込むことを可能にします。

たとえば、`src/api/**` にスコープした rule はドキュメントだけのセッションではコンテキストに入りません。Claude が `src/api/` ディレクトリ内のファイルを読んだときにだけ読み込まれます。

書き方は次のとおりです。

```
---
paths:
  - "src/api/**"
  - "**/*.handler.ts"
---
All API handlers must validate input with Zod before processing.
```

**Tip**: 「マイグレーションは append-only」のようなファイル固有の制約は、**rule** として `paths:` の frontmatter に置くのが最適です。コードベースの (すべてではなく) 複数の箇所に現れる横断的な関心事やファイルに関する指示なら、ネストした CLAUDE.md ではなく path-scoped な rule を選びましょう。

### Skills

[**Skills**](https://code.claude.com/docs/en/skills) は `.claude/skills/` 配下に置かれた、指示・スクリプト・リソースのフォルダで、Claude が動的に読み込みます。各 skill には `SKILL.md` ファイルがあり、name、description、本文を持ちます。

セッション開始時に読み込まれるのは name と description のみで、本文は Claude がその skill を呼び出したとき (slash コマンド `/code-review` などの明示的な呼び出し、またはタスクへの自動マッチ) に読み込まれます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a340f852d1f938ab867559f_2199ed03.png)

Skills はシステムプロンプト経由でトリガーされます。

たとえば `/code-review` はビルトインの skill で、現在の diff をレビューし、ファイルを編集することなく指摘を報告します。skill が手順書を定義しているため、Claude は呼び出されるたびに同じ構造化されたアプローチをたどります。

Compaction 時、Claude Code は呼び出し済みの skill を共有予算の範囲で再注入します。セッション中に多くの skill を呼び出していた場合、もっとも古いものから順に落ちていきます。

**Tip:** デプロイのワークフロー、リリースチェックリスト、レビュープロセスのような手順的な指示は、CLAUDE.md ではなく skill に置くべきです。

Claude Code には組み込みの skill が付属していますが、自分でカスタム skill を書くこともできます。[Claude 向けの skill を作るための完全ガイド](https://claude.com/blog/complete-guide-to-building-skills-for-claude) で書き方を解説しています。

### Subagents

[**Subagents**](https://code.claude.com/docs/en/sub-agents) は `.claude/agents/` に置かれる markdown ファイルで、特定のサイドタスク向けの隔離されたアシスタントを定義します。各ファイルは YAML frontmatter (name、description、加えてモデルやツールアクセスを指定するオプションフィールド) と、その subagent のシステムプロンプトとなる本文で構成されます。

Subagents は skills と似ていて、name、description、ツール一覧がセッション開始時に読み込まれますが、subagent の本文に含まれるより大きなコンテキストは自動では呼び出されません。Claude は Agent ツールを通じて、プロンプト文字列を渡しながら呼び出します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a340f852d1f938ab86755a2_914c1942.png)

Claude Code のコンテキストウィンドウは、Claude がセッションについて知っているすべてを保持します。[こちらのインタラクティブなタイムライン](https://code.claude.com/docs/en/context-window) で、何がいつ読み込まれるかが分かります。

Subagent 本文内の大きな指示用コンテキストは自動呼び出しされないだけでなく、親会話に入り込むこともまったくありません。

そして subagent は自分専用の真新しいコンテキストウィンドウで実行され、メインセッションに返ってくるのは subagent の最終メッセージ (多くの場合、多数のサブタスクの集約結果) とメタデータだけです。

このパターンはスケールします。Subagent は 5 階層までネストでき、[dynamic workflows](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) は subagent アーキテクチャの各細部を指定しなくても、数十から数百のバックグラウンドエージェントをオーケストレーションします。オーケストレーション計画と中間結果は Claude のコンテキストウィンドウではなくスクリプト変数の中に存在するため、指示の忠実度を失うことなくスケールできます。

**Tip:** この隔離こそが、skill ではなく subagent を選ぶ主な理由の 1 つです。深掘り調査、ログ解析パス、依存関係監査など、後で参照しない中間結果でメインの会話が散らかってしまうサイドタスクには subagent を使いましょう。ステップごとに見ながらステアリングしたいなら、メインスレッド内で手順を展開させる skill を使いましょう。

### Hooks

[**Hooks**](https://code.claude.com/docs/en/hooks-guide) は、ユーザー定義のコマンド、HTTP エンドポイント、または LLM プロンプトです。ファイル編集、ツール呼び出し、セッション開始など [Claude のライフサイクル上の特定のイベント](https://code.claude.com/docs/en/hooks#hook-lifecycle) で発火することで、Claude の振る舞いに対してより決定論的な制御を提供します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a340f852d1f938ab867559c_e782277c.png)

Claude Code セッションで hook が発火しうるイベントのマップ。

Hooks は `settings.json`、管理ポリシー設定、または skill/agent の frontmatter に登録します。

Hook の種類は複数あります。command、HTTP、mcp\_tool、prompt、agent です。すべての hook は決定論的にトリガーされます。最初の 3 つは決定論的に実行され、後の 2 つ (prompt と agent) は固定のルールではなく Claude の判断を用いて出力を決めます。

Hooks は設定や指示がメインのコンテキストウィンドウの外側に存在するため、コンテキストコストが低いです。ハーネスはハンドラ (command、http、mcp\_tool) を実行するか、別のウィンドウでモデル呼び出し (prompt、agent) を行います。

Hook によっては、出力をメインのコンテキストウィンドウに保存するものもあります。たとえば、ブロッキング hook の標準エラーはコンテキスト内に保存され、Claude が呼び出しが拒否された理由を理解できるようにします。

しかし、ほとんどの hook は、設定で明示的に返さない限り、出力をメインウィンドウに保存しません。`PreCompact` イベントを使って compaction 前にチャット履歴を別ファイルにバックアップしていても、どのファイルにチャット履歴が保存されたかを Claude は知ることができません。

これは hook を CLAUDE.md、rules、skills とは根本的に異なるものにしています。詳しくは [**hooks の設定方法**](https://claude.com/blog/how-to-configure-hooks) を参照してください。

**Tip:** 決定論的に起こるべきことには hook を使いましょう。編集後の linter 実行、完了時の Slack への投稿、特定のコマンドを実行前にブロックするといった用途です。`PreToolUse` hook は任意のツール呼び出しを検査し、exit code 2 で拒否できます。

Hooks は Claude に読み込ませる指示ではなく、ハーネスが実行するコードであるため、コンテキストコストが低くなります。

### Output styles

[**Output styles**](https://code.claude.com/docs/en/output-styles) は `.claude/output-styles/` に置かれるファイルで、システムプロンプトに指示を注入します。compaction されず、毎セッション開始時に読み込まれ、セッション内の最初のリクエスト以降はキャッシュされるため、コンテキストコストは中程度です。

システムプロンプト内に置かれるため、output styles はこれまで紹介してきたどの方法よりも指示への追従重みが高く、慎重に使うべきです。

**Output style を変更するとデフォルトの output style は置き換えられます** (style の frontmatter に `keep-coding-instructions: true` を設定しない限り)。

Claude Code では、これは Claude にソフトウェアエンジニアリングのタスクを助けていると伝える指示や、その他の重要なデフォルト指示を取り除いてしまいます。たとえば次のような指示です。

- 変更のスコープをどう絞るか
- いつコメントを追加し、いつ省くか
- セキュリティ上の懸念をどう扱うか
- 作業完了を宣言する前にテストを実行するなどの検証習慣

デフォルトでは、カスタム output style はこれらをすべて落とし、Claude Code はソフトウェアエンジニアリングのアシスタントというよりも汎用アシスタントに近くなります。

**Tip**: カスタム output style を書く前に、組み込みの style を確認してください。**Proactive**、**Explanatory**、**Learning** は、style ファイルを自分でメンテナンスしなくても、もっとも一般的なニーズ (自律性、教えるモード、協調コーディング) をカバーします。

### システムプロンプトへの追記

Output style の変更に代わる方法として、`append-system-prompt` フラグがあります。output style ファイルを変更すると Claude の振る舞いに大きく意図しない変更が起こり得るのに対し、append フラグは元のシステムプロンプトに追加するだけです。Claude の役割を変更するのではなく、デフォルトの役割に指示を加えるだけです。

また、起動時に渡され、その起動にだけ適用され、ファイルとしてセッションをまたいで永続化されることはありません。

システムプロンプトへの追記は、他の指示の渡し方と比べてコンテキストコストが高くなる可能性があります。入力トークンが増えますが、セッション内の最初のリクエスト以降はプロンプトキャッシュによってこのコストは軽減されます。Claude により詳細で長いスタイルを使うよう指示すると、出力トークンも増えます。

**Tip:** システムプロンプトへの追記は、特定のコーディング標準、出力フォーマット、ドメイン固有の知識を追加するのに最適です。追記には追従への逓減効果がある点に留意してください。一般的に、この方法でより多くの指示を与えるほど、Claude はそれらを厳密には守らなくなります。特に互いに矛盾する場合にそうなります。

## Claude Code カスタマイズのクイック Tips

以下のようなことをしていたら、別の場所への指示の配置を検討するとよいでしょう。

**CLAUDE.md に「毎回 X したら、必ず Y する」と書いている。** すべての編集の後に prettier を走らせる、完了時に Slack に投稿するなど、確実に行われるべき振る舞いであれば、代わりに `settings.json` の hook を使いましょう。モデルがフォーマッタを実行するかどうかを判断するのと、フォーマッタが自動で実行されるのとは別物です。

**CLAUDE.md に「絶対にこれをするな」と書いている。** 絶対に起こってはならないことがあるとき、指示は適切な道具ではありません。Claude はほとんどの場合指示に従いますが、長いセッションや曖昧な状況、あるいはタスクの一環としてアクセスしたファイル内のプロンプトインジェクションといったプレッシャーのもとでは、指示で書かれたルールに従えないことがあります。本当のガードレールは決定論的でなければならず、その強制手段は [hooks](https://code.claude.com/docs/en/hooks) と [permissions](https://code.claude.com/docs/en/permissions) です。`PreToolUse` hook は呼び出しを検査して exit code 2 でブロックできます。[**Managed settings**](https://code.claude.com/docs/en/settings#managed-settings) はさらに踏み込んだものです。これは管理者によって配布され、ユーザーのローカル設定で上書きすることができず、組織全体で決定論的なガードレールを強制する唯一の手段です。

**CLAUDE.md に 30 行の手順を書いている。** 手順は skill に置くべきです。CLAUDE.md は、ビルドコマンド、モノレポのレイアウト、チーム規約のような、Claude が常に持っておくべき事実のためのものです。デプロイの runbook やセキュリティレビューのチェックリストは `.claude/skills/` に置き、呼び出されたときだけ本文が読み込まれるようにしましょう。

**paths のない API 固有の rule。** Rule が `src/api/**` にだけ適用されるなら、`paths:` でスコープしておけば無関係な作業中にコンテキストから外しておけます。スコープのない rule は、その内容を CLAUDE.md に置くのと機械的に同じで、常に読み込まれ、常にトークンを消費します。

**個人的な好みをプロジェクトレベルの CLAUDE.md に書く。** すべてのファイルベースの方法には、どのリポジトリでの Claude Code セッションでも読み込まれるユーザーレベルのカウンターパートがあります。個人的な好み (semantic commit メッセージを必ず使う、など) はローカルファイルに置きましょう。プロジェクトレベルのファイルは、チーム全体に共通だが特定のコードベースに固有の好みのために確保してください。

## はじめに

環境の設定から並列セッションへのスケールまで、Claude Code を最大限に活用するための Tips とパターンは [best practices for Claude Code](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md) のドキュメントにまとめられています。

これらをいくつか動かせるようになったら、その多く (skills、subagents、hooks、output styles) を [plugin](https://code.claude.com/docs/en/plugins) としてバンドルし、まとまった構成をチームメイトやプロジェクト間で共有できます。
