---
date: '2026-08-18'
final_url: https://claude.com/blog/the-claude-science-product-guide
number: 119
selector_used: main
slug: the-claude-science-product-guide
source_url: https://claude.com/blog/the-claude-science-product-guide
title: The Claude Science product guide
title_ja: Claude Science プロダクトガイド
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7365ae69f4d9f4f96fa2_Object-DoubleHelix.svg)

# Claude Science プロダクトガイド

ライフサイエンス業界は、AI 導入の旅において転換点を迎えています。[デロイトの 2026 年ライフサイエンス業界見通し](https://www.deloitte.com/us/en/insights/industry/health-care/life-sciences-and-health-care-industry-outlooks/2026-life-sciences-executive-outlook.html)によると、バイオファーマおよび医療機器業界のリーダーの 78% が、今年 AI が大きな変化を牽引する中心的な役割を果たすと期待している一方で、組織の日常業務に AI ツールを完全に導入できていると回答したのはわずか 14% にとどまります。化学、物理学、生物学、計算科学分野の研究者へのインタビューをもとにした Anthropic 独自の社内調査でも、科学者の 91% が研究にもっと AI を活用したいと考える一方で、79% が信頼性と再現性を採用の最大の障壁として挙げています。

[**Claude Science**](https://www.anthropic.com/news/claude-science-ai-workbench)(ベータ版)は、この課題に対する Anthropic の答えです。ライフサイエンスのあらゆるデジタル業務ステップに対応する AI ワークベンチであり、科学者のデータのすぐそばで動作し、追跡可能・再現可能・説明可能な結果を生み出すよう設計されています。Claude Science は、より広い Claude 製品ファミリー——Claude Chat、Claude Cowork、Claude Code、Claude for Microsoft 365、Claude Platform、Claude Managed Agents を含む——の一部として位置づけられており、[Novo Nordisk](https://claude.com/customers/novo-nordisk)、[Garvan Institute](https://claude.com/customers?fcdaa149_1_industry_equal=%5B%22Life+sciences%22%5D&fcdaa149_sort_date=desc)、[Benchling](https://claude.com/customers/benchling) といったライフサイエンス組織は、科学そのものを取り巻く文書作成・規制対応・エンタープライズ業務にこれらの製品を活用しています。本ガイドでは、どのような場面でどの Claude サーフェスを使うべきかを整理したうえで、研究組織内で Claude Science を展開する方法について、顧客事例と導入ロードマップを交えながら詳しく解説します。

本ガイドでは、以下の内容を紹介します。

- 科学領域でどの Claude サーフェスをいつ使うべきか——分析・図表・結果作成には Claude Science、文書作成や規制対応業務には Claude Cowork と Claude for Microsoft 365、本番パイプラインの構築には Claude Code
- Claude Science が内部でどのように動作するか——データ、計算リソース、エージェントを自分のマシン上に保ちながら、重い処理を自前の GPU、SLURM クラスタ、クラウドアカウントへディスパッチするローカルデーモンによって実現されている仕組み
- Claude の科学的分析がレビューに耐えられる理由となる、5 つの設計上の選択
- Foundation(基盤)、Pilot(試験導入)、Scale(拡大)の 3 フェーズから成る導入ロードマップ——各段階で何をすべきか、何が見えてくるか、そしてパイロットがうまくいっていることを示す指標
- 単一細胞 RNA-seq のクラスタリングから、方法論セクションの執筆支援まで、発見・分析・論文発表にまたがる機能別・ワークフロー別のユースケース

詳しくは[こちら](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6a83dc7ae3c1656fe5f41d40_Claude-eBook-Claude-Science-product-guide-08112026%20(2).pdf)をご覧ください。

***今すぐ*** [***Claude Science***](https://www.anthropic.com/news/claude-science-ai-workbench) ***を始めましょう。***

‍
