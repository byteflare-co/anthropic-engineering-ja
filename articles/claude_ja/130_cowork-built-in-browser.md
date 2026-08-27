---
date: '2026-08-26'
final_url: https://claude.com/blog/cowork-built-in-browser
number: 130
selector_used: main
slug: cowork-built-in-browser
source_url: https://claude.com/blog/cowork-built-in-browser
title: Claude gets its own browser in Cowork
title_ja: "Claude Cowork に専用ブラウザが搭載されました"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b8840b2f6f9a40fe0_8925ac952fa2cb8eb5e845b2e44f3e71b33fd695-1000x1000.svg)

# Claude Cowork に専用ブラウザが搭載されました

Claude には今、デスクトップアプリの Claude Cowork にブラウザが組み込まれました。タスクにウェブサイトの利用が必要な場合、サイドパネルにブラウザが開き、Claude がウェブページを閲覧し、読み取り、クリックし、入力を行います。これでタスクのウェブ部分を任せて、自分は今の作業を続けることができます。Claude はフォームへの入力、ダッシュボードからの数値の取得、コネクタが存在しないポータルでの作業などをこなします。拡張機能は不要で、セットアップも不要、そしてユーザーが選択しない限り自分のブラウザから何も共有されません。

これまで、Claude Cowork でウェブを利用する能力を Claude に与えるには、[Claude in Chrome](http://claude.com/claude-in-chrome) 拡張機能を通じて自分のブラウザへのアクセスを許可する必要がありました。作業対象がすでに開いているページである場合は、今でもそれが正しい選択です。しかし、多くのウェブタスクは*あなたの*ブラウザを必要とせず、単に*何らかの*ブラウザを必要とするだけであり、今 Claude はそれを持つようになりました。

今週から Pro、Max、Team プランの Claude デスクトップアプリで展開が始まります。Enterprise の管理者は本日から組織向けに有効化できます。

## どちらのブラウザを、いつ使うか

これは Claude のブラウザであり、あなたのものではありません。組み込みブラウザはユーザー自身のブラウザとは別のものです。Claude がユーザーのタブやブックマーク、パスワードを見ることはありません。利用中のサイトにログインした状態を保つには、macOS では Chrome、Edge、Firefox から、Windows と Linux では Firefox から、サイトごとにログイン情報を持ち込むことができます。銀行、メール、シングルサインオンのサイトは、ユーザーが選択しない限り対象から除外されます。

これは、Claude がウェブを利用する 2 つの方法の違いでもあります。組み込みブラウザは、ユーザーが作業を続けながらウェブタスクを Claude に任せるためのものです。レポート用の調査資料を集めたり、今月分の請求書をベンダーポータルから収集したりといった作業です。Claude in Chrome は、すでに開いているページ、すでにログイン済みのアカウントを使う場合のためのものです。CRM の更新や、受信トレイの整理、目の前で開いているドキュメントの編集などがこれにあたります。

すでに Claude in Chrome を使用している場合は、それは引き続き動作し、デフォルトのまま使われます。そうでない場合は、Claude は組み込みブラウザを使用します。設定 → Cowork → 優先ブラウザからいつでも切り替えられます。

## 制御を保つ

組み込みブラウザには、ブラウザ内で行動する他の AI エージェントと同様に、[プロンプトインジェクション](https://www.anthropic.com/research/prompt-injection-defenses)のリスクが伴います。これは、ページに隠された指示によって Claude を誘導しようとするものです。組み込みブラウザは、Claude in Chrome と同じ安全対策を実行しており、Claude の行動をユーザーの依頼内容と照合して確認する仕組みも含まれます。これらの対策については、[Claude in Chrome のブログ記事](http://claude.com/blog/%20claude-in-chrome-generally-available)で説明しています。こうした対策はリスクを大幅に低減しますが、完全に排除することはできないため、信頼できるサイトから使い始めることをお勧めします。詳しくは[安全に関するガイド](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely)をご覧ください。

## 始め方

組み込みブラウザは、今後 1 週間かけて、macOS、Windows、Linux(ベータ版)の Claude デスクトップアプリで Pro、Max、Team プランに順次展開されます。展開されると、デフォルトで有効になります。ウェブサイトを利用するタスクを Claude に与えると、ブラウザが自動的に開きます。Enterprise プランでは現在すでに利用可能で、管理者は組織設定 → Cowork → 組み込みブラウザで管理できます。

組み込みブラウザはデスクトップアプリ内で動作します。ウェブやスマートフォンからでも、デスクトップアプリが開いてオンラインになっている限り、Claude は引き続きこれを操作できます。デスクトップアプリを使わずウェブから利用する場合は、Claude in Chrome が Claude にブラウザを与える手段であり続けます。
