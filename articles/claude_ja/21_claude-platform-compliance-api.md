---
date: '2026-03-30'
final_url: https://claude.com/blog/claude-platform-compliance-api
number: 21
selector_used: main
slug: claude-platform-compliance-api
source_url: https://claude.com/blog/claude-platform-compliance-api
title: Audit Claude Platform activity with the Compliance API
title_ja: Compliance API で Claude Platform のアクティビティを監査する
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Compliance API で Claude Platform のアクティビティを監査する

## Compliance API で Claude Platform のアクティビティを監査する

Compliance API が Claude Platform で利用可能になりました。管理者は組織全体の監査ログにプログラマティックにアクセスできます。セキュリティ・コンプライアンスチームは、ユーザーアクティビティの追跡、設定変更の監視、Claude の利用データを既存のコンプライアンスインフラストラクチャに統合することができます。

## 組織向けの監査ログ

金融サービス、ヘルスケア、法律などの規制産業の組織は、誰が何にアクセスし、いつ、何が変更されたかの詳細な記録を必要とします。このデータにプログラマティックにアクセスできなければ、コンプライアンスチームは手動のエクスポートと定期的なレビューに頼らざるを得ず、スケールしません。

Compliance API は、組織全体のセキュリティ関連イベントを記録するアクティビティフィードを提供します。管理者は、時間範囲、特定のユーザー、または API キーでフィルタリングしてアクティビティログを取得できます。

API は現在、2 つのカテゴリのアクティビティを追跡しています：

- **管理者およびシステムのアクティビティ：** ワークスペースへのメンバー追加、API キーの作成、アカウント設定の更新、エンティティアクセスの変更など、リソースへのアクセスや設定を変更するアクション。
- **リソースのアクティビティ：** ファイルの作成、ファイルのダウンロード、スキルの削除など、ユーザー主導でリソースデータを作成・変更するアクション。データに影響を与えたり、リソースが機密情報にアクセスできるようにするアクションを対象としますが、モデルとの直接的なやり取りは除外されます。

これらを合わせると、ユーザーのログイン・ログアウトイベント、アカウント設定の更新、ワークスペースの変更、その他の組織監査イベントをカバーします。API は、ユーザーとモデルのやり取りやモデルのアクティビティなど、推論アクティビティはログに記録しません。

## 始め方

組織で Compliance API を有効にするには、アカウントチームにお問い合わせください。有効化されたら、管理者 API キーを作成し、アクティビティフィードエンドポイントへのクエリに使用します。なお、ログ記録は API が有効化された時点から始まり、それ以前の過去のアクティビティは取得できません。

Claude Enterprise 向けの Compliance API をすでに利用している組織は、Claude API の組織を同じ親組織に追加し、単一のフィードから両方のアクティビティをフィルタリングできます。

詳細については、[Anthropic Trust Center](https://trust.anthropic.com/resources?s=tob70gqyan60x3dwb7nkap&name=anthropic-compliance-api) のドキュメントをご覧ください。
