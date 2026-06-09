---
date: '2026-06-08'
final_url: https://claude.com/blog/observability-for-developers-building-connectors
number: 68
selector_used: main
slug: observability-for-developers-building-connectors
source_url: https://claude.com/blog/observability-for-developers-building-connectors
title: Observability for developers building connectors
title_ja: コネクタを構築する開発者向けのオブザーバビリティ
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

# コネクタを構築する開発者向けのオブザーバビリティ

## コネクタを監視・デバッグし、改善する

[ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.cb147317-f48a-4146-b56b-5b1b03b579b3/directory/connectors)で公開されているコネクタに対して、Claude の各プロダクトサーフェスでのパフォーマンスを示すダッシュボードが利用できるようになりました。コネクタのオーナーは、これを以下の用途に活用できます。

- **採用状況の追跡。** アクティブユーザー数、ツール呼び出しの総数、そしてディレクトリ内の順位を時系列でモニタリングできます。
- **エラーとレイテンシの診断。** ヘルススコア、エラー率、レイテンシを一目で確認でき、ツールごとのエラー内訳によって、何が失敗しているのかを特定できます。**‍**
- **プロダクト別の利用状況の内訳。** Claude、Claude Code、Cowork などにわたってツール呼び出しを比較し、ユーザーがどこで活発に利用しているかを把握できます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a26eb0505466f798299b38a_MCP%20Observability.png)

*コネクタのオブザーバビリティのスタイライズドビュー。データはイメージです。*

本日よりパブリックベータで利用可能です。Claude の [組織設定](https://claude.ai/redirect/claudedotcom.v1.cb147317-f48a-4146-b56b-5b1b03b579b3/admin-settings/organization) 内の [ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.cb147317-f48a-4146-b56b-5b1b03b579b3/admin-settings/directory/submissions) からアクセスできます。利用には Team または Enterprise アカウントで Admin または Owner の権限が必要です。あるいは Enterprise において Libraries 権限を持つ [カスタムロール](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans) でもアクセス可能です。

## ディレクトリへの参加

コネクタは [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) の上に構築されています。[ディレクトリ](https://claude.ai/redirect/claudedotcom.v1.cb147317-f48a-4146-b56b-5b1b03b579b3/directory/connectors) には 300 を超えるサードパーティ製コネクタが存在し、毎日数百万人に利用されています。ご自身の MCP サーバーをディレクトリに登録したい場合は、Claude から直接申請できるようになりました。[詳細はこちら](https://claude.com/docs/connectors/building/submission)。
