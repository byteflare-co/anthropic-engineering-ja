---
date: '2026-03-23'
final_url: https://claude.com/blog/dispatch-and-computer-use
number: 20
selector_used: main
slug: dispatch-and-computer-use
source_url: https://claude.com/blog/dispatch-and-computer-use
title: Put Claude to work on your computer
title_ja: Claude にあなたのコンピュータで作業させる
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Claude にあなたのコンピュータで作業させる

Claude Cowork と Claude Code で、Claude にあなたのコンピュータを使ってタスクを完了させることができるようになりました。Claude が必要なツールにアクセスできない場合、画面上の操作を自分で行います——ポイント、クリック、ナビゲーションを使って、ファイルを開き、ブラウザを操作し、開発ツールを自動的に実行します。セットアップは不要です。

この機能は、Claude Pro および Max サブスクライバー向けにリサーチプレビューとして利用可能です。Claude にスマートフォンからタスクを割り当てられる [Dispatch](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) との組み合わせで特にうまく機能します。

## Claude がコンピュータを使う仕組み

Claude はまず最も正確なツールから使います。Slack や Google Calendar などのサービスへのコネクタから始めます。コネクタがない場合、Claude はブラウザ、マウス、キーボード、画面を直接制御してタスクを完了します。必要に応じてスクロール、クリックして開く、探索を行いますが、常に最初にあなたの明示的な許可を求めます。

私たちはプロンプトインジェクションを含むリスクを最小限に抑えるセーフガードを備えてこの機能を構築しました。Claude がコンピュータを使用する際、私たちのシステムはモデル内のアクティベーションを自動的にスキャンし、そのような活動を検出します。また、いつでも Claude を停止する機能があり、Claude は新しいアプリケーションにアクセスする前に必ず許可を求めます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c0acb66ca028e43998d824_Cowork-Dispatch-Blog-Permissions.png)

コンピュータ操作は、Claude のコーディング能力やテキスト操作能力と比べるとまだ初期段階です。Claude は間違いを犯す可能性があり、セーフガードの改善を続けていますが、脅威も常に進化しています。信頼できるアプリから始め、機密データを扱わないことをお勧めします。このため、一部のアプリはデフォルトでアクセス制限されています。安全のベストプラクティスについては[こちら](https://support.claude.com/en/articles/14128542)をご覧ください。

## どこからでも Claude にメッセージを送る

先週、[Dispatch](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) をリリースしました。これは Claude Cowork の新機能で（Claude Code でも利用可能になりました）、スマートフォンからでもデスクトップからでも、Claude と一つの継続した会話ができます。スマートフォンで Claude にタスクを割り当て、別のことに注意を向け、コンピュータで完了した成果物を開くことができます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c0acc3f9e37117f1f547a8_Cowork-Dispatch-Blog-Code-Session.png)

Dispatch を使えば、Claude に毎朝メールを自動チェックさせたり、毎週メトリクスを取得させたり、レポートやプルリクエストのために Claude Cowork や Claude Code のセッションを起動させたりできます。

Claude の新しいコンピュータ操作機能により、Dispatch はさらに便利になります。あなたが離席している間に、Claude があなたの代わりにコンピュータを使うことができます。たとえば、電車の中にいる間にモーニングブリーフィングを作成したり、IDE で変更を加えてテストを実行し PR を出したり、3D プリントプロジェクトを当初の計画通りに進め続けたりできます。

## 始め方

Claude Cowork と Claude Code における Claude のコンピュータ操作機能はリサーチプレビュー段階です。常に完璧に動作するわけではありません。複雑なタスクでは再試行が必要な場合があり、画面を介した操作は直接統合よりも低速です。Claude Cowork のときと同様、どこでうまくいき、どこで不足があるかを学ぶため、早い段階で共有しています。

Claude Pro および Claude Max サブスクライバーが今すぐご利用いただけます。コンピュータ操作は macOS と Windows に対応しており、デスクトップアプリの設定で有効にする必要があります。また、デスクトップアプリが起動中でスリープしていないことを確認してください。その後、モバイルアプリとペアリングし、スマートフォンからタスクを引き渡してみてください。
