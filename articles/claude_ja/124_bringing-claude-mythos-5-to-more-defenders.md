---
date: '2026-08-21'
final_url: https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders
number: 124
selector_used: main
slug: bringing-claude-mythos-5-to-more-defenders
source_url: https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders
title: Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders
title_ja: Claude Mythos 5 のサイバーセキュリティ能力をより多くの防御者へ
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Claude Mythos 5 のサイバーセキュリティ能力をより多くの防御者へ

*より多くのチームがサイバー防御にフロンティア能力を活用できるよう進めてきた取り組みについて、最新情報をお伝えします。* [*Claude Mythos 5*](https://www.anthropic.com/news/claude-fable-5-mythos-5) *が* [*Claude Security*](https://claude.com/product/claude-security) *で利用可能になり、パートナー各社のサイバー防御ツールへの導入も間もなく始まります。あわせて、オープンソースソフトウェアの安全性向上を支援する 3,500 万ドルのファンドを立ち上げ、*[*Cyber Verification Program*](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)*の拡大計画も共有します。*

4 月、私たちは [Project Glasswing](https://www.anthropic.com/glasswing) を立ち上げ、当社で最も高性能なフロンティアモデルである Claude Mythos Preview（およびその後継である Claude Mythos 5）を、世界で最も重要なソフトウェアを守る一部の組織の手に届けました。これにより防御者は、同等の能力を持つモデルが一般提供されたり悪意ある行為者の手に渡ったりする前に、脆弱性を発見し修正する時間的猶予を得ることができました。

私たちが一貫して目指してきたのは、安全に配慮しながら Mythos レベルの防御能力をできる限り多くの防御者に広げることです。そのために、Mythos クラスのモデルへのアクセスを、その攻撃的なサイバー能力が誤った手に渡らないようにしながら拡大するための、[安全性分類器](https://www.anthropic.com/research/next-generation-constitutional-classifiers)や保護策の開発を進めてきました。[Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) はその第一歩であり、デュアルユースのサイバー関連作業をブロックしながらモデルを広く利用可能にしました。

本日、私たちは次のステップに進みます。最もリスクの高い挙動が生じるのは、ユーザーがモデルに直接アクセスでき、悪意ある行為者がそれを有害な用途へと誘導しようとする場合です。しかし、ユーザーが受け取れるのが脆弱性のパッチやセキュリティアラートといった特定の出力に限られるのであれば、そのリスクは大幅に低くなります。今回発表する変更は、モデルへの直接アクセスに関する適切なガードレールを維持しつつ、防御的な成果へのユーザーのアクセスを広げるものです。

- **防御者が頼りにしているツールへの Claude Mythos 5 の統合。** 私たちはサイバーセキュリティの技術・サービスパートナーと協力し、防御者がすでにソフトウェアの保護に使用している製品やサービスに Claude Mythos 5 を組み込んでいます。
- **Claude Security のスキャンが Claude Mythos 5 上で実行可能に。** Claude Enterprise プランの顧客は、Claude Security 上で当社最高性能のモデルを実行し、コードベースをスキャンしてセキュリティ脆弱性を検出し、パッチを提案させることができるようになりました。
- **オープンソースセキュリティ向けに 3,500 万ドル分のクレジット。** 新設の Defender Advantage Fund（0xDAF）は、オープンソースプロジェクトの脆弱性修正、スキャン・パッチ工程の一部自動化、新たなセキュリティ手法の実験に取り組む組織に対し、3,500 万ドル分のクレジットを提供します。
- **Cyber Verification Program の拡大。** 本プログラムは既に、審査を通過した防御者に対して Opus および Sonnet モデルの保護策を緩和した形で提供しています。今後数週間で、Opus と Sonnet におけるデュアルユース能力をより広範囲に含める形にプログラムを拡張し、続いて Mythos クラスへのアクセスも追加していきます。

私たちの目的は変わらず、AI モデルがますます強力になる中で、組織がサイバーセキュリティの速度と要求に適応できるよう支援することです。今後も保護策、アクセスプログラム、コミュニティ支援を発展させ、当社の最も高性能なモデルを幅広い人々や組織に安全に提供できるようにしていきます。

## Mythos を既存のサイバー防御ツールに統合する

病院、公益事業、金融システム、そしてソフトウェアサプライチェーンを守るチームは、セキュリティ運用、インシデント対応、脅威インテリジェンス、検知エンジニアリングのために、すでに一連の製品やサービスに頼っています。こうした防御者にフロンティア能力を届ける最も速い方法は、Mythos クラスのモデルを彼らがすでに使っているツールに統合することです。

私たちのパートナーの多くは、すでに [Claude Opus 上にサイバー製品を構築](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity)しており、セキュリティチームがアラートのトリアージ、脅威の特定、脆弱性の修正をより速く行えるよう支援しています。現在私たちは、これらのパートナーやその他の企業と協力し、Claude Mythos 5 を彼らの製品やサービスに組み込むことで、顧客に Mythos レベルの防御成果を届けられるようにしています。

エンドユーザーがこうした製品を使用する際、Mythos と直接やり取りするわけではありません。代わりに、特定のタスクのために裏側で Mythos を実行する専用インターフェースを通じて作業し、その製品が提供することを意図した特定の成果物だけを受け取ります。例えば、脆弱性を修正するツールであれば、提案されたパッチのリストを出力として提供するかもしれません。この出力は Mythos によって生成されますが、ユーザーには、例えば脆弱性のエクスプロイトを開発するようモデルに指示する手段はありません。私たちとパートナーは、モデルが意図された範囲内にとどまることを検証するための不正利用防止対策も講じています。

この取り組みはまだ始まったばかりで、今後拡大していく予定です。セキュリティ製品やサービスを構築しており、顧客に Claude Mythos 5 を届けたいという方は、[こちらから登録](https://claude.com/form/mythos-cyber-partner)できます。

## Enterprise 顧客向けに Claude Mythos 5 で Claude Security を利用可能に

本日より、[Claude Security](https://claude.com/product/claude-security) のスキャンは Claude Mythos 5 上で実行されるようになりました。Claude Security はコードベースをスキャンして脆弱性を検出し、人間によるレビュー向けにパッチを提案します。現在 Claude Enterprise 顧客向けにパブリックベータとして提供されており、Mythos 5 によるスキャンは追加のアドオンなしで、既存プランの下で通常のトークン利用として課金されます。

Enterprise の管理者は、[管理コンソール](http://claude.ai/redirect/claude_com.v1.eb7da372-5123-477f-8b4a-89c111df2e2a/admin-settings/claude-code)から Claude Security を有効化できます。[claude.ai/security](http://claude.ai/redirect/claude_com.v1.eb7da372-5123-477f-8b4a-89c111df2e2a/security) から、ユーザーは Claude Mythos 5 を使ってスキャンするリポジトリを選択できます。Claude はコードベースを脆弱性についてスキャンし、各検出結果を [CWE](https://cwe.mitre.org/)（Common Weakness Enumeration）カテゴリ、信頼度と深刻度の評価、そして提案される修正とともに返します。

その後ユーザーは、Web 版の Claude Code を開いて修正を実装できます。インタラクティブなパッチ適用には、組織が Claude Code で利用できるモデルが使用されます。Mythos によるスキャン自体が、他のサーフェスへの Mythos アクセスを拡張するわけではありません。すべてのパッチは、実装される前に必ず人間によるレビューと承認を経る必要があります。

Claude Security は、所有するコードのスキャンに Mythos 5 を使用し、モデル自体を露出させることなく、生の出力ではなく詳細な検出結果を返します。これにより防御者は、悪用しうる相手にモデルがアクセス可能になることなく、Claude Mythos 5 の能力を活用できます。

Claude Security の詳細については、[はじめ方ガイド](https://claude.com/resources/tutorials/getting-started-with-claude-security)をご覧ください。

## オープンソースソフトウェアの安全性向上に向けた Defender Advantage Fund の立ち上げ

世界で最も広く使われているプログラムの一部は、オープンソースソフトウェアの上で動いています。しかしこうしたプロジェクトは、しばしばボランティアや非営利団体によって維持されており、攻撃から包括的にプロジェクトを守るためのリソースや人員を欠いていることがあります。Project Glasswing を通じて、私たちはオープンソースセキュリティ団体への直接寄付として 400 万ドルを提供し、プログラムに参加するオープンソースセキュリティ財団にクレジットを提供し、広く使われているプロジェクトのスキャンとパッチ適用を支援し、[Akrites](https://akrites.org/) や [Gold Eagle](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/) のような協調的な脆弱性修正の取り組みを支援してきました。

新設の Defender Advantage Fund（0xDAF）は、この取り組みをさらに発展させ、オープンソースのメンテナーがソフトウェアを保護するのを支援する組織に 3,500 万ドル分の Claude クレジットを提供します。助成は 3 つの領域に重点を置きます。広く使われているプロジェクトにおける現存する脆弱性の修正、他のプロジェクトが再現できる形でのスキャンとパッチ適用の自動化、そしてプロジェクトが攻撃の種類全体に対して耐性を持つような、より野心的なセキュリティ手法を追求する支援です。

まずは少数の大規模なパイロット助成から始め、何がうまく機能し、どうスケールするのが最善かを学んでいきます。初期の受給者の詳細については、今後数週間のうちに共有する予定です。

## Cyber Verification Program の拡大

これまで、Cyber Verification Program は Claude Opus および Sonnet モデルを使用する際に、デュアルユース能力へのアクセスを組織に提供してきました。プログラムに参加する組織は保護策が緩和され、正当なサイバーセキュリティ業務を行う承認済みチームへの支障を最小限に抑えています。

今後数週間で、私たちはこのプログラムを発展させ、保護策付きのアクセスを Claude Mythos にも拡大します。この一環として、脆弱性のトリアージや検証といった防御的な能力へのアクセスが Mythos クラスのモデルにも広がり、サイバー防御者は Claude Opus および Sonnet クラスのモデルにおけるブロックの軽減を経験することになります。さらに、米国政府のパートナーと連携し、Project Glasswing を通じた Claude Mythos へのアクセス拡大も継続しており、厳格なセキュリティ管理要件を満たす重要インフラの防御者に重点を置いています。

Cyber Verification Program の拡大については、今後数週間のうちに詳細を共有します。それまでの間、正当なサイバーセキュリティ業務を行うすべてのセキュリティチームには、Claude Opus および Sonnet モデルにおける保護策の緩和を受けるためにプログラムへの申し込みをお勧めします。すでに登録・承認済みの方は、対応の必要はありません。最新情報をお伝えします。

## 今後の展望

これらの取り組みは、フロンティアモデルの防御能力をより多くの人々や組織に届け、オープンソースコミュニティが攻撃に対してプロジェクトを強化するのを支援するという、私たちの継続的な取り組みの一環です。今日の高性能な AI モデルが求める強靭なサイバーインフラを構築するため、私たちは政府パートナー、各組織、オープンソースのメンテナー、そして業界全体と協力し続けます。

- [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet) に申し込む。
- Mythos を使ったサイバー製品やサービスの構築に興味がある方は[こちらから登録](https://claude.com/form/mythos-cyber-partner)。
- Claude Security は Enterprise 顧客向けにパブリックベータで提供中です。管理者は[管理コンソール](http://claude.ai/redirect/claude_com.v1.eb7da372-5123-477f-8b4a-89c111df2e2a/admin-settings/claude-code)から Claude Security を有効化できます。詳しい手順は[はじめ方ガイド](https://claude.com/resources/tutorials/getting-started-with-claude-security)をご覧ください。
