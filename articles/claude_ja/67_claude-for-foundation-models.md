---
date: '2026-06-08'
final_url: https://claude.com/blog/claude-for-foundation-models
number: 67
selector_used: main
slug: claude-for-foundation-models
source_url: https://claude.com/blog/claude-for-foundation-models
title: Building intelligent apps for Apple platforms with Claude in the Foundation
  Models framework
title_ja: Foundation Models フレームワークで Claude を使い、Apple プラットフォーム向けのインテリジェントなアプリを構築する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

# Foundation Models フレームワークで Claude を使い、Apple プラットフォーム向けのインテリジェントなアプリを構築する

本日、私たちは Foundation Models フレームワークでの Claude サポートを、新しい Swift パッケージを通じて公開します。これにより、Apple の開発者は Apple の Foundation Models フレームワークを使って、より複雑なワークフローのために Claude を呼び出せるようになります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a26f71ab79bc169ff9bdec4_8dfc12d1.png)

Apple の Foundation Models フレームワークは、開発者が Swift からネイティブにモデルへアクセスできるようにするものです。とても扱いやすく、ガイド付き生成によって、わずか 3 行程度のコードで型付きの Swift の値を返せます。開発者はこれを使って、要約や抽出といった高速かつローカルなタスクのために、Apple のオンデバイスモデルを活用できます。

開発者は今後、Apple の Foundation Models フレームワークを使って、複数ステップの推論やコード生成などが必要なリクエストを Claude に引き渡せるようになります。Claude は最新情報を得るために Web を検索したり、データ分析のためにコードを実行したりもできます。Claude のレスポンスは、同じビューにそのままストリーミングして表示できます。

Apple のフレームワークは `@Generable` アノテーションから型付きの Swift の値を返すため、開発者は生のユーザーテキストではなく、整理済みの入力を持った状態で Claude API 呼び出しにたどり着けます。

## これにより何が可能になるか

Foundation Models フレームワークは、すでにオンデバイスのインテリジェントな機能を数多く支えています——パーソナライズされたプロンプトを差し出してくれるジャーナリングアプリ、契約書を要約してくれるドキュメントアプリ、学習者のレベルに合わせて概念を説明してくれる学習アプリなどがその例です。ここに Claude を加えると、これらのパターンそれぞれが拡張されます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a26f71ab79bc169ff9bdec1_7c4a5aaf.png)

ジャーナリングアプリは、毎日のプロンプトをオンデバイスで生成し、その上で何ヶ月分ものエントリにまたがる共通の糸口を見つけ出すよう Claude に依頼できます。学習アプリは、用語の定義をオンデバイスで行い、学生が「これは、これまで扱ってきた他のすべてとどう関わるのですか？」とフォローアップしてきたタイミングで Claude に引き渡せます。

ユーザーから見れば 1 つの体験ですが、その裏では各ステップに最適なモデルが使われています。

## はじめ方

Foundation Models フレームワークでの Claude サポートは明日から利用可能になり、iOS 27、iPadOS 27、macOS 27、visionOS 27、そして watchOS 27 上の Apple Foundation Models フレームワークを通じて動作します。プロジェクトに追加し、Anthropic API キーでサインインし、Apple のオンデバイスでの処理から得られた型付きの出力を Claude へのリクエストに渡してください——あとはパッケージが、ストリーミング、ツール呼び出し、構造化されたレスポンスを SwiftUI ビューに戻すところまで面倒を見てくれます。
