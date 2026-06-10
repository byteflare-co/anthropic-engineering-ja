---
date: '2026-06-09'
final_url: https://claude.com/blog/whats-new-in-claude-managed-agents
number: 69
selector_used: main
slug: whats-new-in-claude-managed-agents
source_url: https://claude.com/blog/whats-new-in-claude-managed-agents
title: 'New in Claude Managed Agents: run agents on a schedule and store environment
  variables in vaults'
title_ja: "Claude Managed Agents の新機能: エージェントをスケジュール実行し、環境変数を vault に保管する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

# Claude Managed Agents の新機能: エージェントをスケジュール実行し、環境変数を vault に保管する

本日より、Claude Managed Agents をスケジュール実行できるようになり、CLI ツールやその他の認証済みサービスへ安全にアクセスできるようになります。どちらの機能も Claude Platform 上でパブリックベータとして利用可能です。

## **エージェントをスケジュール実行する**

エージェントをスケジュールに沿って実行し、定型業務を自動でこなせるようになりました。[スケジュールドデプロイメント](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) では、エージェントに cron スケジュールを与えます。スケジュールが発火するたびに、エージェントは新しいセッションを開始してタスクを完了させます。スケジューラーを自前で構築したりホスティングしたりする必要はありません。

夜間のデータ同期、週次のコンプライアンススキャン、日次のダイジェストといった、繰り返し発生する業務に使えます。デプロイメントを稼働させた後は、いつでも一時停止・再開・アーカイブができますし、必要に応じて追加実行をトリガーすることもできます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2704ab5b6bc1de3bb952fc_Claude-Console-Scheduled-Deployments.png)

各チームはすでにスケジュールドデプロイメントを使って繰り返し業務を自動化しています。

