---
date: '2026-03-13'
final_url: https://claude.com/blog/1m-context-ga
number: 12
selector_used: main
slug: 1m-context-ga
source_url: https://claude.com/blog/1m-context-ga
title: 1M context is now generally available for Opus 4.6 and Sonnet 4.6
title_ja: Opus 4.6 と Sonnet 4.6 で 1M コンテキストが一般提供開始
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

# Opus 4.6 と Sonnet 4.6 で 1M コンテキストが一般提供開始

Claude Opus 4.6 と Sonnet 4.6 は、Claude Platform 上で標準価格のまま完全な 1M コンテキストウィンドウを利用できるようになりました。ウィンドウ全体にわたって標準価格が適用されます——Opus 4.6 は 100 万トークンあたり $5/$25、Sonnet 4.6 は $3/$15 です。倍率はかかりません：900K トークンのリクエストも 9K トークンのリクエストも、同じトークン単価で課金されます。

**一般提供での変更点：**

- **単一価格でフルコンテキストウィンドウ。** ロングコンテキストのプレミアム料金はありません。
- **すべてのコンテキスト長でフルのレートリミット。** 標準アカウントのスループットがウィンドウ全体に適用されます。
- **リクエストあたりのメディアが 6 倍に**。最大 600 枚の画像または PDF ページに対応し、従来の 100 から大幅に拡大しました。本日より Claude Platform ネイティブ、Microsoft Foundry、Google Cloud の Vertex AI で利用可能です。
- **ベータヘッダーは不要に。** 200K トークンを超えるリクエストは自動的に処理されます。すでにベータヘッダーを送信している場合は無視されるため、コード変更は不要です。

**1M コンテキストが Claude Code の Max、Team、Enterprise ユーザー向けに Opus 4.6 で利用可能になりました。** Opus 4.6 セッションではフルの 1M コンテキストウィンドウが自動的に使用されるため、コンパクション（圧縮）の回数が減り、会話のより多くの部分がそのまま保持されます。1M コンテキストは以前、追加の使用量が必要でした。

### **精度を維持するロングコンテキスト**

100 万トークンのコンテキストは、モデルが適切な詳細を想起し、それらを横断して推論できて初めて意味を持ちます。Opus 4.6 は MRCR v2 で 78.3% のスコアを記録しており、このコンテキスト長におけるフロンティアモデルの中で最高値です。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b49c06e1c573f3ce50276b_image%20(3).png)

Claude Opus 4.6 と Sonnet 4.6 は、フルの 1M ウィンドウ全体にわたって精度を維持します。ロングコンテキスト検索はモデル世代ごとに改善されてきました。

つまり、コードベース全体、数千ページの契約書、あるいは長時間稼働するエージェントの完全なトレース——ツール呼び出し、観測結果、中間推論——をそのまま読み込んで直接使用できるということです。ロングコンテキスト処理に以前必要だったエンジニアリング作業、損失を伴う要約、コンテキストのクリアはもはや不要です。会話全体がそのまま保持されます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

科学的発見には、研究文献、数学的フレームワーク、データベース、シミュレーションコードを同時に横断する推論が必要です。Claude Opus 4.6 の 1M コンテキストと拡張されたメディア制限により、私たちのエージェントシステムは数百の論文、証明、コードベースを一度のパスで統合でき、基礎物理学と応用物理学の研究を劇的に加速しています。

Dr. Alex Wissner-Gross、共同創業者

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d248b84e40f85eca3f68_GC%20AI%20220px%20navy%20(1).png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d24b433e03540b6f6bc5_GC%20AI%20220px%20(1).png)

Claude の 1M コンテキストがあれば、社内弁護士は 100 ページのパートナーシップ契約の 5 回分のやり取りを 1 つのセッションに持ち込み、交渉の全体像をようやく把握できます。バージョン間を行き来したり、3 ラウンド前に何が変わったかを見失うこともなくなります。

Bardia Pourvakil、共同創業者兼 CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

