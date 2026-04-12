---
date: '2026-03-24'
final_url: https://claude.com/blog/auto-mode
number: 14
selector_used: main
slug: auto-mode
source_url: https://claude.com/blog/auto-mode
title: Auto mode for Claude Code
title_ja: Claude Code の Auto mode
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225c16d1b0cc3b1ded5_6457c34fbcb012acf0f27f15a6006f700d0f50de-1000x1000.svg)

# Claude Code の Auto mode

本日、Auto mode を発表します。これは Claude Code の新しいパーミッションモードで、セーフガードがアクション実行前に監視しながら、Claude があなたに代わってパーミッションの判断を行います。Team プランでリサーチプレビューとして本日より利用可能で、Enterprise プランおよび API ユーザーには数日以内に提供予定です。

## 仕組み

Claude Code のデフォルトのパーミッションは意図的に保守的に設定されています：ファイルの書き込みや bash コマンドの実行のたびに承認を求めます。安全なデフォルト設定ですが、大きなタスクを任せてその場を離れることができません。Claude が処理の途中で頻繁に人間の承認を求めるからです。パーミッションチェックを省略するために --dangerously-skip-permissions を選ぶ開発者もいますが、パーミッションの省略は危険で破壊的な結果を招く可能性があり、分離された環境以外では使用すべきではありません。

Auto mode は、すべてのパーミッションを省略するよりもリスクを抑えつつ、中断を減らしてより長いタスクを実行できる中間的な選択肢です。各ツール呼び出しの実行前に、分類器がそれを確認し、ファイルの大量削除、機密データの持ち出し、悪意のあるコード実行など、[潜在的に破壊的なアクションをチェック](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)します。

分類器が安全と判断したアクションは自動的に進行し、リスクのあるものはブロックされ、Claude は別のアプローチを取るようリダイレクトされます。Claude が継続的にブロックされるアクションを実行しようとし続ける場合、最終的にはユーザーにパーミッションプロンプトが表示されます。

## 期待されること

Auto mode は --dangerously-skip-permissions と比較してリスクを低減しますが、完全に排除するものではなく、分離された環境での使用を引き続き推奨します。分類器がリスクのあるアクションを許可してしまう場合もあります：たとえば、ユーザーの意図が曖昧な場合や、Claude がアクションによって追加のリスクが生じる可能性を判断するのに十分な環境のコンテキストを持っていない場合です。また、無害なアクションをブロックしてしまうこともまれにあります。時間をかけて体験を改善していきます。

Auto mode は、ツール呼び出しにおけるトークン消費量、コスト、レイテンシにわずかな影響を与える場合があります。

## 始め方

Auto mode は、本日より Claude Team ユーザー向けのリサーチプレビューとして Claude Code で利用可能です。Enterprise および API ユーザーには数日以内に展開予定です。Claude Sonnet 4.6 と Opus 4.6 の両方で動作します。

- **管理者向け**: Auto mode は Enterprise、Team、Claude API プランのすべての Claude Code ユーザーに間もなく提供されます。CLI と VS Code 拡張機能で無効にするには、管理設定で "disableAutoMode": "disable" を設定してください。Auto mode は Claude デスクトップアプリではデフォルトで無効になっており、Organization Settings -> Claude Code からオンに切り替えられます。
- **開発者向け**: `claude --enable-auto-mode` を実行して Auto mode を有効にし、Shift+Tab で切り替えます。デスクトップおよび VS Code 拡張機能では、まず Settings -> Claude Code で Auto mode をオンにしてから、セッション内のパーミッションモードのドロップダウンから選択してください。

詳細は[ドキュメント](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)をご覧ください。
