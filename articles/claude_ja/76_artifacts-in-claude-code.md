---
date: '2026-06-18'
final_url: https://claude.com/blog/artifacts-in-claude-code
number: 76
selector_used: main
slug: artifacts-in-claude-code
source_url: https://claude.com/blog/artifacts-in-claude-code
title: Claude Code now supports artifacts
title_ja: "Claude Code が artifacts に対応"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Claude Code が artifacts に対応

本日から、Claude Code は作業の進捗を artifact として取り込めるようになりました。これにより、Claude Code の作業はライブで共有可能なビジュアルなページ — PR ウォークスルー、システム解説、ダッシュボード、リリースチェックリストなど — に変換され、セッションが進むにつれてそれ自身が更新されていきます。

Claude Code のセッションは、インシデント調査からサービスのリファクタリング、数か月分のデータ分析まで、実に多岐にわたります。Artifacts はその作業を、誰でも開いて探索できる Web ページに変換します。たとえば、プルリクエストのウォークスルー、フィルタやソートができるダッシュボード、あるいは作業が進むにつれて自身が埋まっていくリリースチェックリストといった具合です。Artifacts は共有作業でのコラボレーションを容易にし、チームは状況報告に費やす時間を減らし、構築により多くの時間を使えるようになります。

## **セッションのコンテキストから組み立てる**

Claude Code は、コードベース、コネクタ、そして会話そのものを含む、セッションの完全なコンテキストを使って artifact を組み立てます。1 枚のインシデントページには、コードから抽出した失敗テストとその背後にある関数、接続済みモニタリングツールからのエラー急増、そして今しがた実行したセッションでの根本原因の推論を、まとめて載せられます。Artifacts なら、データソースを配線したりインフラを構築したりする必要はありません。ページを依頼するだけで、Claude Code がすでに存在するものから組み立ててくれます。

## **その場で更新されるライブなページ**

Claude Code が artifact を更新すると、開いているページはその場で再読み込みされ、チームメイトにも公開された瞬間に更新が見えます。公開のたびに同じリンク上で新しいバージョンが作られ、バージョン履歴からはいつでも復元できます。さらにギャラリーでは、自分が作ったすべての artifact を閲覧・管理できます。

私たちの社内テストで最も多かったユースケースの 1 つはデバッグでした。典型的には次のような流れになります。あるエンジニアが、朝のスタンドアップ前にインシデント調査を始めます。Claude Code はログを読み解きながら、タイムライン、容疑のあるコミット、エラーレートのチャートからなる artifact を公開します。彼女はページのヘッダーからチームにリンクを共有します。スタンドアップが始まる頃には、Claude は調査の進展に合わせて最新情報を取り込みながら、すでに 2 回そのページを再公開しています。Artifacts によって、チームメンバーやステークホルダーが「エージェントが見つけたことを順に説明してもらう」必要はなくなります。全員が同じビューを、同じコンテキストで見ているからです。

## **組織にプライベートな状態を保つ**

すべての artifact は、デフォルトでは作成者にのみプライベートです。準備ができたら、ページから直接チームメイトや組織に共有できます。Artifact は組織の認証済みメンバーだけが閲覧でき、公開状態にすることはできません。管理者は組織レベルのトグルとロールベースのスコープでアクセスを管理し、保持ポリシーを設定し、コンプライアンス API を通じて組織全体の可視性を得られます。

## **使い始める**

セッションに対して artifact を依頼する、あるいは何かビジュアルなものを依頼するだけで構いません。役割別のアイデアをいくつか挙げます。

- **法務 / オープンソース**: リポジトリから直接、すべての依存ライブラリのライセンス監査を行い、コピーレフトのものをフラグ付けします。*"Build an artifact listing every third-party dependency and its license, flagging anything copyleft."*
- **プライバシー**: 個人データがコード全体のどこで収集・保存・ログ記録されているかのデータフローマップ。*"Trace where we touch personal data across the codebase into an artifact for the privacy review."*
- **セキュリティ**: 該当する行に直接リンクされた検知結果。修正箇所が曖昧になりません。*"Build an artifact of the auth findings from this review, each linked to the code."*
- **FinOps / プラットフォーム財務**: インフラストラクチャ・アズ・コードからマッピングされたクラウドリソースとコスト要因。*"Map our cloud resources from the Terraform into an artifact, grouped by service, with the big cost drivers."*
- **ソフトウェアエンジニア**: 差分とその周辺コードから取り出した、レビュアーが本当に追える PR またはバグのウォークスルー。"Make an artifact walking through this PR — the diff, the reasoning, and what I tested."
- **デザイナー & フロントエンドエンジニア**: ある画面について、実在のコンポーネントから組み立てられた複数の UX 方向性。これにより、選んだものはそのままリリース可能になります。"Give me an artifact with 5 UX variations of this signup form, built from our component library."
- **スタッフエンジニア & アーキテクト**: ホワイトボードではなく、実際の import グラフから描き出された、サービスの実際の組み合わさり方のマップ。"Map how the payments service fits together into an artifact, from the code."
- **SRE & オンコール**: 調査が進むにつれて成長し、そのままポストモーテムになるインシデントページ。"Turn this incident into an artifact — timeline, suspect commits, error spike from our monitoring — and republish as I work through it."
- **エンジニアリングマネージャー**: マージ済みの PR から組み立てられた、実際に出荷されたものをまとめたページ。"Build an artifact of what merged on my team this week from the PRs, grouped by project."

Claude Code がページを作成し、リンクを返します。ブラウザまたはデスクトップアプリで開き、ヘッダーから共有してください。更新は自動的に同じ URL に公開されます。

## **提供状況**

Artifacts は、Claude Team および Enterprise 組織向けにベータとして提供されており、Claude Code CLI とデスクトップアプリから利用でき、ページは任意のブラウザで閲覧できます。

[***Claude Code***](http://code.claude.com/docs/en/artifacts) ***で今日から始めましょう。***
