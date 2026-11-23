---
date: '2026-11-23'
final_url: https://claude.com/resources/articles/introducing-claude-ship
number: 205
selector_used: article
slug: introducing-claude-ship
source_url: https://claude.com/blog/introducing-claude-ship
title: Introducing Claude Ship
title_ja: "Claude Ship のご紹介（Introducing Claude Ship）"
---

プルリクエストを作成したことがある人なら、この流れはよくご存じでしょう。次の作業に取りかかったところでレビューが返ってきます。そこで手を止め、古いコードを掘り返し、修正をプッシュして、レビューが再び実行されるのを待ちます。そして今度は、承認してくれる人を探しに行くのです。

このやり方には、もっともな理由があります。ほとんどのチームは、すべての変更を人が承認することを望んでおり、すべての行を人が書いていた頃は、それに追いつくのも簡単でした。しかし今では、多くの開発者がエージェントを使って開発しています。Claude Code チームでは、[コードの大半を Claude が書いており](https://claude.dev/blog/how-the-claude-code-team-thinks-about-verification/)、PR 以降のすべての工程も同じスピードで進めたいと考えました。

そこで私たちは、本日ベータ版として提供を開始する [Claude Ship](https://claude.com/product/claude-ship) を開発しました。Claude Ship は、PR をレビューし、修正し、各チームが設定したポリシーに基づいてマージ可能なものを判断できます。どこで実行するか、どの変更に人の確認が必要かは、引き続きチームがコントロールします。目指すのは、チームがコードを書くのと同じ速さでコードを出荷することです。

> 対象となる Claude Enterprise 組織は、少なくとも 10,000 ドル分の Claude Ship クレジットを申請でき、申請から 30 日以内に利用できます。申請期限は 2027 年 1 月 15 日です。[規約が適用されます。](https://support.claude.com/en/articles/17603594-free-code-review-promotional-credits-for-claude-enterprise)

### Claude Ship の仕組み：レビュー、修正、承認

Claude Ship は、すでに一般提供されている [Code Review](https://claude.com/resources/articles/code-review-is-now-generally-available) と、ベータ版の 2 つの新しいエージェントである PR Steward と Claude Approvals で構成されています。これらが連携して、プルリクエストをレビュー、修正、承認判断まで進めるため、チームは各ステップを手作業で管理する必要がありません。

![Claude Ship は、チームが PR をレビューし、修正し、マージ可能なものを判断するのを支援します。Claude Ship は AI を使用しているため、バグやセキュリティ脆弱性、その他の問題を見逃す可能性があります。](https://assets.claude.com/2a72b687af32e0d798bd2859b12576be1f607f13.png)

**Code Review** は、複数の観点からコードベースに照らしてプルリクエストを詳細にレビューします。指摘事項を収集し、敵対的に検証し、分類したうえで PR に投稿します。Claude によるレビューをより広範なプロセスの一層として位置づけている Claude Code チームでは、6 月から 9 月にかけてマージされた PR が[2 倍以上に増え](https://claude.dev/blog/solving-code-review-at-anthropic/)、一方でリバートされた割合は 40% 以上減少しました。Code Review は、迅速なレビューと明確な指摘事項を提供し、リポジトリごとに Quick、Standard、Deep のレビューレベルを選択できます。

![Code Review がプルリクエストに指摘事項を投稿している例。](https://assets.claude.com/a30243fe61e4cc224ebfdcdb8d693b69c125b060.png)

**PR Steward** は PR をグリーンの状態に保つよう動作しますが、プルリクエストを承認したりマージしたりはしないよう設計されています。失敗している CI チェック、マージコンフリクト、そして Code Review や他のレビューツール、チームメンバーからのレビューフィードバックに対応します。プッシュのたびに、何を変更したか、それをどう元に戻せるかをコメントします。開発者は `@claude` に指示を添えてコメントすることで作業の方向を調整でき、`@claude stop` とコメントすれば手を引かせることができます。

![PR Steward がプルリクエストの修正に取り組んでいる例。](https://assets.claude.com/c6832086d36407567641b1b4de4d705f79ef3fca.png)

そこから、**Claude Approvals** が、チームがリポジトリ内にファイルとして記述した承認ポリシーを適用します。ポリシーが許可していれば、Claude は定型的な変更を自ら承認でき、特定のシナリオではより踏み込んだ人間による承認を必須にすることもできます。いわば、より賢い CODEOWNERS ファイルのように機能します。チームは、Code Review の指摘事項や、自然言語で記述した独自の分類器など、さまざまなシグナルを Claude Approvals の判断に考慮させることができます。ほとんどのお客様には、まず観察専用モードで有効にして信頼を築いてから、Claude Approvals の承認をブランチ保護で必須にするよう設定することをお勧めします。

![Claude Approvals のポリシーファイルの例。](https://assets.claude.com/6beae6085c1dc6bb43a62e6acf1f5563a14f4238.png)![承認ポリシーを満たしたプルリクエストの例。](https://assets.claude.com/635a1675ea125007f1d5f686db25959d8485d5fc.png)

## 始めるための 2 つの方法

### 開発者向け：Claude Code から `/ship` する

開発者は、Claude Code の新しい `/ship` コマンドを使って、自分のプルリクエストで Claude Ship を試せます。変更の準備ができたら `/ship` を実行します。Claude が変更をプッシュし、PR を作成し、変更をレビューし、フィードバックや失敗しているチェックに対応して、マージできる状態に近づけます。何をマージできるかは、開発者の権限とリポジトリのブランチルールによって決まります。

![Claude Code で /ship を実行している例。](https://assets.claude.com/3b5fa6d188937030373792607c2cc73fc01e52b1.png)

### 管理者とエンジニアリングリーダー向け：リポジトリごとにルールを設定する

リポジトリ全体で Claude Ship を有効にすると、チームが管理する設定と承認ポリシーのもとで、チームのプルリクエスト全体に自動的に適用されます。開発者が `/ship` コマンドを手動で呼び出す必要はありません。

- **実行場所は管理者が選びます。** 管理者はリポジトリごとに Code Review と PR Steward を有効にします。Claude Approvals は、接続されたリポジトリのデフォルトブランチにポリシーファイルがあると開始され、管理者はこれを無効にすることもできます。
- **リポジトリごとに必要な設定ができます。** 管理者は、レビューレベル（Quick、Standard、Deep）、レビューを実行するタイミング、利用上限額を設定できます。
- **チームは既存のツールをそのまま使えます。** Claude Ship は、既存のブランチ保護や必須チェックと連携して動作します。

ペースはチームが決めます。まず 1 つのリポジトリから始め、レビューレベルとレビューの実行タイミングを選び、月間の利用上限額を設定し、信頼できるようになるまで承認ポリシーを観察モードで運用できます。

### Claude Code チームの出荷方法

私たちは、自分たちのプルリクエストの多くで Claude Ship を使っています。最も大きな変化の 1 つは、顧客からのフィードバックに誰が対応できるかです。たとえば、Claude Code チームのプロダクトマネージャーは、フィードバックを読み、Claude Tag とアイデアやトレードオフについて話し合い、PR を作成させたら、あとは Claude Ship がレビュー、修正、承認判断まで進めてくれるので、次の作業に移れるようになりました。

最近、ある顧客が、Analytics API のドキュメントに Admin キーで Pro と Team の利用状況を取得できるかのような記述があったために混乱していました。PM が Claude Tag に修正が進行中かどうかを尋ねたところ、Claude Tag が修正の PR を作成しました。Code Review でブロッキングとなる問題は見つからず、ドキュメントのレビュアーが承認し、Claude Approvals を通過して、修正はその日の夜のうちにマージされました。

### お客様の声

> 「Claude Code Review が、人間のレビュアーがプルリクエストを見る前に実際の問題を検出し、PR Steward がコントリビューターによる修正を支援したケースが数多くありました。私たちのレビュアーはもともと、増え続けるボリュームに対応するために Claude Code を使っていたので、プルリクエストが作成されると Code Review、PR Steward、Claude Approvals が自動的に動き出すことで、作業がよりシンプルになりました。人間の関与は維持しつつ、その時間は本当に人の目が必要な変更に充てられるようになっています。」
> Vatsal Bhatt 氏、TELUS Digital、Director of Engineering

> 「PR Steward のおかげで、パイロットに参加しているチームはコードレビューのフィードバック対応に費やす時間が減り、開発により多くの時間を使えるようになっています。変更の提案方法やフィードバックの整理方法など、チームのプロセスに合わせてカスタマイズできます。その柔軟性によって、開発ワークフローの有用な一部となっています。」
> Alex Devkar 氏、Carvana、Senior Vice President, Engineering and Analytics

### 提供状況

Claude Ship は、GitHub 上のリポジトリを対象に、Claude Team プランと Enterprise プランで利用できます。Code Review は[一般提供](https://claude.com/resources/articles/code-review-is-now-generally-available)されており、PR Steward と Claude Approvals はベータ版です。

Claude Ship の利用はトークン単位で課金されるため、有効にすると組織のコストが増える可能性があります。金額は、対象となるプルリクエストの数と規模、レビューレベル、レビューの実行頻度、PR Steward の作業量によって異なります。管理者は Code Review と PR Steward に利用上限額を設定できます。Claude Approvals には基本料金はありませんが、ポリシー内の分類器は使用したトークンに応じて課金され、Claude のレビューを使用するポリシーは、観察モードであっても課金対象の Code Review を実行します。`/ship` の実行は、通常の Claude Code の利用としてカウントされます。

Claude Ship は、Zero Data Retention、HIPAA 構成、またはカスタマー管理の暗号化キーを利用している組織では利用できません。

### 始めましょう

開発者は Claude Code をアップデートし、次の変更で `/ship` を実行できます。`/ship` は本日から Claude Code とデスクトップアプリで順次提供が開始されます。

すでに Code Review を利用しているチームは、リポジトリに PR Steward を追加し、承認ポリシーを観察モードで導入できます。

Code Review を初めて利用するチームは、[セットアップガイド](https://code.claude.com/docs/en/code-review-setup)を参照して GitHub を接続し、最初のリポジトリで有効にしてください。

詳しくは[ドキュメント](https://code.claude.com/docs/en/claude-ship)をご覧ください。
