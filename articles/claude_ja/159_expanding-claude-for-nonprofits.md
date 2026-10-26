---
date: '2026-10-26'
final_url: https://claude.com/resources/articles/expanding-claude-for-nonprofits
number: 159
selector_used: article
slug: expanding-claude-for-nonprofits
source_url: https://claude.com/blog/expanding-claude-for-nonprofits
title: Expanding Claude for Nonprofits
title_ja: Claude for Nonprofits を拡充します
---

本日、約 30 の非営利団体とともに構築したスキルとコネクタのセット、Claude for Nonprofits プラグインをリリースします。このプラグインは、組織のコンテキストやポリシーに沿って Claude を責任ある形でセットアップすることを支援し、リサーチからレポーティングまでファンドレイジングをサポートし、少人数のチームを圧迫しがちな業務オペレーションを引き受けます。また、米国の非営利団体にキャリア初期のフェローを派遣するプログラム [Claude Corps](http://anthropic.com/claude-corps) を、[Taproot](https://taprootfoundation.org/) とのパートナーシップを通じて拡大する計画も進めています。

公益法人（public benefit corporation）として、Anthropic には、世界で最も困難な課題に取り組む組織にとって私たちの製品が利用しやすく、役に立つものであるようにする責任があります。昨年 12 月、私たちは最大 75% の割引、Blackbaud・Candid・Benevity 向けのコネクタ、そして GivingTuesday と共同で制作した無料の AI Fluency コースを備えた [Claude for Nonprofits](https://www.anthropic.com/news/claude-for-nonprofits) を立ち上げました。現在では 25,000 を超える非営利団体が業務で Claude を利用しています。その多くは小規模な地域の団体で、75% 以上が Claude のシート数 10 未満です。今回のアップデートが最も大きな効果をもたらすのは、こうした団体だと考えています。

International Rescue Committee（IRC）で AI Transformation を率いる Katherine Rodrigues 氏は、Claude が肺炎症例の急増を察知し、対応の動員に役立った経緯を説明しています。

この 1 年間、私たちは非営利団体と直接協力し、そのニーズに応えてきました。非営利団体向けプランで利用できるモデルを通常の Team / Enterprise プランと同じものに拡大し、Team プランの最低人数を 2 名の組織から利用できるように引き下げ、さらに Claude Code を追加費用なしで非営利団体向けプランに含めました。そして 9 月の国連総会の期間中には、低・中所得国の認証済み非営利団体向けに約 90% の新たな割引を開始し、標準の Team シートを 1 ユーザーあたり月額 3 ドルで提供できるようにしました。

コストは障壁の 1 つにすぎません。非営利団体からは、ほかに 2 つの障壁があると聞いています。AI を実務に活かすスキルを持つ人材の不足と、非営利団体の業務のあり方に合わせて作られたツールの不足です。

- **AI スキルを持つ人材が少なすぎる**。Claude Corps は、1,000 人のキャリア初期のフェローを少なくとも 400 の米国の非営利団体に派遣し、各団体のチームとともに Claude を使った開発に取り組んでもらいます。受け入れ団体は大規模な組織から小規模な地域チームまで多岐にわたり、フードバンク、美術館、退役軍人支援団体なども含まれます。現在、このプログラムを Taproot とのパートナーシップを通じて拡大する計画を進めており、非営利団体と経験豊富なプロボノコンサルタントをマッチングし、より短期のプロジェクトベースの業務を支援する予定です。非営利団体の導入を支援できるパートナーも増えており、Accenture、Boston Consulting Group（BCG）、The Bridgespan Group、Civis Analytics、Deloitte、fusionSpan、Idealist Consulting、Myridius、SapienAI、Slalom、v4c.ai、Vera Solutions などが参加しています。また、自力で始めるチームのために、2 回のライブウェビナーを開催します。管理者向けの [Claude for Nonprofits: An Admin's Guide to Data Handling and AI Use Policy](https://claude.com/resources/webinars/claude-for-nonprofits-admin-guide-to-data-handling-ai-policy) を 11 月 10 日に、[Claude for Nonprofits: A Staff Guide to Making Claude Useful on Day One](https://claude.com/resources/webinars/claude-for-nonprofits-a-staff-guide-to-making-claude-useful-on-day-one) を 11 月 12 日に開催します。
- **非営利団体の実情に寄り添うツールが少なすぎる。** 本日リリースするスキルは、Design Partner Circle に参加する非営利団体とともに構築しました。Design Partner Circle には、米国の一地域を対象とする小規模なチームから、数十か国で活動する国際組織まで約 30 の団体が参加しており、教育、経済的モビリティ、保健、人道支援などに取り組んでいます。その多くは自ら助成を行う団体でもあります。この秋、これらの団体のファンドレイザー、オペレーション担当責任者、チーフ・オブ・スタッフの方々が、スキルの初期バージョンを実際の業務で試し、うまくいかない点を教えてくれました。私たちはそのフィードバックをもとにブレインストーミングと改良を重ね、ソリューションを更新しました。

## **プラグインの内容**

まずは、非営利団体から特に緊急性が高いと聞いた 3 つの領域から始めます。年末のファンドレイジングが本格化する時期にあたり、なおさら重要な領域です。

### **チームの力を広げる**

多くの非営利団体から同じ声を聞きました。やるべき仕事に対して人手が足りず、誰もが同時に複数の役割を担っている、というものです。Claude はチームの力を広げ、少人数のスタッフでも大きなチームのように働き、より多くの時間をミッションに充てられるようにします。

- **マーケティング:** チームのキャパシティに見合った規模のキャンペーンを計画し、組織の語り口で下書きを書けるよう Claude に教え、公開前のコンテンツにセカンドオピニオンを得られます。
- **採用と人材:** 面接ガイドと評価ルーブリック付きの求人票を作成し、新入社員の最初の 90 日を計画し、自団体のハンドブックに基づいてスタッフの質問に答えられます。
- **理事会とリーダーシップ**: 理事会に不足しているスキルを把握し、候補者へのアプローチ文を下書きし、オリエンテーション資料で新任理事の立ち上がりを支援し、次回会議のスライド構成を計画できます。

### **Claude を責任ある形でセットアップする: セキュリティ、ガバナンス、コンテキスト**

Claude は、ミッション、プログラム、業務の流れ、コミュニケーションの原則、ポリシーといった組織のコンテキストを把握し、スタッフが Claude と協働するための明確なルールを持っているときに最も力を発揮します。まずは Claude に次のことを頼んでみてください。

- **組織のマップを作る**。Claude は、寄付者データ、助成関連ファイル、財務、ポリシーなど、記録の種類ごとにどこに保管しているかを尋ね、メモリがオンになっていれば、そのマップを各ユーザーごとに保存します。そのうえで、まだアクセスできないツールへの接続を提案します。プラグイン内の他のスキルはすべて最初にこのマップを参照するため、Claude はどこを探せばよいかを把握しており、タスクごとに同じ情報源を指示する必要はありません。
- **AI ポリシーで許可されている範囲を確認する**。スタッフは「これに Claude を使ってもいいですか？」と尋ねるだけで、組織独自の AI ポリシーに基づいた回答を得られます。（まだポリシーがない場合は、下記の Claude Academy のチュートリアルをご覧ください。）

### **ミッションのための資金を確保する**

ファンドレイジングは非営利団体の生命線であり、年末に向けてその重要性はさらに増します。一方で、時間がかかりプロセスも煩雑なため、小規模な団体にとっては大きな負担になりがちです。このプラグインはファンドレイジングのライフサイクル全体をサポートし、関係構築やどの機会を追求するかの判断といった、人にしかできない仕事にチームが時間を使えるようにします。

- **適切な資金提供者と助成金を見つける。** 寄付者、財団、企業をリサーチし、公募中の助成金を出典付きで提示します。
- **何に応募するかを決める**。RFP を転送すると、応募資格、要件、競争に必要なことの内訳が得られます。
- **提案書と報告書を書く**。RFP を要件リストに変換し、自団体の資料をもとに最初の下書きを作成します。助成金の報告書には、数値の出典が含まれます。
- **関係を良好に保つ**。資金提供者との通話前にはブリーフを、通話後には議事メモとお礼状を、そして組織の語り口で寄付者向けの近況報告を作成できます。寄付者との関係を再構築する方法を尋ねれば、スチュワードシップ計画が得られます。

## **非営利団体で生まれている成果**

![Start Early](https://assets.claude.com/6541206dc090ad5a7fadf587667a4ee86936b847.png)

> 「Start Early にとって、AI はミッションを担う人々を支えるツールです。Claude は当初、書式設定などの作業でスタッフの時間を節約してくれました。非営利団体向けスキルはそれをさらに推し進め、AI が単一のタスクではなくワークフロー全体を支えられるというビジョンを示してくれます。それにより、チームは確かな出発点を得て、子どもと家族のための成果を前進させることにより多くの時間を割ける機会が生まれます。」

Stella Owings 氏、Senior Project Manager、Start Early

![StriveTogether](https://assets.claude.com/225161d8c9a7bd9037ec36a8242931806b2faad1.png)

> 「優れた投資家エンゲージメントは、資金提供者が何を目指しているかを理解することから始まります。Claude の非営利団体向けスキルは、資金調達の機会を見つけ、資金提供者の目標を私たちのプログラムと結びつけ、CRM から関係の履歴を引き出すのに役立つ事務ツールとなっています。これにより、私たちのチームは、すべての子どもがゆりかごからキャリアまで成功できるよう支援するという StriveTogether のミッションを前進させる関係の強化に、より多くの時間を使えるようになりました。」

Amanda Jenkins 氏、Senior Manager, Development、StriveTogether

![Taleemabad](https://assets.claude.com/3a7627767b214c5b6ab07277dafa43ed4a36499f.png)

> 「私たちは、すべての教師がポケットにコーチを持てるよう、Claude を使って Rumi を構築しました。国のカリキュラムを 1 年分の日々の授業に落とし込む作業は、かつては専門家チームが何年もかけて行うものでした。今では私たちのエージェントがそれを 1 週間でこなし、さらに毎日、教師それぞれの言語で指導を行っています。教師の 95% が授業計画を役に立つと評価しています。私たちは 6 か国で 16,000 人の教師と 418,000 人の学習者を支援しており、Rumi はオープンソースなので他の人も利用できます。」

Haroon Yasin 氏、CEO、Taleemabad

![Allies against slavery](https://assets.claude.com/e87a1a8972f585dbd62ff9625f53dd0706d2fe27.png)

> 「私たちは Claude を、決して疲れることのないリサーチフェローだと考えています。その助けにより、たった 1 人の政府渉外チームが、750 を超える州の人身取引対策ポリシーの分析を、地域の支援者が議員に持ち込める提言へと変え、人々を脆弱な状態に置いている隙間を埋められるようになりました。」

John Nehme 氏、President & CEO、Allies Against Slavery

![Best Friends Animal Society](https://assets.claude.com/f1d64616128457ba4f6b6bedd60d89ed441d14ba.png)

> 「Best Friends では、チームが命を救うことに集中できるよう、障壁を取り除く方法を常に模索しています。Anthropic の Design Partner Circle に参加したことで、非営利団体が実際に直面する課題に即したツールづくりに関わる機会を得ました。Anthropic がフィードバックを素早く取り入れ、団体のインパクトを高める実用的な改善へとつなげてくれたことに感銘を受けました。」

Marc Peralta 氏、Chief Program Officer、Best Friends Animal Society

![Braven](https://assets.claude.com/f2ffb1d3609f6c15e4dc83ea5ef0bee069cc767a.png)

> 「Braven では AI を効果的に活用したいと考えており、Claude はそこに到達するための重要な手段です。全員がアクセスでき、独自のトレーニングを実施し、IT チームが構築した Claude のスキルを今では組織全体で共有しています。AI を善のために活かす最善の方法は、自分たち自身で使い、何がうまくいき何がうまくいかないかを絶えず試し、学び続けることだと考えています。」

Alina Yang 氏、Head of Transformation、Braven

![Civis](https://assets.claude.com/08c4f5da87e4e523c0ac482c0890bd538a62f17b.png)

> 「サッカーチームより少ない人数で、何千もの市民の提案を信頼できる政府の政策へと変えるのは容易なことではありません。Claude Code のおかげで、WhatsApp、ボイスメモ、フォームから寄せられたフィードバックを、追跡可能でクラスタリングされたレポートに変換するツールを素早くプロトタイピングし、改良できました。これにより政府は、集約された提案だけでなく、最終的に公共政策を形づくる声そのものを見ることができます。」

Antaraa Vasudev 氏、CEO & Founder、Civis

![Code the Dream](https://assets.claude.com/cdf44f0d096adb8d278ed54f938c9f5973f6361f.png)

> 「Claude は、スタッフの定着率に関するレポートを洗練された理事会向けスライドに仕上げてくれました。ブラッシュアップの過程も協働的で、取り組みがいのあるものでした。理事会から追加の質問が寄せられたときも、約 15 分で明確な回答を用意できました。本来ならはるかに長い時間がかかっていた作業です。」

Lucy Martinez 氏、Chief Operating Officer、Code the Dream

![Colnodo](https://assets.claude.com/c9497a2e12d119b25032fdb7ba7c1b24fc4524ce.png)

> 「Colnodo では、Claude を使って Community-Centered Connectivity Initiatives に関する世界中の情報を集めたプラットフォームを構築し、プロジェクトのモニタリングを改善し、以前よりもはるかに多くのことに取り組めるようになりました。そのすべてを、コロンビアの農村地域にインターネットアクセスを届ける活動と並行して進めています。」

Julián Casasbuenas G. 氏、Director、Colnodo

![Direct Relief](https://assets.claude.com/fd774a72422f993c526a34af3e4853f3d9c85e60.png)

> 「Claude Code は、危機の状況と私たちの対応に関する信頼できる情報を、最新の文書にまとめるのに役立っています。これらの文書は私たちの業務上の意思決定に組み込まれており、ファンドレイジングの大きな成功にも貢献しています。」

Mila Dorji 氏、Public Health Data Scientist、Direct Relief

![Forte](https://assets.claude.com/b871f40d87f637c0cf1e581828cf33f142a9aa1c.png)

> 「寄付者とのやり取りの文面は、まさに私たちらしいものでした。Claude は、同じ提案を 3 度繰り返すのではなく、パートナーシップのより取り組みやすい出発点を提案してくれました。また、スキルを組織の働き方に合わせてカスタマイズできる点も評価しています。これにより、AI は私たちのことを知らないという懸念が解消されます。」

Krystal Brooks 氏、Senior Director, Career Success and Business Development、Forte

![Gates Foundation](https://assets.claude.com/481f9d75a658cd9c1d1aafc6f83f51f3f05cc4fa.png)

> 「私たちは 25 年分の助成実績を 1 つのナレッジグラフにつなぎ、財団の誰もが対話型 AI を使って探索できるようにしました。」

Mike Phipps 氏、Lead AI Engineer、Gates Foundation

![International Justice Mission](https://assets.claude.com/4780933bf29e0c36e3c852676defff9ab2b4cc93.png)

> 「私たちのチームは提案書を自分たちで書いているため、Design Partner Circle を通じて、徹底したレビュアーと、応募するかどうかの判断に対するより良いサポートを求めました。その結果には非常に感銘を受けています。判断は私たちの人間に委ねたまま、提案書の質を高めてくれます。」

Miles Zinn 氏、Director, Grants Portfolio、International Justice Mission

![Montgomery County Food Bank](https://assets.claude.com/07a7c659a67267cb5cdc870284f7b3c7c4bdb6dd.svg)

> 「Claude は、私たちだけでは決して気づかなかった節約の機会を見つけてくれます。あるパートナー機関に対して、小売で購入した場合と私たちを通じて購入した場合の支払額を比較して示したところ、その機関は今では同じ地域の人々に食料を届けるための支出を 40% 削減しています。Claude のおかげで、私たちは 1 ドル 1 ドルをはるかに上手に管理できるようになっています。」

Scott Burns 氏、President & CEO、Montgomery County Food Bank

![Operation Fistula](https://assets.claude.com/533a91130e8c33a3fc524e83a07eb2711bb50984.png)

> 「かつてアナリストが 10 日かけていた作業を、Claude は 30 分でこなしてくれます。女性がケアを受けるために国境を越えなければならない場所など、膨大なデータの山の中から針を見つけ出してくれるのです。こうしたインサイトは満たされていないニーズを明らかにし、質の高い、人生を変えるケアを、それを最も必要とする女性たちのより身近に届ける助けとなっています。」

Helen Davies 氏、COO、Operation Fistula

![Prosper Global](https://assets.claude.com/b90a1ccb5d91763c4639523e90cd6803b58fcafe.png)

> 「私たちはすべてのスキルをテストし、最初のバージョンが米国の小規模な慈善団体を前提としていたことも含め、Anthropic に率直なフィードバックを伝えました。次のバージョンでは、ボゴタでの職種の求人票をコロンビアの事情を踏まえて扱えるようになっていました。私たちの意見がこれほど早く反映されたことは、私たちのようなグローバルな組織にとって大きな意味があります。」

Nayid Orozco 氏、AI Solutions and Delivery Manager、Prosper Global

## **ミッションを守る安全性とセキュリティ**

非営利団体は、支援する人々に関する機密情報を扱っています。管理者は誰がアクセスできるか、組織でどのコネクタを使えるかを管理でき、また私たちはデフォルトでお客様のデータをモデルの学習に使用しません。IT チームは [Anthropic Trust Center](https://trust.anthropic.com/) でセキュリティとコンプライアンスに関するドキュメントを確認できます。また、新しい Claude Academy のチュートリアル [Claude for Nonprofits: Data handling and your AI use policy](https://academy.claude.com/tutorials/claude-for-nonprofits-data-handling-and-your-ai-use-policy) では、Claude がデータをどのように扱うか、そしてシンプルな AI 利用ポリシーをどのように起草・展開するかを管理者向けに解説しています。

## **今後の方向性を一緒に形づくってください**

このプラグインは、今後も非営利団体とともに構築していく一連のリリースの第一弾です。これまで時間を割いてくださったすべての団体に感謝します。チームにとって最も役立つものを[こちら](https://form.typeform.com/to/lm9ayGxo)からお知らせください。また、今後のリリースを私たちとより緊密に形づくっていきたい場合もぜひご連絡ください。

Claude for Nonprofits プラグインは、Team および Enterprise プランの非営利団体に追加費用なしで自動的にインストールされます。まずは、組織が情報をどこに保管しているかのマップを作るよう Claude に頼んでください。他のスキルはそのマップをもとに動作します。スキルの実際の動作を見るには、[Claude Academy](https://academy.claude.com/collections/nonprofits) をご覧ください。

まだ Claude を利用していない非営利団体は、[プランと料金はこちら](https://claude.com/solutions/nonprofits#pricing)からご確認いただけます。

私たちの [Beneficial Deployments](https://www.anthropic.com/beneficial-deployments) チームが非営利団体とどのように連携しているか、さらに詳しくご覧ください。
