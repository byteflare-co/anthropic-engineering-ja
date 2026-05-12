---
date: '2026-05-11'
final_url: https://claude.com/blog/agent-view-in-claude-code
number: 44
selector_used: main
slug: agent-view-in-claude-code
source_url: https://claude.com/blog/agent-view-in-claude-code
title: Agent view in Claude Code
title_ja: Claude Code の agent view
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

# Claude Code の agent view

本日、Claude Code に agent view を導入します。これは、すべての Claude Code セッションをひとつの場所で管理するための機能です。

これまで複数のエージェントを並行して動かす際には、複数のターミナルタブや tmux のグリッドをやりくりし、次に何に取り組むべきかを頭の中で大量にメモしておく必要があったはずです。

Claude Code の agent view を使えば、新しいエージェントを立ち上げてバックグラウンドに送り、Claude があなたの判断を必要とするときだけ介入できます。どのエージェントがあなたの応答を待っていて、どれがまだ作業中で、どれが完了したかを一目で把握できるので、多数のエージェントを同時に簡単に操縦できます。

## 仕組み

agent view は、CLI 上の Claude Code セッションの可視化と操作を改善します。

### すべてを一度に見渡す

任意のセッションから左矢印キーを押すか、ターミナルで `claude agents` を実行すると agent view が開きます。各行にはセッション、あなたの入力を必要としているかどうか、最後の応答の内容、最後にやり取りした時刻が表示されます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02147d18cd3a9a9fe18c4f_aef149a9.png)

### その場で覗き見て返信する

セッションを選択すると、直近のターンを覗き見できます。判断を待っているセッションがあれば、その場で答えればセッションは再開します。Enter を押せば対象のセッションに直接アタッチし、トランスクリプト全体を確認できます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a02147d18cd3a9a9fe18c52_57c35e02.png)

### なんでもバックグラウンドへ

さらに、既存のセッションを `/bg` で agent view に追加することもできますし、`claude --bg [task]` を使えばフォアグラウンドを完全にスキップして新しいセッションを起動できます。

## 開発者の使い方

早期ユーザーから見えてきたパターンをいくつか紹介します。

- **並行セッション数のスケーリング:** 複数のアイデアを一度にディスパッチし、それぞれを必要に応じて skill とペアにして、戻ってきたときにはレビュー待ちのプルリクエストが並んでいるという使い方。
- **長時間動くエージェントの管理:** PR の見守り役、ダッシュボードの更新役など、ループして動くジョブが、リストの中に次回の実行時刻を表示します。
- **別々のセッションを行き来する:** あるセッションの最中に左矢印キーを押し、関連するタスクや簡単なコードベースへの質問を始めて、右矢印キーで元の作業に戻る、という使い方。回答が返ってくれば peek でその内容を確認できます。
- **何がシップされたかを確認する:** 各行のステータスインジケーターと peek 内のタイトルがあるので、どのセッションが PR を生み出したのかをひと目でスキャンできます。

## 始め方

agent view は本日より、Pro、Max、Team、Enterprise、Claude API の各プランでリサーチプレビューとして利用可能です。`claude agents` を実行してオプトインしてください。通常のレート制限が適用されます。詳しくは[ドキュメント](https://code.claude.com/docs/en/agent-view)をご覧ください。
