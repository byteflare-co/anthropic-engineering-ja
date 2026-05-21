---
date: '2026-05-21'
final_url: https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity
number: 54
selector_used: main
slug: how-our-partners-are-putting-opus-to-work-for-cybersecurity
source_url: https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity
title: How our partners are putting Opus to work for cybersecurity
title_ja: パートナー各社は Opus をサイバーセキュリティにどう活用しているか
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

# パートナー各社は Opus をサイバーセキュリティにどう活用しているか

AI は、セキュリティ脆弱性が発見され悪用されるまでのスピードを変えつつあります。それに対する最も明確な答えは、セキュリティチームが高い能力を備えたモデルを自らの防御に活用することです。

[Claude Security のパブリックベータ](https://claude.com/blog/claude-security-public-beta) を発表した際、私たちは Claude Opus の上に構築する一連のテクノロジー／サービスパートナーも紹介しました。導入への最短経路はチームごとに異なるからです。Claude を直接利用するチームもあれば、既に運用しているプラットフォーム経由で使うチーム、自分たちの環境を熟知したサービスパートナーを通じて使うチームもあります。

その中のいくつかが本日リリースに至り、初期の結果は、フロンティアモデルによる防御が実際にどのようなものかを示しています。

## 初期の成果

パートナー各社は、社内利用と顧客環境の両方で、Opus を活用した防御能力の大幅な向上を報告しています。

- 週あたり 150,000 以上の本番アセットに対する継続的なペネトレーションテストを実施し、検証済みの高深刻度・重大深刻度の発見事項を毎週数千件、誤検知ゼロで浮かび上がらせている（Wiz、顧客本番環境にて）。
- 1 年分のペネトレーションテストに相当する作業を、3 週間未満で完了（Palo Alto Networks、社内テストにて）。
- セキュリティテストのカバレッジを約 10% から 80% 超へ、1,600 のアプリケーションと 500,000 を超える API にわたって引き上げ、スキャンのターンアラウンドを 3〜5 日から 1 時間未満に短縮（Accenture、自社インフラ上にて）。

これらの取り組みは、3 つの領域に分類できます。スケールでの攻撃的テスト、発見から修正までのギャップを縮める取り組み、そしてガバナンス付きで AI を本番投入する取り組みです。

## 本番規模での継続的な攻撃的テスト

攻撃的テストとは、敵が行うのと同じやり方で自社システムを攻撃することを意味します。悪用可能な経路を、自分たちが先に見つけるためです。

Wiz の [Red Agent](https://www.wiz.io/blog/red-agent-claude-opus) は、Opus を使って本番の Web アプリケーションや API に対して人間のペネトレーションテスターのように推論する AI 駆動の攻撃者です。アプリケーションのロジックを分析し、ステップをチェーンし、リアルタイムのサーバー応答に適応することで、従来のスキャナーが見逃すロジック起因の欠陥を浮かび上がらせます。週あたり 150,000 以上の本番アセットに対して継続的に動作し、数千件の高深刻度・重大深刻度の発見事項を、悪用可能性の証拠と Wiz Security Graph によるビジネスコンテキスト付きで、それぞれ検証しています。「セキュリティチームはもはやデータの不足ではなく、それに基づいて行動する能力に制約されています」と Wiz の VP AI & Threat Research を務める Alon Schindel は語ります。「フロンティアモデルを Wiz Agents に組み込むことで、私たちは組織が AI のスピードで防御できるようにしているのです。」

[Unit 42 Frontier AI Defense](https://www.paloaltonetworks.com/unit42/ai-advantage) は Palo Alto Networks のエキスパート主導のサービスで、Opus を使って隠れた脆弱性を発見し、それらがどのように連鎖して重要な攻撃経路を形成するかをマッピングし、AI を活用した攻撃に対する堅牢化のロードマップを構築します。このサービスは、その露出分析を、マシンスピードでの防御に向けたベンチマーク済みのブループリントと、実践的な変革作業と組み合わせます。「攻撃者がフロンティアモデルを武器化してサイバー攻撃を自動化する中、防御側もより速く動かなければなりません」と Palo Alto Networks の Unit 42 を率いる SVP の Sam Rubin は語ります。

CrowdStrike の [Frontier AI Readiness and Resilience Service](https://www.crowdstrike.com/en-us/services/ai-security-services/frontier-ai-readiness-and-resilience/) は、Fortune 500 の 60% 以上に信頼されるプラットフォームに同等クラスの能力をもたらします。Opus を CrowdStrike の AI Red Team Services および独自のエージェントフレームワークと組み合わせ、顧客アプリケーション内に潜む未知のゼロデイを継続的に狩り出し、発見事項を検証し、新しいコードが本番に到達する前に修正を加速させます。

> 「Anthropic の Claude Opus のようなフロンティアモデルは、1 年前には存在しなかった能力上のアドバンテージを防御者に与え、脆弱性管理を一気に左方向（より上流）へと押し進めています。」 - **Mark Manglicmot, Global VP of Consulting Services, CrowdStrike**

## 発見と修正のギャップを縮める

脆弱性を見つけてから修正するまでのギャップは、脆弱性露出の多くが居座る場所です。トリアージ、優先順位付け、パッチテスト、チーム間の引き継ぎはどれも時間を消費するからです。

Accenture の [Cyber.AI](https://newsroom.accenture.com/news/2026/accenture-and-anthropic-team-to-help-organizations-secure-scale-ai-driven-cybersecurity-operations) は、アセット、アイデンティティ、脅威、コントロールを単一の運用モデルに接続し、その上で Opus が推論を行い、検知・優先順位付け・修正を継続的なループとして実行するエージェント型プラットフォームです。Accenture はまずスケールでの検証を社内で行いました。1,600 のアプリケーションと 500,000 を超える API にわたるセキュリティテストカバレッジを約 10% から 80% 超に引き上げ、自社のグローバル IT インフラ上でスキャンのターンアラウンドを 3〜5 日から 1 時間未満へと短縮したのです——これらが、Cyber.AI が現在クライアントに提供している成果の土台になっています。

> 「ビジネスリーダーは、史上もっとも速く動き、もっとも複雑なサイバー脅威ランドスケープを切り抜けようとしています。Anthropic とのパートナーシップにより、クライアントが先んじ続けるために必要なツールを届けていきます。」  - **Harpreet Sidhu, Global Lead, Accenture Cybersecurity**

TrendAI™ [Vision One](https://www.trendmicro.com/en_us/business/products/one-platform.html) は、Opus による脆弱性リサーチの支援を活用して、185 か国にまたがる企業が露出を特定し、仮想パッチを通じてリスクを軽減できるようにしています。検証済みの発見事項は TrendAI Zero Day Initiative にも流れ込み、協調的な開示を通じて、ベンダーパッチが提供されるよりも最大で 96 日早くリスクのあるシステムを保護するのに役立っています。「AI が脆弱性発見を加速させるにつれて、防御者にとっての本当の課題は、スケールでの修正へと移っていきます」と TrendAI の Chief Platform and Business Officer 兼 Head of TrendAI を務める Rachel Jin は語ります。「Anthropic と協力し、攻撃者が隙を突くより前に、緩和策と仮想パッチによってリスクを下げられるよう、顧客を支援しています。」

Deloitte の [Continuous Threat Exposure Management (CTEM)](https://www.deloitte.com/global/en/services/consulting-risk/services/deloitte-cyber-attack-surface-management.html) は Deloitte Ascend™ の上に構築されており、検出、検証、優先順位付け、修正を 1 つのワークフローとして実行します。パッチが存在しない場合の対策設計も含まれます。Opus のコード推論と自動的な安定性テストにより、チームは数日や数週間ではなく数時間で修正を行う自信を持てるようになります。「Ascend 上の CTEM は、脆弱性修正における意思決定のレイテンシを下げるために存在します」と Deloitte の Partner 兼 US Cyber Leader である Adnan Amjad は語ります。「そのギャップが、勝利の窓を攻撃者が手にするのか、防御者が手にするのかを決めるのです。」

## AI をガバナンス付きで本番投入する

エージェント型 AI のユースケースという新しい世界は、多くのチームにとって新たな課題を提示しました。明確なフレームワークがなければ、デプロイのためのコントロール、監査エビデンス、自律性の境界を整備する作業のせいで、セキュリティ領域での AI 導入はパイロット段階の煉獄に留まりがちです。

PwC の [Claude Native Cybersecurity offering](https://www.pwc.com/us/en/technology/alliances/anthropic.html) は、CISO がそろって挙げる 2 つの問題に取り組みます。AI を安全に本番投入することと、サイバー機能そのものを近代化することです。Secure AI Adoption は、サンドボックスから本番までの移行を四半期単位ではなく数週間で実現し、CISO や CRO が安心してチームにイノベーションをもたらせるよう、デプロイ、ガバナンス、監査エビデンスを提供します。Scaled Frontier Defense は、Opus を活用したエージェント的推論を既存の脆弱性管理、検知、セキュリティエンジニアリング、GRC のワークフローに統合し、定義されたガードレールと監査可能性の中で自律的な実行を可能にします。

> 「これはサイバーセキュリティにとっての画期的な瞬間であり、AI 駆動のトランスフォーメーションが、レジリエンスと競争力を維持するために不可欠なものになりつつあります。」 - **Morgan Adamski, U.S. Cyber, Data & Tech Leader, PwC**

## 拡大するエコシステム

BCG、Infosys、SentinelOne も Opus を基盤とした防御的サイバー製品を構築中であり、それぞれが利用可能になり次第、詳細をお伝えしていきます。

上記のすべての製品は、同じ Opus の基盤能力の上で動いています。コードについて推論し、どの露出が実世界のリスクに繋がるのかを理解し、長く続くエージェント的なワークフローを維持する力です。私たちはこれらのパートナーと協力し、より多くのセキュリティチームに、それぞれに最も合ったアクセスポイントを通じてフロンティアの防御を届けられることを楽しみにしています。

*[Claude のセキュリティユースケース](https://claude.com/solutions/security) について、より詳しくはこちらをご覧ください。*

‍
