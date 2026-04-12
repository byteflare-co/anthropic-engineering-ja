---
date: '2026-04-09'
final_url: https://claude.com/blog/the-advisor-strategy
number: 17
selector_used: main
slug: the-advisor-strategy
source_url: https://claude.com/blog/the-advisor-strategy
title: 'The advisor strategy: Give agents an intelligence boost'
title_ja: 'Advisor 戦略：エージェントにインテリジェンスのブーストを'
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

# Advisor 戦略：エージェントにインテリジェンスのブーストを

インテリジェンスとコストのバランスを最適化したい開発者たちが収束しているのが、私たちが Advisor 戦略と呼ぶアプローチです：Opus をアドバイザーとして、Sonnet または Haiku をエグゼキューターとしてペアにします。これにより、コストを Sonnet レベル近くに抑えながら、Opus に近いレベルのインテリジェンスをエージェントにもたらすことができます。

本日、Claude Platform 上で Advisor ツールを導入し、Advisor 戦略を API 呼び出しの 1 行の変更で実現できるようにしました。

## Advisor 戦略でコスト効率の高いエージェントを構築

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcf4_e9f8286d.png)

Advisor 戦略では、Sonnet または Haiku がエグゼキューターとしてタスクをエンドツーエンドで実行し、ツールを呼び出し、結果を読み取り、ソリューションに向けてイテレーションします。エグゼキューターが合理的に解決できない判断に直面すると、アドバイザーとして Opus に相談します。Opus は共有コンテキストにアクセスし、計画、修正、または停止シグナルを返し、エグゼキューターが処理を再開します。アドバイザーはツールを呼び出したりユーザー向けの出力を生成したりすることはなく、エグゼキューターにガイダンスを提供するのみです。

これは、より大きなオーケストレーターモデルが作業を分解し、より小さなワーカーモデルに委任するという一般的なサブエージェントパターンを逆転させたものです。Advisor 戦略では、より小さくコスト効率の高いモデルが主導し、分解もワーカープールもオーケストレーションロジックも必要とせずにエスカレーションします。フロンティアレベルの推論はエグゼキューターが必要とするときにのみ適用され、残りの実行はエグゼキューターレベルのコストで進みます。

私たちの評価では、Opus をアドバイザーとした Sonnet は [SWE-bench Multilingual](https://www.swebench.com/multilingual.html)1 で Sonnet 単体と比較して 2.7 パーセントポイントの向上を示し、エージェンティックタスクあたりのコストを 11.9% 削減しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d908f43209164823554d52_Claude-Blog-Advisor-tool-SWE-bench-Multilingual.png)

## **Advisor ツール**

Advisor 戦略を API で利用できるようにするのが [**Advisor ツール**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)です。これはサーバーサイドツールで、Sonnet と Haiku はガイダンスや特定のタスクについてヘルプが必要なときにこれを呼び出すことを理解しています。

私たちの評価では、Opus アドバイザーを付けた Sonnet は BrowseComp2 と Terminal-Bench 2.03 のベンチマークでスコアが向上し、タスクあたりのコストは Sonnet 単体よりも低くなりました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcfa_880b9e59.png)

Advisor 戦略は Haiku をエグゼキューターとした場合にも機能します。BrowseComp では、Opus アドバイザーを付けた Haiku は 41.2% のスコアを記録し、単体スコア 19.7% の 2 倍以上となりました。Opus アドバイザーを付けた Haiku は Sonnet 単体よりもスコアで 29% 低いものの、タスクあたりのコストは 85% 削減されます。アドバイザーは Haiku 単体と比べてコストを追加しますが、合計価格は Sonnet のコストのごく一部に収まるため、インテリジェンスとコストのバランスが求められる大量タスクに適した選択肢です。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d7a8216b96ea826922fcfd_ca657f5f.png)

Messages API リクエストで advisor\_20260301 を宣言すると、モデルのハンドオフは単一の /v1/messages リクエスト内で行われます——追加のラウンドトリップやコンテキスト管理は不要です。エグゼキューターモデルがいつ呼び出すかを判断します。呼び出し時には、キュレーションされたコンテキストをアドバイザーモデルにルーティングし、計画を返し、エグゼキューターが続行します——すべて同じリクエスト内で完結します。

```
response = client.messages.create(
    model="claude-sonnet-4-6",  # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",
            "max_uses": 3,
        },
        # ... your other tools
    ],
    messages=[...]
)

# Advisor tokens reported separately
# in the usage block.
```

**料金設定**。アドバイザートークンはアドバイザーモデルの料金で課金され、エグゼキュータートークンはエグゼキューターモデルの料金で課金されます。アドバイザーは短い計画（通常 400〜700 テキストトークン）のみを生成し、エグゼキューターがより低い料金でフル出力を処理するため、全体コストはアドバイザーモデルをエンドツーエンドで実行する場合を大幅に下回ります。**組み込みのコスト制御。** max\_uses を設定して、リクエストあたりのアドバイザー呼び出しを制限できます。アドバイザートークンは使用量ブロックで個別にレポートされるため、ティアごとの支出を追跡できます。

**既存のツールとの共存。** Advisor ツールは Messages API リクエスト内のもう 1 つのエントリに過ぎません。エージェントは同じループ内で[ウェブ検索](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)、[コード実行](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)、Opus への相談を行えます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5e2d606b4e122c0dcd1d_bolt-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5e323ed055ab39ba3f17_bolt-dark-theme.svg)

「複雑なタスクではより優れたアーキテクチャ上の判断を下しながら、シンプルなタスクではオーバーヘッドがゼロです。計画と軌道がまったく別物になりました。」

Eric Simmons、CEO 兼創業者、Bolt

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c33d3cb4813a779adb7133_cs-logo-genspark-light-theme.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68c33d3e748405bce1e71684_cs-logo-genspark-dark-theme.svg)

「エージェントのターン数、ツール呼び出し、全体スコアに明確な改善が見られました——自分たちで構築したプランニングツールよりも優れています。」

Kay Zhu、共同創業者兼 CTO、Genspark

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b3147bbe3d3dd4357707fb_Logo%20-%20Black%20on%20Transparent%20Background.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31483fee3cafc3e1abc8b_Logo%20-%20White%20on%20Transparent%20Background.svg)

「構造化文書抽出タスクにおいて、Advisor ツールにより Haiku 4.5 は複雑さに応じて Opus 4.6 に相談してインテリジェンスを動的にスケールさせることができ、5 倍低いコストでフロンティアモデル品質に匹敵する結果を実現しています。」

Anuraj Pandey、機械学習エンジニア、Eve Legal
