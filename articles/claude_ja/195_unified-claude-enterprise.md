---
date: '2026-10-23'
final_url: https://claude.com/resources/articles/unified-claude-enterprise
number: 195
selector_used: article
slug: unified-claude-enterprise
source_url: https://claude.com/blog/unified-claude-enterprise
title: Claude Cowork and chat come together for Enterprise
title_ja: Enterprise 向けに Claude Cowork とチャットが統合（Claude Cowork and chat come together for Enterprise）
---

# Enterprise 向けに Claude Cowork とチャットが統合（Claude Cowork and chat come together for Enterprise）

*編集部注：2026 年 10 月 30 日より前の本記事における Max への言及には、現在の Max プランと Ultra プランの両方が含まれます。*

チャットと Cowork は、9 月に Pro プランと Max プラン向けに先行して[統合されました](https://claude.com/resources/articles/cowork-is-now-claude)。そして今回、同じ統合された Claude の体験が Claude Enterprise プランでも一般提供（GA）となりました。

チャットと Cowork は、Web、デスクトップ、モバイルのいずれでも 1 つの Claude になりました。これにより、チームは同じ会話の中で、ちょっとした質問をすることも、プロジェクト全体を任せることもできます。エージェント的な作業は Anthropic が管理するクラウド環境で実行され、[Claude Enterprise の管理者](https://claude.com/resources/webinars/unified-claude-what-it-means-for-admins)はロールごとにアクセスを制御し、新しい Efficient モードで使用量を管理できます。

## あらゆるタスクに 1 つの Claude

チームメンバーは、Claude との作業を始める前にチャットと Cowork のどちらを使うかを選ぶ必要がなくなりました。会話はチャットとして始まり、シンプルな質問には引き続きすばやく回答が返ってきます。タスクでコードの実行やファイルの操作が必要になると、Claude はクラウド上で作業を続け、完成したドキュメント、分析、スライド資料を返します。作業はクラウドで実行されるため、ノート PC を閉じた後も処理は続き、Web、デスクトップ、モバイルのどこからでも再開できます。チャット、プロジェクト、コネクタ、スキル、プラグインは新しい統合体験にそのまま引き継がれます。

すでに多くの組織が、チーム全体で統合された Claude の体験から価値を得ています。

![DXC](https://assets.claude.com/a6cc538462d716535ab150bb67609835002f2376.svg)

> 「チャットと Cowork の機能が統合される前は、それぞれが別々の体験で、個別に利用・管理する必要がありました。両者が一体になったことで、ユーザーにとっても管理者にとっても、すべてがシンプルになりました。移行はシームレスで、コネクタ、スキル、MCP のいずれも壊れることはありませんでした。より広く展開していくことに自信を持っています。」

Daniel Padilla, CTO of LabX

![LifeMoves](https://assets.claude.com/3bf5eaab2f0360b235789384c0f4535f6e7f7258.png)

> 「もうチャットと Cowork のどちらかを選ぶ必要はありません。10 分足らずのプロンプトで、Claude は郡・州・連邦の予算書や公開会議の資料の山を読み込み、資金の流れがどうつながっているかを整理し、私たちのチームなら何週間もかかったであろう包括的なレポートを作成しました。どのステップでどのツールを使うかを判断する必要は一度もありませんでした。このレポートは、私たちの戦略計画と今後の予算策定プロセスに活かされます。」

Paul Simpson, CFO and Head of Technology

![Quantium](https://assets.claude.com/0e6b8d1ab806b1a949b793cce5bc3b294fe8d88c.svg)

> 「チャットと Cowork の統合は、クライアントから繰り返し寄せられていた『どの Claude を使えばいいのか』『どれが何をするのか』という疑問への答えです。モバイル、デスクトップ、ブラウザを問わず、働き方や働く場所に合わせて適応してくれます。Quantium では、自社の AI に関する目標の拡大と、クライアントに提供できる価値の拡大に役立っています。」

Harley Barnes, Executive Manager, AI Technology

![Carvana](https://assets.claude.com/6d55e4e27973e13fce3e66d63ef5618d65cb12ae.svg)

> 「Carvana の仕事はデスクの前だけで行われるわけではありません。統合された Claude の体験により、従業員はコンピューターでタスクを始め、スマートフォンで続きを行えます。Claude が結果を出したときや入力が必要なときには通知も届きます。デスクにいるときも現場を訪れているときも、私たちのチームの働き方にフィットしています。」

Charles Sellers, Senior Director, Engineering

## セキュリティの維持

組織ですでに Claude のチャットが承認されている場合、今回の統合は、シングルサインオン（SSO）や Compliance API など、既存のエンタープライズ向けコントロールの上に構築されます。Anthropic は引き続き転送中および保存時のデータを暗号化し、デフォルトではデータをモデルのトレーニングに使用しません。

Claude はエージェント的な作業をクラウドセッションで行います。各セッションはそれぞれ独立した仮想マシン上で実行され、Claude Enterprise ではネットワークの外向き通信（egress）がデフォルトで無効になっており、コネクタの認証情報はサンドボックスの外に保持されます。作業は Anthropic が管理する単一の環境で実行されるため、セキュリティチームはそれを一元的に可視化・制御できます。アーキテクチャの全体像については、Anthropic Trust Center の[セキュリティベストプラクティスガイド](https://trust.anthropic.com/resources?s=3puokpm2aa1nn24nbcp0l&name=unified-claude-security-best-practices)をご覧ください。

## コストの管理

Claude Enterprise の料金体系は引き続き従量課金です。最新の Claude モデルは従来モデルよりも効率的になっています。従量課金の場合、一般的なワークロードにおいて Claude Opus 5.5 は Claude Opus 5 より[実行コストが 40% 低く](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/)、Claude Sonnet 5.5 はほとんどの作業で Claude Sonnet 5 より最大 30% 低コストです。

タスクによっては、エージェント的な作業は簡単なチャットよりも多くのトークンを消費する場合があります。Claude Enterprise の管理者は、この使用量を管理するために 4 つのコントロールを利用できます。Efficient モードは、統合された Claude の体験で Sonnet および Haiku モデルのみを使用するようにする新しい設定です。モデルの利用権限（model entitlements）では、各ロールが使用できるモデルを設定できます。[支出上限](https://claude.com/resources/articles/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)は組織、グループ、メンバーの各レベルで適用でき、プール型のグループ予算では、グループ全体で共有する月額予算を 1 つ設定できます。

## はじめに

統合された Claude の体験は、本日より Claude Enterprise プランで一般提供されています。管理者は組織設定からロールアウトを管理できます。Claude Code でゼロデータ保持（ZDR）を利用している組織、HIPAA 対応構成の組織、顧客管理の暗号鍵を使用している組織は、現在の構成のまま維持されます。

詳細は[管理者向けセットアップガイド](https://support.claude.com/en/articles/17444462)をご覧ください。既存の Claude Enterprise のお客様には、組織へのロールアウトについてメールでお知らせします。
