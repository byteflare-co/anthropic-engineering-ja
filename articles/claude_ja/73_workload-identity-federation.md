---
date: '2026-06-17'
final_url: https://claude.com/blog/workload-identity-federation
number: 73
selector_used: main
slug: workload-identity-federation
source_url: https://claude.com/blog/workload-identity-federation
title: Secure access to the Claude Platform with Workload Identity Federation
title_ja: "Workload Identity Federation で Claude Platform への安全なアクセスを実現する"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Workload Identity Federation で Claude Platform への安全なアクセスを実現する

Workload Identity Federation (WIF) が Claude Platform で一般提供 (GA) となりました。WIF は任意の OIDC 準拠 ID プロバイダと互換性があり、ファーストパーティの SDK や Claude Code 経由でアクセスする場合も含めて、すべての Claude API エンドポイントをカバーします。

ワークロード向けの WIF と、対話セッション向けの [ant auth login](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#authentication) を使うことで、開発者は Claude Platform を活用してビルドする際に、もはや静的な API キーを扱う必要がありません。

## Workload Identity Federation の仕組み

WIF は静的な API キーを、リクエスト時に発行される短命でスコープ付きの認証情報に置き換えます。GitHub Actions を動かしている 2 人のスタートアップであれ、詳細な認証情報ポリシーを持つエンタープライズであれ、スタックの他の部分で認証しているのと同じやり方で Claude Platform に対しても認証できるようになりました。

WIF を使えば、作成・ローテーション・漏洩の心配をすべき静的な Anthropic の認証情報は存在しません。ワークロードは既に持っている ID — AWS IAM ロール、GCP や Kubernetes のサービスアカウント、Azure マネージド ID、GitHub Actions のトークン、Okta、その他の OIDC 準拠プロバイダ — を使って認証します。

また、Claude Platform にサービスアカウントを導入します。これにより、各ワークロードは共有 API キーではなく、それぞれ独自の ID、ロール、監査証跡を持つことができます。まず、フェデレーションルールが外部 ID をサービスアカウントに紐付けます。次に、ワークロードがアクセスを要求すると、Claude Platform はワークロードの署名付き OIDC トークンを検証し、そのクレームをフェデレーションルールと突き合わせ、サービスアカウントのロールに制限された短命のアクセストークンを発行します。すべての交換とリクエストは、監査ログ上でそのサービスアカウントに紐付けて記録されます。

## 最初のワークロードを数分でセットアップ

[Claude Console](https://platform.claude.com/) には、ワークロード ID を設定するためのガイド付きセットアップフローがあります。セットアップでは各ステップを検証し、最後にワークロードが認証できることを確認するテストコマンドで完了します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a32fdc2f8d799c035dbec52_Screenshot%202026-06-17%20at%203.39.59%E2%80%AFPM.png)

## 組織全体を静的キーなしで運用する

WIF は組織管理向けの [Admin API](https://platform.claude.com/docs/en/build-with-claude/administration-api) と互換性があります。フェデレーションルールは、きめ細かいスコープを通じて最小権限アクセスを実現するように構成できます。

大規模に運用している組織のために、フェデレーションの構成は完全にプログラマブルにもなっています。新しい Admin API エンドポイントを使えば、issuer、サービスアカウント、フェデレーションルールの作成と更新が可能です。

## はじめに

API キーは WIF と並行して動作するため、ワークロードを一つずつ移行できます。各 ID プロバイダ向けのセットアップ[ガイド](https://platform.claude.com/docs/en/build-with-claude/workload-identity-federation)を参照するか、[Claude Console](https://platform.claude.com/) を開いて最初のワークロードを接続してください。
