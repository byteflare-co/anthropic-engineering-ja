---
date: '2026-10-21'
final_url: https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes
number: 199
selector_used: article
slug: claude-security-now-scans-continuously-and-tracks-fixes
source_url: https://claude.com/blog/claude-security-now-scans-continuously-and-tracks-fixes
title: Claude Security now scans continuously and tracks fixes
title_ja: Claude Security が継続的なスキャンと修正の追跡に対応（Claude Security now scans continuously and tracks fixes）
---

[Claude Security](https://claude.com/product/claude-security) が [4 月にパブリックベータとして提供開始](https://claude.com/resources/articles/claude-security-public-beta)されて以来、数千の組織がこれを利用し、100 万件を超える脆弱性を発見してきました。

Claude Security は、誰かがスキャンを開始するのを待つのではなく、コードの変更に合わせてリポジトリを追い続け、どの検出結果が修正されたかを追跡し、チームから伝えられた環境に関する情報をもとに何が重要かを判断するようになりました。Claude Security は Claude Mythos を含む当社のモデルファミリー全体によって動作しており、Cyber Verification Program へのアクセスは必要ありません。

最新バージョンの Claude Security は、本日より Claude Enterprise のお客様向けにパブリックベータとして提供されます。組織には 2 か月間、毎月 25,000 ドル分の無料利用クレジットが付与されます。このオファーは 2026 年 12 月 31 日までの利用が対象です。利用条件の詳細は [ヘルプセンター](https://support.claude.com/en/articles/14661296-use-claude-security) でご確認いただけます。

## **継続的なモニタリングでコードの変化に追従**

スキャンが捉えるのはある一時点の状態にすぎず、コードは毎日変わります。チームからは、誰かがスケジュールを組まなくても常に最新の状態をカバーしてほしいという声が寄せられていました。

プロジェクトを作成し、Claude GitHub アプリ（GitHub Enterprise Server を含む）経由、または GitLab やその他の Git プロバイダーのアクセストークンを使ってリポジトリを接続し、それぞれのブランチとスコープを選択します。Claude はまず詳細なベースラインスキャンを実行し、その後はリスクと複雑さに応じて変更を定期的にスキャンするため、検出結果の一覧はコードの現在の状態に近いまま保たれます。

1 つのプロジェクトには複数のリポジトリを含めることができるため、クライアント側で検証されるはずだった入力をバックエンドが信頼してしまっているような、サービス間にまたがる問題も Claude が検出できます。

![Claude Security UI](https://assets.claude.com/fe39204ec42e8d48c853bf16bb08bdb19bf99a22.png)

## **修正がリリースされると検出結果は修正済みに**

ほとんどの修正は、問題を発見したツールの外で行われます。Claude Security は未解決の検出結果を変更されたコードと照合し、修正が反映された時点で修正済みとしてマークします。チームが Claude Code で修正した場合でも、別のプロセスで修正した場合でも同様です。後で Claude Security が同じ問題を再び検出した場合、その検出結果は自動的に再オープンされます。

![Claude Security UI](https://assets.claude.com/579a7fb43c95d281cf38ba2dafca75eea40a7058.png)

## **チームの知識がスキャンを形づくる**

どの環境にも、スキャナーがコードだけからは把握できないコントロールがあります。チームからは、そうしたコントロールを Claude Security に伝えたい、また相互に依存するサービスを横断して見たいという要望がありました。現在では各プロジェクトにナレッジベースがあり、コードのデプロイ方法、適用されるセキュリティポリシー、チームに新しく加わったセキュリティエンジニアが知っておくべきことなどを記述できます。

![Claude Security UI](https://assets.claude.com/440f4c1037a629695ec66eb0a17c218782b51d35.png)

さらに Claude Security は、コードから脅威モデルを生成し、チームはそれをレビュー・編集できます。以降のスキャンでは、この脅威モデルを使って何を指摘すべきかを判断します。追加されたコンテキストにより、Claude Security は環境側ですでに対処されているリスクをスキップすることもできます。

## **すべての検出結果に深刻度と悪用経路を提示**

各検出結果には、プロジェクトの脅威モデルに照らして判定された深刻度と、攻撃者がどのようにして脆弱なコードに到達しうるかの説明が付きます。これにより、チームは実際に到達可能なものから優先して修正できます。検出結果には攻撃経路の図が含まれることもあります。

![Claude Security UI](https://assets.claude.com/58c85ec0105dd3b16b367ae71e70c14db55e6d4f.png)

## **検出結果を既存ツールへ連携、大規模展開のためのコントロールも**

新しい API を使うと、Claude Security を既存のワークフローに統合できます。プロジェクトや検出結果の一覧表示・参照、検出結果の解決・再オープン、プロジェクトとそのリポジトリの作成・管理が可能です。ユーザーは Claude Security の設定で個人用アクセストークンを作成でき、そのトークンはユーザー本人が閲覧・変更できる範囲にしかアクセスできません。また、Webhook を使えば新しい検出結果が発生したときにシステムへ通知できます。

Claude Security は、[Claude.ai](http://claude.ai/redirect/claudedotcom.v1.ef4d825f-fe4d-4a33-ae56-a5f4ae1ddbad) と Claude Code で MCP コネクタとしても利用できます。エンジニアは同じセッション内で、検出結果を呼び出し、それについて Claude に質問し、修正を開始し、解決済みとしてマークできます。

新しいロールベースのアクセス制御により、管理者はプロジェクトの閲覧、検出結果のトリアージ、プロジェクトの作成をそれぞれ誰が行えるかを決められます。組織は、全員にプロジェクト作成権限を与えることなく、コードを所有するより多くのチームに Claude Security を開放できます。

## **はじめに**

最新バージョンの [Claude Security](http://claude.ai/redirect/claudedotcom.v1.ef4d825f-fe4d-4a33-ae56-a5f4ae1ddbad/security) は、本日より Claude Enterprise のお客様向けにパブリックベータとして提供されます。管理者は管理コンソールで有効化し、チーム内の誰がアクセスできるかを設定できます。

最初のプロジェクトのセットアップには [Getting Started Guide](https://academy.claude.com/tutorials/getting-started-with-claude-security) をご利用ください。詳細は [ヘルプセンター](https://support.claude.com/en/articles/14661296-use-claude-security) をご覧ください。

*組織には 2 か月間、毎月 25,000 ドル分の無料利用クレジットが付与されます。このオファーは 2026 年 12 月 31 日までの利用が対象です。利用条件の詳細は [ヘルプセンター](https://support.claude.com/en/articles/14661296-use-claude-security) でご確認いただけます。*

> 「Claude Security は、同時期に実施した従来のペネトレーションテストでは見逃されていた重大な問題を数多く発見しました。そのうちのいくつかは、実環境で悪用されていれば大きな影響を及ぼしていたはずです。」

Jon Donovan, Software Engineer, IonQ

> 「Claude Security は一度コードをスキャンしてベースラインを設定しました。今ではコードの変更に追従しており、チームは別のツールに切り替えることなく Claude の中で直接問題を修正しています。」

Jake Meredith, Product Security, Gusto

> 「API と MCP の追加はまさにゲームチェンジャーであり、IonQ の Product Security チームが Claude Security をさらに運用に組み込んでいくための道筋になるでしょう。」

Joe Coniglio, Security Engineer, IonQ

> 「Claude Security は、他のどのツールも捉えられなかった数多くのロジック上の欠陥を発見しました。外部ユーザーが実際に到達できる範囲に焦点を当てた独自のリスクポリシーを脅威モデルに書き込んでからは、検出結果が単なる深刻度スコアではなく、私たちの優先順位の付け方に沿ったものになりました。」

Nathan Hunstad, Director of Security, Vanta
