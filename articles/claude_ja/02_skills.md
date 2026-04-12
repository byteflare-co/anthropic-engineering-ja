---
date: '2025-10-16'
final_url: https://claude.com/blog/skills
number: 2
selector_used: main
slug: skills
source_url: https://claude.com/blog/skills
title: Introducing Agent Skills
title_ja: Agent Skills の紹介
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2307f9555d7c1bc46cb_77dd9077412abc790bf2bc6fa3383b37724d6305-1000x1000.svg)

# Agent Skills の紹介

***アップデート:*** *Skills の[組織全体での管理機能](/blog/organization-skills-and-directory)、パートナーが構築した Skills を掲載する[ディレクトリ](https://claude.com/connectors)を追加し、[Agent Skills](https://agentskills.io) をクロスプラットフォームの互換性を実現するオープンスタンダードとして公開しました。(2025 年 12 月 18 日)*

Claude は *Skills* を使って特定のタスクの実行方法を改善できるようになりました。Skills は、Claude が必要に応じてロードできる指示、スクリプト、リソースを含むフォルダです。

Claude は、手元のタスクに関連する場合にのみ Skill にアクセスします。使用された場合、Skills により Claude は Excel の操作や組織のブランドガイドラインへの準拠など、専門的なタスクをより上手にこなせるようになります。

Skills が実際に活躍している様子は、Claude アプリですでにご覧いただけています。Claude はそこで Skills を使ってスプレッドシートやプレゼンテーションなどのファイルを作成しています。今後は、独自の Skills を構築し、Claude アプリ、Claude Code、API の全体で使用できます。

## Skills の仕組み

タスクに取り組む際、Claude は利用可能な Skills をスキャンして関連するものを見つけます。一致するものがあれば、必要最小限の情報とファイルのみをロードします——専門的な知識にアクセスしながらも、Claude の高速さを維持します。

Skills の特徴:

- **組み合わせ可能 (Composable)**: Skills は積み重ねて使えます。Claude はどの Skills が必要かを自動的に判断し、連携を調整します。
- **ポータブル (Portable)**: Skills はどこでも同じフォーマットを使用します。一度構築すれば、Claude アプリ、Claude Code、API のすべてで使えます。
- **効率的 (Efficient)**: 必要なものだけを、必要なときにロードします。
- **パワフル (Powerful)**: Skills には実行可能なコードを含めることができ、従来のプログラミングの方がトークン生成よりも信頼性が高いタスクに対応します。

Skills は、専門知識をパッケージ化してあなたにとって最も重要なことのスペシャリストにする、カスタムのオンボーディング資料と考えてください。Agent Skills の設計パターン、アーキテクチャ、開発のベストプラクティスについての技術的な詳細は、[エンジニアリングブログ](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)をご覧ください。

## Skills はすべての Claude 製品で動作します

### **Claude アプリ**

Skills は Pro、Max、Team、Enterprise ユーザーが利用できます。ドキュメント作成などの一般的なタスク用の Skills、カスタマイズ可能なサンプル、そして独自のカスタム Skills を作成する機能を提供しています。

![Claude.ai の Skills 機能インターフェース。サンプル Skills がオンに切り替えられた状態。](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690267e194f8fd4618cb330e_image.webp)

Claude はタスクに基づいて関連する Skills を自動的に呼び出します——手動での選択は不要です。Claude が作業中の思考の連鎖の中に Skills が表示されるのも確認できます。

Skills の作成はシンプルです。「skill-creator」Skills がインタラクティブなガイダンスを提供します。Claude がワークフローについて質問し、フォルダ構造を生成し、SKILL.md ファイルをフォーマットし、必要なリソースをバンドルします。手動でのファイル編集は不要です。

Skills は[設定](https://claude.ai/redirect/website.v1.51f73c97-b077-44e7-85ba-8b27a025dfdf/settings/features)で有効化できます。Team および Enterprise ユーザーの場合、管理者がまず組織全体で Skills を有効化する必要があります。

### **Claude Developer Platform (API)**

Agent Skills（一般的に単に Skills と呼ばれています）を Messages API リクエストに追加できるようになりました。新しい `/v1/skills` エンドポイントにより、開発者はカスタム Skills のバージョン管理と管理をプログラムで制御できます。Skills の実行に必要なセキュアな環境を提供する [Code Execution Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool) ベータが必要です。

Anthropic が作成した Skills を使って、Claude に数式を含むプロフェッショナルな Excel スプレッドシート、PowerPoint プレゼンテーション、Word ドキュメント、入力可能な PDF の読み取りと生成を行わせることができます。開発者は、独自のユースケースに合わせてカスタム Skills を作成し、Claude の機能を拡張できます。

また、開発者は Claude Console を通じて Skills のバージョンの作成、表示、アップグレードを簡単に行えます。

詳しくは[ドキュメント](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)、[Skills クックブック](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)、または [Anthropic Academy](https://www.anthropic.com/learn/build-with-claude) をご覧ください。

‍

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills は管理会計・財務ワークフローを効率化してくれます。Claude は複数のスプレッドシートを処理し、重要な異常を検出し、私たちの手順に従ってレポートを生成します。以前は丸一日かかっていた作業が、今では 1 時間で完了できます。

Yusuke Kaji, General Manager AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Skills は Claude に Box コンテンツの扱い方を教えます。ユーザーは保存されたファイルを、組織の標準に沿った PowerPoint プレゼンテーション、Excel スプレッドシート、Word ドキュメントに変換でき、何時間もの作業を節約できます。

Yashodha Bhavnani, Head of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

Canva は Skills を活用してエージェントをカスタマイズし、その能力を拡張する計画です。これにより、Canva をエージェントワークフローにより深く組み込む新しい方法が開かれ、チームが独自のコンテキストを取り込み、美しく高品質なデザインを簡単に作成できるようになります。

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

Skills により、Claude は Notion とシームレスに連携し、ユーザーを質問からアクションへとより速く導きます。複雑なタスクでのプロンプト調整が少なくなり、より予測可能な結果が得られます。

MJ Felix, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills は管理会計・財務ワークフローを効率化してくれます。Claude は複数のスプレッドシートを処理し、重要な異常を検出し、私たちの手順に従ってレポートを生成します。以前は丸一日かかっていた作業が、今では 1 時間で完了できます。

Yusuke Kaji, General Manager AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Skills は Claude に Box コンテンツの扱い方を教えます。ユーザーは保存されたファイルを、組織の標準に沿った PowerPoint プレゼンテーション、Excel スプレッドシート、Word ドキュメントに変換でき、何時間もの作業を節約できます。

Yashodha Bhavnani, Head of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

Canva は Skills を活用してエージェントをカスタマイズし、その能力を拡張する計画です。これにより、Canva をエージェントワークフローにより深く組み込む新しい方法が開かれ、チームが独自のコンテキストを取り込み、美しく高品質なデザインを簡単に作成できるようになります。

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

Skills により、Claude は Notion とシームレスに連携し、ユーザーを質問からアクションへとより速く導きます。複雑なタスクでのプロンプト調整が少なくなり、より予測可能な結果が得られます。

MJ Felix, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills は管理会計・財務ワークフローを効率化してくれます。Claude は複数のスプレッドシートを処理し、重要な異常を検出し、私たちの手順に従ってレポートを生成します。以前は丸一日かかっていた作業が、今では 1 時間で完了できます。

Yusuke Kaji, General Manager AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Skills は Claude に Box コンテンツの扱い方を教えます。ユーザーは保存されたファイルを、組織の標準に沿った PowerPoint プレゼンテーション、Excel スプレッドシート、Word ドキュメントに変換でき、何時間もの作業を節約できます。

Yashodha Bhavnani, Head of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

Canva は Skills を活用してエージェントをカスタマイズし、その能力を拡張する計画です。これにより、Canva をエージェントワークフローにより深く組み込む新しい方法が開かれ、チームが独自のコンテキストを取り込み、美しく高品質なデザインを簡単に作成できるようになります。

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

Skills により、Claude は Notion とシームレスに連携し、ユーザーを質問からアクションへとより速く導きます。複雑なタスクでのプロンプト調整が少なくなり、より予測可能な結果が得られます。

MJ Felix, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills は管理会計・財務ワークフローを効率化してくれます。Claude は複数のスプレッドシートを処理し、重要な異常を検出し、私たちの手順に従ってレポートを生成します。以前は丸一日かかっていた作業が、今では 1 時間で完了できます。

Yusuke Kaji, General Manager AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Skills は Claude に Box コンテンツの扱い方を教えます。ユーザーは保存されたファイルを、組織の標準に沿った PowerPoint プレゼンテーション、Excel スプレッドシート、Word ドキュメントに変換でき、何時間もの作業を節約できます。

Yashodha Bhavnani, Head of AI
