---
date: '2026-06-22'
final_url: https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
number: 77
selector_used: main
slug: the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
source_url: https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
title: The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry
title_ja: "AWS、Google Cloud、Microsoft Foundry でフルセットの Claude Desktop 体験を"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

# AWS、Google Cloud、Microsoft Foundry でフルセットの Claude Desktop 体験を

AWS、Google Cloud、Microsoft Foundry を通じて Claude Desktop を利用している組織で、Desktop のフル体験 — チャット、Claude Cowork、Claude Code のすべて — を 1 つのアプリで使えるようになりました。

これにより IT チームは、推論を製品横断で自社環境内に保ったまま、ユーザーごとの SSO、MDM ポリシーテンプレート、オフラインインストーラのオプション、そして完全にデバイス上で実行できる M365 コネクタを伴って、Claude Desktop を組織全体にデプロイできるようになります。

推論は、お客様が構成したリージョンの、お客様のクラウド上で実行され、会話履歴はローカルに保存されます。データコネクタが到達するエンドポイントも、Anthropic に送信される集計テレメトリも、すべてお客様が制御します。

### 組織全体のための単一サーフェス

これまで、AWS、Google Cloud、Microsoft Foundry を通じて Claude Desktop を利用しているお客様がアクセスできたのは、Claude Cowork と Claude Code だけでした。今日からは、1 つのデプロイメントですべての役割をカバーでき、各サーフェスには独自のポリシーキーがあるので、誰にいつ何を提供するかをお客様が決められます。

チャットは、手早い答えや問題を考え抜くためのもの。Claude Cowork は、できれば人に任せたい仕事のためのもので、Claude が承認済みのソースを横断してリサーチし、すでにデバイスにあるファイルとともに作業して成果物を構築し、終わったら結果を見せてくれます。Claude Code は、ターミナルに張り付かずにエージェント的なコーディングを行いたいエンジニア向けです。

### デプロイメント制御

Claude Desktop を組織全体にデプロイするということは、お客様がすでに持っているシステムの中で機能させるということです。

**他の業務アプリと同じようにサインインする。** 従業員は、他のすべてに使っているのと同じ業務アカウントを使います。IAM Identity Center、Workforce Identity Federation、Microsoft Entra ID、あるいは Okta のような任意の OIDC プロバイダです。ローテーションすべき共有鍵もなく、エンドユーザーのマシンにクラウド認証情報を置くこともありません。

**すでに管理している他のアプリと同じようにデプロイする。** セットアップ UI からポリシーテンプレートをエクスポートし、Intune、GPO、Jamf を通じて配布できます。エアギャップ環境向けには、オフラインインストーラが用意されています。

**誰も触る前に、ちゃんと動くことを確かめる。** すべてのコネクタをテストし、プロバイダがどの Claude モデルを提供しているかを確認し、接続を検証する — これらすべてをロールアウト前に行えます。モデルガードによって、設定が誤っていてもルーティングは Claude 上に留まり続けます。これは GovCloud でも同様です。

**小さく始めて、採用が広がったら拡張する。** チャット、Claude Cowork、Claude Code にはそれぞれ独自のポリシーキーがあるので、非技術系のチームにはチャットと Claude Cowork を、エンジニアリングには Claude Code を渡し、各サーフェスがチームに浸透するにつれてアクセスを広げていくことができます。お客様のハードな拒否ルールは、すべてのタブにまたがって適用されます。

**仕事のある場所に Claude を連れて行く。** Microsoft 365 コネクタによって、Claude はお客様自身の Entra アプリを通じてメールやドキュメントにアクセスできます。テナントの許可リスト機能と、GCC High/DoD エンドポイントのベータサポートも用意されています。もっとも厳格なレジデンシー要件には、ローカルコネクタを使えば、接続はデバイスと Microsoft の間に留まります。

> 「私たちは、既存のクラウド環境を通じて Claude Desktop を素早くロールアウトしました — 別途ベンダー契約をする必要はありませんでした。自前の LLM Gateway によって、1 つのチームが大規模なインフラ構築なしに、世界中の数百のユーザーにこれをデプロイすることができたのです。」 - Sarang Oh, Analytics/AI Team Leader, Hanwha Solutions

### 使い始める

管理者向けには、[デプロイメントガイド](http://claude.com/docs/third-party/claude-desktop/installation) が SSO、ポリシーテンプレート、ロールアウト前の検証について案内します。あるいは担当アカウントチームにお問い合わせいただければ、ロールアウトの計画立案をお手伝いします。
