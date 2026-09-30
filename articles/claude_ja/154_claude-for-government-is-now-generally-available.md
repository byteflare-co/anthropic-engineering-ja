---
date: '2026-09-30'
final_url: https://claude.com/blog/claude-for-government-is-now-generally-available
number: 154
selector_used: main
slug: claude-for-government-is-now-generally-available
source_url: https://claude.com/blog/claude-for-government-is-now-generally-available
title: Claude for Government is now generally available
title_ja: "Claude for Government が一般提供を開始しました"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

# Claude for Government が一般提供を開始しました

本日、[Claude for Government](https://claude.com/solutions/government) が連邦政府機関および州政府機関向けに一般提供を開始しました。このプラットフォームは、FedRAMP High 認定環境を通じて Claude のコーディングおよびエージェント作業の機能を提供するもので、[7月からパブリックベータ](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government)として提供されてきました。

政府機関は、コンプライアンス要件を妥協することなく、Anthropic の商用顧客と同等の機能にアクセスできます。新しい機能は基本的に商用リリースと同じサイクルで提供されます。

[Claude](https://claude.com/product/overview) はデスクトップ上のファイルと直接連携するため、政府機関の職員はメモ作成、RFP レビュー、ケースワークなどの業務でスキル、プラグイン、プロジェクトを利用できます。[Claude Code](https://claude.com/product/claude-code) を使えば、公共部門のチームは公共サービスを支える基盤となるソフトウェアシステムを構築・近代化できます。

Claude for Government のガバナンス管理機能は、公共部門機関向けに専用設計されています。管理者は設定のデフォルト値を設定できるほか、部門ごとの支出の割り当てと管理も行えます。セキュリティチームおよび認可担当者は、機関の ATO(運用認可)プロセスをサポートする監査ログとドキュメントを利用できます。調達担当者は Anthropic と直接契約を結び、一般提供の条件で発注できます。

Claude Code のコマンドラインインターフェースと [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365) も、同じ環境と同じ管理機能を通じてアーリーアクセスとして展開が進んでいます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6abd44931eac8f7038069dbe_a433ad54.png)

*管理コンソールの設定画面*

## 課金、管理、監視

**シート料金なし。** 政府機関は使用量に応じて固定単位で支払い、上限額を超えないハードな上限が設定されているため、支出が機関の予算を超えることはありません。管理者はグループごとに支出とモデルの上限を持つユーザー階層を定義し、ユーザーごと・モデルごとの使用状況を追跡し、残高が少なくなる前にバーンダウンアラートを受け取ります。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6abd44931eac8f7038069dbb_0a9d452c.png)

*管理コンソールの支出分析画面*

**部門の組織構造に合わせた管理。** 部門レベルの管理者は、各下部機関が自らのユーザーを管理しつつ、前払いの使用枠を下部機関に割り当てられます。各機関は独自の ID プロバイダーをシングルサインオンのために接続でき、管理ポータルでセルフサービスによる設定が可能です。SCIM のグループマッピングにより、シート階層ごとのレート制限、支出上限、利用可能なモデルを設定できます。階層化された設定により、下部機関に対するデフォルト値(Claude が接続できる対象や利用可能な機能を含む)を設定できます。

**設計段階からの監視。** 管理操作はすべて監査ログに記録され、組織の管理者が確認できます。Anthropic 側でのセンシティブな操作には、2人による承認が必要です。使用状況のエクスポートはメータリングデータのみであるため、機関はセンシティブな資料を移動させることなく ATO や監察官(IG)からの要求に対応できます。会話履歴は機関が管理するデバイス上にローカルに保存されます。

## はじめに

Claude for Government は本日より、連邦政府機関および州政府機関に一般提供されています。政府機関は利用開始にあたり別途クラウドプロバイダーとの契約を結ぶ必要はありません。既存の顧客は、アプリ内インポートを通じて会話履歴を引き継いだまま、デスクトップアプリケーションに移行できます。

[FedRAMP セキュア構成ガイド](https://trust.anthropic.com/resources#6ab2b125752bf0e0e8025505)は、Anthropic の[トラストセンター](https://trust.anthropic.com/)から入手できます。アプリケーションは標準的な機関の MDM プラットフォームを通じて展開されます。

新規の政府機関は [claude.com/solutions/government](http://claude.com/solutions/government) からアクセスをリクエストできます。Claude Code CLI または Claude for Microsoft 365 のアーリーアクセスに参加するには、公共部門担当チームまでお問い合わせください。
