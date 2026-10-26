---
date: '2026-10-15'
final_url: https://claude.com/resources/articles/code-review-is-now-generally-available
number: 158
selector_used: article
slug: code-review-is-now-generally-available
source_url: https://claude.com/blog/code-review-is-now-generally-available
title: Code Review is now generally available
title_ja: Code Review の一般提供を開始しました
---

Code Review はリサーチプレビューを終了し、Claude Team および Enterprise の組織でご利用いただけるようになりました。

> 対象となる Claude Enterprise の組織は、2027 年 1 月 15 日までに申請することで、最低 10,000 ドル分の Code Review クレジットを受け取ることができます。クレジットは申請から 30 日後に失効します。[規約が適用されます。](https://support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise)

### Code Review の新機能

コーディングエージェントによってチームがコードを書くペースは上がり続けていますが、[レビューのボトルネック](https://claude.com/resources/articles/the-ai-native-sdlc-playbook)は解消されていません。一般提供にあたり、私たちは Code Review をより高速にし、本当に重要なバグをより的確に見つけられるようにし、さらにリポジトリごとに調整しやすくしました。

[リサーチプレビュー](https://claude.com/resources/articles/code-review)の公開以来、Code Review は精度を高め、本来なら本番環境に到達していたはずのバグをより多く検出できるようになりました。また、Anthropic 社内でもプルリクエストに Code Review を実行しており、それによって自社のエンジニアにとってレビューがどこで足かせになっているかが見えてきます。残りの部分は、プレビュー期間中に Code Review を利用したチームが教えてくれました。人間のレビュアーが PR を見る前に実際の問題を検出できている一方で、レビューをもっと静かに、変更の規模に見合ったものに、そしてもっと速くしてほしい、という声です。私たちがリリースした内容は次のとおりです。

- **スピード:** ほとんどのレビューが、プレビュー期間中と比べて約 3 倍速く（約 20 分から 6〜10 分に）完了するようになりました。
- **品質:** 重要なバグをより多く検出し、問題点、それが発生する条件、修正方法を数文で示す、明確で簡潔な指摘を行います。
- **柔軟性:** 管理者はリポジトリごとに Quick、Standard（デフォルト）、Deep を選択できます。日常的なコードベースには素早いチェックを、最も重要なコードベースには詳細なレビューを適用できます。どのレベルでも高品質なレビューを提供します。

### はじめに

Code Review は現在、Team プランおよび Enterprise プランで一般提供されています。

- **管理者の方へ**: [Claude Code の設定](http://claude.ai/redirect/claudedotcom.v1.549d75cc-b81c-42b7-be15-6d0eee5fac99/admin-settings/claude-code)で Code Review を有効にし、GitHub App をインストールして、レビューを実行したいリポジトリを選択してください。
- **開発者の方へ**: 有効化されると、新しい PR に対してレビューが自動的に実行されます。設定は不要です。

詳しくは[ドキュメント](http://code.claude.com/docs/en/code-review)をご覧ください。
