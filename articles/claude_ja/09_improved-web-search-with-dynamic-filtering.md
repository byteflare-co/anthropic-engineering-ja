---
date: '2026-02-17'
final_url: https://claude.com/blog/improved-web-search-with-dynamic-filtering
number: 9
selector_used: main
slug: improved-web-search-with-dynamic-filtering
source_url: https://claude.com/blog/improved-web-search-with-dynamic-filtering
title: Increase web search accuracy and efficiency with dynamic filtering
title_ja: ダイナミックフィルタリングでウェブ検索の精度と効率を向上
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

# ダイナミックフィルタリングでウェブ検索の精度と効率を向上

Claude [Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) および [Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) と同時に、[web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) および [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) ツールの新バージョンをリリースします。Claude はウェブ検索中にネイティブにコードを記述・実行し、結果がコンテキストウィンドウに到達する前にフィルタリングできるようになり、精度とトークン効率が向上しました。

## **ダイナミックフィルタリング付きウェブ検索**

ウェブ検索は非常にトークン集約的なタスクです。基本的なウェブ検索ツールを使用するエージェントは、クエリを発行し、検索結果をコンテキストに取り込み、複数のウェブサイトからフル HTML ファイルを取得し、すべてを推論してから応答する必要があります。しかし、検索から取り込まれるコンテキストには無関係なものが多く、応答の品質を低下させてしまいます。

Claude のウェブ検索パフォーマンスを改善するために、web search ツールと web fetch ツールはクエリ結果を後処理するコードを自動的に記述・実行するようになりました。フル HTML ファイルを推論する代わりに、Claude は検索結果をコンテキストにロードする前に動的にフィルタリングし、関連するものだけを残して残りを除外できます。

この手法は他のエージェントワークフローでも[効果的であることが確認されており](https://www.anthropic.com/engineering/advanced-tool-use)、API でのネイティブサポートとして [code execution](http://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool) や [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) などのツールを追加してきました。今回、同じ手法を web search と web fetch にも適用します。

## **Claude のウェブ検索能力の評価**

ダイナミックフィルタリングの有無を比較して、Sonnet 4.6 と Opus 4.6 のウェブ検索を評価しました（他のツールは有効化していません）。[BrowseComp](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf) と [DeepsearchQA](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf) の 2 つのベンチマークにおいて、ダイナミックフィルタリングは平均 11% のパフォーマンス向上を達成し、入力トークンは 24% 削減されました。

**BrowseComp: ウェブを検索して一つの答えを見つける**

BrowseComp は、エージェントが多数のウェブサイトを巡回して、オンラインで意図的に見つけにくくされている特定の情報を発見できるかどうかをテストします。ダイナミックフィルタリングにより Claude の精度は大幅に向上し、Sonnet 4.6 は 33.3% から 46.6% に、Opus 4.6 は 45.3% から 61.6% になりました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fbbb7eec8e454d86c9d_Dynamic-filtering-on-browsecomp.png)

**DeepsearchQA: ウェブを検索して多数の答えを見つける**

DeepsearchQA は、多数の正解を持つリサーチクエリをエージェントに提示し、すべての答えをウェブ検索で見つけなければなりません。エージェントが体系的に計画を立て、多段階の検索を実行し、答えを一つも漏らさないかどうかをテストします。評価指標は「F1 スコア」で、精度と再現率のバランスをとります——返された回答の正確さと検索の網羅性の両方を捉える指標です。

ダイナミックフィルタリングにより、Claude の F1 スコアは Sonnet 4.6 で 52.6% から 59.4% に、Opus 4.6 で 69.8% から 77.3% に向上しました。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fcede000ba1d5aab33d_Dynamic-filtering-on-DeepsearchQA.png)

トークンコストは、モデルがコンテキストをフィルタリングするために記述するコードの量によって異なります。価格加重トークンは Sonnet 4.6 では両方のベンチマークで減少しましたが、Opus 4.6 では増加しました。自社のコストをより正確に把握するために、本番環境でエージェントが遭遇する可能性のある代表的なウェブ検索クエリのセットに対してこのツールを評価することをお勧めします。

## カスタマースポットライト: Quora

[Quora](https://quora.com) の [Poe](https://poe.com) は、最大規模のマルチモデル AI プラットフォームの一つであり、単一のインターフェースを通じて数百万人のユーザーに 200 以上のモデルへのアクセスを提供しています。Quora 社内チームは、ダイナミックフィルタリング付きの Opus 4.6 が「他のフロンティアモデルと比較して、社内評価で最高の精度を達成した」ことを確認しました、と Product and Research Lead の Gareth Jones 氏は述べています。「このモデルは実際のリサーチャーのように振る舞い、Python を記述して結果を解析、フィルタリング、クロスリファレンスします。コンテキスト内の生の HTML を推論するのではなく」

## ダイナミックフィルタリングと web search / web fetch ツール

ダイナミックフィルタリングは、Claude API で新しい web search および web fetch ツールを Sonnet 4.6 と Opus 4.6 とともに使用する際、デフォルトで有効になります。技術ドキュメントの精査や引用の検証など、複雑なウェブ検索クエリに対して、上記と同様のパフォーマンス改善が期待できます。

API での使用方法は以下の通りです:

```
{
  "model": "claude-opus-4-6",
  "max_tokens": 4096,
  "tools": [
    {
      "type": "web_search_20260209",
      "name": "web_search"
    },
    {
      "type": "web_fetch_20260209",
      "name": "web_fetch"
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
    }
  ]
}
```

## Code execution、Memory、その他のツールが一般提供開始

トークン集約的なタスクでエージェントのパフォーマンスを向上させるために、いくつかのツールを一般提供 (GA) に昇格させます:

- [Code execution](http://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)**:** 会話中にエージェントがコンテキストのフィルタリング、データ分析、計算を行うためのコードを実行するサンドボックスを提供します。
- [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool): 永続的なファイルディレクトリを通じて、会話をまたいで情報を保存・取得します。エージェントはコンテキストウィンドウにすべてを保持することなく、コンテキストを維持できます。
- [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)**:** 複雑なマルチツールワークフローをコード内で実行し、中間結果をコンテキストウィンドウの外に保持します。
- [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool): 大規模なツールライブラリから、すべての定義をコンテキストウィンドウにロードすることなく、動的にツールを検出します。
- [Tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples)**:** ツール定義にサンプルのツール呼び出しを直接含めることで、使用パターンを示し、パラメータエラーを削減します。

### **始め方**

改善された web search と web fetch、および code execution、memory、programmatic tool calling、tool search、tool use examples は、Claude Platform で今すぐ利用可能です。始めるには [API ドキュメント](https://platform.claude.com/docs/en/build-with-claude/overview)をご覧ください。
