---
date: '2026-11-24'
final_url: https://claude.com/resources/articles/install-as-app
number: 207
selector_used: article
slug: install-as-app
source_url: https://claude.com/blog/install-as-app
title: Turn artifacts into Mac and Windows apps
title_ja: "Artifacts を Mac・Windows アプリに（Turn artifacts into Mac and Windows apps）"
---

本日より、Claude の Artifacts を使ってデスクトップアプリを作成・実行・共有できるようになりました。「Install as app」機能は、Claude for Mac および Windows でベータ版として順次提供を開始しています。

Artifact を Mac または Windows アプリとしてインストールすると、専用のアイコンが付き、Claude の中ではなく独立したウィンドウで開きます。他の人と共有することもでき、コンピューターを操作する前にはあなたの許可が必要です。どこまで許可するかはあなたが選べます。

各アプリは Claude やあなたのコネクタを利用でき、元の Artifact が編集されると自動的に更新されます。これにより、ナレッジワーカーにとっても開発者にとっても、アプリの構築と保守のプロセスがシンプルになります。アプリが Claude に送信するリクエストは、ご利用プランの使用量上限にカウントされます。

Artifacts は当初、グラフやウェブページのように、共有するための成果物として始まりました。現在では、カレンダーやメールから定期的に情報を取り込むミーティング準備ページや、当日出荷が必要な注文のトラッカーなど、日々の業務のためのツールとして使われています。

仕事で頼りにしているツールであれば、ほかのアプリと同じように開けて、対応が必要なときには知らせてくれるべきです。

## インストールしたアプリでできること

インストールしたアプリは、通知を送ったり、メニューバーやシステムトレイに項目を追加したりできます。権限はアプリごとに選択でき、Team および Enterprise の管理者は、組織全体でアプリの権限やフルアクセスのオン・オフを切り替えられます。

Anthropic の社員は、これを使って次のようなものを作りました。

- [Linnet（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/HPtmhTpoSdHmRKNCJEUsoS)：レイヤー機能を備えた本格的な画像エディタ
- [Phosphor（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/UtJhPrH24ejRTTWRtohwbx)：映画のセットのために作られたかのような見た目のファイルマネージャー
- [Sift（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/BDCr8b2L6rbJQXhsztAL2x)：フォルダのルールを設定し、Claude を使ってファイルを整理し続けてくれるアプリ
- [Tern（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/7QjDeZEKPQUsDUCmFEjvyy)：Claude がそばで手助けや説明をしてくれるターミナル
- [Vitals（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/NSkw2jaPZdkdqkrVfswSGc)：コンピューターのパフォーマンスをさっと確認できるメニューバー／トレイアプリ

当社のエンジニアの 1 人が作成したその他のデモアプリは[こちら（新しいタブで開きます）](https://claude.ai/redirect/claudedotcom.v1.a2e5df5b-460e-47be-9836-1c5042872183/artifact/9j53nCVcrSdZyCHtxUZkWJ)でご覧いただけます。

![Artifacts として作られたデモアプリが並ぶレトロなピクセルアート風デスクトップ。Library アプリのメニューが開かれ、4 つのアプリウィンドウが表示されている](https://assets.claude.com/1d558aa9dd6599dfad2f4ae46a5f7bcff085d8bb.png)

## 権限

権限には 3 つのレベルがあります。

- **デフォルト：** インストールしたアプリは、ブラウザ上でできることしかできません。
- **アプリ権限：** 常に最前面に表示されるウィンドウの作成、グローバルショートカットの受け付け、通知の送信など、Claude が厳密に制御できる一般的な機能の利用をアプリが要求できます。
- **コンピューターへのフルアクセス：** プログラムの実行や、ファイルの読み取り・変更・削除を、毎回確認することなく行う許可をアプリが要求できます。

許可は現在のバージョンのアプリにのみ適用されるため、アップデートのたびに（あなた自身による編集であっても）Claude は改めて確認を求めます。なお、アプリの一部が別のウェブサイトから読み込まれている場合、その部分は Claude が再確認することなく変更される可能性があります。

フルアクセスを付与できるのは、自分で作成したアプリ、または Team および Enterprise では組織内のメンバーが作成したアプリに限られます。Anthropic はインストール前にアプリを審査していないため、フルアクセスは信頼できるアプリにのみ付与してください。

## はじめ方

作りたいアプリを Claude に説明し、Artifact として試してから「Install as app」をクリックしてください。パッケージ化や署名は不要で、あなたの Claude アカウントを使うため、API キーや別途のログインも必要ありません。

Install as app は、すべてのプランでベータ版として順次提供中です。HIPAA 対応の組織およびハイブリッドデプロイメントではご利用いただけません。Team では、フルアクセスはオフの状態で、機能自体はデフォルトでオンになっています。Enterprise では、オーナーが有効にするまでオフです。アプリを開くには、オンラインで Claude にサインインしている必要があります。Claude Docs、Slides、Sheets など、一部の Artifacts はインストールできません。

Claude for Mac または Windows をアップデートし、毎日使っている Artifact を開いて、Share メニューから「Install as app」を選んでください。