大規模本番システムには無限のコンテキストがあり、本番インシデントは非常に複雑になり得ます。Claude の 1M コンテキストウィンドウにより、最初のアラートから修復まで、すべてのエンティティ、シグナル、仮説を視野に入れ続けることができます。繰り返しコンパクションしたり、これらのシステムのニュアンスを犠牲にする必要はありません。

Mayank Agarwal、創業者兼 CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016becf0259a067d4331fa_logo_hex-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016beff1534c67cafdc9b5_logo_hex-dark.svg)

Opus のコンテキストウィンドウを 200K から 500K に引き上げたところ、エージェントはより効率的に動作するようになりました——実際にはトークン消費量が全体的に減少しています。オーバーヘッドが減り、目の前の目標により集中できるようになりました。

Izzy Miller、AI リサーチリード

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e72946ac912c35a42e8_Endex%20Combined%20Transparent.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b4b0ec5b32b9b274cbac47_Endex%20Combined%20Transparent%20White.svg)

実世界のスプレッドシートタスクには、深いリサーチと複雑なマルチステップの計画が必要です。Claude の 1M コンテキストウィンドウにより、タスクへの忠実さと細部への注意を維持できます。

Tarun Amasa、CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

Claude Code は Datadog、Braintrust、データベース、ソースコードの検索で 10 万以上のトークンを消費することがあります。するとコンパクションが始まり、詳細が消えてしまいます。同じところを堂々巡りでデバッグすることになります。1M コンテキストがあれば、検索し、再検索し、エッジケースを集約し、修正を提案する——すべてを 1 つのウィンドウ内で完結できます。

Anton Biryukov、ソフトウェアエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e943b167e62bb019de7_Logo_green.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e9850d979b6157caf78_Logo_white.svg)

Opus 4.6 の 1M コンテキストウィンドウ以前は、ユーザーが大きな PDF、データセット、画像を読み込むとすぐにコンテキストをコンパクションする必要がありました——最も重要な作業の忠実度がまさに失われていたのです。コンパクションイベントが 15% 減少しました。今では私たちのエージェントはすべてを保持し、1 ページ目に読んだ内容を忘れることなく何時間も稼働し続けます。

Jon Bell、CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96fc452118ce3fff64d_Cognition_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96abcdb567698a5166a_Cognition_dark.svg)

Opus 4.6 の 1M コンテキストウィンドウにより、Devin Review エージェントの効果が大幅に向上しました。大きな差分は 200K のコンテキストウィンドウに収まらなかったため、エージェントはコンテキストをチャンクに分割する必要があり、パス数が増えてファイル間の依存関係が失われていました。1M コンテキストがあれば、差分全体を投入して、よりシンプルでトークン効率の高いハーネスから、より高品質なレビューを得られます。

Adhyyan Sekhsaria、ファウンディングエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b3147bbe3d3dd4357707fb_Logo%20-%20Black%20on%20Transparent%20Background.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31483fee3cafc3e1abc8b_Logo%20-%20White%20on%20Transparent%20Background.svg)

Eve は 1M コンテキストをデフォルトにしています。原告側弁護士の最も困難な問題がそれを必要とするからです。400 ページの証言録取書のクロスリファレンスであれ、訴訟ファイル全体にわたる重要なつながりの発見であれ、拡張されたコンテキストウィンドウにより、以前と比べて格段に質の高い回答を提供できます。

Mauricio Wulfovich、ML エンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

科学的発見には、研究文献、数学的フレームワーク、データベース、シミュレーションコードを同時に横断する推論が必要です。Claude Opus 4.6 の 1M コンテキストと拡張されたメディア制限により、私たちのエージェントシステムは数百の論文、証明、コードベースを一度のパスで統合でき、基礎物理学と応用物理学の研究を劇的に加速しています。

Dr. Alex Wissner-Gross、共同創業者

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d248b84e40f85eca3f68_GC%20AI%20220px%20navy%20(1).png)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d24b433e03540b6f6bc5_GC%20AI%20220px%20(1).png)

Claude の 1M コンテキストがあれば、社内弁護士は 100 ページのパートナーシップ契約の 5 回分のやり取りを 1 つのセッションに持ち込み、交渉の全体像をようやく把握できます。バージョン間を行き来したり、3 ラウンド前に何が変わったかを見失うこともなくなります。

