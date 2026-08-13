---
date: '2026-08-12'
final_url: https://claude.com/blog/cowork-chrome-side-panel
number: 113
selector_used: main
slug: cowork-chrome-side-panel
source_url: https://claude.com/blog/cowork-chrome-side-panel
title: The Claude in Chrome side panel is now Claude Cowork
title_ja: "Claude in Chrome のサイドパネルが Claude Cowork になりました"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Claude in Chrome のサイドパネルが Claude Cowork になりました

[Claude in Chrome](https://claude.com/blog/claude-for-chrome) のサイドパネルが、[Claude Cowork](https://claude.com/product/cowork) のセッションになりました。会話は履歴に保存され、skill やコネクタもブラウザ内で動作し、あるタブで開始したタスクを Claude のデスクトップ、ウェブ、モバイルアプリで続きから完了できます。本日より Max プランと Team プランで利用可能になり、数週間かけて Pro プランのユーザーにも展開されます。

Claude in Chrome は、Claude が今開いているページを見て、リンクのクリック、テキストの入力、ページ間の移動、フォームの入力といった操作を、既存のログイン情報を使って行えるようにするブラウザ拡張機能です。

日々使うツールの多くは[直接 Claude と連携](http://claude.com/connectors)できますが、社内ダッシュボードやレガシーシステム、ベンダーポータルなど、連携できないものもあります。Claude in Chrome を使えば、Claude はブラウザを通じてこうしたアプリでも作業できます。

これまで、サイドパネルのセッションは Claude アプリのセッションとは別物だったため、コンテキストや会話がそれらの間で引き継がれることはありませんでした。今回のアップデートにより、サイドパネルはデスクトップ、ウェブ、モバイルで長時間・複数ステップの作業に使うのと同じ Claude Cowork のセッションで動作するようになります。セッションは特定のデバイスではなくアカウントに紐づくため、ブラウザで作業を始めて、後で別の場所から続きに取りかかることができます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7ccc8227b8db87f3b33e7b_image%20(16).png)

例えば、予算のスプレッドシートをまとめていて、複数のベンダーポータルから請求書の情報を取り込む必要があるとします。Claude in Chrome に金額と日付を集めるよう依頼すれば、Claude がタブを開き、各請求書を読み取り、スプレッドシートを作成してくれます。その後、デスクトップアプリでそのセッションを引き継ぎ、パソコン内のファイルを追加したり、先月の予算を取り込んで変更点を尋ねたりすることができ、作業を進めながらサーフェスをまたいでコンテキストを維持できます。

## リスクを理解する

Claude in Chrome には、ブラウザ内で動作する AI エージェントに共通するリスク、とりわけ[プロンプトインジェクション](https://www.anthropic.com/research/prompt-injection-defenses)のリスクがあります。悪意のある行為者は、ウェブページやメール、ドキュメントといったウェブコンテンツに指示を隠します。こうした指示はユーザーの目には見えないことがありますが、Claude を意図しない行動に誘導する可能性があります。

[パイロット版以降](https://claude.com/blog/claude-for-chrome)、私たちは Claude 自身の行動をチェックする仕組みを追加しました。「自動承認」を使うと、Claude はステップごとに許可を求めて止まることなくタスクを進めます。フォームの送信、メッセージの送信、ファイルのダウンロードなど、重大な影響を伴う行動の前には、別のチェックがその行動を当初のユーザーの依頼内容と照らし合わせてレビューし、一致しないものはブロックします。これにより、監督を維持しながら中断の回数を減らすことができます。

購入やパーソナルデータの共有など、一部の不可逆的またはコストの大きい行動については、Claude は引き続き事前に確認を求めます。これらの対策はリスクを大幅に低減しますが、完全になくすことはできません。プロンプトインジェクションは常に変化する脅威であるため、私たちは新たな攻撃手法を探し続け、そこから学んだことを新しいモデルごとに組み込んでいます。まずは信頼できるサイトから使い始めることをお勧めします。詳しいベストプラクティスは[安全ガイド](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely)をご覧ください。

## 始め方

Claude in Chrome を使い始めるには、[Chrome ウェブストア](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)からインストールし、サインインしてサイドパネルを開いてください。新しいサイドパネルは本日より Max プランと Team プランで利用可能で、数週間かけて Pro プランのユーザーにも展開されます。Enterprise プランでは、Claude in Chrome はデフォルトでオフになっています。管理者はこれを有効にし、承認済みのドメインに限定することができます。詳しくは[管理者向けセットアップガイド](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls#h_bdb63199e1)をご覧ください。

パソコン内のファイルや他のアプリケーションを扱う場合は、引き続き Claude デスクトップアプリを使用する必要があります。Claude in Chrome は、他の Chromium ベースのブラウザやモバイルではまだ動作しません。
