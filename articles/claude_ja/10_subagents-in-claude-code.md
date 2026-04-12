---
date: '2026-04-07'
final_url: https://claude.com/blog/subagents-in-claude-code
number: 22
selector_used: main
slug: subagents-in-claude-code
source_url: https://claude.com/blog/subagents-in-claude-code
title: How and when to use subagents in Claude Code
title_ja: Claude Code でサブエージェントを使うタイミングと方法
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

# Claude Code でサブエージェントを使うタイミングと方法

[Claude Code](https://code.claude.com/docs/en/overview) は複雑なマルチステップのプロジェクトを上手く処理しますが、長いセッションは重みを蓄積します。読んだファイル、探索した脇道、中途半端な思考のすべてがコンテキストウィンドウに残り、レスポンスを遅くし、トークンコストを押し上げます。

大規模な TypeScript モノレポで新機能を構築することを考えてみてください。メインの作業は実装ですが、サイドタスクが次々と現れます：既存のサービスが認証をどう処理しているかを追う、日付フォーマット用の共有ユーティリティを見つける、デザインシステムに必要なものに近いコンポーネントがすでにあるか確認する。これらのどれもプロジェクト全体のコンテキストを必要とせず、メインセッション内で実行するとノイズが増えるだけです。並行して実行できたらどうでしょうか？

ここで登場するのが[サブエージェント](https://code.claude.com/docs/en/sub-agents)です。サブエージェントは、独自のコンテキストウィンドウを持つ隔離された Claude インスタンスです。タスクを受け取り、作業を行い、結果のみを返します。サブエージェントは Claude Code セッションにおけるブラウザのタブのようなものと考えてください：メインスレッドを見失うことなく脇道を追いかけるための場所です。

この記事では、サブエージェントを使うのが理にかなうケース、呼び出し方、そしてオーバーヘッドに見合わないケースについて議論します。

## サブエージェントとは何か？

サブエージェントは、独自のコンテキストウィンドウで動作する自己完結型のエージェントです。Claude がサブエージェントを生成すると、そのアシスタントはファイルの読み取り、コードの探索、変更の実行を独立して行います。タスクが完了すると、サブエージェントは関連する結果のみをメインの会話に返します。

各サブエージェントはまっさらな状態から始まり、会話の履歴や呼び出されたスキルの影響を受けません。複数のサブエージェントを並行して実行でき、それぞれ異なるパーミッションを持たせることができます：調査用のサブエージェントは読み取り専用アクセスのみ、実装用のサブエージェントは完全な編集権限を持つ、といった具合です。

Claude Code にはいくつかの組み込みサブエージェントタイプがあります：

- **汎用エージェント** - 複雑なマルチステップタスク用
- **Plan エージェント** - 実装戦略を提示する前にコードベースを調査する
- **Explore エージェント** - 高速な読み取り専用コード検索に最適化

Claude Code はしばしば、割り当てられたタスクを処理するために自らサブエージェントを生成します。その振る舞いを明示的に指示することも、Claude が自動的に委任する再利用可能なスペシャリストを定義することもできます。サブエージェントに手を伸ばすべきタイミングを知ることが、この機能を有用にする鍵です。

## いつサブエージェントを使うべきか？

特定のカテゴリの作業は、サブエージェントへの委任から明確に恩恵を受けます。それらを認識できるようになると、この機能ははるかに効果的になります。

### リサーチの多いタスク

何かの仕組みを理解することが変更の前提条件となる場合、サブエージェントがコードベースを探索して要約を返すことで、何十ものファイルを会話にダンプする必要がなくなります。

**シグナル：** コンテキスト収集に何十ものファイルの読み取りが必要。

**メリット：** メインの会話がクリーンに保たれ、生のコンテンツの代わりに統合された知見が届く。

### 複数の独立したタスク

複数のファイルにまたがるエラーの修正、複数コンポーネントでのパターン更新、互いに依存しない変更を行う場合、並行サブエージェントがタスクをより速く完了します。

**シグナル：** サブタスク間に依存関係がない。

**メリット：** 3 つのサブエージェントが同時に作業すれば、一般的にタスクがより短時間で完了する。

### フレッシュな視点が必要なとき

実装の偏りのないレビューが目的の場合、サブエージェントはプライマリの会話からの前提、コンテキスト、盲点を引き継がないため、クリーンな状態を提供します。

**シグナル：** 会話の履歴が分析に影響しない形で検証が必要。

**メリット：** よりクリーンで客観的なフィードバック。

**プロのコツ：** /clear コマンドもコンテキストと会話履歴をリセットし、同様に偏りのない状態を提供しますが、履歴を完全に失うという代償があります。サブエージェントならメインの会話はそのまま維持しつつ、同じフレッシュな視点を実現できます。

### コミット前の検証

変更を確定する前に、独立したサブエージェントが実装をテストに過剰適合していないか、エッジケースを見逃していないかを検証できます。

**シグナル：** コードをコミットする前にセカンドオピニオンが必要。

**メリット：** コードへの慣れが覆い隠す問題を検出できる。

### パイプラインワークフロー

タスクに明確なフェーズ（設計、次に実装、次にテスト）がある場合、各段階が集中的な注意から恩恵を受けます。

**シグナル：** 明確な引き継ぎがある逐次的な段階。

**メリット：** 各サブエージェントが自分のフェーズに集中し、他の段階のコンテキストがノイズを生まない。

**プロのコツ：** タスクが 10 個以上のファイルの探索を必要とする場合、または 3 つ以上の独立した作業を含む場合、それは Claude にサブエージェントの方向へ導く強いシグナルです。

## サブエージェントの使い方を指示する方法

サブエージェントを呼び出す方法は、シンプルな会話から自動化ワークフローまで複数あります。適切な出発点はワークフローによって異なり、パターンが明確になるにつれて洗練度を重ねていけます。

### 会話での呼び出し

最も柔軟なアプローチは、会話の中で単に Claude にサブエージェントを使うよう頼むことです。これはすべての Claude Code インターフェースで機能します：ターミナル、VS Code、JetBrains、ウェブ、デスクトップアプリケーション。

サブエージェントを確実に呼び出す自然言語パターンには次のようなものがあります：

- 「サブエージェントを使って、このコードベースの認証の仕組みを調べて」
- 「別のエージェントにこのコードのセキュリティの問題をレビューしてもらって」
- 「並行でリサーチして。API ルート、データベースモデル、フロントエンドコンポーネントを同時にチェックして」
- 「サブエージェントを起動して、異なるパッケージ間のこれらの TypeScript エラーを修正して」

明示的であることが重要です。スコープを指定し、タスクが独立している場合は並行実行をリクエストし、期待する出力を説明してください。

効果的なプロンプト構造の例：

```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

このプロンプトが効果的なのは、3 つの独立したタスクを明確に定義し、並行実行を明示的にリクエストし、出力フォーマットを指定しているからです。Claude は意図を理解し、適切なサブエージェントを生成します。

効果的な会話での呼び出しのコツ：

- **タスクのスコープを明確にする。** 「すべてを調べて」より「決済の仕組みを調べて」の方が効果的。
- **並行化を明示的にリクエストする。** 「これらは並行で実行できます」や「3 つとも同時に作業して」と伝える。
- **何を返すべきか指定する。** 要約、特定の知見、推奨事項。出力フォーマットを指定すると、Claude がそれに応じて提供しやすくなる。
- **偏りのない分析が重要な場合はフレッシュなコンテキストを要求する。** 「以前の議論を見ないサブエージェントを使って」と指定すれば、クリーンな評価が保証される。

**プロのコツ：** サブエージェントに時間がかかっている場合、Ctrl+B でバックグラウンドに送れます。それが実行されている間も会話を続けられ、完了すると結果が自動的に表示されます。/tasks コマンドでバックグラウンドで実行中のタスクを確認できます。

### カスタムサブエージェント

同じ種類のサブエージェントが繰り返しリクエストされる場合（セキュリティレビュアー、テストライター、ドキュメント校正者など）、一度カスタムサブエージェントとして定義できます。

Claude はタスクがその説明に一致するたびに自動的に委任します。プロンプトは不要です。

カスタムサブエージェントは `.claude/agents/`（プロジェクトレベル、チームで共有）または `~/.claude/agents/`（ユーザーレベル、すべてのプロジェクトで利用可能）に Markdown ファイルとして配置します。それぞれ独自のシステムプロンプト、ツールパーミッション、オプションで独自のモデルを持てます。

最も簡単な作成方法は /agents コマンドで、対話形式でセットアップを案内し、説明から最初のドラフトを生成できます。手動でファイルを書くこともできます。例：

```
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities,
  injection risks, auth issues, and sensitive data exposure.
  Use proactively before commits touching auth, payments, or user data.
tools: Read, Grep, Glob
model: sonnet
---

You are a security-focused code reviewer. Analyze the provided
changes for:
- SQL injection, XSS, and command injection risks
- Authentication and authorization gaps
- Sensitive data in logs, errors, or responses
- Insecure dependencies or configurations

Return a prioritized list of findings with file:line references
and a recommended fix for each. Be critical. If you find nothing,
say so explicitly rather than inventing issues.
```

これを配置すれば、Claude は一致する作業を自動的にサブエージェントにルーティングします。名前で呼び出すこともできます：「security-reviewer にステージされた変更を見てもらって」。

カスタムサブエージェントが効果的なケース：

- Claude がタスクに一致した場合に自動的に委任できるスペシャリストを用意したいとき
- 厳密にスコープされたシステムプロンプトと制限されたツールが作業に有益なとき
- チーム全体で共有したり、プロジェクト間で再利用すべき設定があるとき

**プロのコツ：** description フィールドは、Claude が委任のタイミングを判断するために使います。能力だけでなく、トリガー条件を具体的に記述してください。「コミット前にコードのセキュリティ問題をレビューする」は「セキュリティエキスパート」よりも的確にルーティングされます。

パーミッションモードやプロジェクトレベル・ユーザーレベルのサブエージェントの相互作用を含む完全な設定リファレンスは、[Claude Code サブエージェントのドキュメント](https://code.claude.com/docs/en/sub-agents)を参照してください。

### CLAUDE.md での指示

カスタムサブエージェントはスペシャリストが誰かを定義します。CLAUDE.md ファイルは、Claude がいつそれらを使うべきかのルールを定義します。すべてのコードレビューが読み取り専用サブエージェントを通るべき場合、またはすべてのアーキテクチャの質問で最初にリサーチパスを実行すべき場合、そのポリシーを置くのが CLAUDE.md です。Claude はすべての会話の開始時にこれを読むため、セッションやチームメンバー間で一貫した動作が維持され、誰も頼むことを覚えておく必要がありません。

CLAUDE.md がサブエージェントの指示に適しているケース：

- コードレビューで常に読み取り専用サブエージェントを使うべきとき
- プロジェクトに Claude が従うべき特定のリサーチパターンがあるとき
- チームメンバーやセッション間で一貫した動作が必要なとき

特定の条件でサブエージェントをトリガーするシンプルな CLAUDE.md ファイルの例：

```
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access
(Glob, Grep, Read only). The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md

Return findings as a prioritized list with file:line references.
```

上記の CLAUDE.md ファイルにより、すべてのコードレビューリクエストが自動的に定義されたパターンを使用し、毎回指定する必要がなくなります。

CLAUDE.md ファイルの詳細については、[Customizing Claude Code for your codebase: setting up a CLAUDE.md file](https://preview.claude.ai/chat/link) および Claude Code の [CLAUDE.md ファイルドキュメント](https://code.claude.com/docs/en/memory#claude-md-files)を参照してください。

### Skills

繰り返し実行される複雑なマルチステップワークフローには、Skills が再利用可能なインターフェースを提供します。.claude/skills/ にスキルを一度定義すれば、/skill-name で呼び出すか、タスクが説明に一致した場合に Claude が自動的にロードします。

Skills は CLAUDE.md ファイルとはスコープが異なります。CLAUDE.md ファイルは常にロードされ、すべてのインタラクションに影響を与えます。スキルはオンデマンドでロードされ、明示的に呼び出されたか、Claude が現在のタスクとスキルの description フィールドをマッチさせたときに読み込まれます。そのため、利用可能だがすべてのプロンプトに適用されるべきではないワークフローを置くのに適した場所です。

Skills が適しているケース：

- 特定のアクションを定期的に実行する場合
- チームの異なるメンバーが同じ複雑な操作にアクセスする必要がある場合
- チーム全体で特定のタスクの実行方法を標準化することが重要な場合

包括的なコードレビュー用の deep-review スキルの例：

```
# .claude/skills/deep-review/SKILL.md

---
name: deep-review
description: Comprehensive code review that checks security,
  performance, and style in parallel. Use when reviewing staged
  changes before a commit or PR.
---

Run three parallel subagent reviews on the staged changes:

1. Security review - check for vulnerabilities, injection risks,
   authentication issues, and sensitive data exposure
2. Performance review - check for N+1 queries, unnecessary iterations,
   memory leaks, and blocking operations
3. Style review - check for consistency with project patterns
   documented in /docs/style-guide.md

Synthesize findings into a single summary with priority-ranked issues.
Each issue should include the file, line number, and recommended fix.
```

上記のコードスニペットでは、/deep-review がオンデマンドで 3 部構成のサブエージェント分析をトリガーします。description がコミット前のステージされた変更のレビューに言及しているため、そのコンテキストが出てきた場合に Claude がこのスキルを自動的に選択することもできます。

スキルはディレクトリであり、単一のファイルではありません。`SKILL.md` と並んで、Claude が記入するテンプレート、期待されるフォーマットを示すサンプル出力、ワークフローの一部として Claude が実行するスクリプトを含めることができます。レガシーの `.claude/commands/` フォーマットは単一のフラットファイルだったため、すべてをプロンプト自体に収める必要がありました。

Claude Code での Skills の使い方については、[Claude Code Skills ドキュメント](https://code.claude.com/docs/en/skills#extend-claude-with-skills)を参照してください。

### Hooks

Hooks は、Claude Code のライフサイクルの特定のポイントで自動的に実行される、ユーザー定義のシェルコマンド、HTTP エンドポイント、または LLM プロンプトです。[Hooks](https://code.claude.com/docs/en/hooks-guide) はイベントに基づいてサブエージェントワークフローを自動化できます。Hooks は特定のアクションでトリガーされ、手動で呼び出すことなくサブエージェントタスクを実行します。

Hooks が適切なツールとなるケース：

- すべてのコミットが作成前に自動的にレビューされるべきとき
- セキュリティチェックが誰も頼むことを覚えていなくても実行されるべきとき
- CI のような品質ゲートがローカル開発プロセスに組み込まれるべきとき

テストが通過するまで Claude がターンを終了できないようにする Stop フックの例：

```
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/check-tests.sh"
          }
        ]
      }
    ]
  }
}
```

`.claude/hooks/check-tests.sh` のスクリプト：

```
#!/bin/bash
INPUT=$(cat)
STOP_HOOK_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false')

