---
date: '2026-07-22'
final_url: https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
number: 98
selector_used: main
slug: building-verification-loops-in-claude-code-with-skills
source_url: https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
title: Building verification loops in Claude Code with skills
title_ja: "Claude Code で skills を使って検証ループを構築する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224d39f9b8e905d1823_b68cbb43d7c8f56f0b14cc867e8d4d74445f78b0-1000x1000.svg)

# Claude Code で skills を使って検証ループを構築する

ほとんどの[エージェント型コーディング](https://claude.com/blog/introduction-to-agentic-coding)セッションは、あるループに従います。変更を依頼すると、Claude がコンテキストを集め、行動を起こし、結果を検証し、必要であればコンテキスト収集に戻る、というものです。

検証とは、エージェントが応答する前に自分の作業を確認する仕組みです。Claude はすでに、型チェッカー、リンター、テスト、ランタイムエラーといったコードベース内の決定論的なシグナルを観察することで、この一部を行っています。Claude が推測できないものは、あなたが手作業で機能を確認するステップとして残ります。

しかし、こうした手作業のステップは検証ループへと変換できます。[Claude Code](https://claude.com/product/claude-code) における検証ループとは、Claude が作業を確認し、修正を試みる反復的なプロセスのことです。

![diagram of the agentic loop: 1. gathering context, 2. taking action, 3. verifying results.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a60f2068656db3211c097af_5b4284f8.png)

*エージェント型ループ: 1. コンテキストの収集、2. 行動、3. 結果の検証。*

本稿では、もっとも一般的な検証ループの種類を取り上げ、Anthropic 社内で実際に使っているものを紹介します。そのうえで、あなたがすでに行っている手作業の確認を skills としてエンコードし、Claude が自ら自分自身のフィードバックループを閉じられるようにする方法を示します。これにより、Claude が反復している間に、あなたは別の作業に取りかかれるようになります。

## 組み込みの検証ループ

独自の検証ループを設計する前に、Claude にすでに組み込まれているさまざまな検証ループのサポートを理解しておくと役立ちます。よく使われる機能やアプローチには次のようなものがあります。

- **/verify skill**: アプリケーションをビルドし、実行し、変更を観察します。
- **ツールチェーン**: Claude は、リンターなど提供されたあらゆるツールから得られるエラーコードや警告を捕捉し、それに対応しようとします。正確なビルドコマンドやテストコマンドを CLAUDE.md に書いておくのがよい方法です。そうすれば Claude がそれを推測する必要がなくなります。
- **Code Review (研究プレビュー)**: 有効化したリポジトリの PR に対して自動レビューパスを実行する、マネージド型のマルチエージェントサービスです。指摘事項を手作業で修正してプッシュすることも、(下記の GitHub Actions をすでに設定済みであれば) 指摘に対して @claude とコメントしてループを閉じることもできます。
- **GitHub Actions**: 検証用の skill で Claude を呼び出すジョブを定義すれば、プッシュや PR のたびに、あなたがローカルで実行しているのと同じチェックが走ります。
- **仕様検証**: リポジトリ内の markdown 仕様に対して各変更を検証し、違反があれば修正しようとする skill です。
- **Claude Managed Agents (ベータ版) のルーブリック**: 別のグレーダーエージェントを使ってルーブリックに対する成果を検証できる、マネージド型のエージェントサービスです。失敗した場合は自動的にやり直しのループに戻ります。

## 検証ループを書く

既存のプロジェクトがあり、Claude が新機能を実装するたびに同じ小さな修正を毎回入れていることに気づいたら、そのステップを自分専用の検証ループに変えるタイミングです。最初のステップは、毎回行っていることをすべて書き出すことです。

新しいプロジェクトを始めていて、プロジェクトがどう振る舞うべきかを詰めていく必要がある場合も同様です。ベストプラクティス版を平易な英語で、初日の新しいチームメイトに渡すつもりで書いてください。

検証チェックそのものをうまく言語化できない場合は、まず Claude にベストプラクティスを尋ね、そこから編集していきましょう。あなたのバージョンはおそらくいくつかの具体的な点で異なっているはずで、その違いこそがまさに捉えるべきものです。

**Pro tip**: チェックは定性的なものである必要はありません。「バックフィルのステップなしにカラムを削除するマイグレーションはすべて却下する」というのは、汎用のリンターでは検出できないが、プロジェクト固有のリンターなら検出できる決定論的なルールです。手作業でのチェックとして常に強制せざるを得ないものは何であれ、ループとして捉える価値があります。

## skill にする

繰り返し行うステップを検証ループとしてエンコードする最も一般的な方法は、それを[skill](https://claude.com/blog/complete-guide-to-building-skills-for-claude)として書くことです。そして skill を作る最速の方法は、skill-creator プラグインをインストールして、Claude にインタビューしてもらうことです。

例:

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

markdown ファイルをプロジェクトの .claude/skills/ に置くことで、自分で skill を手書きすることもできます。もっともシンプルな検証用 skill は、数行の frontmatter と本文だけで構成されます。

```
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.

For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.

Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```

完全なスキーマとその背後にある思想については、[skill 構築の完全ガイド](https://claude.com/blog/complete-guide-to-building-skills-for-claude)をご覧ください。

## チェックを実行場所に合わせる

次に決めるべきことは、検証ループがどのように起動するかです。スタンドアロン、埋め込み、連鎖、あるいは PR に紐づくかのいずれかになります。

### スタンドアロン

成果物ができたあとに、あなたが意図的に呼び出します。スタンドアロンの skill は、毎回は当てはまらない横断的なチェックにこそふさわしい存在です。コミット前のセキュリティスキャン、PR 前のアクセシビリティ監査、リポジトリ全体のライセンスヘッダー検証などです。多くのワークフローで使えるようにしておきたいが、コード変更のたびに発火してほしくないもの全般が対象です。

コストは、呼び出すたびに、あなたがそれを覚えて実行するターンが必要になることです。スタンドアロンから卒業すべきサインは、変更のたびにそれを実行するようになったときです。その時点で、その手順は恒久的な居場所を得たことになります。埋め込むか、連鎖させましょう。

### 埋め込み

生成元の skill の一部として自動的に発火します。そのチェックは 1 つの特定のワークフローに属し、そのワークフローはもうあなたが頼まなくてもそれを実行するようになります。

もっともシンプルなバージョンは、生成元の skill の本文への 1 行の追記です。

```
# .claude/skills/scaffold-component/SKILL.md
---
name: scaffold-component
description: Scaffold a new React component under src/components/, including the component file, its co-located test, and an index export. Use when the user asks to create a new component.
allowed-tools: [Read, Write, Edit, Bash, Glob]
---

# Scaffold a new React component

Given a component name (PascalCase), create the following under `src/components/<Name>/`:

1. `<Name>.tsx`: function component with a typed props interface and a default export.
2. `<Name>.test.tsx`: React Testing Library test that renders the component and asserts it mounts without throwing.
3. `index.ts`: re-export the default and any named exports.

Follow the patterns in `src/components/Button/` as the reference. Match the import alias style (`@/components/...`) used throughout the codebase.

# code continues...

After creating the component file, run eslint on it and
address any errors before reporting completion.
```

埋め込みがうまく機能しているかは、新しいタスクで skill を呼び出し、追加されたステップが出力の一部として実行されることを確認して検証してください。もし実行されなければ、その skill の description か、それより前の指示が、追記したチェックをうまく引き込めていないということです。

埋め込みが機能するのは、あなたが編集できる skills だけです。つまり、自分で書いたものや、プロジェクトレベルでインストールされていて SKILL.md ファイルをあなたが管理できるものに限られます。組み込みの skills やプラグイン管理の skills (アップデートで上書きされる類のもの) には、このパターンは使えません。それらについては連鎖を使ってください。

複数のワークフローにまたがるチェックには埋め込みを使わないでください。そうしたチェックはどんな文脈からでも呼び出せるよう、スタンドアロンにしておくべきです。

### 連鎖

ある skill が最後に別の skill を呼び出し、いくつもの検証済みの引き継ぎが端から端まで実行されます。

Anthropic の Claude Code チームのメンバーは、日々の作業でこのパターンを使っています。/code-review がバグを探し、/simplify が diff を整理し、/verify skill がエンドツーエンドの振る舞いを確認し、変更が UI に触れていればカスタムの /design skill が DESIGN.md ファイル内のガイドラインと照らし合わせてチェックします。

連鎖はまた、自分では変更できない skill に検証を追加する方法でもあります。元の skill を呼び出し、続けて自分の検証用 skill を呼び出す、カスタムのラッパー skill を作りましょう。以下に示す通りです。

```
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```

「/simplify のあとはいつも /verify を実行する」という習慣として始まったものが、「/simplify は終わったら必ず /verify を実行する」という契約になります。連鎖は開発サイクル全体を自律的に実行します。何かがエスカレーションしてあなたのところに戻ってきたときだけ、あなたが介入すればよいのです。

各ステップが十分に独立していて、ときにはどれか 1 つだけを実行したい場合は、連鎖を見送ってもかまいません。連鎖は柔軟性を自動化と引き換えにします。連鎖された検証ループはトークン消費を増やすことがあるため、広く展開する前にテストしておくのが最善です。

### すべての PR で

自分の変更に対する連鎖が固まったら、同じ手順をすべての PR で実行できます。チームメイトの変更も、その人が連鎖の呼び出しを覚えていたかどうかにかかわらず、あなたの変更と同じゲートを通過します。このインフラは、あなたがすでに書いた連鎖と同じ種類のものであり、一歩進んだだけのものです。同じ skills、同じルーブリック、同じ基準が、作者の几帳面さに依存することなく適用されます。

ここで検証は、個人のインフラであることをやめ、[チームのインフラ](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)になります。週に 2 分の手間を省くために書き留めたチェックが、今やすべての変更において、全員の 2 分を節約しています。連鎖がまだ流動的なうちは、PR 全体に及ぶゲートの導入は控えましょう。調整のたびにチーム全体から見えるイベントになってしまうからです。

このプロセスを一度身につければ、あなたのループ設計を広げていく準備は整っています。検証ループを作るプロセスは、何を自動化していても、どんな環境であっても一貫しています。

1. 今週いちばん頻繁に行った手作業のフォローアップを選ぶ。
2. まず組み込みの /verify skill を試してみて、自分のプロセスに役立つか確かめる。
3. 手順を平易な英語で、初日の新しいチームメイトに渡すつもりで書く。
4. それを skill-creator に渡すか、自分で markdown ファイルを .claude/skills/ に置く。
5. 新しいタスクでそれを呼び出し、チェックが出力の一部として実行されることを確認し、必要なら反復する。
6. skill の連鎖を試して、エンドツーエンドの検証フローを作ってみる。

Claude が従うべきものをより多くエンコードできればできるほど、Claude の応答は最初の一回でより望みに近いものになります。もう手作業で細かく直さなくてよくなった修正の分だけ、どの skill も書き留めることができない、あなただけの専属の作業に注意を向けられるようになります。

***[Claude Code](https://www.anthropic.com/product/claude-code)*** ***で検証ループを始めましょう。***

*本稿は Claude Code チームのメンバーである Delba de Oliviera が執筆しました。*