- [Rakuten](https://claude.com/customers/rakuten-qa) は、スプレッドシートのデータを分析して週次や月次のスケジュールでレポートやスライドを作成するためにスケジュールドデプロイメントを使っています。本番のログやメトリクスを監視させることもしており、プロダクトマネージャーがダッシュボードを作らずにアプリケーションの健全性を確認できるようにしています。
- [Actively AI](https://actively.ai/) は、セールスチーム向けにアカウント横断のエージェント型サーチを実現するために Managed Agents を使っています。スケジュールドデプロイメントが回答を定期的に更新するようになり、チームが自前で構築していたスケジューリングインフラを置き換えて、スタックがシンプルになりました。[‍](https://ando.so)
- [Ando](https://ando.so) は、採用とセールスのチームの業務を止めずに前へ進めるためにスケジュールドデプロイメントを使っています。エージェントは複数のチャンネルを自律的に見張り、次の打ち手の候補を拾い上げ、期限が来たらフォローアップし、ミーティングのリマインダーを送ります。

## **環境変数を vault に保管して CLI やその他のツールを認証する**

エージェントは、直接的な API 呼び出し、CLI、MCP を介して [外部システムに接続します](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp)。今回、[vault](https://platform.claude.com/docs/en/managed-agents/vaults) を環境変数にも対応させました。これにより、CLI やその他のツールから認証付きリクエストを送れるようになります。CLI はシェル経由で既存のコマンドラインツールをエージェントに直接動かさせる仕組みであり、高速で軽量な統合パスになります。API キーを環境変数名と到達可能なドメインとともに登録すれば、エージェントのサンドボックスにインストールされた CLI がそのキーを使って認証付き API 呼び出しを行えます。

エージェントがあなたのキーそのものを見ることはありません。サンドボックスにはプレースホルダーだけが置かれ、本物のキーはネットワーク境界で、しかも許可したドメインへのリクエストにのみ付与されるため、承認した宛先以外には流れません。キーを変更したい場合は vault 側で更新するだけでよく、稼働中のセッションも次の呼び出しから新しい値を拾います。Browserbase、KERNEL、Notion、Ramp、Sentry の CLI など、HTTP リクエストでキーを送る大半の CLI はこの方式で動作します。[Browserbase](https://docs.browserbase.com/integrations/anthropic/managed-agents/quickstart) と [KERNEL](https://www.kernel.sh/docs/integrations/claude-managed-agents) は Managed Agents にブラウザ機能を初めてもたらすもので、エージェントは他のツールと並んで Web をナビゲートしたり操作したりできるようになります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a27074e40b19ba74e79b134_Claude-Managed-Agents-CLI-credential-vaults-diagram%20(1).png)

各チームは vault の環境変数を活用して、認証付きツールへエージェントに安全にアクセスさせています。

- [Notion](https://claude.com/customers/notion-qa) は、MCP ツールと並べて自社の CLI を展開するために vault の環境変数を使っており、API トークンをモデルに渡すことなくエージェントへファイルアップロード機能を加えています。
- [Browserbase](https://www.browserbase.com/) は、vault で認証された [browse CLI](https://www.npmjs.com/package/browse) を使って、ブラウザスキルのパブリックカタログを構築しました。スケジュールドデプロイメントがそのカタログを定期的に検証し、正確さを保ち続けます。
- [KERNEL](https://www.kernel.sh/docs/integrations/claude-managed-agents) は、利用状況とカスタマーとの会話を追跡しているデータベースへエージェントを安全に接続するために vault の環境変数を使っています。エージェントは利用量の急増を発生時点でフラグ立てし、チームがその活動が意図したものかをカスタマーに確認できるようにします。[‍](https://getmilana.ai/)
- [Milana](https://getmilana.ai/) は、AI プロダクトエンジニアをカスタマーのコードベースに安全に接続するために vault の環境変数を使っています。エージェントはバグを自動で発見・修正し、大規模なデータ分析も以前より高速に実行されます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

「vault の環境変数のおかげで、機微な API トークンをエージェントに一切渡すことなく、セキュリティチームの厳しいガイドラインに沿った形で Notion CLI を安全に展開できました。CLI は MCP ツールを補完するもので、Claude Managed Agents にファイルアップロード機能をもたらしてくれます。」

Quan Nguyen, Public API Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

「Rakuten 全社のチームが、スプレッドシートのデータを分析して週次や月次のスケジュールでレポートやスライドを作成するためにスケジュールドデプロイメントを使っています。私たちのパワーユーザーはそれを本番のログとメトリクスにも適用しており、プロダクトマネージャーが分析ダッシュボードを作らずに自分のアプリケーションの健全性を確認できるようになっています。」

Yusuke Kaji, General Manager of AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcd77828fd211e8ca469_ando-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcdb9e60b6c1a29d80cb_ando-dark.svg)

「私たちのユーザーの多くは、数多くのエージェントを扱うよりも、少数のエージェントと働くことを好みます。スケジュールドデプロイメントによって、より多くの能力を 1 つの自律的なエージェントに束ねられるようになりました。たとえば、1 つのエージェントが複数のセールスや採用のプロセスを見張り、適切な人にアップデートを問い合わせ、次の打ち手を前に進めていく、といった具合です。」

Sara Du, Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21d94491a062e83ceac776_actively_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21d9473660bc98f662b338_actively_dark.svg)

「私たちは Claude Managed Agents の上にアカウント横断のエージェント型サーチシステムを構築しました。セールスチームは『今日アプローチすべきアカウントはどれか』といった質問を投げかけられます。顧客は答えが定期的に更新されることを望むので、自前で組んでいたスケジューリングインフラをスケジュールドデプロイメントに置き換えました。これによりスタックは大きくシンプルになり、プロダクトの開発サイクルも改善しました。」

Mihir Garimella, Co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21c12cb4f396accc11370b_milana_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21c12f2f12836173fd5883_milana_dark.svg)

「Claude Managed Agents を使うことで、エージェントを顧客の実際のコードベースに根づかせられました。扱いやすく、ほぼ即座に高品質な結果が得られています。決定的だったのは vault の環境変数で、これによってエージェントはクレデンシャルを晒すことなく CLI 経由でプライベート API を呼び出せます。大規模なデータ分析は劇的に高速になり、アウトカムによってあらゆる出力の品質を担保できています。」

Raghav Sethi, Co-founder & CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a17890e390d07357c12beba_logo_browserbase-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a17891ccfcb6c4d6dcb3ce0_logo_browserbase-dark.svg)

「vault の環境変数によって、エンジニアリングチームは 2 つの大きなコンピュートのプリミティブ、つまりエージェントとブラウザを組み合わせられるようになりました。Browserbase では、エージェントが Web をナビゲートするのを助けるブラウザスキルのパブリックカタログを生成するために、browse CLI とともに Claude Managed Agents を使っています。スケジュールドデプロイメントが、私たちのパブリックカタログに対する定期的な検証を実行しています。」

Ziray Hao, Product Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28b0dd0f38383998beeebe_logo-kernel-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28b0e712c7ce11a06c9665_logo-kernel-dark.svg)

「Kernel のブラウザインフラストラクチャ上の利用量は急増することがあります。多くは顧客がデプロイした直後です。vault の環境変数によって、私たちのエージェントは利用状況と顧客との会話を追跡しているデータベースへ直接接続できるようになりました。30 日分の日次利用量を秒単位で取得し、急増を発生時点でフラグ立てし、その活動が意図したものかを顧客に確認するチームを支援します。」

Catherine Jue, Co-founder & CEO

## **使い始める**

詳しくは [ドキュメント](https://platform.claude.com/docs/en/managed-agents/overview) を参照するか、[Claude Console](https://platform.claude.com/) にアクセスして最初のエージェントをデプロイしてみてください。