# Don't loop forever — if we already blocked once this turn, let it through
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
  exit 0
fi

if ! npm test --silent > /dev/null 2>&1; then
  jq -n '{
    decision: "block",
    reason: "Tests are failing. Run `npm test` to see the failures and fix them before finishing."
  }'
  exit 0
fi

exit 0
```

Claude がターンを終了すると、Stop イベントが発火します。スクリプトがテストスイートを実行し、テストが失敗した場合、`decision: "block"` と `reason` を含む JSON を返します。Claude Code はそれを読み取り、Claude の終了を許可せず、理由を作業を続行するための指示として会話にフィードバックします。先頭の `stop_hook_active` ガードは無限ループを防ぎます：前回の stop-hook ブロックにより Claude がすでに続行している場合、スクリプトはそのまま終了させます。

Hooks はサブエージェントオーケストレーションの中で最も自動化されたアプローチです。会話での呼び出しや CLAUDE.md の指示がより良い出発点であり、Hooks はワークフローが成熟してから導入するものです。

完全な Hooks の設定については、[Claude Code power user customization: how to configure hooks](https://claude.com/blog/how-to-configure-hooks) または [Claude Code Hooks ドキュメント](https://code.claude.com/docs/en/hooks)を参照してください。

## サブエージェントを使う実践的なパターン

以下のパターンは、一般的なシナリオに適用されたサブエージェントの活用方法を示しています。

### 実装前のリサーチ

不慣れなコードに機能を追加する場合、リサーチをサブエージェントに委任することで、実装の議論が探索的ではなく情報に基づいたものになります。例：

```
Before I implement user notifications, use a subagent to research:
- How are emails currently sent in this codebase?
- What notification patterns already exist?
- Where should new notification logic live based on the current architecture?

