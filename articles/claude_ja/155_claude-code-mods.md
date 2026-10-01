---
date: '2026-10-01'
final_url: https://claude.com/blog/claude-code-mods
number: 155
selector_used: main
slug: claude-code-mods
source_url: https://claude.com/blog/claude-code-mods
title: Customize Claude Code with mods
title_ja: "mods で Claude Code をカスタマイズする"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# mods で Claude Code をカスタマイズする

本日、Claude Code の動作を変更する小さな TypeScript 関数である mods(モッズ)を発表します。mod はプロンプトを書き換えたり、新しい UI を追加したり、組み込み機能を置き換えたり、まったく新しい機能を追加したりできます。mod は自分で書くこともできますし、Claude Code に書かせることもできます。mod はプラグインの中に同梱されるため、他のプラグインと同じようにインストールしたり共有したりできます。Claude Code の CLI とデスクトップアプリの両方で動作します。

mod は Claude Code 自体と同じレベルでマシンにアクセスできます。サンドボックス化されていないため、コンピューターにインストールする他のコードと同様、信頼できる提供元の mod のみをインストールするようにしてください。

mod にできることを知るには、[最初の mod を作るためのガイド](https://claude.dev/blog/getting-started-with-claude-code-mods/)をお読みください。

### mods を作った理由

開発者からは、私たちが機能をリリースするのを待たずに Claude Code の動作をより細かく制御したいという要望が寄せられていました。[フック](https://code.claude.com/docs/en/hooks)はこうした制御をある程度可能にしましたが、フックはイベントを書き換えたり、新しい UI を描画したり、機能を置き換えたりすることはできません。mods ならそれができます。

私たちは Claude Code を、自分の作業スタイルに合わせて形作れる「自分だけのもの」にしたいと考えています。そのためローンチ前に [GitHub で mods の設計を公開](https://github.com/anthropics/claude-code/issues/91870)し、開発者からフィードバックを募りました。意見を寄せてくださったすべての方に感謝します。

### mods の仕組み

Claude Code は何かを実行するたびにイベントを発行します。例えば、ツールの呼び出し、権限のリクエスト、画面の一部の描画などです。mod はこれらのイベントのいずれかにフックする関数です。mod はイベントの前、後、あるいはイベントの代わりに実行できます。また、イベントの前後両方でコードを実行する形でイベントをラップすることもできます。1つの関数で、mod は次のようなことができます。

- モデルに届く前にプロンプトを書き換える
- ツール呼び出しをブロック、書き換え、または再試行する
- 権限リクエストを承認または拒否する
- Claude がツールの出力を読む前にシークレットをマスクする

mod は見た目を変えることもできます。Claude Code が描画する画面の一部、例えばツールの結果や Claude からの質問などを編集したり置き換えたりできます。ボタンや入力欄を追加することもでき、他の mod がそれらが押されたときに反応することもできます。現時点では、mod はターミナル、デスクトップアプリ、あるいはその両方を対象にできます。

複数の mod が同じイベントにフックしている場合、読み込まれた順に実行されます。最初に読み込まれた mod がそのイベントを最初に見て、結果を最後に見ます。これにより、異なる作者の mod を重ねて使うことができます。

Claude Code を使って Claude Code を改造することもできます。Claude に mod の作成を依頼すれば、TypeScript を書き、インストールし、セッション内でホットリロードしてくれます。

### 組み込み機能を自分のものに置き換える

Claude Code の組み込み機能の一部は、すでに mod として提供されるようになっています。例えば、組み込みの `/diff` 機能は今では mod になっており、(`/plugin` で)オフにしたり、独自のバージョンに置き換えたりできます。今後も時間をかけてより多くの組み込み機能を mod に移行していく予定で、これにより Claude Code を小さなコアまで削ぎ落とし、必要なものだけを追加し直せるようになります。

### チームやエンタープライズ向けの mods

mods はプラグインの中に同梱されるため、既存のプラグイン管理がそのまま適用されます。管理者はプラグインのマーケットプレイスを許可またはブロックできます。Team プランおよび Enterprise プランでは、オーナーが管理コンソールでこれを設定します。Claude API プランおよびサードパーティ API プランでは、管理者がユーザーのマシンに管理対象設定をプッシュします。

Team プランと Enterprise プラン、および管理対象設定が適用されているマシンでは、`sec-default`(「セキュリティデフォルト」)と呼ばれる組み込みの mod が最初に読み込まれます。これにより、ユーザーがインストールした mod が、権限の拒否ルールを上書きするなどの危険な操作を行うことを防ぎます。何が制限されているかは[ソースコード](http://github.com/anthropics/claude-code/tree/main/mods)で確認できます。管理者は代わりに自分自身の mod を最初に読み込むこともできます。その場合は、`sec-default` の制限を維持するために、それを自分のリストに追加してください。

チームは mods を使って独自の制御や機能を構築することもできます。例えば次のようなものです。

- **CI/CD ステータス:** 会話の横のペインにパイプラインのステータスを表示し、ビルドの成功・失敗に応じて更新する mod
- **本番環境の安全対策:** 本番環境の設定に触れるコマンドの前に必ず確認を求める mod
- **監査ログ:** 最初に読み込まれ、他のすべての mod が行う呼び出しを記録する mod

### はじめよう

mods は本日より、Claude Code の CLI とデスクトップアプリの両方で利用できます。mod を含むプラグインは、[Claude ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.0eb37340-adda-4cfe-80d4-075232719e4a/directory)から、または CLI で `/plugin` を実行してインストールできます。mod を共有するには、プラグインにパッケージ化して[ディレクトリに提出](https://claude.ai/redirect/claudedotcom.v1.0eb37340-adda-4cfe-80d4-075232719e4a/directory/manage)してください。

自分で mod を作るには、[はじめ方ガイド](https://claude.dev/blog/getting-started-with-claude-code-mods/)または[ドキュメント](https://code.claude.com/docs/en/plugins/mods/overview)をご覧ください。