Bardia Pourvakil、共同創業者兼 CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

大規模本番システムには無限のコンテキストがあり、本番インシデントは非常に複雑になり得ます。Claude の 1M コンテキストウィンドウにより、最初のアラートから修復まで、すべてのエンティティ、シグナル、仮説を視野に入れ続けることができます。繰り返しコンパクションしたり、これらのシステムのニュアンスを犠牲にする必要はありません。

Mayank Agarwal、創業者兼 CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016becf0259a067d4331fa_logo_hex-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016beff1534c67cafdc9b5_logo_hex-dark.svg)

Opus のコンテキストウィンドウを 200K から 500K に引き上げたところ、エージェントはより効率的に動作するようになりました——実際にはトークン消費量が全体的に減少しています。オーバーヘッドが減り、目の前の目標により集中できるようになりました。

Izzy Miller、AI リサーチリード

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e72946ac912c35a42e8_Endex%20Combined%20Transparent.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b4b0ec5b32b9b274cbac47_Endex%20Combined%20Transparent%20White.svg)

実世界のスプレッドシートタスクには、深いリサーチと複雑なマルチステップの計画が必要です。Claude の 1M コンテキストウィンドウにより、タスクへの忠実さと細部への注意を維持できます。

Tarun Amasa、CEO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

Claude Code は Datadog、Braintrust、データベース、ソースコードの検索で 10 万以上のトークンを消費することがあります。するとコンパクションが始まり、詳細が消えてしまいます。同じところを堂々巡りでデバッグすることになります。1M コンテキストがあれば、検索し、再検索し、エッジケースを集約し、修正を提案する——すべてを 1 つのウィンドウ内で完結できます。

Anton Biryukov、ソフトウェアエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e943b167e62bb019de7_Logo_green.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e9850d979b6157caf78_Logo_white.svg)

Opus 4.6 の 1M コンテキストウィンドウ以前は、ユーザーが大きな PDF、データセット、画像を読み込むとすぐにコンテキストをコンパクションする必要がありました——最も重要な作業の忠実度がまさに失われていたのです。コンパクションイベントが 15% 減少しました。今では私たちのエージェントはすべてを保持し、1 ページ目に読んだ内容を忘れることなく何時間も稼働し続けます。

Jon Bell、CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96fc452118ce3fff64d_Cognition_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a96abcdb567698a5166a_Cognition_dark.svg)

Opus 4.6 の 1M コンテキストウィンドウにより、Devin Review エージェントの効果が大幅に向上しました。大きな差分は 200K のコンテキストウィンドウに収まらなかったため、エージェントはコンテキストをチャンクに分割する必要があり、パス数が増えてファイル間の依存関係が失われていました。1M コンテキストがあれば、差分全体を投入して、よりシンプルでトークン効率の高いハーネスから、より高品質なレビューを得られます。

Adhyyan Sekhsaria、ファウンディングエンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b3147bbe3d3dd4357707fb_Logo%20-%20Black%20on%20Transparent%20Background.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31483fee3cafc3e1abc8b_Logo%20-%20White%20on%20Transparent%20Background.svg)

Eve は 1M コンテキストをデフォルトにしています。原告側弁護士の最も困難な問題がそれを必要とするからです。400 ページの証言録取書のクロスリファレンスであれ、訴訟ファイル全体にわたる重要なつながりの発見であれ、拡張されたコンテキストウィンドウにより、以前と比べて格段に質の高い回答を提供できます。

Mauricio Wulfovich、ML エンジニア

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

科学的発見には、研究文献、数学的フレームワーク、データベース、シミュレーションコードを同時に横断する推論が必要です。Claude Opus 4.6 の 1M コンテキストと拡張されたメディア制限により、私たちのエージェントシステムは数百の論文、証明、コードベースを一度のパスで統合でき、基礎物理学と応用物理学の研究を劇的に加速しています。

Dr. Alex Wissner-Gross、共同創業者
