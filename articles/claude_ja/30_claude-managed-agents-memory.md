---
date: '2026-04-23'
final_url: https://claude.com/blog/claude-managed-agents-memory
number: 30
selector_used: main
slug: claude-managed-agents-memory
source_url: https://claude.com/blog/claude-managed-agents-memory
title: Built-in memory for Claude Managed Agents
title_ja: "Claude Managed Agents に組み込みのメモリー"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

# Claude Managed Agents に組み込みのメモリー

[Claude Managed Agents](https://claude.com/blog/claude-managed-agents) のメモリーが、本日からパブリックベータで利用可能になりました。あなたのエージェントは、パフォーマンスと柔軟性を両立させた、インテリジェンス最適化されたメモリー層を使って、セッションごとに学習できるようになります。メモリーはファイルとして保存されるため、開発者はそれをエクスポートし、API を介して管理し、エージェントが何を保持するかを完全にコントロールできます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e911b25f02df256c8cba87_Claude-Blog-CMA-Memory.png)

## セッションをまたいで学習するエージェント

Managed Agents は、本番環境向けのインフラと、パフォーマンス向けにチューニングされたハーネスを組み合わせたものです。メモリーはそれを拡張します——セッションをまたいで改善し、学んだことを互いに共有するような長時間稼働のエージェントに向けて、内部ベンチマークで最適化されています。

私たちは、エージェントがすでに使っているツールの上にメモリーを積み上げたとき、メモリーが最も効果を発揮することに気づきました。Managed Agents のメモリーはファイルシステムに直接マウントされるため、Claude は、エージェンティックなタスクで力を発揮させているのと同じ bash やコード実行機能に頼ることができます。ファイルシステムベースのメモリーによって、[最新のモデル](https://www.anthropic.com/news/claude-opus-4-7#:~:text=Memory.%20Opus%204.7%20is%20better%20at%20using%20file%20system%2Dbased%20memory.%20It%20remembers%20important%20notes%20across%20long%2C%20multi%2Dsession%20work%2C%20and%20uses%20them%20to%20move%20on%20to%20new%20tasks%20that%2C%20as%20a%20result%2C%20need%20less%20up%2Dfront%20context.) はより包括的で整理されたメモリーを保存し、あるタスクについて何を覚えておくべきかをより的確に見極められるようになります。

## 本番品質のエージェントに向けた、ポータブルなメモリー

メモリーは、スコープ付きの権限、監査ログ、完全なプログラマティック制御を備え、エンタープライズ配備向けに作られています。ストアは、異なるアクセススコープを持つ複数のエージェント間で共有できます。たとえば、組織全体のストアを読み取り専用にしつつ、ユーザー単位のストアでは読み書きを許す、といった具合です。複数のエージェントが、互いを上書きすることなく同じストアに対して同時に動作できます。

メモリーはファイルであり、API を通じてエクスポートしたり独立して管理したりできます。開発者に完全なコントロールが委ねられています。すべての変更は詳細な監査ログで追跡され、どのエージェントのどのセッションに由来するメモリーかを特定できます。以前のバージョンへロールバックしたり、履歴からコンテンツを削除したりすることも可能です。更新は [Claude Console](https://platform.claude.com/) にもセッションイベントとして現れるため、エージェントが何を学び、それがどこから来たのかを開発者が追跡できます。

## **チームが作っているもの**

各チームはメモリーを使って、フィードバックループを閉じ、検証を高速化し、独自の検索インフラを置き換えています。

- **Netflix** のエージェントは、複数ターンを経て明らかになった洞察や、会話の途中で人間から受けた修正を含む文脈をセッションをまたいで保持し、プロンプトやスキルを手作業で更新する必要がなくなっています。
- **Rakuten** のタスクベースの長時間稼働エージェントは、メモリーを使ってセッションごとに学習し、過去の誤りを繰り返すのを避けており、ワークスペース単位でスコープされ観測可能な境界の内側で、初回パスの誤りを 97% 削減しています。
- **Wisedocs** は、文書検証パイプラインを Managed Agents の上に構築し、セッションをまたぐメモリーを使って文書の繰り返し発生する問題を見つけて覚えさせ、検証を 30% 高速化しました。**‍**
- **Ando** は、職場向けメッセージングプラットフォームを Managed Agents の上に構築しており、メモリーインフラを自前で作る代わりに、組織ごとのやり取りの仕方を取り込んでいます。

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Claude Managed Agents のメモリーは、継続的な学習を大規模に本番投入することを可能にしてくれます。私たちのエージェントはセッションごとに教訓を抽出し、初回パスの誤りを 97% 削減しつつ、コストを 27%、レイテンシを 34% 下げています。そのため、システムがすでに学習済みの誤りをユーザーがわざわざ修正させる時間は減ります。加えて、メモリーはワークスペース単位でスコープされ観測可能なので、継続的な学習は私たちのコントロール下にとどまります。

Yusuke Kaji, General Manager, AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2b0eeb286e0a7c7bf61a_ando-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2b1178ce135b536f2f95_ando-dark.svg)

Ando での私たちの仕事の多くは、チームと彼らのエージェントとの間で目まぐるしく動く、雑然とした会話を理解することにあります。メモリーによって、メモリーインフラを作るのをやめて、プロダクトそのものに集中できるようになります。

Sara Du, Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2b010f3f3d0c408c6ec5_wisedocs-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ea2afe43c6e63a42d7d5ce_wisedocs-dark.svg)

よくできたメモリー API は、特にエージェントやセッションをまたいで構築する場合に、多くのインフラ面の頭痛のタネを取り除いてくれます。私たちの Claude Managed Agents 上の文書検証パイプラインでは、セッションをまたぐメモリーを使い、エージェントに一般的な問題——私たちが想定していなかったものも含めて——を特定して覚えさせました。それによって検証は 30% 高速化しています。

Denys Linkov, Head of Machine Learning
