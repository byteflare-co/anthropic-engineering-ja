---
date: '2026-06-29'
final_url: https://claude.com/blog/introducing-the-claude-apps-gateway
number: 81
selector_used: main
slug: introducing-the-claude-apps-gateway
source_url: https://claude.com/blog/introducing-the-claude-apps-gateway
title: Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud
title_ja: Amazon Bedrock と Google Cloud のための Claude apps gateway を発表
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

# Amazon Bedrock と Google Cloud のための Claude apps gateway を発表

本日、Amazon Bedrock と Google Cloud のための Claude apps gateway を発表します。これまで、これらのプラットフォーム上で Claude Code を運用するためには、開発者ごとにクラウドのクレデンシャルをプロビジョニングし、設定を各ラップトップに手動でプッシュし、開発者単位の支出を可視化するための別途ツールを立ち上げる必要がありました。Claude apps gateway は、コーポレート SSO ログイン、中央で強制されるポリシー、ロールベースのアクセス、そして Claude Code のユーザー単位コスト按分を提供する、セルフホスト型のコントロールプレーンです。

## **ゲートウェイのデプロイ**

ゲートウェイは、Linux 上にデプロイされ PostgreSQL データベースを背後に持つ、単一のステートレスコンテナとして動作します。アップストリームのクレデンシャルを保持し、開発者を ID プロバイダに対して認証し、管理対象設定の配布と強制を行い、ユーザー単位の利用状況をお客様が運用するコレクターに報告します。開発者のオンボーディングは、ID プロバイダ (IdP) に追加するだけ。オフボーディングは、そこから削除するだけです。

ゲートウェイは Anthropic が構築・提供し、開発者がすでにインストールしているのと同じ `claude` バイナリに同梱されているため、お客様のインフラ上で 1 つのステートレスコンテナとして動かせます。ゲートウェイとクライアントは一体で構築されているので、`/login` フローはゲートウェイを認識し、クライアントはサインイン時に管理対象設定を自動適用し、ポリシーはすべてのリクエストに対して一貫して強制されます。

## **ゲートウェイの仕組み**

ゲートウェイは以下を担います。

- **アイデンティティ。** Google Workspace、Microsoft Entra ID、Okta、あるいは標準準拠の任意の OIDC プロバイダに対して OpenID Connect (OIDC) のリライングパーティとして動作し、短命のセッションを発行します。長命のシークレットが開発者のマシンに置かれることはありません。
- **ポリシー。** 管理対象設定をサーバー側で一度定義しておくと、クライアントはサインイン時にポリシーを受け取り、ゲートウェイはすべてのリクエストでそれを強制します。許可するモデルや既定値を中央で調整できます。
- **テレメトリ。** クライアントはリクエストごとに利用メトリクスをスタンプし、ゲートウェイはそれを OTLP 経由でお客様が構成したコレクターへ中継します。ネットワークも保持期間もすべてお客様の管理下です。
- **ルーティング。** ゲートウェイがアップストリームのクレデンシャルを保持し、推論を Claude API、Amazon Bedrock、Google Cloud にルーティングします。プロバイダ間のフェイルオーバーもオプションで利用できます。
- **支出上限。** ゲートウェイでは日次・週次・月次の支出上限を設定できます。組織単位、グループ単位、ユーザー単位で適用可能です。

ゲートウェイは、Claude API を使うように構成しない限り、推論トラフィックや利用状況データを Anthropic に送ることはありません。また、ゲートウェイが使うプロトコルは公開しており、他のゲートウェイ開発者が同じ機能を実装できるようにしています。

## **使い始める**

ゲートウェイは現在提供中です。使い始めるには以下を行ってください。

- **ゲートウェイをデプロイする**: Claude Code CLI バイナリをダウンロードし、`gateway.yaml` を OIDC issuer とアップストリームのクレデンシャルに向け、IdP に OIDC アプリを 1 つ登録します。
- **ロールアウトする**: クライアントマシンの `managed-settings.json` で `forceLoginMethod` と `forceLoginGatewayUrl` パラメータを構成します。クライアントは初回起動時にお客様のゲートウェイに接続します。

詳しくは [ドキュメント](https://code.claude.com/docs/en/claude-apps-gateway) をご覧ください。