Summarize findings, then we'll plan the implementation together.
```

20 ファイル分の生のコンテキストの代わりに統合された要約が届き、実装の議論が堅固な基盤から始まります。

### 並行修正

同じパターンを複数のファイルにわたって更新する必要がある場合、並行サブエージェントがより速く完了し、集中を維持します。例：

```
Use parallel subagents to update the error handling in these files:
- src/api/users.ts
- src/api/orders.ts
- src/api/products.ts

Each should follow the pattern established in src/api/auth.ts.
Work on all three simultaneously.
```

3 つのサブエージェントが並行で作業すれば、1 つで行う場合のおよその時間で完了します。それぞれが自分のファイルに集中し、他のファイルのコンテキストが混乱や不整合を生むことがありません。

### 独立したレビュー

複雑なものを実装した後、実装の過程に影響されていないサブエージェントによる検証は、慣れが覆い隠すものを発見します。例：

```
Use a fresh subagent with read-only access to review my implementation of the payment flow. It should not see our previous discussion. I want an unbiased review.

Check for: security vulnerabilities, unhandled edge cases, and error handling gaps. Be critical.
```

レビュー用のサブエージェントは、どのようなトレードオフが検討されたか、どのアプローチが却下されたか、どのような前提が置かれたかを知らずにコードを評価します。この外部の視点が、メインの会話では見逃しがちな問題を浮き彫りにします。

### パイプラインワークフロー

マルチステージのタスクでは、フェーズ間の明確な引き継ぎとサブエージェントの連鎖により、各段階の集中が保たれます。例：

```
Let's build this feature as a pipeline:

