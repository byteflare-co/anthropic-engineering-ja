---
date: '2026-08-06'
final_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
number: 108
selector_used: main
slug: run-claude-code-sessions-on-your-own-compute
source_url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
title: Run Claude Code sessions on your own compute
title_ja: 自社のコンピュートで Claude Code セッションを実行する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22651dd05046d0fdb0b_39c40393e610cc0a5e65f50ad12ff5ada273f792-1000x1000.svg)

# 自社のコンピュートで Claude Code セッションを実行する

現在パブリックベータ版として提供されているセルフホスト環境を使うと、自社のインフラ上で Claude Code セッションを実行できます。Web、モバイル、デスクトップ、またはルーチンからセッションを開始すると、Anthropic がホストするインフラではなく、貴社のネットワーク内、すなわち社内サービスやツールチェーン、セキュリティ管理のすぐそばで実行されます。

多くのエンタープライズに対しては、運用のシンプルさ(インフラを稼働・保守する必要がない点)から、当社のホスト型オファリングを強くお勧めします。セルフホスト環境は、ネットワーク、ツール、またはコンプライアンス上の要件から、エージェントの実行を自社が管理するインフラ上に留める必要があるチーム向けです。この経路を選ぶ場合は、セットアップと継続的な保守を担うエンジニアリング体制を計画してください。

### **なぜセルフホストするのか**

プレビュープログラムに参加した組織がセルフホスト環境を採用した理由として、主に次のようなものが見られました。

- **ネットワークアクセス:** セッションが貴社のネットワーク内で実行されるため、内部サービス、データベース、レジストリにパブリックインターネットへ公開することなくアクセスできる
- **カスタマイズ性:** コンパイラ、SDK、社内 CLI を環境にあらかじめインストールしておくことで、すべてのセッションがビルド可能な状態からスタートできる
- **コンプライアンス:** ソースコードとビルド成果物を、自社が管理するインフラ上に留められる

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5b9_6a71ea6c8fc8ac632732466a_logo_faire-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5bd_6a71ea6c2122143c0b574194_logo_faire-dark.svg)

「セルフホスト環境のおかげで、既存の開発ワークフローに Claude Code を組み込みながら、当社のセキュリティおよび運用管理を維持できます。この構成により、Claude は需要に応じてスケールするコンピュートを使って PR を生成し、CI の問題修正を助け、開発者ワークフローのイベントに応答できます。Claude は当社のコードベースを理解しているため、当社のエンジニアリングチームの開発スタイルに非常によく合っています。」

George Jacob 氏、シニアエンジニアリングマネージャー

### **はじめに**

セルフホスト環境は、Claude Team および Enterprise プランの組織向けにパブリックベータ版として提供されています。デフォルトでは無効になっており、ZDR を利用している組織では利用できません。

プラットフォーム、開発者エクスペリエンス、または開発者生産性を担うチームが、セットアップと継続的な運用(ランナーイメージの構築と保守、ランナーの更新、オンデマンドモードを利用する場合はオーケストレーターの運用を含む)を担当することを想定してください。

詳しくは[ドキュメント](https://code.claude.com/docs/en/self-hosted-environments)をご覧ください。フィードバックは [GitHub](https://github.com/anthropics/claude-code/issues) 経由、または Anthropic のアカウントチームを通じてお寄せください。
