---
date: '2026-09-28'
final_url: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
number: 151
selector_used: main
slug: giving-companies-more-control-over-their-ai-agents-with-nvidia
source_url: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
title: Giving companies more control over their AI agents, with NVIDIA
title_ja: "NVIDIA と共に、企業が自社の AI エージェントをより制御できるようにする"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

# NVIDIA と共に、企業が自社の AI エージェントをより制御できるようにする

NVIDIA は本日、AI セキュリティを強化するためのオープンなソフトウェアプラットフォームおよびリファレンスシステム設計である [Open Agent Safety Platform](https://nvidianews.nvidia.com/news/open-agent-safety-platform) を発表しました。Anthropic は NVIDIA と協力し、エージェントスタックにさらなる層のセキュリティと制御をもたらしています。

本番環境向けのエージェントを大規模に構築・デプロイするための構成可能な API 群である Claude Managed Agents は、エージェントが必要とする認証情報をボールト内に保持し、エージェント自身がそれを目にすることはありません。オープンソースの NVIDIA OpenShell ソフトウェアは、エージェントが作業中に何を実行し、何にアクセスできるかを制御するよう設計されています。Managed Agents と OpenShell を併用している顧客は、エージェントができることを制限し、エージェントが行ったことをレビューし、制限が確かに機能していることを確認できます。

企業は、質問に答えるために AI を使うことから、複数の事業部門にまたがる複雑な業務を担い、独自データを利用し、ユーザーに代わって行動を取るエージェントを展開する段階へと移行しつつあります。モデルが向上するにつれて、エージェントの用途は増え、アクセス権限も拡大します。エージェントが持つアクセス権限が大きいほど、企業はエージェントの行動をより厳密に制御し、確認する必要があります。

## **層になった保護**

保護はまず、モデル内部のセーフガードから始まります。Managed Agents と NVIDIA OpenShell は、モデルの外側に位置し、エージェントの行動そのものに適用される制限を追加します。各層はそれぞれ独立して制限を強制するよう設計されているため、保護が単一の層に依存することはありません。各層はモジュール式になっており、企業は自社の構成に合ったものを選んで採用できます。

## **Claude Managed Agents が作業を行い、認証情報を保持する**

Managed Agents では、エージェントのループはサンドボックス(作業が実際に行われる隔離環境)とは別のサーバー上で実行されます。パスワードやアクセスキーといった認証情報は、別のボールトに保持されるため、エージェントがそれを目にすることはありません。

Managed Agents はまた、各エージェントが行ったことを記録する監査証跡を提供し、企業が既に持っているアクセス制御との連携も行います。企業は自社のサンドボックス構成を持ち込み、どこでどのように実行するかを選択できます。

## **NVIDIA OpenShell が、エージェントが到達できる範囲を設定する**

[OpenShell](https://www.nvidia.com/en-us/ai/openshell/) は、NVIDIA によるオープンソースのセキュアなランタイムソフトウェアです。すべての AI エージェントの動作を統制・監視し、あらゆるアクションにポリシーを強制します。OpenShell はルールで許可されない限り、すべてをブロックします。エージェントが使おうとする各ツールをチェックし、エージェントがアクセスするファイル、ネットワーク接続、データにルールを適用します。ルールはエージェントの外側で強制され、OpenShell は許可・ブロックしたすべての判断をログに記録します。

チームはまず狭い権限から始め、ログをレビューし、Claude を使ってルールをタスクに必要な最小限のアクセス権に近づけていくことができます。OpenShell のポリシープルーバーは、チームが書いたルールの下でエージェントが到達できる範囲を、数学的な証明によって確認します。

## **Claude Managed Agents に含まれるもの**

- 安全なサンドボックス化、認証、ツール実行があらかじめ処理された、本番環境向けのエージェント。
- 切断が発生しても進捗と出力が保持され、何時間も自律的に動作する長時間セッション。
- エージェントが他のエージェントを立ち上げて指揮し、複雑な作業を並列化できるマルチエージェントオーケストレーション。
- スコープ付きの権限、ID 管理、実行トレースを組み込んだ、実システムへのアクセスをエージェントに与える信頼性の高いガバナンス。

## **チームによる Managed Agents の活用事例**

- [Notion](https://claude.com/customers/notion-qa) では、チームが自社のワークスペース内で Claude に作業を任せられるようにしています。エンジニアはコードの出荷に、他の従業員はウェブサイトやプレゼンテーションの作成に利用しています。数十件のタスクを並列で実行しながら、チームは結果について共同で作業できます。
- [Rakuten](https://claude.com/customers/rakuten-qa) は、エンジニアリング、プロダクト、営業、マーケティング、財務にまたがる専門エージェントを運用しており、それぞれ 1 週間以内にデプロイされています。
- [Asana](https://claude.com/customers/asana-qa) は、Asana のプロジェクト内で人と共に働き、タスクを引き受けて成果物のドラフトを作成するエージェントである AI Teammates を構築しました。Managed Agents を使うことで、チームは高度な機能をこれまでより速く追加できました。

## **提供状況**

Managed Agents は本日より利用可能です。自社のインフラ上で稼働させるか、マネージドプロバイダーを使うかを問わず、自分たちで管理するサンドボックス内で動作させることができます。NVIDIA OpenShell は Apache 2.0 ライセンスの下でオープンソース化されており、[GitHub](https://github.com/NVIDIA/OpenShell) および NVIDIA の[開発者向けリソースページ](https://docs.nvidia.com/openshell/latest/about/overview)から入手できます。