1. First subagent: Design the API contract and write it to docs/api-spec.md
2. Second subagent: Implement the backend endpoints based on that spec
3. Third subagent: Write integration tests for the implementation

Each stage should complete before the next begins. Use the output
files as the handoff mechanism between stages.
```

パイプラインワークフローを使えば、タスクの各段階が集中したコンテキストを受け取ります。設計のサブエージェントは実装の懸念に惑わされず、実装のサブエージェントはクリーンな仕様から作業し、テストのサブエージェントは結果を独立して評価します。

## サブエージェントを使うべきでないとき

サブエージェントは有用な機能ですが、オーバーヘッドを伴います。それぞれが独自のコンテキストを起動し、トークンを消費し、開発者と作業の間に間接的なレイヤーを追加します。コンテキストの隔離、並行性、フレッシュな視点が実際に役立つ場合にのみ、そのコストに見合います。

小規模または密に逐次的なタスクでは、メインの会話にとどまる方が通常はシンプルです。例：

- **逐次的で依存関係のある作業。** ステップ 2 がステップ 1 の完全な出力を必要とし、ステップ 3 が両方を必要とする場合、チェーンを処理する単一のセッションの方が、ファイルを介して状態を受け渡すサブエージェントのリレーよりも通常はクリーンです。
- **同一ファイルの編集。** 2 つのサブエージェントが同じファイルを並行して編集するのはコンフリクトのもとです。密に結合した変更は 1 つのコンテキストウィンドウ内に留めてください。
- **小さなタスク。** 素早い修正や集中した質問には、委任のオーバーヘッドがメリットを上回ります。メインの会話でプロンプトするか質問するだけで十分です。
- **スペシャリストエージェントが多すぎる場合。** あらゆることにカスタムサブエージェントを定義したくなりますが、Claude に選択肢を溢れさせると自動委任の信頼性が低下します。ほとんどのチームは、膨大な名簿ではなく、数個のスコープの明確なエージェントに落ち着きます。
- **エージェント同士が連携する必要がある作業。** サブエージェントはメインの会話に結果を返しますが、互いに通信することはできません。サブエージェント間のコミュニケーションが必要なタスクには、[Agent Teams](https://code.claude.com/docs/en/agent-teams) を使ってください。Agent Teams では、サブエージェントは 1 つのセッション内ではなく、別々のセッション間で連携するため、より重量級で高コストになります。サブエージェントと Agent Teams のどちらを使うべきかの詳細なガイダンスは、[Claude Code Agent Teams ドキュメント](https://code.claude.com/docs/en/agent-teams)をご覧ください。

先に述べたシグナル（セカンドオピニオンの必要性、サブタスク間の依存関係の欠如、広範なリサーチ）が、サブエージェントへの委任に見合うかどうかを明確にしてくれます。

## まずは会話から、自動化は後から

サブエージェントは、意図的に使うことでその真価を発揮します。Claude が提供する自動呼び出しは役立ちますが、リサーチの委任、作業の並行化、フレッシュな視点のリクエストのタイミングを知ることで、偶然に任せるよりも良い結果が得られます。

サブエージェントを使う際は、会話でのプロンプトから始めてください。繰り返し発生するリクエストに気づき、そのパターンが明確になるにつれて自動化を構築していきましょう。目標は、サブエージェントへの委任を effortless にし、重要な作業に注意を集中させることです。
