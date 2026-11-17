---
date: '2026-11-13'
final_url: https://claude.com/resources/articles/claude-tag-guide-for-startups
number: 171
selector_used: article
slug: claude-tag-guide-for-startups
source_url: https://claude.com/blog/claude-tag-guide-for-startups
title: The Claude Tag guide for startups
title_ja: スタートアップのための Claude Tag ガイド
---

スタートアップは、少人数のチームで一人が何役もこなしながら、速いペースで仕事を進めることがよくあります。多くの点で、[Claude Tag](https://claude.com/product/tag)（ベータ版）はスタートアップの働き方に適しています。コンテキストが集まっている Slack チャンネルに @Claude で Claude を招き入れ、コネクタを追加すれば、チーム全員でタスクを割り当て、方向づけていくことができます。

Claude Tag を使い始めたばかりのスタートアップチームから最もよく寄せられる質問のひとつが、「最初にどのチャンネルに Claude を追加すべきか？」というものです。この問いに答えるため、私たちは急成長中のスタートアップ 8 社に話を聞き、各社のチーム内で Claude Tag がどのように機能しているかを調べました。

### インサイトを提供してくれた企業

- [![Kikoff](https://assets.claude.com/58247642907b2621ae6d414ecb7dc6714bcf1e03.svg)](https://kikoff.com/)
- [![Campfire](https://assets.claude.com/547f3af27e33331c1409324c549d765f790ca68d.svg)](https://campfire.ai/)
- [![NavigateAI](https://assets.claude.com/5348eaceef888ace36b50da1a6c9f8126ad2f1bb.svg)](https://www.navigate.ai/)
- [![Moritz](https://assets.claude.com/6b65c9f5d995c188f6273248826bbe5fc494b4ff.svg)](https://www.moritzlegal.com/)
- [![Flagler Health](https://assets.claude.com/157cc2437bd370ee12b67e1ba178b5cded79cbfc.svg)](https://www.flaglerhealth.io/)
- [![Valence](https://assets.claude.com/5855d903e0e618842304aaf2e9b02e7d648a90e2.png)](https://www.valence.co/)
- [![Orderful](https://assets.claude.com/dcd269d39d743ba04bbf4a2e803b60367c0d6b88.svg)](https://www.orderful.com/?utm_source=anthropic&utm_medium=referral&utm_campaign=claude_tag_guide)
- [![Descript](https://assets.claude.com/05128b9e935b6625beecc1bc4c6fa08814473e3e.svg)](https://www.descript.com/)

話を聞いたのは、法律事務所の再発明から次世代の資源計画ソフトウェアの構築まで、さまざまなビジョンを持つ企業のリーダーたちです。ほぼすべてのチャンネルに Claude を追加している企業もあれば、1〜2 個の特定のユースケースに深く絞り込んでいる企業もありました。

| 企業 | オンコール | スレッドから PR へ | 社内の頭脳 | セルフサービスのデータ分析 | 定型レポート |
| --- | --- | --- | --- | --- | --- |
| Kikoff | ● | ● |  | ● | ● |
| NavigateAI | ● | ● | ● |  | ● |
| Campfire | ● | ● | ● |  |  |
| Flagler Health | ● | ● | ● |  |  |
| Moritz |  |  | ● |  | ● |
| Orderful | ● | ● | ● | ● |  |
| Valence |  | ● | ● |  | ● |
| Descript |  | ● |  | ● | ● |

しかし、話を聞いた全員に共通していたのは、数分間の Claude Tag とのやり取りが何日分もの作業に取って代わったり、本来なら埋もれたままだったはずのインサイトを掘り起こしたりしたことに気づいた「なるほど！」という瞬間があったことです。

このガイドでは、そのなかでも特によく見られたものを、実践的な導入の詳細とともに紹介します。創業者が自分のチームにとって大きな効果をもたらすユースケースを見つけ、展開できるよう構成しています。話を聞いたスタートアップでどれほどの効果があったのか、いくつか例を挙げます。

![Campfire](https://assets.claude.com/547f3af27e33331c1409324c549d765f790ca68d.svg)

**21 分**：Slack でのメンションから PR のオープンまで

![NavigateAI](https://assets.claude.com/5348eaceef888ace36b50da1a6c9f8126ad2f1bb.svg)

**134 件**：Slack スレッドからマージされたプルリクエスト

![Moritz](https://assets.claude.com/6b65c9f5d995c188f6273248826bbe5fc494b4ff.svg)

**5 分**：毎日のシフト終了時の報告にかかる時間（以前は 1 時間）

![Valence](https://assets.claude.com/5855d903e0e618842304aaf2e9b02e7d648a90e2.png)

**1 時間未満**：クライアントからの依頼からノーコードでの解決まで

![Orderful](https://assets.claude.com/dcd269d39d743ba04bbf4a2e803b60367c0d6b88.svg)

**2 日**：Slack での質問から本番リリースまで

![Descript](https://assets.claude.com/05128b9e935b6625beecc1bc4c6fa08814473e3e.svg)

**数日から数時間へ**：定期レポートの準備にかかる時間

このガイドでは、先進的なスタートアップが Claude Tag を活用している代表的なユースケース、チャンネル、そして共通するインサイトを紹介します。

---

## Claude をタグ付けすべき主なチャンネル

話を聞いたスタートアップ 8 社は Slack 全体で Claude Tag を使っていますが、最初に始める場所として何度も挙がったチャンネルがいくつかありました。

## 01 オンコールを担う Claude

設定例：

チャンネル

`#on-call` `#alerts-ci` `#deploy-watch` `#support-escalations`

コネクタ

GitHub、GitLab、Sentry、dbt、PagerDuty、Linear、Datadog、Jira、Grafana、incident.io

スレッドとルーティン

インシデント対応、朝のインシデントダイジェスト、月曜日のオンコール引き継ぎ、毎日のヘルスサマリー、毎時のインシデント振り返り

最初の指示の例

> @Claude remember for this channel: monitor alerts and immediately triage each one in its own thread. Check for an existing ticket. Query the data first, then theorize, and separate what you verified from what you inferred. If it's real, name the likely root cause with links, tag the owner, and open a draft PR only if the fix is contained. If no action is needed, say so. After each incident, add what you learned to [lessons file].

（訳：@Claude このチャンネルでは次のことを覚えておいて。アラートを監視し、それぞれを専用のスレッドですぐにトリアージすること。既存のチケットがないか確認すること。まずデータを照会してから仮説を立て、検証したことと推測したことを区別すること。本物の問題であれば、リンク付きで考えられる根本原因を示し、オーナーをタグ付けし、修正が限定的な場合にのみドラフト PR を作成すること。対応不要であれば、そう伝えること。各インシデントの後には、学んだことを [lessons file] に追記すること。）

トリアージ用のチャンネルは、ノイズが多いことで知られています。Sentry のエラー、Datadog のアラート、顧客からのバグ報告、サポート依頼などが絶え間なく割り込み、ノイズの中からシグナルを見つけ出すのが難しくなっています。チームが Claude に最初に任せるのは、たいていこの作業です。

Claude を[ファーストレスポンダー](https://claude.com/resources/articles/ai-ci-cd-on-call)としてチャンネルに置くと、オンコールのエンジニアがノートパソコンを開く前に、一次対応が済んでいることもよくあります。Claude は届いた項目を順に読み、コードベースやアクセスできるツールを調べ、わかったことを共有します。修正が限定的であればドラフト PR を作成し、そうでなければ調査結果を添えて適切な担当者に問題を回します。こうした構成では、各修正はマージ前に人がレビューし、本当に新しい問題についてのみ、人が自ら調査を始める必要があります。

財務チーム向けの AI ネイティブな ERP を構築している Campfire では、あるエンジニアが「自社の AI エージェントが生成した回答の一部がユーザーに届いていない」という報告に Claude をタグ付けしました。21 分後には Claude が PR を作成し、その日の午後にはマージされました。

### Kikoff：すべてのトリアージチャンネルにファーストレスポンダーを

Kikoff は、消費者の信用構築、流動性ニーズの解決、経済的な安定の実現を支援するフィンテックのスタートアップです。Claude Tag は、社内の次のようなトリアージチャンネルでファーストレスポンダーを務めています。

- `#deploys`：リリースのたびに何を監視すべきかを Claude が判断し、そのリリースで壊れたものがあれば知らせます。
- `#alerts-ci`：ビルドが失敗すると、Claude が原因を突き止め、修正をドラフト PR として提案します。
- `#alerts-sentry-backend`：Sentry の例外やクラッシュの一次対応を Claude が担います。
- `#dog-fooding`：社員がドッグフーディング中に報告した事項を Claude が調査し、適切なオーナーをタグ付けします。
- `#support`：サポートチケットの一次対応を Claude が担います。

Kikoff では当初、メンションされたときにだけ Claude が会話に参加する形で始めましたが、最大の成果が出たのは、Claude が自発的に会話に加わることをチームが許可してからでした。サインアップが壊れたとき、Claude はその原因をバックエンドの変更までたどり、影響範囲を見積もり、修正を担当するチームを特定し、その間アプリが穏当にエラー処理できるようにするドラフト PR を作成しました。

![Claude がサインアップの不具合を知らせ、原因、影響範囲、修正担当者、ドラフト PR を示している Slack メッセージ。](https://assets.claude.com/2b0f5523a07eac627cacb997fda4823706524505.png)

Claude がサインアップの不具合を知らせ、原因をバックエンドの変更までたどり、影響範囲を見積もり、修正を担当するチームを特定し、アプリが穏当にエラー処理できるようにするドラフト PR を作成しています。Kikoff での会話を再現したものです。名前と画像は変更しています。Kikoff の許可を得て掲載しています。

![](https://assets.claude.com/a6d8144b8cb41f297d29241e3e22bcb6898594d2.jpg?w=168&q=75&fm=webp&fit=max)
> 「モニターや人間より先に Claude が問題を見つけると、いつもワクワクします。一人の人間が自分で把握できるコンテキストには限りがあります。Claude Tag はコンテキストの一部を整理して受け持ってくれるので、私たちは成果の管理に集中できます。」

Alex Dejeu 氏（Kikoff、エンジニアリングマネージャー）

### NavigateAI：断片化したコンテキストからバグを修正する

NavigateAI は、建設現場のチーム向けに AI コパイロットを構築しています。同社は約 90 のチャンネルで Claude Tag を運用し、アラートのトリアージ、バグバッシュ、ちょっとした機能開発、サポートのエスカレーションに活用しています。6 月以降、Claude は Slack のスレッドから直接約 223 件の PR を作成し、そのうち 134 件がマージされました。PR のオープンからマージまでの時間の中央値は 2 時間です。

NavigateAI にとって、トリアージは特に価値の高いユースケースとなっています。Claude は非常に多くのコンテキストを持っているため、一見しただけでは見逃されがちな、直感に反する根本原因を見つけ出すことができます。

![](https://assets.claude.com/8146467a01dc8932c5071f62327bec5e7fa4b7bc.jpg?w=168&q=75&fm=webp&fit=max)
> 「Claude Tag で一番『すごい！』と思ったのは、負荷の問題をデバッグしていたときのことです。ある顧客の呼び出しが失敗していたので、その顧客が原因のように見えていました。普通の人間なら、そのままその顧客を追いかけ続けるでしょう。しかし Claude は他の多くのデータソースにアクセスできたので、同じ時間帯に動いていた、計測されていない社内の cron ジョブが原因だと突き止めたのです。」

Mike Chen 氏（NavigateAI、エンジニアリング責任者）

Claude の導入により、問題解決までの平均時間は改善しました。あるケースでは、Sentry のアラートが発報されてから 8 分後に Claude が根本原因を特定し、アラートから 93 分後には修正がマージされました。

「動きの速いスタートアップは、たいてい構造よりもスピードを選ばざるを得ません。Claude Tag はその両方を与えてくれます。あらゆるツールをまたいで点と点をつなぐ頭脳のような存在なので、自分たちで作り込まなくても構造が手に入るのです」と Mike 氏は語ります。

## 02 スレッドから PR へ

設定例：

チャンネル

`#quick-wins` `#bug-bash` `#product-feedback` `#feature-requests` `#ux-papercuts` `#tech-debt` `#design-polish`

コネクタ

GitHub、GitLab、Linear、Jira、Confluence、Notion、Figma、Sentry

スレッドとルーティン

1 スレッドにつき 1 リクエスト、週次のバックログ整理、毎日の PR まとめ、週次のリリース振り返り

最初の指示の例

> @Claude remember for this channel: when someone describes a bug or small feature, work on it in its own thread. Check for an existing ticket and read the related code first. If details are missing, ask for them or for a real example instead of guessing. If the change is small and contained, open a draft PR with a short summary of what changed and how you tested it. Never merge; a person reviews and approves. If it's too big or risky, say why and suggest a ticket.

（訳：@Claude このチャンネルでは次のことを覚えておいて。誰かがバグや小さな機能について説明したら、専用のスレッドで取り組むこと。まず既存のチケットを確認し、関連するコードを読むこと。詳細が足りない場合は、推測せずに詳細や実例を求めること。変更が小さく限定的であれば、何を変更し、どうテストしたかの短い要約を付けてドラフト PR を作成すること。マージは決して行わないこと。レビューと承認は人が行う。変更が大きすぎたりリスクが高すぎたりする場合は、その理由を述べ、チケットの作成を提案すること。）

スピードはスタートアップの最大の強みのひとつですが、ユーザーを喜ばせる小さな要望は、往々にしてどさくさに紛れて埋もれてしまいます。こうした情報は顧客対応チームが集めて Slack に投稿することが多く、見落とされなかったとしても、最終的には Linear や Jira に登録され、何百もの他のチケットと優先順位を競うことになります。

Claude Tag を使えば、技術職かどうかに関係なく、誰でも PR の下書きを作れます。スレッドでアイデアを出し、同じ場所でプロダクト、エンジニアリング、GTM の各チームからリアルタイムにフィードバックを受ければ、Claude がそのスレッドを全員の意見を反映したドラフト PR に変えてくれます。

話を聞いたスタートアップの多くは、Claude Tag を「軽くて喜ばれる」機能の追加や、レビューはすぐ済むものの普段なら優先されない、細かな使いにくさ（ペーパーカット）の解消に使っていました。

### Orderful：Slack でのやり取りから 2 日で本番機能に

Orderful は、API またはブラウザから直接、企業と取引先をつなぐ EDI プラットフォームです。顧客はこのプラットフォームを通じて、取引先と標準文書をやり取りしています。

ある文書タイプ「753」は、Orderful の Web アプリでサポートされていませんでした。この要望はバックログに残ったままで、ある大手小売業者向けの出荷が遅れていました。

アカウントマネージャーが Slack でフォローアップしたとき、PM が Claude をタグ付けしました。「@Claude、これを作ってほしい」。Claude は実際のフォーマットに沿って作れるよう文書の実例を求め、そのうえで 753 のサポートを追加するドラフト PR を作成しました。

![実際の 753 トランザクションで印刷ビューの修正が機能することを Claude が確認し、チームメイトがリアクションしている Slack スレッド。](https://assets.claude.com/1921c58bc091958f185f0fc960870d6dd18f7bd3.png)

Claude が実際の 753 トランザクションで修正が機能することを確認しています。名前と画像は変更しています。Orderful の許可を得て掲載しています。

翌朝、Claude は小売業者からの応答にあたる関連文書「754」のチケットを起票し、2 つ目の PR を作成しました。Slack でのやり取りから約 2 日後には、両方とも本番環境にリリースされていました。

「以前なら数週間から数か月かかっていたことが、Slack での会話だけで済んだのです」と Orderful の CTO、Piers MacDonald 氏は語ります。「価値を証明しにくい軽めの機能は、以前はバックログで止まっていました。今ではそこから抜け出す道があります。」

### Valence：機能要望から展開まで

Valence は世界最大級の雇用主と協力し、AI コーチ「Nadia」によって企業の人材とパフォーマンスをつないでいます。ある重要なクライアントから依頼された緊急のプロダクト変更への対応方法を Valence のエンジニアが Slack で説明したとき、Claude は単に指示に従うだけではありませんでした。同じ設定が 2 か所に存在していたため、追加で必要な変更があることを指摘したのです。Claude がいなければ、最初の変更は不完全なままだったでしょう。

![Valence のエンジニアが Claude に変更の確認を求め、Claude がそれは 2 つの変更だと返答している Slack のやり取り。](https://assets.claude.com/20696126082a923a5dc573f7571aadb71caf617e.png)

依頼された変更が実際には 2 つの変更であることを Claude が指摘しています。Valence の許可を得て掲載しています。

![](https://assets.claude.com/3a62ff7d092a4f9d3cd4b74f49c1aa2e0a9a8340.jpg?w=168&q=75&fm=webp&fit=max)
> 「Claude は専門家の言うことにただ同意するだけではありませんでした。人間が見失いがちな、設定の重複を見つけてくれたのです。」

Sameer Bansal 氏（Valence、プリンシパル AI エンジニア）

別のケースでは、あるクライアントから緊急でカスタマイズの依頼がありました。Claude はコードを確認し、エンジニアと協力して、コードを変更せずに対応できることを確かめました。1 時間もしないうちに、チームメイトはクライアント向けの解決策を用意できました。

## 03 社内の頭脳

設定例：

チャンネル

`#ask-anything` `#company-wiki` `#product-questions`

コネクタ

GitHub、Notion、Google Drive、Linear、Jira、Confluence、Granola、Metabase

スレッドとルーティン

1 スレッドにつき 1 つの質問、意思決定ログの更新、週次の古いドキュメントのチェック、繰り返される質問のまとめ

最初の指示の例

> @Claude remember for this channel: answer questions from our code, docs and past threads, and link your sources. If sources disagree, check the code, give the current answer, and flag the stale doc. If you aren’t sure, say so and tag the owner. When a thread reaches a decision, record it in [docs location]. Anything going to a client needs a human check first.

（訳：@Claude このチャンネルでは次のことを覚えておいて。コード、ドキュメント、過去のスレッドをもとに質問に答え、情報源へのリンクを示すこと。情報源同士が食い違う場合はコードを確認し、現時点での答えを示したうえで、古くなったドキュメントを指摘すること。確信がない場合はそう伝え、オーナーをタグ付けすること。スレッドで結論が出たら、[docs location] に記録すること。クライアントに送るものは、必ず先に人が確認すること。）

スタートアップでは、製品の請求コードの細かな仕様からオンボーディング資料の置き場所まで、組織の知識が人の頭の中にしかないことがよくあります。

話を聞いたスタートアップの多くで、Claude Tag は社内の頭脳になっています。Claude は情報源を添えて回答し、確信が持てない場合はオーナーをタグ付けします。知識を最新の状態に保つ役割も担います。スレッドで結論が出れば、Claude はその日のうちにドキュメントに記録し、古くなったドキュメントを指摘できます。

![チームメイトが Claude に何が決まったかを尋ね、Claude がチャンネルの内容を要約している Slack チャンネル。](https://assets.claude.com/a4edb94f8444bc21a1fc8aa3d489f15358328129.png)

やり取りの例。

### Moritz：受付からスタッフ配置まで、生きた唯一の情報源

Moritz は AI ネイティブな法律事務所で、契約書を即日で仕上げることを約束しています。Moritz によれば、業界標準は少なくとも 3 週間です。受付や見積もりからスタッフ配置、フォローアップまで、法律業務を取り巻くあらゆることが Slack 上にあり、案件ごとにスレッドが、クライアントごとにチャンネルが用意されています。

今では CEO からパラリーガルまで、誰もがまず Claude に尋ねます。Slack で検索するのに最大 30 分かかっていた質問が、2 分以内に答えられるようになりました。シフト終了時の報告は、その日のスレッドから下書きされるようになり、約 1 時間かかっていた取りまとめ作業が 5 分の編集作業になりました。

その時間は法律業務に戻されます。Claude Tag は、フォローアップの質問、リマインダー、状況報告など、案件にまつわる事務作業を担当します。クライアントの文書や、Moritz の弁護士との秘匿特権のある会話にはアクセスできません。

![](https://assets.claude.com/39f487100b408fabef0773334afb8c15e050525f.jpg?w=168&q=75&fm=webp&fit=max)
> 「44 か国で業務を行う事務所では、誰も機能を作ろうとは思わないような単発の質問が、毎月何百件も発生します。Claude Tag は、Slack にある私たち自身の履歴からそれらに答えてくれます。すべての回答がリンク付きのスレッドとして残るので、組織の記憶が積み重なっていきます。」

Stefan Mandaric 氏（Moritz、共同創業者兼 CTO）

### Campfire：オンデマンドのカスタマーエクスペリエンス

ある Slack チャンネルが特に「爆発的な人気」を集めました。CX（カスタマーエクスペリエンス）チャンネルです。営業チームは「10 人に別々に問い合わせる」代わりに、このチャンネルを「見込み客との会話中に特定の機能を確認する」ために使っています。

この種のチャンネルが特に効果的なのは、顧客が関心を向けているその場で営業担当者が答えられ、初期の顧客との会話において、より自立して自信を持って動けるようになるからです。

![](https://assets.claude.com/921fd10de481a1094bdd4b483f52933e68791fb2.jpg?w=168&q=75&fm=webp&fit=max)
> 「Claude Tag は基本的に、私たちの中央ナレッジベースとして機能しています。」

Nancy Jin 氏（Campfire、AI エンジニアリングマネージャー）

## 04 セルフサービスのデータ分析

設定例：

チャンネル

`#data-requests` `#ask-revops` `#metric-definitions`

コネクタ

dbt、GitHub、Metabase、BigQuery、Snowflake、Databricks、Notion

スレッドとルーティン

1 スレッドにつき 1 つの質問、週次のスタンドアップ前レポート、ローンチや実験の結果レポート、パイプライン障害のトリアージ、新しい質問のトリアージ

最初の指示の例

> @Claude remember for this channel: answer from our governed models and the definitions in [data skills repo]. If the data isn’t covered there, say it’s unvalidated instead of guessing. Lead with the answer, then give the number, what’s driving it, and any caveat. Check recent incidents, releases, and Slack discussions before explaining a change. If a metric’s definition is unclear, ask which one we mean. For anything important, share your plan or SQL before you run it. Separate what you verified from what you assumed, and list any open data quality warnings at the end of your answer. If someone finds a mistake, draft a fix for a data team member to review. If a question comes up twice, suggest scheduling it.

（訳：@Claude このチャンネルでは次のことを覚えておいて。ガバナンスの効いたモデルと [data skills repo] にある定義に基づいて答えること。そこでカバーされていないデータについては、推測せずに未検証であると伝えること。まず結論を述べ、次に数値、その要因、注意点を示すこと。変化を説明する前に、最近のインシデント、リリース、Slack での議論を確認すること。指標の定義が不明確な場合は、どの定義を指しているのか尋ねること。重要な事項については、実行前に計画や SQL を共有すること。検証したことと仮定したことを区別し、未解決のデータ品質に関する警告があれば回答の最後に列挙すること。誰かが誤りを見つけたら、データチームのメンバーがレビューできるよう修正案を作成すること。同じ質問が 2 回出たら、定期実行するよう提案すること。）

急成長中のスタートアップでは、あらゆる部門が数字を求め、データチームは誰の依頼を先に処理するかを決めなければなりません。Claude Tag をデータに接続すれば、誰でもデータチームの順番待ちをせずに、平易な英語で質問できます。

これは私たち自身も採用しているユースケースです。[あるデータチャンネルでは、1 か月の間に投稿された質問の 75% 以上に Claude Tag が回答し、その多くは 1〜2 分以内でした](https://claude.com/resources/articles/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)。Claude Tag は、ガバナンスの効いたデータと、アナリストが使っているのと同じ定義に基づいて動作します。これらの定義はバージョン管理されたリポジトリにあり、Claude は会話のたびにそれを読み直します。

![Claude Tag が、データウェアハウスで何が変動したかと、ナレッジインデックスから得たその理由とを組み合わせ、サインアップ数の落ち込みについてひとつの回答にまとめる様子を示した図。](https://assets.claude.com/4cf8ac80c074a4f3b28e78bd605ec9a881a611a8.png)

「Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions」より。

### Descript：アドホックなデータ依頼への対応

Descript は AI を活用した動画編集プラットフォームです。現在、Claude Tag はデータ依頼や初期分析の最初の窓口になっています。プロダクト、グロース、RevOps、財務の各チームが Slack で質問し、Descript の dbt モデルに基づいた回答を得ています。

![](https://assets.claude.com/93f058c356e58c0f49205fd19e8f3585533542bf.jpg?w=168&q=75&fm=webp&fit=max)
> 「以前は複雑な SQL を書いて、毎週あるいは毎月、手作業で数字を更新していました。今では、データチームのダッシュボードのいくつかを自分で作った Claude のアーティファクトに置き換え、手作業で更新する必要もなくなりました。」

Daisy Zhang 氏（Descript、グロースマーケティング責任者）

Daisy 氏の定期レポートの準備は、数日から数時間に短縮されました。

たとえばグロースチームは、ライフサイクルのサブスクリプションがなぜ減少したのか、有料検索がラストタッチの貢献を他のチャンネルに奪われていないか、セルフサービスのアカウントがエンタープライズの商談になるまでにどれくらいかかるのか、といった質問をしています。データチームは、Claude が生成したアーティファクトを追跡して、チーム全体でどのデータ資産が最も重要なのかを把握し、自分たちの時間は戦略的な問いや、セルフサービスを機能させるためのコンテキスト構築に使っています。

![](https://assets.claude.com/04cc4542c1f0cb9d273d22b2597f8e856abe542a.jpg?w=168&q=75&fm=webp&fit=max)
> 「ビジネスインテリジェンスの約束は、昔からビジネスユーザーのためのセルフサービスでした。データに関する膨大なコンテキストを持たせて Claude Tag を設定するまで、それが本当に実現したのを見たことはありませんでした。」

Jen Huhn 氏（Descript、マネタイゼーション PM）

### Orderful：質問からダッシュボードへ

Orderful では、セルフサービス分析が対話型の分析から本格的なデータ構築にまで及んでいます。誰でも Slack での質問から、本番環境にマージされたダッシュボードまでたどり着けます。鍵となるのは、合意済みの定義や指標を記述したセマンティックレイヤーです。これにより、すべての回答とすべての構築で同じ定義が使われます。

![](https://assets.claude.com/ae41953c096037ea0d3a369b9af1e1f52378367a.jpg?w=168&q=75&fm=webp&fit=max)
> 「出力を信頼できるのは、セマンティックレイヤーが SQL を制約し、CI がビルドをゲートし、定義について合意するプロセスがあるからです。これらがなければ、もっともらしく見える誤った答えが返ってきます。こうしたガードレールを整えてしまえば、Claude Tag の接続は 30 分もかかりませんでした。今ではチームメイトが一人で作業するのではなく、共有の Slack スレッドで一緒に構築しています。」

Piers MacDonald 氏（Orderful、CTO）

## 05 レポートと引き継ぎ

設定例：

チャンネル

`#sales-pipeline` `#customer-handoffs` `#standup-summary` `#qbr-prep`

コネクタ

Notion、Google Drive、Gong、Salesforce、Gainsight

スレッドとルーティン

終業時の状況報告の下書き、QBR 前のブリーフィング、商談の引き継ぎ

最初の指示の例

> @Claude remember for this channel: draft each recurring report from our threads, docs, and data, and link your sources. Lead with what changed and what needs a decision. Separate what you verified from what you assumed, and flag anything missing instead of filling the gap. Post the draft in its own thread for [owner] to edit. Nothing goes out until a person approves it. If a report keeps getting the same edits, suggest updating these instructions.

（訳：@Claude このチャンネルでは次のことを覚えておいて。スレッド、ドキュメント、データをもとに各定期レポートの下書きを作成し、情報源へのリンクを示すこと。何が変わったのか、何について判断が必要なのかを最初に述べること。検証したことと仮定したことを区別し、欠けている情報は埋め合わせずに指摘すること。下書きは [owner] が編集できるよう専用のスレッドに投稿すること。人が承認するまで何も外部に出さないこと。レポートに同じ修正が繰り返し入る場合は、この指示を更新するよう提案すること。）

ここまで紹介した例の多くは受動的なものでした。何かが起きて、Claude がそれに対応するというものです。定型レポートは、チームメイトが定期的な成果物を受け持つのと同じように、Claude がスケジュールに沿って受け持つ仕事です。

![チームメイトが Claude に月曜日のパイプライン更新を依頼し、Claude がグラフ付きの週次ダイジェストを投稿している Slack のやり取り。](https://assets.claude.com/8d3d8fd8252fc93f3bd80bb28ae0a728142a7ef2.png)

Claude Tag でルーティンを使う例。

求める成果を一度説明すれば、Claude が毎回それを実行し、チームがすでに作業している場所に結果を投稿します。

### Valence：商談レビューと引き継ぎ

Valence は、四半期ごとのビジネスレビュー（QBR）の前に、顧客の健全性、進行中の商談、阻害要因、次のステップについて Claude がチームに説明するよう設定を進めています。また、商談成立時の営業からカスタマーサクセスへの引き継ぎを、よりスムーズにする取り組みも進めています。Claude はエンゲージメント全体の詳細を集約することでチームの時間を節約し、見落とされがちな重要事項を見つけることもよくあります。

「商談が成立すると、Tag が商談の履歴、通話、契約書から引き継ぎ資料を作成します。誰が誰なのか、何を約束したのか、何がカスタマイズされているのか、何が未解決なのか。カスタマーサクセスは、キックオフの前にそれをレビューします」と Sameer 氏は語ります。

## 06 導入チェックリスト

以下のチェックリストは、これらのスタートアップチームのベストプラクティスをまとめたものです。自社のワークフローに取り入れてください。

### ローンチ前

**前提条件を確認する。**

Claude Tag は Claude Team プランと Enterprise プランでパブリックベータとして提供されており、Free、Pro、Max プランでは利用できません。両者を接続するには、Claude 組織のオーナーと Slack ワークスペースの管理者が必要です。また、管理者がルーティンを有効にする必要があり、Team プランでは Claude が応答する前に利用クレジットが必要です。

**バンドルで Claude のアクセス権を設定する。**

チャンネル内では、Claude は誰かの個人ログインではなくサービスアカウントを使い、独自の[エージェントアイデンティティ](https://claude.com/docs/claude-tag/concepts/agent-identity)で動作します。Claude に必要なコネクタ、リポジトリ、指示を[バンドル](https://claude.com/docs/claude-tag/admins/add-connections)にまとめ、組織全体、ワークスペース単位、またはチャンネル単位で割り当てます。これによって、各場所で Claude が何にアクセスできるかが決まり、チャンネル内の全員が同じアクセス権を得ます。最初は範囲を狭くし、最初のチャンネルの仕事に必要なものだけに絞りましょう。

**プライベートチャンネルで試す。**

話を聞いたスタートアップのほぼ半数は、少人数の部門横断チームがプライベートチャンネルで試すところから Claude Tag の活用を始めていました。「さまざまな役割のメンバーでプライベートに始めて、それからグループチャンネルに移りましょう」と Sameer 氏は言います。

**境界を決める。**

デフォルトでは、Slack ワークスペースの誰もが、Claude アカウントを持っていなくても Claude を使えます。[アクセスを組織内に制限](https://claude.com/docs/claude-tag/admins/restrict-access)し、検索対象を Claude が参加しているチャンネルに限定することもできます。Enterprise プランでは、特定のロールや選んだチャンネルにアクセスを制限することも可能です。

Claude にできること、そして決してしてはならないことについて、明確な期待値を設定しましょう。話を聞いたチームのいくつかは、Claude にドラフト PR の作成を許可していますが、レビューとマージは人が行います。Orderful では、「インフラの変更、監査、機密データ」は Tag ではなく [Claude Code](https://claude.com/resources/articles/claude-code-guide-for-startups) が扱います。「複数のサービスにまたがる PR」のような「難しい判断」については、Claude はセカンドオピニオンを求めます。Moritz は、クライアントの文書や弁護士との秘匿特権のある会話へのアクセスを Claude Tag に与えていません。

**セキュリティレビューを早めに始める。**

よく挙がる質問はデータの保持期間と、Claude が何にアクセスできるかの 2 点で、[セキュリティ](https://claude.com/docs/claude-tag/concepts/security-and-data)と[データライフサイクル](https://claude.com/docs/claude-tag/concepts/data-lifecycle)のページで両方に答えています。Claude Tag は、ゼロデータ保持（ZDR）が有効な組織、顧客管理の暗号化（CMEK）ポリシーを適用している組織、HIPAA 構成の組織では利用できず、Business Associate Agreement（BAA）の対象にもなっていないため、展開を計画する前に確認してください。

**予算とアラートを設定する。**

Claude Tag は使用量に応じて課金されるため、早めに話し合っておけば、利用が広がったときに驚かずに済みます。全体およびチャンネルごとに[支出上限を設定](https://claude.com/docs/claude-tag/admins/set-spend-limit)でき、チャンネルごとにモデルを選び、Enterprise Analytics API を使ってユーザー単位で[コストを割り当てる](https://claude.com/docs/claude-tag/admins/attribute-costs)こともできます。Orderful は組織全体の上限を設け、75% と 90% でアラートを出しています。「私たちはチャンネルのコストに徹底したオーナーシップを持っています。オーナーが『この支出はアウトプットや成果に見合っている』と説明するのです」と Kikoff のエンジニアリングマネージャー、Alex Dejeu 氏は語ります。次のチャンネルの規模を見積もるには、最初のチャンネルの実際のコストを使いましょう。

### 展開

**オンコールのアラートやバグのトリアージなど、チームがすでに使っているチャンネルで、明確なタスクをひとつ選ぶ。**

「特定のチームで試してみて、何がうまくいくかを確認し、問題点を解消できたと確信できたら、そのアイデアを他のチームにも広げ、それぞれの似たようなチャンネルに追加してもらいます。AI のミスへの許容度が低い人たちにとって、信頼を損なうような体験は避けたいのです」と Kikoff のエンジニアリングマネージャー、Alex Dejeu 氏は語ります。

**専門家や文化の担い手に先陣を切ってもらう。**

チームがすでに信頼している人たちに、最初に、しかもオープンな場で Claude を使ってもらいましょう。

「オープンな場で Claude とやり取りするのは、生産的で楽しいものでした。営業やカスタマーサクセスの何人かは、専門家が [Claude Tag とやり取りする] 様子を見てから、自分でも Claude に質問するようになり、すぐに価値を得ていました」と Valence のプリンシパル AI エンジニア、Sameer Bansal 氏は語ります。

**ノイズを調整する。**

複数のスタートアップが、Claude の発言の多さを調整する必要があったと話してくれました。しゃべりすぎはひとつのリスクです。

「アドホックな依頼での会話は、ときにノイズが多くなることがあります。ここでは応答性を下げるよう調整しつつ、アドホックな依頼で Claude を何に使うかについても、より原則に基づいて考えるようにしています」と NavigateAI のエンジニアリング責任者、Mike Chen 氏は語ります。

一方で、口数が少なすぎるのもリスクです。忙しいチャンネルでは、「毎回 @ でメンションしないと、あまり動いてくれない」と Flagler Health の共同創業者、Will Hu 氏は言います。そして「誰もチャンネルを注意深く見ていなかったり、やり取りしていなかったりすると、Claude は何もせずに待機したままになります」。

**チームメイトに自分のアカウントを接続してもらう。**

セットアップ時に管理者が作成したバンドルは、チャンネル内の全員に対して Claude がアクセスできる範囲を決めるものです。[個人コネクタ](https://claude.com/docs/claude-tag/concepts/personal-connectors)は仕組みが異なります。Claude は質問した人の権限で動作するため、その人が承認すれば、その人のドキュメント、受信トレイ、CRM から情報を取得できます（まずオーナーが組織にコネクタを追加する必要があり、Enterprise プランでは管理者が個人コネクタを管理します）。それでも回答はチャンネルに投稿されるため、機密性の高いものについては「Allow with review」（レビュー付きで許可）を選んでください。

**新入社員のオンボーディングのつもりでチャンネルの指示を書く。**

最初に何を確認するか、いつ PR を作成するか、いつ質問するか、そして「対応不要」も正当な回答であることを書いておきましょう。

**フィードバックは DM ではなくチャンネルで伝える。**

スレッドの中で修正しましょう。Claude は[チャンネルごとに記憶](https://claude.com/docs/claude-tag/users/memory)し、チームメイトはその様子を見て Claude との働き方を学びます。恒久的に直したい場合は、このチャンネルの記憶を更新するよう Claude に頼みましょう。

![オープンな場で Claude と一緒に質問に取り組んだ同僚に、Valence の社員 2 人が感謝している Slack メッセージ。](https://assets.claude.com/7e4a82b6f73aabecf6a5a5fe148c38a53659ba7a.png)

同僚がオープンな場で Claude と一緒に質問に取り組む様子を見た Valence の社員 2 人が、その同僚に感謝しています。Valence の許可を得て掲載しています。

次に何をすべきかわからなければ、Claude をタグ付けして、組織について何を学んだか、どのユースケースに広げるとよいかを尋ねてみましょう。

Moritz の共同創業者兼 CTO の Stefan Mandaric 氏は、チームごとのユースケースを推薦するよう Claude に依頼しました。15 分後、Claude は事務所の Slack チャンネル、Linear の issue、Notion の SOP、Drive、Metabase のダッシュボードを読み込み、25 個のユースケースを公開しました。「25 個のうち 18 個は追加のセットアップなしで機能しました。それがそのまま私たちの展開計画になったのです。」

---

## 最後に：「すごい」瞬間から学んだこと

「すごい」と感じた瞬間は、必ずしもスピードに関するものではありませんでした。多くの場合、Claude は誰も探すよう頼んでいなかったものを見つけていました。ときには、Claude が出しゃばらなかったこと自体が驚きでした。そしてときには、思いがけないやり取りが驚きをもたらしました。「そのうち Claude がジョークに乗ってくることにも慣れて、ノリがよくて真っ先に笑ってくれる相手だとありがたく思えるようになります」と Orderful の CTO、Piers MacDonald 氏は語ります。

![画像付きの返信とリアクションがある Slack スレッド。](https://assets.claude.com/8884ca89d9b6e0bf91eb7b426d8546c971d8079d.png)

Orderful の Slack での会話を再現したもの。Orderful の許可を得て掲載しています。

このガイドがお役に立てば幸いです。経験とインサイトを共有してくださった Campfire、Descript、Flagler Health、Kikoff、Moritz、NavigateAI、Orderful、Valence の皆さまに、特に感謝いたします。

---

## その他のリソース

### はじめに

- [Claude Tag の概要](https://claude.com/product/tag)
- [Claude Tag のドキュメント](https://claude.com/docs/claude-tag)
- [Claude Tag のセットアップ](https://claude.com/docs/claude-tag/admins/setup-overview)
- [オンコールのガイド付きセットアップ](https://claude.com/docs/claude-tag/admins/setup-oncall)
- [セットアップのトラブルシューティング](https://claude.com/docs/claude-tag/admins/troubleshooting)

### ツールの接続

- [接続とバンドルの追加](https://claude.com/docs/claude-tag/admins/add-connections)
- [GitHub アクセスの設定](https://claude.com/docs/claude-tag/admins/configure-github)
- [個人コネクタ](https://claude.com/docs/claude-tag/concepts/personal-connectors)
- [ネットワーク要件](https://claude.com/docs/claude-tag/admins/network-requirements)

### アクセス、セキュリティ、支出

- [アクセスの制限](https://claude.com/docs/claude-tag/admins/restrict-access)
- [エージェントアイデンティティの仕組み](https://claude.com/docs/claude-tag/concepts/agent-identity)
- [セキュリティとデータ](https://claude.com/docs/claude-tag/concepts/security-and-data)
- [データライフサイクルと削除](https://claude.com/docs/claude-tag/concepts/data-lifecycle)
- [Claude Slack アプリがアクセスできるもの](https://claude.com/docs/claude-tag/admins/for-slack-admins)
- [支出上限の設定](https://claude.com/docs/claude-tag/admins/set-spend-limit)
- [ユーザーへのコストの割り当て](https://claude.com/docs/claude-tag/admins/attribute-costs)

### Slack で Claude と働く

- [Claude が応答するタイミングの制御](https://claude.com/docs/claude-tag/users/when-claude-responds)
- [Claude Tag が理解するコマンド](https://claude.com/docs/claude-tag/users/commands)
- [チャンネルの記憶](https://claude.com/docs/claude-tag/users/memory)
- [ルーティンの設定](https://claude.com/docs/claude-tag/users/proactivity)

### ユースケース

- [ユースケースライブラリ](https://claude.com/docs/claude-tag/users/use-cases)
- [バグの修正](https://claude.com/docs/claude-tag/users/use-cases/fix-bugs)
- [データに関する質問への回答](https://claude.com/docs/claude-tag/users/use-cases/answer-data-questions)

### Anthropic における Claude Tag の活用

- [Claude Tag が Anthropic の CI/CD 障害のファーストレスポンダーとして機能する仕組み](https://claude.com/resources/articles/ai-ci-cd-on-call)
- [Anthropic が Claude によってセルフサービスのデータ分析を実現している方法](https://claude.com/resources/articles/how-anthropic-enables-self-service-data-analytics-with-claude)
