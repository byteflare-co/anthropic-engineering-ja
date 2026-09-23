---
date: '2026-09-23'
final_url: https://claude.com/blog/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace
number: 146
selector_used: main
slug: how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace
source_url: https://claude.com/blog/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace
title: How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel
  on Claude Marketplace
title_ja: CodeRabbit、Power Digital、ThoughtSpot が Claude Marketplace 上の Snowflake と Vercel でスケールする方法
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

# CodeRabbit、Power Digital、ThoughtSpot が Claude Marketplace 上の Snowflake と Vercel でスケールする方法

Claude で構築する企業は、データを保存・分析する Snowflake やアプリを実行する Vercel など、他のソフトウェアにも頼っています。Claude Marketplace を使えば、Anthropic とのコミットメントを持つ企業は、その一部をチームがすでに利用しているツールに充てることができ、新たな予算申請なしに、一つの投資でチームが日々使うものをより多くカバーできます。

CodeRabbit、Power Digital、ThoughtSpot が Claude Marketplace を使って、Vercel や Snowflake との取り組みをどのように拡大したかを紹介します。

## **Power Digital はクライアントのデータを Snowflake 上で運用する**

[Power Digital](https://powerdigitalmarketing.com/) は、自社のチームとクライアント向けのプラットフォーム Nova を構築するマーケティングエージェンシーです。クライアントは Nova を通じてデータを接続し、Nova は Snowflake 上で稼働してレポーティング、社内ツール、マーケティング成果を高めるモデルを支えています。Snowflake により、Power Digital は各クライアント向けの安全なデータ環境を迅速に構築でき、Snowflake Cortex AI を使うことで、既存のガバナンス体制の中でそのデータに対して直接 Claude のようなモデルを実行できます。

Claude は現在、クライアント向け成果物や財務業務から、自社製品に組み込まれたモデルに至るまで、Power Digital 全体で稼働しています。利用者数は1月時点の約12人のエンジニアから、現在では800人以上へと拡大しました。
‍
5年来の Snowflake 顧客である Power Digital は、今年 Claude Marketplace を通じて Snowflake とのコミットメントを拡大しました。支出はすでに承認済みの予算から賄われるため、各チームは Snowflake の利用を迅速に拡大できます。

> *「私たちは Claude 上での運用を大きく集中化しており、社内では数百のツールを管理しています。Claude Marketplace のおかげで、クライアントのデータを保持する Snowflake を、同じ Anthropic とのコミットメントに組み込むことができました。依頼した頃には、契約はすでに準備が進んでいました」と Power Digital のシニアバイスプレジデント、イノベーション担当の John Saunders 氏は述べています。*

## **ThoughtSpot は Snowflake 上で AI アナリティクスを構築する**

[ThoughtSpot のエージェント型アナリティクスプラットフォーム](https://www.thoughtspot.com/)は、決定論的で検証可能なクエリを通じて、企業のセマンティックレイヤーおよびコンテキストレイヤーに基づいた、信頼できる意思決定に直結するインサイトをビジネスユーザーに提供します。

AI 機能を実現するために、ThoughtSpot は Snowflake の推論 API を利用して、Snowflake 内の顧客データに対して直接 Claude のようなモデルを実行し、データ、ビジネスコンテキスト、アクセス制御、AI を一つのエコシステム内に保持しています。ThoughtSpot は Snowflake の推論 API の購入を既存の Anthropic とのコミットメントに適用したため、プロダクトチームはすでに確保済みの予算で API を使った構築をすぐに始めることができました。

> 「*私たちのエージェント型アナリティクスプラットフォームは Claude 上で稼働しているため、Claude Marketplace を通じて Snowflake の推論 API を購入するのは自然な流れでした。すでに行っていたコミットメントを適用したので、購入はすでに承認済みの予算から出すことができました*」と ThoughtSpot の SVP プロダクトマネジメント担当、Francois Lopitaux 氏は述べています。

ThoughtSpot は Claude とともに成長を続けています。同社の AI アナリストである [Spotter](https://claude.com/connectors/thoughtspot-spotter) は Claude 向けのコネクタとして提供されており、ユーザーは Claude を離れることなくデータを分析し、ダッシュボードを構築・閲覧し、アクションを実行できます。

> 「*私たちの AI アナリスト Spotter はすでに Claude のコネクタディレクトリに登録されており、私たち自身のエージェント型製品もマーケットプレイスを通じて販売し、顧客が私たちと同じことをまさに実現できるようにしたいと考えています*」と Lopitaux 氏は付け加えました。

## **CodeRabbit は Vercel 上でコーディングエージェントを実行する**

[CodeRabbit](https://claude.com/platform/marketplace/coderabbit) は Claude を基盤として AI 生成コードを検証し、エンジニアリングチームが何をデプロイするかをコントロールできるようにしています。同社のエージェントはコードを書きテストするため、それを安全に実行する場所が必要です。[Vercel Sandbox](https://vercel.com/sandbox) は、他のジョブや CodeRabbit 自身のシステムから隔離された、独自のファイルシステムとネットワークを持つ分離済みの Linux マイクロ VM 内で各エージェントのコードを実行します。[Vercel Workflows](https://vercel.com/workflows) がこの作業を調整するため、長時間実行されるジョブも時間制限に達することなく一時停止、再開、完了できます。

CodeRabbit のエンジニアリングおよびプロダクトのリーダーたちが、従量課金制の Vercel プランからコミット型プランへの移行を望んだ際、同社は最近拡大した Anthropic とのコミットメントからそのアップグレードの資金を賄いました。予算がすでに承認されていたため、この契約は1週間以内に成立しました。

> ‍*「私たちにとっての価値は柔軟性です。すでに承認済みの予算で、エンジニアが信頼するツールを支えられることです。その同じ価値を、Claude Marketplace を通じて顧客に直接届けられるという点は、まさに双方にとってのメリットです」と CodeRabbit のグローバルパートナーシップ責任者、Blair Pierson 氏は述べています。*

## **Snowflake と Vercel は Claude 上で構築する顧客とともに成長する**

[Snowflake](https://claude.com/platform/marketplace/snowflake) や [Vercel](https://claude.com/platform/marketplace/vercel) のような販売パートナーにとって、Claude Marketplace はすでに Claude 上で構築している顧客にリーチし、Anthropic とのコミットメントを持つ顧客により迅速な購入手段を提供する方法です。

> *「AI が信頼されるのは、それがデータとコンテキストに根ざしているときです。Claude は Snowflake 内で直接稼働するため、当社の顧客のガバナンス、コンテキスト、権限は初日から信頼できるインサイトの基盤としてすでに整っています。Claude Marketplace はこの関係を拡張しやすくし、顧客が Anthropic とのコミットメントの一部を AI ワークロード向けに Snowflake へ直接振り向けられるようにします。これは、共有アカウント全体で Anthropic とともに拡大している取り組みです」と Snowflake のエンタープライズ・テクノロジー・パートナーシップ担当ディレクター、Omar Bed-Mohamed 氏は述べています。*

> *「Claude Marketplace により、CodeRabbit のような顧客は Vercel の Agentic Infrastructure を迅速に調達し、自社プラットフォームをスケールさせることができます。Claude 上で構築するすべての企業のためにエージェントの実行を支援できることを楽しみにしています」と Vercel のプロダクトパートナーシップ責任者、Zack Ciesinski 氏は述べています。*

## **Claude Marketplace を通じた購入**

Claude で構築するということは、多くの場合、チームがすでに依存しているデータプラットフォームやインフラストラクチャを取り込むことを意味します。[Claude Marketplace](https://claude.com/marketplace) では、顧客が Anthropic とのコミットメントの一部を Vercel や Snowflake などのパートナーに充てられるため、チームは調達にかける時間を減らし、構築そのものにより多くの時間を割くことができます。

Anthropic とのコミットメントをこの方法で利用できるのは、現在限定プレビュー段階です。コミットメントをお持ちの方は、担当のアカウントチームにご相談いただくか、[こちらからリクエストを送信](https://claude.com/marketplace-contact-sales)して対象となるかどうかをご確認ください。[Claude Marketplace について詳しくはこちら](https://claude.com/blog/claude-marketplace)。
