---
date: '2026-08-26'
final_url: https://claude.com/blog/claude-in-chrome-generally-available
number: 128
selector_used: main
slug: claude-in-chrome-generally-available
source_url: https://claude.com/blog/claude-in-chrome-generally-available
title: Claude in Chrome is generally available
title_ja: "Claude in Chrome が一般提供を開始しました"
---

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Claude in Chrome が一般提供を開始しました

Claude in Chrome が、すべての有料 Claude プランで一般提供されるようになりました。Claude は、これまでのようにひとつひとつの操作に承認を求めることなく、ブラウザ内で自律的に行動を取れるようになります。各操作を実行する前には安全性分類器がその操作を検証し、安全であることとユーザーの依頼内容に合致していることを確認します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e8c30f077b615a7429ea1_a9d1d161.png)

日々使うツールの多くは[Claude と連携](http://claude.com/connectors)できますが、社内ダッシュボードやレガシーシステム、ベンダーポータルなど、連携できないものも数多くあります。Claude in Chrome を使えば、Claude はこうしたツールにもアクセスできるようになります。今開いているページを見て、テキストの読み取りや入力、リンクのクリック、ページ間の移動、フォームの入力といった操作を、既存のログイン情報を使って行えます。

私たちは昨年、Claude in Chrome をパイロット版として初めて発表しました。それは[プロンプトインジェクション](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)——ウェブサイトやメール、ドキュメントに隠された悪意のある指示によって AI エージェントをユーザーの意図に反して行動させようとする攻撃——への防御を固めながら、機能をテストするためでした。以下で説明するこれらの対策により、Claude in Chrome を広く一般提供することへの確信が持てるようになりました。

## プロンプトインジェクションへの対策

パイロット版発表時に[説明した](https://claude.com/blog/claude-for-chrome)とおり、ブラウザ内で動作する AI エージェントはプロンプトインジェクションに対して脆弱です。そのため、Claude in Chrome をより広く提供する前に、対策の改善に取り組んできました。

プロンプトインジェクション攻撃では、悪意のある行為者がウェブページやメール、フォームフィールドといったウェブコンテンツに指示を隠します。ユーザーがそれを目にすることはないかもしれませんが、こうした指示はエージェントを本来意図しない行動に誘導する可能性があります。例えば、Claude にメールへの返信案を作成させている場合、あるメッセージに隠された指示によって、Claude が他のメールを攻撃者に転送してしまう、といったことが起こり得ます。

パイロット版の発表時には、こうした攻撃に対する Claude の防御力をどのようにテストしたか、また当時講じていた対策について説明しました。その後、[ブラウザ利用時の安全対策](https://www.anthropic.com/research/prompt-injection-defenses)についてさらに詳しく説明する記事も公開しています。それ以降、モデルと[プローブ](https://www.anthropic.com/research/next-generation-constitutional-classifiers)双方の訓練方法を改善し、Claude が Chrome 内でより自律的な行動を安全に取れるようにする新たな分類器群を追加しました。次のセクションでは、これらの対策の有効性を示す評価結果について説明します。

**Claude はより多くの攻撃を認識できるようになりました。** 私たちは、社内の自動攻撃システム、外部のレッドチーム、そして実際の運用中のモニタリングから収集した、増え続けるプロンプトインジェクション攻撃のライブラリを使って Claude を訓練しています。新しい攻撃が現行モデルに対して成功すると、それはライブラリに追加され、将来のモデルの訓練や、運用中の対策にも反映されて、その攻撃を認識できるようになります。2025 年 11 月に[ブラウザ利用時のプロンプトインジェクション対策](https://www.anthropic.com/research/prompt-injection-defenses)について最初に記事を公開して以来、Claude はこうした攻撃に対して大幅に耐性を高めています。

**プローブが、Claude が行動を取る前にウェブコンテンツを審査します。** ウェブコンテンツは、ツールの実行結果を通じて Claude に届きます。ページの読み取りやメールを開くといった操作を行うには、モデルがツール呼び出しを行い、その実行結果を通じてモデルが出力内容(この場合はページやメールの内容)を読み取ります。私たちはプローブを訓練し、これらの実行結果を走査して潜在的なプロンプトインジェクションを検出させています。プローブが攻撃の可能性を検知すると、Claude はそのコンテンツを疑わしいものとして扱うよう警告を受け、必要に応じて行動を取る前にユーザーに確認します。このプローブは Claude Opus 4.5 で初めて導入し、その後カバーする攻撃の種類を拡大してきました。

**行動は実行前に検証されます。** Claude in Chrome では、Claude Code の[オートモード](https://claude.com/blog/auto-mode-default-in-claude-code)と同じ仕組みを使い、Claude が安全と判断した行動を自動的に承認するようになりました(設定で無効にして、引き続き手動で Claude の行動を承認することもできます)。分類器は、新しいウェブサイトへの移動やページへのテキスト入力など、Claude がこれから取ろうとしている行動を確認し、それがユーザーの当初の依頼内容と一致しているかを照合します。一致しない場合、その行動はブロックされます。

## プロンプトインジェクションに対する Claude の堅牢性の測定

こうした対策をテストし、Claude in Chrome がブラウザ内での作業に安全に使えることを確認してきました。ここでは、直近の評価結果を報告します。

[初回の評価](https://claude.com/blog/claude-for-chrome)(Claude in Chrome パイロット版のリリース時に最初に開発されたもの)では、Claude Cowork のプロンプトインジェクション攻撃への耐性をテストし、上記のプローブや分類器なしでも、[Cowork のハーネス](https://claude.com/blog/cowork-chrome-side-panel)内で Claude Fable 5、Claude Opus 5、Claude Sonnet 5 のいずれに対しても攻撃は成功しませんでした。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e8c30f077b615a7429ea7_8477d7f5.png)

*Claude Opus 4.5、Sonnet 5、Opus 5、Fable 5 に対するプロンプトインジェクション攻撃の成功率。Opus 4.5 は拡張思考(extended thinking)を有効にして実行しました。これは、新しいデフォルトである適応的思考(adaptive thinking)に対応していないためです。他のすべてのモデルは、デフォルトの適応的思考をミディアム強度で実行しています。* [*2025 年 11 月のブログ記事*](https://www.anthropic.com/research/prompt-injection-defenses) *で報告した結果は拡張思考を無効にして実行したものですが、Fable 5 では思考を無効化できないため、ここでは思考を有効にした結果を報告しています。11 月に使用した採点モデルも現在は利用できなくなったため、より高性能な採点パイプラインに、成功した攻撃の手動レビューを組み合わせた方式に移行しました。これにより偽陽性が減少しています。*

この評価は飽和状態(成功率 0% という結果がその証拠)に達したため、私たちはこれを廃止することにしました。プロのレッドチームが提供するより強力な攻撃を使用する[現行の評価](https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude%20Opus%205%20System%20Card.pdf#page=76.73)では、モデルに到達した攻撃は、追加の対策なしの状態で Opus 4.5 に対して 17.6%、Opus 5 に対して 3.8% の確率で成功しました。2025 年 11 月時点で利用可能だった最も強力な対策を使用した場合、プローブを実行した状態の Opus 4.5 に対する攻撃の成功率は 16.7% でした。Opus 4.8 以降のすべてのモデルでは、プローブと安全性分類器を実行した状態で、Claude Sonnet 5、Claude Opus 5、Claude Mythos 5 に対する攻撃は一件も成功しませんでした。Fable 5 に対しては 0.3% の攻撃成功率が見られました。成功した突破はすべて低深刻度のシナリオであることを手動で確認しており、これらの緩和にも取り組んでいます。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e8c30f077b615a7429ea4_b8a100e7.png)

*プローブに加えて自動承認の安全性分類器を使用した場合、Claude Sonnet 5 または Opus 5 に対して成功した攻撃はなく、Fable 5 に対しては 0.3% の攻撃が成功しました。Opus 4.5 はモデルの挙動によりモデルに到達する攻撃数が少なくなっていますが、それでも攻撃成功率は最も高くなっています。*

プロンプトインジェクションは今も変化し続ける脅威です。この対策は現在の攻撃に対しては有効ですが、攻撃者の手法の進化に対しても対策を先行させ続ける必要があります。モデルのリリースごとに、攻撃発見、レッドチーミング、そしてより強力な分類器の構築のための、より高度な自動化システムへの投資を続けていきます。

## 始め方

Claude in Chrome を使い始めるには、[Chrome ウェブストア](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)からインストールしてください。Enterprise プランでは、管理者が組織設定でこれを管理し、承認済みのドメインに限定することができます。詳しくは[管理者向けセットアップガイド](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls#h_bdb63199e1)をご覧ください。

パソコン内のファイルや他のアプリケーションを扱う場合は、引き続き Claude デスクトップアプリを使用する必要があります。Claude in Chrome は、他の Chromium ベースのブラウザやモバイルではまだ動作しません。

‍

*¹ すべての攻撃がモデルに到達する——つまりモデルに認識される——わけではありません。場合によっては、Claude が取る行動の結果として、悪意のある指示に一切遭遇しないこともあります。*
