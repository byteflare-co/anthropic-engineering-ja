---
date: '2026-05-13'
final_url: https://claude.com/resources/articles/best-practices-for-computer-and-browser-use-with-claude
number: 179
selector_used: article
slug: best-practices-for-computer-and-browser-use-with-claude
source_url: https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude
title: Best practices for computer and browser use with Claude
title_ja: Claude によるコンピュータ操作・ブラウザ操作のベストプラクティス
---

Claude の[最新モデル](https://www.anthropic.com/news/claude-sonnet-4-6)は、コンピュータ操作（computer use）とブラウザ操作（browser use）の能力において大きな前進を遂げました。これらの機能により、LLM はソフトウェアアプリケーションの構築や、複数の異なるテクノロジーにまたがるワークフローの自動化といった実際の業務を担う、ますます複雑なエージェントシステムを動かせるようになっています。

このブログ記事では、シンプルな設定変更からより高度な統合パターンまで、Claude をコンピュータ操作・ブラウザ操作で活用するためのベストプラクティスを紹介します。Claude のコンピュータ操作・ブラウザ操作の機能を自社プロダクトに統合し始める際に、本記事がお役に立てば幸いです。あわせて、これらのベストプラクティスの一部を取り入れ、Claude のコンピュータ操作機能の上に開発する際に役立つ追加ツールを備えた新しい[デモ実装](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-best-practices)も公開します。

*なお、特に記載がない限り、これらの推奨事項は Claude 4.6 ファミリー（Opus 4.6、Sonnet 4.6、Haiku 4.5）および Claude Opus 4.7 に適用されます。4.6 ファミリーと Opus 4.7 でガイダンスが異なる場合は、本文中でその旨を明記しています。本記事の知見は社内での実験に基づくものであり、新しいモデルや手法の登場に伴って今後更新される可能性があります。*

## **はじめに：解像度とスケーリング**

クリック精度は、あらゆるコンピュータ操作統合の土台です。クリックが本来の位置に当たらなければ、その後の処理はすべて機能しません。フォームは入力されず、ボタンは押されず、ワークフローは失敗します。最もインパクトの大きい最適化は、最もシンプルなものの 1 つでもあります。それは、スクリーンショットを API に送る前にあらかじめ縮小しておくことです。

## **適切なスケーリングを確保する**

Claude の Computer Use API にスクリーンショットを送ると、モデルはそれを見て、指定された display\_width\_px / display\_height\_px の座標空間でクリック座標を返します。ただし、重要な制約があります。API には画像サイズに関する内部処理上の上限があるのです。この上限を超える画像は、モデルが見る前に縮小されます。つまり、ハーネス側は元の解像度に合わせた座標を期待しているのに、モデルは劣化した画像を元にクリック位置を決めていることになります。

Claude 4.6 モデルファミリーの場合、API の上限は次のとおりです。

- **長辺の最大値**: 1568 ピクセル
- **総ピクセル数の最大値**: 1.15 メガピクセル
- **いずれか**の上限を超えた画像は内部で縮小されます

Opus 4.7 モデルはより高い解像度に対応しています。上限は次のとおりです。

- **長辺の最大値**: 2576 ピクセル
- **総ピクセル数の最大値**: 3.75 メガピクセル
- **いずれか**の上限を超えた画像は内部で縮小されます

座標空間とモデルが認識する画像が一致しない場合、モデルが予測したクリック位置は、実際に見ている画像とは異なる表示スケール上に置かれることになります。これが高解像度でクリックが不正確になる主な原因です。解決策は単純で、API に送る前に必ずスクリーンショットをこれらの上限内に収まるよう縮小することです。上限を超えた画像では一貫して大幅な精度低下が見られ、この 1 つの変更は他のほぼどの最適化よりも価値があります。

## **推奨解像度**

**まずは 1280x720 から始めてください。** ほとんどのユースケースにとって、安全かつ実用的なデフォルトです。ピクセル予算の約 80% を使い、長辺と総ピクセル数のどちらの上限にも十分収まり、さらにモデルが学習中に目にしてきた標準的な解像度でもあります。モダンな Web UI にもレガシーなデスクトップアプリケーションにも適しています。

**Opus 4.7 を使用している場合は、1080p から始めることをおすすめします。** 720p と比べて意味のある品質向上が得られ、トークン使用量とパフォーマンスのバランスも良好です。

**モデルが受け取る視覚情報を最大化したい開発者向け**には、「max API fit」アプローチもおすすめします。これは、元画像のネイティブなアスペクト比に基づいて、画像ごとに最適な解像度を計算する方法です。

```
import math

# 1568 for 4.6 family, 2576 for Opus 4.7
MAX_LONG_EDGE = 1568

# 1.15MP for 4.6 family, 3.75MP for Opus 4.7
MAX_PIXELS = 1_150_000

def compute_max_api_fit(native_w, native_h):
    """Compute the largest resolution that fits API limits
    while preserving aspect ratio."""
    aspect = native_w / native_h

    # Compute max dimensions from pixel budget
    h_from_pixels = math.sqrt(MAX_PIXELS / aspect)
    w_from_pixels = h_from_pixels * aspect

    # Apply long edge constraint
    if native_w >= native_h:
        w = min(w_from_pixels, MAX_LONG_EDGE)
        h = w / aspect
    else:
        h = min(h_from_pixels, MAX_LONG_EDGE)
        w = h * aspect

    # Never upscale beyond native
    w = min(w, native_w)
    h = min(h, native_h)

    return int(w), int(h)
```

このアプローチはやや複雑になりますが、アスペクト比の歪みを避けつつ、各画像で利用可能なピクセル予算を最大限に活用できます。固定の 1280x720 と比べた精度向上は控えめですが、16:9 の元画像を 4:3 の表示解像度に無理に合わせたときに生じる歪みを避けられる、素直な実装です。

**避けるべき解像度：**

- **ネイティブ解像度（未縮小）**: 元画像がたまたま上限を下回っている場合を除き、ネイティブ解像度のスクリーンショットを送ることは、クリック精度が低下する最も一般的な原因です。
- **非常に低い解像度（960x540 未満）**: 低解像度の画像では詳細が失われすぎて、モデルが小さな UI 要素を正確に識別できなくなります。
- **MacOS の場合:** ブラウザ操作でよくある問題として、MacOS のスクリーンショットはデバイスピクセル比 2 でキャプチャされることが多く、画面座標の 2 倍の解像度の画像になってしまうことがあります。
- **4.6 ファミリーを使用している場合、1920x1080 以上は避けてください:** これらはピクセル数の上限を超えるため、何の通知もなく縮小されます。Opus 4.7 では上限が高い（3.75 MP）ため、1080p や 1440p は予算内に収まります。ただし、ネイティブの 4K を縮小せずに送ることは引き続き避けてください。

## **座標のスケーリング**

スクリーンショットをリサイズしてから送信した場合、モデルは指定した表示解像度でクリック座標を返します。クリックを実行する前に、これを実際の画面解像度にスケールし直す必要があります。

```
# Your screen is screen_w x screen_h
# You sent a screenshot resized to display_w x display_h
scale_x = screen_w / display_w
scale_y = screen_h / display_h

screen_x = int(api_returned_x * scale_x)
screen_y = int(api_returned_y * scale_y)
```

これは単純ですが非常に重要です。スケーリングを忘れたり、`display_width_px` / `display_height_px` が実際に送信した画像の寸法と一致していなかったりすると、すべてのクリックが一定方向にずれてしまうからです。

## **messages 配列内のコンテンツの順序**

messages の content 配列を構築する際は、以下のコードスニペットのように、テキストの指示を画像の*前に*配置してください。こうすることで、モデルはスクリーンショットを処理する時点で何を探しているかを把握でき、クリック精度が向上します。

```
# RECOMMENDED — text instruction first, then screenshot:
content = [
    {"type": "text", "text": "Click on the Submit button"},
    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": screenshot_b64}},
]

# NOT RECOMMENDED — image first, then text:
content = [
    {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": screenshot_b64}},
    {"type": "text", "text": "Click on the Submit button"},
]
```

## **クリックの問題を診断する**

クリックがターゲットを外している場合、その原因はたいてい以下のいずれかに行き着きます。

| 症状 | 考えられる原因 | 試すこと |
| --- | --- | --- |
| クリックが一貫して一方向にずれる | - display\_width\_px / display\_height\_px が実際に送信した画像の寸法と一致していない - スクリーンショットが API の上限を超えており、何の通知もなく縮小されている - コンテンツの順序がテキスト先ではなく画像先になっている | - 表示寸法をネイティブ解像度ではなく、リサイズ後のスクリーンショットと正確に一致させる - 1280x720 に事前縮小するか、compute\_max\_api\_fit を使う - content 配列内でテキストの指示を画像の前に移動する |
| クリックはおおよそ正しい領域に当たるが、ターゲットを外す | - ターゲットが非常に小さい（チェックボックス、アイコン、トグル） - 元画像が非常に高解像度（4K 以上）で、縮小時に詳細が失われた - ネイティブでないアスペクト比を強制したことによる歪み | - 密度の高い UI では enable\_zoom: True を有効にする - 低い DPI でキャプチャするか、縮小前に画面の該当領域を切り出す - リサイズ時に元のアスペクト比を維持する |
| まったく別の要素をクリックする | - 指示があいまい（Submit 系のボタンが複数あるのに「Submit をクリック」と指示している） - ターゲットの近くに見た目の似た要素がある - 1 つの指示で扱うには UI が複雑すぎる | - 位置情報を含むより具体的なプロンプトを使う（「フォーム右下の青い Submit ボタンをクリック」） - 複雑な操作をより小さなステップに分割する - ページのレイアウトについて追加のコンテキストを提供する |
| 全体的に精度が低い | - スクリーンショットが API の上限を超えたまま送信されている - 元画像が非常に高解像度のディスプレイ（4K 以上）由来で、圧縮率が極端に高い - 解像度が低すぎて重要な詳細が失われている | - すべてのスクリーンショットを上限内に収まるよう事前縮小する - 4.6 ファミリーで 4K 以上の元画像を扱う場合、Sonnet は Opus 4.6 よりも大幅な縮小に強い。Opus 4.7 ではこの差はほぼ解消されるため、4.7 のピクセル予算（最大 3.75 MP）を活用し、そもそも必要な縮小を減らす - ベースラインとして 1280x720 を試し、情報の損失が大きすぎる場合は compute\_max\_api\_fit を使う |

## **クリックタスクのためのモデル選択**

社内テストによると、Claude Sonnet 4.6 はクリックの機械的な精度が高い（空間的な精度が高く、ニアミスが少ない）傾向があり、一方 Claude Opus 4.6 はより強力な推論能力をもたらします。また、元画像を大幅に縮小する必要がある場合も、Sonnet 4.6 のほうが頑健です。

Opus 4.7 はこの差を縮めています。テストの結果、Opus 4.7 のクリック精度は Sonnet 4.6 とほぼ同等であり、さらに高い解像度予算のおかげでそもそも必要な縮小の量が減ることがわかりました。そのため、Opus レベルの推論と高いクリック精度を両立させたい場合に有力な選択肢となります。

ほとんどのタスクでは、クリック精度・推論・コストのバランスが最も優れている Sonnet 4.6 から始めることをおすすめします。より強力な推論が必要な場合、特に高解像度の元画像を使う場合は Opus 4.7 を選んでください。レイテンシを最優先する場合は、Haiku 4.5 が引き続き優れた選択肢です。高度なワークフローでは、推論モデルが計画と意思決定を担い、Sonnet や Haiku が機械的なクリック操作を実行する、オーケストレーター＋サブエージェントのパターンが引き続き有効な場合があります。

## **小さなターゲットへの対処**

ターゲットが小さくなるほど、クリック精度は低下します。大きめ・中程度の UI 要素（ボタン、入力フィールド、標準的なメニュー項目）は、安全な範囲内のどの解像度でも確実にクリックできます。課題となるのは、チェックボックス、システムトレイのアイコン、ドロップダウンの矢印、小さなトグルスイッチ、ツリービューの展開・折りたたみボタンといった、小さなターゲットやごく小さなターゲットです。

アプリケーションで小さなターゲットを頻繁にクリックする場合は、次の戦略を検討してください。

**密度の高い UI ではズームを使う。** Claude 4.6 および 4.7 モデルはズーム機能をサポートしており、モデルはクリックする前に画面の特定領域をより高い解像度で確認できます。[ツール設定](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)で有効にしてください。

```
{
    "type": "computer_20251124",
    "name": "computer",
    "display_width_px": 1280,
    "display_height_px": 720,
    "enable_zoom": True
}
```

**ターゲットを大きくする。** 自動化対象の UI を自分で制御できる場合、クリックターゲットのサイズを（わずかでも）大きくすると、信頼性に不釣り合いなほど大きな効果があります。具体的には、システムの DPI を下げる、ブラウザでズームする、UI のスケーリング設定を調整する、といった方法が考えられます。

**ごく小さなターゲットにはキーボードによる代替手段を使う。** システムトレイのアイコンや小さなチェックボックスのような非常に小さな要素には、クリックよりもキーボードショートカットや Tab キーによるナビゲーションのほうが確実な場合があります。ワークフロー上可能であれば、特定のステップでキーボード操作を使うようモデルにプロンプトで指示すると、成功率が向上することがあります。

**元画像の解像度を考慮する。** 4K 以上のディスプレイのスクリーンショットを 720p に圧縮すると、大量の詳細が失われます（たとえば、3840x2160 のネイティブ解像度で 16px のチェックボックスは、1280x720 の表示解像度ではおよそ 5px になり、ターゲットがはるかに小さくなるため、クリックが難しくなります）。非常に高解像度のディスプレイを扱う場合は、以前のモデルより解像度の上限が高い Opus 4.7 の使用を検討してください。4.6 モデルを使う場合は、低い DPI でキャプチャする、ディスプレイのスケーリングで UI 要素を拡大する、あるいはディスプレイ全体ではなく画面の該当部分に絞ってスクリーンショットを撮る、といった方法を検討してください。これらのモデルはより少ないピクセルでより多くの情報を表現することになるため、元画像のスケールが大きくなる（つまり必要な圧縮が大きくなる）ほどパフォーマンスが低下することが観察されています。

## **試したものの効果がなかったアプローチ**

社内評価で一般的な最適化手法をいくつか試しましたが、以下のアプローチでは一貫した改善は見られませんでした。ただし、結果は具体的な状況によって異なる可能性があります。

- **画像を小さなタイルに分割する**: スクリーンショットを 4 分割や領域ごとに分けて個別に送信しても、クリック精度は向上しませんでした。
- **座標付きのグリッドパターンを重ねる**: モデルがターゲットの位置を特定しやすいよう、スクリーンショットに視覚的な座標グリッドを追加しても、信頼できる改善は得られませんでした。
- **リサイズアルゴリズムの選択**: PIL LANCZOS、sips、その他の一般的なリサイズアルゴリズムでは、まったく同じ結果になりました。自分のスタックで使いやすいものを使ってください。

## **失敗を調査する**

上記の対策を試してもモデルが予測不能な動作をする場合は、トランスクリプト全体をログに記録し、予測されたクリック位置を元のスクリーンショットに重ねて表示することで、モデルが実際に何を見て、何を判断しているのかを把握してください。

失敗の中には、クリック精度とはまったく関係のないものもあります。たとえば、ドロップダウンメニューの中には、ブラウザのビューポートではキャプチャされないシステムレベルの UI を呼び出すものがあります。この場合、モデルはタスクに失敗しているように見えますが、実際には操作すべきメニューが見えていないだけです。このようなケースでは、モデルはクリックではなく、JavaScript の実行、キーボードナビゲーション、あるいはドキュメントオブジェクトモデル（DOM）の直接操作といった代替手段に頼るべきです。

## **クイックリファレンス**

*コンピュータ操作のために画像をスケーリング・準備する方法*

```
import math
from PIL import Image
import base64
import io

# 1568 for 4.6 family, 2576 for Opus 4.7
MAX_LONG_EDGE = 1568

# 1.15MP for 4.6 family, 3.75MP for Opus 4.7
MAX_PIXELS = 1_150_000

def prepare_screenshot(screenshot: Image.Image, native_w: int, native_h: int) -> tuple[str, int, int]:
    """Resize a screenshot to fit API limits and return base64 + display dimensions."""

    # Option A: Fixed 720p (simple, reliable)
    display_w, display_h = 1280, 720

    # Option B: Max API fit (maximizes fidelity)
    # display_w, display_h = compute_max_api_fit(native_w, native_h)

    resized = screenshot.resize((display_w, display_h), Image.LANCZOS)

    buffer = io.BytesIO()
    resized.save(buffer, format="PNG")
    b64 = base64.standard_b64encode(buffer.getvalue()).decode()

    return b64, display_w, display_h

def scale_coordinates(api_x: int, api_y: int, display_w: int, display_h: int,
                      screen_w: int, screen_h: int) -> tuple[int, int]:
    """Scale API-returned coordinates back to native screen space."""
    screen_x = int(api_x * (screen_w / display_w))
    screen_y = int(api_y * (screen_h / display_h))
    return screen_x, screen_y

def compute_max_api_fit(native_w: int, native_h: int) -> tuple[int, int]:
    """Compute the largest resolution that fits API limits while preserving aspect ratio."""
    aspect = native_w / native_h
    h_from_pixels = math.sqrt(MAX_PIXELS / aspect)
    w_from_pixels = h_from_pixels * aspect

    if native_w >= native_h:
        w = min(w_from_pixels, MAX_LONG_EDGE)
        h = w / aspect
    else:
        h = min(h_from_pixels, MAX_LONG_EDGE)
        w = h * aspect

    w = min(w, native_w)
    h = min(h, native_h)
    return int(w), int(h)
```

**使用例：**

```
import anthropic
from PIL import Image

client = anthropic.Anthropic()

# Capture screenshot (your method here)
screenshot = Image.open("screenshot.png")
native_w, native_h = screenshot.size

# Prepare for API
b64, display_w, display_h = prepare_screenshot(screenshot, native_w, native_h)

# Send to Claude — text before image
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "Click on the Submit button"},
            {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}},
        ]
    }],
    tools=[{
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": display_w,
        "display_height_px": display_h,
    }],
)

# Scale coordinates back for execution
api_x, api_y = extract_click_coords(response)  # your parsing logic
screen_x, screen_y = scale_coordinates(api_x, api_y, display_w, display_h, native_w, native_h)
```

## **コンピュータ操作における思考の effort を調整する**

Claude の最新モデルは [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) をサポートしています。これは、行動する前に中間ステップをどの程度推論するかを Claude 自身が決められる設定です。思考トークンの予算を手動で設定する代わりに、adaptive thinking では、Claude が各リクエストの複雑さに応じて、拡張思考をいつ、どの程度使うかを動的に判断します。コンピュータ操作においては、Claude がクリックやキー入力を確定する前に、画面上で見ているものについて考え、複数ステップの操作を計画し、自己修正できることを意味します。

adaptive thinking では、Claude の思考の深さは thinking パラメータの effort レベルで制御します。レベルは low、medium、high、xhigh（Opus 4.7 のみ）、max です。思考を増やすほど 1 アクションあたりの推論は増えますが、出力トークン、レイテンシ、コストも増加します。

当然、次のような疑問が浮かびます。モデルによって、コンピュータ操作に最適な思考量はどれくらいなのでしょうか。

## **Claude Opus 4.7**

デスクトップアプリケーション、ブラウザ、複数アプリケーションにまたがるワークフローを含む、エンドツーエンドの UI 自動化タスク群で、各 effort レベルをテストしました。

![](https://assets.claude.com/a874bc8fe8c7f6fbddf3d96a797b492a419b6c25.png)

**Opus 4.7 は 4.6 ファミリーを上回ります。** OSWorld Verified ベンチマークでは、同等のトークン使用量と effort 設定において、Opus 4.7 が 4.6 ファミリーのすべてのモデルを上回ることがわかりました。low effort の Opus 4.7 は、max の Sonnet 4.6 と同程度のスコアを、タスクあたり約 10 分の 1 のトークンで達成します。難しいタスクには、Opus 4.7 が当然の選択肢です。

**effort を `high` に設定すると**、`max` の約半分の出力トークンで、最高に近いタスク成功率を達成できます。Opus 4.6 と比べると、low、medium、high はいずれもほぼ同じトークン量を使いながら、OSWorld のスコアを向上させています。社内テストでは、max effort はより多くのトークンを使い、最高のスコアを記録しました。以下の表に、各 effort レベルをどのような場合に使うべきかの推奨をまとめます。

### **effort レベルの推奨**

| シナリオ | 思考の effort | 理由 |
| --- | --- | --- |
| ほとんどのユースケースのデフォルト | high | Opus 4.7 は難しいタスクに最適です。high を使えば、トークン使用量を大幅に増やすことなく、複雑な複数ステップの操作を計画するのに十分な推論をモデルに与えられます。 |
| 高スループット／コスト重視 | low | トークン使用量を抑えつつ、Opus 4.6 の high と max の中間の品質を実現します。 |
| シンプルで明確に定義されたワークフロー／最速 | Sonnet 4.6 を試すことを推奨 | 低レイテンシが最優先の場合に使用します。UI が一貫しており、ワークフローが既知の、短く予測可能なタスクには十分です。 |
| 複雑な一発勝負のタスク | max | タスクが非常に難しく、最初の試行で確実に成功させる必要がある場合に使用します。 |

## **Claude 4.6 モデル**

デスクトップアプリケーション、ブラウザ、複数アプリケーションにまたがるワークフローを含む、エンドツーエンドの UI 自動化タスク群で、各 effort レベルをテストしました。

![](https://assets.claude.com/53c9ab8bef7de617c3dd09ee6b27fb293873d3c6.png)

2 つのパターンが際立っています。

**medium effort がスイートスポットです。** effort を medium に設定すると、high の約半分の出力トークンで、最高に近いタスク成功率を達成できます。medium を超えると、パフォーマンスはほぼ頭打ちになります。注目すべきは、タスクをリトライした場合、medium と high が同じ成功率に収束することです。つまり、high effort は難しいタスクを最初の試行で成功させるのには役立つかもしれませんが、複数回の試行が許されるなら、medium でも低コストで同じくらい確実に目的を達成できる可能性があります。

**少しの思考が大きな効果を生みます。** low effort は意外なほど有力な選択肢です。思考を完全に無効にした場合よりも、総出力トークンが実際には*少なく*なります（モデルのミスが減り、リトライのサイクルも少なくて済むため）。そのうえ、精度は思考なしと同等か、わずかに上回ります。そのため、コスト重視で高スループットのワークロードには最適な選択肢です。以下の表に、effort の推奨をまとめます。

### **effort レベルの推奨**

| シナリオ | 思考の effort | 理由 |
| --- | --- | --- |
| ほとんどのユースケースのデフォルト | medium | 精度とコストの比率が最も優れています。考えすぎることなく、複数ステップの操作を計画するのに十分な推論をモデルに与えます。リトライを含めれば、半分のトークンコストで high と同等のパフォーマンスを発揮します。 |
| 高スループット／コスト重視 | low | 思考なしよりも精度が高く、エラーとリトライが減るためトークン使用量も少なくなります。 |
| シンプルで明確に定義されたワークフロー／最速 | 思考を無効化 | 低レイテンシが最優先の場合に使用します。UI が一貫しており、ワークフローが既知の、短く予測可能なタスクには十分です。 |
| 複雑な一発勝負のタスク | high | タスクが難しく、最初の試行で確実に成功させる必要がある場合に使用します。システムがリトライをサポートしているなら、medium でも最終的に同じ成功率を達成できる可能性があります。 |

コンピュータ操作に `max` effort を使うことはおすすめしません。私たちのテストでは、`high` と比べて精度上のメリットがない一方で、出力トークンのコストがさらに増加しました。UI タスクは深い論理よりも主に知覚に関わるものであり、追加の推論予算は使われないか、考えすぎにつながります。なお、このアドバイスはモデルの進化に伴って変わる可能性がある点に留意してください。

## **medium の effort レベルの設定例**

```
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    betas=["computer-use-2025-11-24"],
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},
    messages=[...],
    tools=[
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1280,
            "display_height_px": 720,
        }
    ],
)
```

## **思考を増やしても必ずしも役立たない理由**

UI 自動化タスクは、コーディングや数学の問題とは根本的に異なります。コンピュータ操作のアクションの大半は、深い論理ではなく、正しい要素を見つけて正しい場所をクリックするといった知覚的・機械的なものです。思考が最も役立つのは、モデルが次のことを行う必要がある場合です。

- 開始前に複数ステップの手順を計画する（例：「設定を開き、プライバシーに移動して、トラッキングを無効にする必要がある」）
- 予期しない UI の状態から回復する（例：想定していなかったダイアログが表示された）
- 画面上の情報とタスクの指示を照らし合わせる
- プロフェッショナル向けソフトウェア上で難しいプロジェクトを完遂する

## **安全性の向上：プロンプトインジェクション分類器の活用**

*このセクションでは、プロンプトインジェクション対策について説明します。この保護は、公式のコンピュータ操作ツールヘッダーを使用している場合、デフォルトかつ無料で提供されます。カスタムのコンピュータ操作・ブラウザ操作ツールでこれを有効にしたい場合は、*[*Prompt Injection Classifiers Interest Form*](https://docs.google.com/forms/d/e/1FAIpQLSfXj6rXC-SUQEYHCLabwUe5JuYiYyJ29Ja-KP7EhLIPlyz0tw/viewform?usp=dialog)*にご記入ください。*

コンピュータ操作エージェントは、その設計上、信頼できないコンテンツとやり取りします。Claude が処理するスクリーンショット、Web ページ、アプリケーションの UI のどれもが、敵対的な指示を含んでいる可能性があります。隠しテキスト、改ざんされた画像、欺瞞的な UI 要素、あるいはエージェントの動作を乗っ取ろうとするソーシャルエンジニアリングの試みなどです。この攻撃対象領域は、入力を自分で制御できる一般的な API 統合とは根本的に異なります。コンピュータ操作では、モデルへの入力はオープンなインターネットであり、エージェントが操作しているあらゆるソフトウェアなのです。

コンピュータ操作エージェントがより高性能になり、より広く展開されるにつれて、プロンプトインジェクションはそれに応じてより深刻なリスクになります。クリック、入力、ナビゲーションができるエージェントは、操られてフォームへの入力、ファイルのダウンロード、悪意ある URL への移動といった現実世界のアクションを実行してしまう可能性があります。こうした攻撃に対する堅牢な防御を構築することは、あらゆる本番環境への展開において不可欠です。

## **プロンプトインジェクション防御へのアプローチ**

ブラウザ操作とコンピュータ操作における[プロンプトインジェクション防御へのアプローチ](https://www.anthropic.com/research/prompt-injection-defenses)については、詳しい記事を公開しています。私たちの防御戦略は、複数のレイヤーで機能します。

**学習時の堅牢性。** 強化学習を用いて、プロンプトインジェクションへの耐性を Claude の能力に直接組み込んでいます。学習中、Claude はシミュレートされた Web ページやアプリケーション UI に埋め込まれたインジェクションのコンテンツにさらされ、悪意のある指示を正しく識別して従うことを拒否したときに報酬を得ます。つまり、Claude の第一の防御線はモデル自体であり、正当なユーザーの指示と、タスク実行中に遭遇する敵対的なコンテンツを区別することを学習しているのです。

**リアルタイム分類器。** Claude のコンテキストウィンドウに入ってくるコンテンツをスキャンし、プロンプトインジェクションの可能性がある試みにフラグを立てるプローブを実行しています。これらのプローブは、ページコンテンツに隠されたテキスト、画像に埋め込まれた指示、エージェントを騙すよう設計された欺瞞的な UI 要素など、複数のモダリティにわたる敵対的なコマンドを検出し、攻撃を特定した場合には Claude の動作を調整します。

**継続的なレッドチーミング。** 当社のセキュリティ研究者はこれらの防御を継続的に検証しており、進化する攻撃手法に対する堅牢性をベンチマークするために、外部の敵対的評価にも参加しています。

最初のコンピュータ操作のリサーチプレビュー以来、私たちはこれら 3 つのレイヤーすべてに多大な投資を続けてきました。新しい世代のモデルごとに、より強力な学習時の防御とより高性能な分類器が組み込まれており、レッドチームが評価する攻撃手法の範囲も拡大しています。

## **Claude の組み込み分類器を使う**

API 経由で Claude の[公式コンピュータ操作ツール](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)を使用すると、すべてのリクエストでプロンプトインジェクション分類器が自動的に実行されます。これらの分類器はメインのモデル推論と並行して動作するため、リクエストに追加されるレイテンシはほぼゼロで、追加コストもかかりません。

この保護を有効にするために設定する必要があるものは何もありません。公式の `computer_20251124` ツールタイプを使用していれば、デフォルトで有効になっています。分類器はスクリーンショットやその他のコンテンツにプロンプトインジェクションの兆候がないかを評価し、それに応じて Claude の応答に影響を与えます。

```
# Classifiers run automatically when using the official CU tool — no extra config needed
tools = [
    {
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": 1280,
        "display_height_px": 720,
    }
]
```

## **公式のコンピュータ操作ツールを使っていない場合**

多くの開発者は、公式の `computer_20251124` ツールタイプではなく、独自のスクリーンショットツールやクリックツールを定義するなど、カスタムのツール定義を使ってコンピュータ操作の統合を構築しています。これに当てはまる場合、上記の組み込み分類器は現時点ではリクエストに対して実行されません。

私たちは、こうしたカスタム実装にもプロンプトインジェクション対策を拡張する方法を積極的に検討しています。公式のツールタイプを使わずにコンピュータ操作・ブラウザ操作の統合を構築していて、プロンプトインジェクション分類器に関心がある場合は、[こちらの関心登録フォーム](https://docs.google.com/forms/d/e/1FAIpQLSfXj6rXC-SUQEYHCLabwUe5JuYiYyJ29Ja-KP7EhLIPlyz0tw/viewform?usp=dialog)にご記入ください。この機能が利用可能になり次第、ご連絡します。

## **分類器の使用有無にかかわらず実践すべきこと**

分類器は防御の 1 つのレイヤーであり、完全な解決策ではありません。あらゆるコンピュータ操作の展開において、次のプラクティスをおすすめします。

**重要度の高いアクションには human-in-the-loop を導入する。** フォームの送信、購入、メッセージの送信、データの変更といった取り消しのきかないアクションを実行する前に、エージェントが一時停止してユーザーに確認を求めるようにします。分類器の性能にかかわらず、これがプロンプトインジェクションに対する最も効果的な緩和策です。

**エージェントの権限を絞る。** エージェントができることを制限します。ワークフローでファイルのダウンロードが必要なければ、エージェントにダウンロードの権限を与えないでください。メールを送信する必要がなければ、メールクライアントへのアクセスを与えないでください。インジェクションが成功した場合の被害範囲を小さくすることは、インジェクション自体を防ぐことと同じくらい重要です。

**エージェントのアクションを監視・記録する。** 各ステップのスクリーンショットを含め、エージェントが実行したアクションの一連の流れをすべてログに記録します。これにより、異常な動作を検出し、問題が起きたときに何が起きたかを監査し、システムの堅牢性を継続的に改善するためのフィードバックループを構築できます。

**すべての Web コンテンツを信頼できないものとして扱う。** ユーザーの指示と、タスク実行中に遭遇したコンテンツを明確に区別するよう、エージェントのシステムプロンプトを設計します。Web ページ、メール、アプリケーション UI 内で見つかったテキストはユーザーからのものではなく、指示として扱うべきではないことをモデルに念押ししてください。

## **コンピュータ操作のためのコンテキスト管理**

コンピュータ操作エージェントを構築していると、スクリーンショットはあっという間に蓄積します。アクションのたびに新しい画像が生成され、各画像は解像度に応じておよそ 1,000〜1,800 トークンを消費します。システムプロンプト、ツール定義、テキストコンテンツを考慮すると、200k のコンテキストウィンドウは 100 枚よりもかなり少ないスクリーンショットで埋まってしまいます。

このコンテキストをうまく管理することには、1) 総トークン数を一定範囲に抑えること、2) 同じプレフィックスに何度も満額を支払わずに済むよう、プロンプトキャッシュを有効に保つこと、という 2 つの目標があります。効果的な[コンテキスト管理](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)は、長時間動作するエージェントのコストとレイテンシに対して、他のほぼどの最適化よりも大きな影響を与えることがわかっています。このセクションでは、きれいに組み合わせられる 3 つのレイヤーを紹介します。キャッシュブレークポイントの配置、キャッシュを壊さずに古いスクリーンショットを削除する方法、そして削除だけでは足りない場合の履歴の要約です。

## **キャッシュブレークポイントを配置する**

プロンプトキャッシュが役立つのは、ブレークポイントがターンをまたいで繰り返し現れるコンテンツに置かれている場合だけです。API がサポートするキャッシュブレークポイントは合計 4 つです。4 つすべてを安定したプレフィックス（システムプロンプト、ツール定義）に置くのは無駄です。そのプレフィックスは一度ヒットすれば無効化されることはないため、ブレークポイントは 1 つで十分です。残りの 3 つは、無効化のリスクが最も高く、長いセッションで節約効果が積み重なる直近の履歴に使うほうが効果的です。

次の配置をおすすめします。

- **システムプロンプトまたは末尾のツール定義に 1 つのブレークポイント。** このプレフィックスはセッション内でほとんど変化しません。
- **直近のツール結果に最大 3 つの追加ブレークポイント。** ターンごとに位置を進め、4 つという上限を超えないよう、前回のブレークポイントはクリアします。

ブレークポイントを直近の複数の位置に分散させることで、段階的な劣化（graceful degradation）が可能になります。画像の削除、コンパクション、ツール定義の変更などによって最新のブレークポイントが無効化されても、それより前のブレークポイントがヒットする可能性があり、入力コストを全額の 100% ではなく 10% に抑え続けられます。

*キャッシュ制御とブレークポイント設定の例：*

```
def set_trailing_cache_control(messages, max_breakpoints=3):
    """Place up to `max_breakpoints` ephemeral cache_control markers on the
    most recent tool_result blocks, after clearing any existing markers."""
    for msg in messages:
        for block in msg.get("content", []):
            if isinstance(block, dict):
                block.pop("cache_control", None)

    placed = 0
    for msg in reversed(messages):
        for block in reversed(msg.get("content", [])):
            if placed >= max_breakpoints:
                return
            if isinstance(block, dict) and block.get("type") == "tool_result":
                block["cache_control"] = {"type": "ephemeral"}
                placed += 1
```

## **アプローチ 1：ローリングバッファ（キャッシュを意識した方式）**

トークン数を一定範囲に抑える最もシンプルな方法は、直近 N 枚のスクリーンショットだけを残し、それ以外を削除することです。各 API 呼び出しの前に message 配列を走査し、古い画像ブロックを短いプレースホルダー（たとえば「[Image omitted]」というテキストブロック）に置き換えます。

このパターンの素朴な実装は、スクリーンショットが古くなるたびに 1 枚ずつ削除するというものですが、これではターンごとにプレフィックスが変わり、プロンプトキャッシュが絶えず無効化されてしまいます。ローリングバッファがキャッシュを壊すという評判が立ったのはこのためです。解決策は、まとめて削除することです。そうすれば、プレフィックスは数ターンの間バイト単位で同一のまま保たれ、一度無効化された後、再び安定します。

私たちがテストした具体的なパターンは次のとおりです。

1. 直近 keep\_n 枚のスクリーンショットをフル解像度で保持する。
2. スクリーンショットの総数が keep\_n + interval を超えたら、最も古い interval 枚を一度にまとめてプレースホルダーに置き換える。
3. 削除のタイミングとタイミングの間は message 配列がターン間でバイト単位で同一になるため、キャッシュブレークポイントはヒットし続ける。

最初のデフォルト値としては、keep\_n = 3、interval = 25 が妥当です。これらは調整可能です。interval を大きくすると削除の回数が減る（キャッシュ効率が上がる）一方で、コンテキスト内に残るフル解像度のスクリーンショットが増えます（トークンが増える）。代表的な軌跡でキャッシュヒット率と総入力トークン数を測定し、調整してください。

*キャッシュブレークポイントを維持しながら過去のスクリーンショットを削除する例：*

```
def prune_old_screenshots(messages, keep_n=3, interval=25):
    """Replace older screenshots with text placeholders in batches.
    Only prunes when the total count exceeds keep_n + interval, so the
    message prefix stays byte-stable for `interval` turns between prunes."""
    image_positions = [
        (msg_idx, block_idx)
        for msg_idx, msg in enumerate(messages)
        for block_idx, block in enumerate(msg.get("content", []))
        if isinstance(block, dict) and block.get("type") == "image"
    ]
    if len(image_positions) <= keep_n + interval:
        return messages

    to_prune = image_positions[:-keep_n][-interval:]
    for msg_idx, block_idx in to_prune:
        messages[msg_idx]["content"][block_idx] = {
            "type": "text",
            "text": "[Image omitted]",
        }
    return messages
```

それでもローリングバッファには 1 つ本質的な制約があります。バッファの外にあるものはすべて失われるということです。元の指示、エージェントがすでに試したこと、タスクのどこまで進んでいるかといった情報は、削除されたスクリーンショットとともにすべて消えてしまいます。短いタスク（約 50 アクション未満）ならそれで問題ありません。それより長いタスクでは、コンパクションと組み合わせてください。

## **アプローチ 2：LLM ベースのコンパクション**

古い画像を黙って削除する代わりに、会話全体を要約してから破棄します。要約には、何が起きたか、ユーザーが何を求めたか、何が完了したか、どこから再開すべきかが保存されます。エージェントが現在見ているものを把握できるよう、直近のスクリーンショットも数枚あわせて保持します。

コンパクションとキャッシュを意識したローリングバッファは補完的な関係にあります。ターンごとのトークン増加を抑えるにはローリングバッファを使い、それより前のコンテキストを失わずにウィンドウの残りを取り戻すには、ときどきコンパクションを使います。コンパクションは設計上、毎回キャッシュの無効化を伴うため、数ターンごとではなく、まれにしか起きないようにするのが望ましいでしょう。

### **要約用プロンプト**

以下のプロンプト例は、各セクションが特定の失敗パターンに対処するよう構成された雛形です。以下の例に示すように、プロンプトは、エージェントが元の会話を読み直さずにタスクを継続するために必要なすべての情報を捉える必要があります。

```
COMPACT_PROMPT = """Your task is to create a detailed summary of this conversation that
will REPLACE the conversation history. The agent will continue working with only this
summary and a few recent screenshots as context.

CRITICAL: Preserve ALL user instructions verbatim. User instructions are the most
critical element. If they are lost, the agent will deviate from the task.

Before providing your summary, analyze the conversation in  tags:
1. Extract every user instruction, requirement, and constraint
2. Identify if this is a repeatable workflow (e.g., processing N items)
3. Chronologically trace what actions were taken and what happened

Your summary MUST include these sections:

1. USER INSTRUCTIONS:
   - Complete initial task definition (verbatim when possible)
   - ALL specific requirements and criteria
   - Every "DO NOT", "ALWAYS", "MUST" instruction
   - Any corrections or feedback that changed the approach

2. TASK TEMPLATE (if this is a repeatable workflow):
   - The pattern being repeated
   - Decision criteria for each iteration
   - Standard workflow steps
   - Example of one completed iteration

3. CONSTRAINTS AND RULES:
   - All user-specified rules and restrictions
   - Edge cases and exceptions discovered

4. ACTIONS TAKEN:
   - Pages visited and elements interacted with
   - Forms filled and buttons clicked

5. ERRORS AND FIXES:
   - What went wrong and how it was resolved
   - Approaches that failed (so they aren't retried)

6. PROGRESS TRACKING:
   - Items completed vs. remaining
   - Current position in the workflow

7. CURRENT STATE:
   - Current application, URL and domain (optional)
   - Important page state (logged in, form progress, etc.)

8. NEXT STEP:
   - Exactly what should be done next to continue
"""
```

上のプロンプトにおいて、**User Instructions** はタスクの逸脱を防ぎます。これがないと、エージェントはコンパクション後にタスクから外れてしまいます。**Task Template** は繰り返しのパターンを捉えるため、エージェントはコンパクション後もワークフローを一から導き直すことなく反復を続けられます。**Constraints and Rules** は、タスク開始前に設定された、あるいはタスク中に発見された制約やエッジケースを保存するため、エージェントは守るべきと知っていた既存のルールに違反せずに済みます。**Actions Taken** は過去の進捗を追跡するのに役立ちます。**Errors and Fixes** は失敗したアプローチの再試行を防ぎます（「Submit のクリックはすでに試した。利用規約のチェックボックスにチェックを入れるまで機能しない」）。**Progress Tracking** は最初からのやり直しや項目の飛ばしを防ぎます。**Current State** と **Next Step** は、再開のための明確な入口を提供します。

### **サーバーサイドのコンパクション（ベータ）**

このプロンプトを使う最もシンプルな方法は、[サーバーサイドのコンパクション](https://docs.anthropic.com/en/docs/build-with-claude/compaction)（ベータ）を使って API にコンパクションを任せることです。独自の要約用プロンプトを `context_management` の `instructions` パラメータとして渡すと、入力トークンがトリガーのしきい値を超えたときに API が自動的に要約します。`instructions` パラメータはデフォルトの要約用プロンプトを完全に置き換えるため、モデルは上記のセクションに従います。`pause_after_compaction` を設定すると、コンパクションをまたいで直近のメッセージ（スクリーンショットを含む）を付加できます。

*自動コンパクションの使用例：*

```
# Minimal — turn on autocompaction with API defaults
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["compact-2026-01-12", "computer-use-2025-11-24"],
    context_management={"edits": [{"type": "compact_20260112"}]},
    messages=[...],
    tools=[...],
)

# Customized — set your own trigger threshold and summarization prompt
response = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    betas=["compact-2026-01-12", "computer-use-2025-11-24"],
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": 150_000},
                "instructions": COMPACT_PROMPT,
            }
        ]
    },
    messages=[...],
    tools=[...],
)
```

### **サーバーに合わせてクライアント側でも切り詰める**

API がサーバーサイドのコンパクションを実行すると、サーバー側ではコンパクション前のコンテンツが置き換えられますが、ローカルの messages 配列には履歴全体が残ったままです。以降のターンでも履歴全体を送り続けると、サーバーがもう必要としていないトークンに対して料金を支払うことになります。さらに、ローリングバッファの削除処理がサーバーの実際に見ているものとは異なるメッセージ範囲に対して動作することになり、先ほど慎重に維持したキャッシュの安定したプレフィックスが壊れる可能性があります。

解決策は、以下のコードスニペットのように、サーバーでの切り詰めをクライアント側でも再現することです。レスポンスがコンパクションの発生を報告したら、次のターンの前に、ローカルの messages 配列からコンパクションのマーカーより前をすべて削除します。こうすることで、クライアントとサーバーの見ている内容が一致し、ローリングバッファも正しく機能し続けます。

```
def truncate_to_last_compaction(messages, response):
    """If the server compacted on this turn, drop pre-compaction messages
    locally so the next turn's cache prefix matches what the server sees."""
    context_mgmt = getattr(response, "context_management", None)
    if not context_mgmt or not context_mgmt.get("applied_edits"):
        return messages

    compaction = next(
        (e for e in context_mgmt["applied_edits"] if e["type"] == "compact"),
        None,
    )
    if compaction is None:
        return messages

    keep_from = compaction["message_index_after_compaction"]
    return messages[keep_from:]
```

## **クライアントサイドのコンパクション**

サーバーサイドのコンパクションをサポートしていないモデルを使っている場合や、完全に制御したい場合は、同じプロンプトを使ってクライアント側でコンパクションを実装します。各 API 呼び出しの後、レスポンスの usage フィールドから総入力トークン数を確認します。それがしきい値（例：コンテキストウィンドウの 90%）を超えたら、COMPACT\_PROMPT をシステムプロンプトとして、会話を要約用モデルに送ります。メッセージ履歴を要約と直近の数枚のスクリーンショットで置き換え、エージェントループを続行します。

## **まとめ**

長時間動作するコンピュータ操作エージェントの良いデフォルト構成は、次のようになります。

- 安定したプレフィックスに 1 つ、末尾のツール結果に 3 つのキャッシュブレークポイントを置き、ターンごとにクリアして再配置する。
- keep\_n = 3、interval = 25 のキャッシュを意識したローリングバッファで、古いスクリーンショットをまとめてプレースホルダーに置き換える。
- 約 150k 入力トークンでトリガーされる、カスタムプロンプトを使ったサーバーサイドのコンパクションに加え、両者の見ている内容を一致させるためのクライアント側の切り詰め処理。

これら 3 つのレイヤーを導入すれば、典型的な長期にわたるコンピュータ操作セッションでは、大多数のターンでプロンプトキャッシュがヒットし、総入力トークン数はコンテキストウィンドウを大きく下回る範囲に抑えられ、コンパクションをまたいでもエージェントがタスクを見失わないだけの履歴が保持されます。

## **コンピュータ操作・ブラウザ操作を改善するための実験的な設定**

以下のパターンは、私たちが実装の中でテストしている手法で、有望ではあるものの、まだ一律に推奨できる段階ではありません。いずれも、特定の種類のワークロードで改善が見込める代わりに、複雑さやコストとのトレードオフがあります。ご自身のワークフローで試せるようここに紹介しますが、このセクションのガイダンスは今後急速に変わる可能性があります。

## **バッチツール**

更新されたリファレンス実装では、標準のコンピュータツールとブラウザツールに加えて、`computer_batch` と `browser_batch` という 2 つのツールを公開しています。それぞれサブアクションのリストを受け取り、1 回のツール呼び出しでまとめて実行します。たとえば、クリック、入力、キー押下をそれぞれ別のターンで行う代わりに、モデルはこの 3 つのアクションをすべて含む 1 回の computer\_batch 呼び出しを出力できます。

魅力は効率性です。N 個の機械的なアクションを含むワークフローが、N 回ではなく 1 回のラウンドトリップで済むため、長期にわたるタスクでは実時間と出力トークンの消費を大幅に削減できます。リスクは誤差の累積です。アクション 2 がアクション 1 によって変化した画面の状態に依存しているのにアクション 1 が失敗した場合、バッチの残りは古い前提に基づいて動作し、エージェントは実際の状態のスクリーンショットを一度も見ないまま逸脱していく可能性があります。

バッチツールは、サブアクションが自己完結しており、互いの視覚的な結果に依存しない場合（フォームの複数のフィールドへの入力、キーボードショートカットの連続実行、スクロールして既知のターゲットをクリックするなど）におすすめします。探索的なナビゲーション、エラーからの回復手順、あるいは「アクション 1 が失敗したら計画を立て直す必要がある」という状況が実際に起こりうるワークフローでは避けたほうがよいでしょう。

バッチツールは独自のカスタム定義であるため、標準のコンピュータツールやブラウザツールときれいに併用できます。両方を利用可能にしておき、モデルに選ばせてください。

## **advisor ツール（ベータ）**

[advisor ツール](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)は、実行役（executor）のモデルと、より高い知能を持つ助言役（advisor）のモデルを組み合わせるもので、executor は生成の途中で advisor に戦略的な指針を相談できます。executor がループを実行し、より深い推論が必要な場面に出くわすと advisor を呼び出し、計画や軌道修正を受け取って処理を続けます。これは 1 回のリクエストの中でサーバー側で行われるため、利用者側で追加のラウンドトリップは発生しません。

特にコンピュータ操作においては、このパターンは、ほとんどのターンが機械的なクリック操作である一方で、ときどき計画が必要な場面（どのタブを開くかの選択、予期しないモーダルからの回復、ある戦略を断念するかどうかの判断など）で Opus レベルの推論が役立つような、長期にわたるタスクで最も有用です。トークン生成の大部分は executor の料金で行われながら、advisor 単体に近い品質が得られます。

*advisor ツールを有効にする例：*

```
response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    betas=["advisor-tool-2026-03-01", "computer-use-2025-11-24"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-7",
        },
        {
            "type": "computer_20251124",
            "name": "computer",
            "display_width_px": 1280,
            "display_height_px": 720,
        },
    ],
    messages=[...],
)
```

advisor ツールで役立つ制御には、次のものがあります。

- **`max_uses`:** リクエストあたりの advisor 呼び出し回数の上限を設定します。最悪の場合のコストを抑えたいときに役立ちます。
- **ハーネス側での会話全体の上限:** advisor は相談のたびに Opus 4.7 の料金で課金されるため、非常に長いセッションでは、一定回数使った後は advisor の提供を停止したほうがよい場合があります。
- **advisor 側のキャッシュ:** 複数回の呼び出しを含む会話では、advisor のプレフィックスをキャッシュすると、およそ 3 回の相談で元が取れます。リファレンス実装では、デフォルトで 5 分間のエフェメラルキャッシュを使用しています。

知っておくべき、わかりにくい点が 2 つあります。advisor はツールなし・コンテキスト管理なしで動作するため、利用者の代わりにクリックやブラウジングを行うことはできず、テキストによる助言を返すだけです。また、executor モデルは長期にわたるタスクでは advisor の存在を必ずしも覚えていないため、後述のリマインダーによる促しのセクションを参照してください。

## **孤立した advisor ブロックのクリーンアップ**

advisor ツールが呼び出されると、executor は返されるコンテンツの中に name: "advisor" の `server_tool_use` ブロックと、それに続く `advisor_tool_result` ブロックを出力します。これらのブロックは、他のすべてのものと一緒に messages 配列に残ります。

その後、会話全体の上限に達した、設定を変更した、モデルを切り替えたなどの理由で tools 配列から advisor ツールを外すと、以前の `server_tool_use` / `advisor_tool_result` ブロックは孤立した状態になります。参照されているツールがもう宣言されていないため、API は次のリクエストで 400 を返します。

解決策はシンプルな送信前の処理です。あるターンで advisor を無効にする場合は、メッセージ履歴を走査し、`server_tool_use` タイプ（name == "advisor"）と `advisor_tool_result` タイプのコンテンツブロックをすべて取り除きます。

*古い advisor ブロックを削除する例：*

```
def strip_orphaned_advisor_blocks(messages):
    """Remove advisor server_tool_use / tool_result blocks from history.
    Call this before any request that doesn't include the advisor tool."""
    for msg in messages:
        content = msg.get("content")
        if not isinstance(content, list):
            continue
        msg["content"] = [
            block for block in content
            if not (
                isinstance(block, dict)
                and (
                    (block.get("type") == "server_tool_use"
                     and block.get("name") == "advisor")
                    or block.get("type") == "advisor_tool_result"
                )
            )
        ]
    return messages
```

## **定期的なリマインダーによる促し**

長いセッションでは、executor モデルがどのツールが利用可能か、どのツールを優先すべきかを忘れてしまうことがあります。私たちのテストでは、2 つの短いリマインダーのパターンが効果を上げています。

**バッチのリマインダー。** 標準ツールと並べて `computer_batch` や `browser_batch` を公開しているのに、バッチが適切な場面でモデルが単一アクションの呼び出しを連続させているのを確認した場合は、次のツール結果の後に、短いシステムレベルの促しを追加します。「Remember you can use `computer_batch` to combine sequential actions in a single tool call when they don't depend on intermediate screenshots.（途中のスクリーンショットに依存しない連続したアクションは、`computer_batch` を使って 1 回のツール呼び出しにまとめられることを思い出してください）」。狙いは、いつバッチを使うかを厳密に指示することなく、モデルをバッチ処理の方向へ引き戻すことです。

**advisor のリマインダー。** advisor ツールは、特に長いターン数にわたって呼び出されていない場合、executor がその存在を忘れやすいツールです。advisor の呼び出しがないまま約 20 ターンを超えたセッションでは、計画や軌道修正が必要な場面で advisor を利用できることを伝える短いリマインダーを追加します。リファレンス実装では、20 ターンごとに 1 行のヒントを追加しています。

どちらの促しも、システムプロンプトの書き換えではなく、軽いコンテキストの注入です。追加 1 回あたりのコストは数十入力トークン程度です。システムプロンプトがすでに長い場合や、キャッシュブレークポイントを精密に配置している場合は、得られる改善が無効化リスクの増加に見合うかどうかを検討してください。

## **リファレンス実装に含まれるデバッグ用の仕組み**

何かがおかしく、問題がハーネスなのか、スクリーンショットなのか、モデルなのかがわからないときは、ログを追加し始める前に、リファレンス実装に含まれる 3 つの補助ユーティリティを使ってみる価値があります。

- **軌跡ビューア（streamlit run viewer/app.py）。** 記録された軌跡を読み込み、各ステップのスクリーンショット、思考、ツール呼び出し、使用量とともにエージェントのターンを 1 つずつ確認できます。実行が失敗した後に「モデルは実際に何を見て、何を判断したのか」を明らかにするのに最適です。
- **ツールデバッグパネル（uvicorn debug.server:app --reload）。** スクリーンショットの取得、クリック座標の取得、入力、スクロール、ズームなど、各ツールを個別に試せる小さな Web UI です。キャプチャのパイプラインと座標のスケーリングが期待どおりの結果を生んでいるかを確認するのに役立ちます。
- **位置特定プレイグラウンド（uvicorn localize.server:app --reload --port 8001）。** 任意の画像をアップロードし、モデルにターゲットを指し示すよう依頼できます。予測された座標を、表示解像度とネイティブ解像度の両方で画像上に描画します。クリックのミスがリサイズのバグなのか、座標スケーリングのバグなのか、本当にモデルの誤りなのかを診断する最速の方法です。顧客からクリックの不具合が報告され、その失敗を切り離して再現したい場合に特に役立ちます。

これらはいずれも、動作する統合を構築するために必須のものではありません。デフォルトのフィードバックループ（ログを取り、再実行し、トランスクリプトを目を凝らして読む）では十分に速くないときのためのデバッグ補助ツールです。

## **信頼性の向上：Claude に教える**

Claude がワークフローを正しくこなせるようになるまでテキストのプロンプトを繰り返し調整する代わりに、正しい振る舞いを直接見せることができます。タスクを実行する自分自身を記録し、各ステップでスクリーンショット、アクション、そして必要に応じて音声ナレーションをキャプチャします。そして、Claude が同じワークフローを実行するときに、その実演をコンテキストとして再生します。記録は Claude が従うことのできる再利用可能な仕様となり、Claude はライブの UI の状態との違いに適応しながらそれに従います。

私たちはこのパターンを Claude in Chrome の内部で使用しており（そこでは「Teach Mode」と呼んでいます）、その根底にあるアプローチはコンピュータ操作やブラウザ操作のプロダクトを構築するあらゆる人にとって広く役立つため、ここで共有します。このパターンには 2 つの利点があります。Claude がおおむね処理できるものの、ときどき間違えるワークフローの信頼性を向上させること、そしてテキストのプロンプトだけでは Claude が完了できないまったく新しいワークフローを可能にすることです。核となるアイデア（実演をキャプチャし、それをコンテキストとして渡す）は実装が簡単で、ブラウザ環境とデスクトップ環境のどちらにもうまく適応します。

### **核となるコンセプト：言葉で説明せず、やって見せる**

従来のプロンプトエンジニアリングでは、ユーザーに望むことを言葉で説明してもらい、AI が誤解したら繰り返し修正します。このパターンはそれを逆転させます。ユーザーがタスクを実演し、その間にシステムがユーザーのアクション、スクリーンショット、そして（必要に応じて）音声ナレーションを記録します。再生時には、Claude は実演の全体をコンテキストとして受け取り、現在の UI の状態との違いに適応しながら、同じ手順に従います。

重要な洞察は、再生が厳密なリプレイではないという点です。Claude は実演をガイドとして使いながら、ライブの環境について推論します。ボタンの位置が変わっていたり、メニューが再編成されていたりしても、Claude は記録された座標を盲目的にクリックするのではなく、現在の UI の中で対応する要素を見つけられます。

### **データモデル**

基本単位は「ワークフローステップ」、つまり記録中にキャプチャされた 1 つのアクションです。各ステップには、何が行われたか、どこで起きたか、画面がどう見えていたかがまとめられています。

```
from dataclasses import dataclass, field
from typing import Literal, Optional

@dataclass
class WorkflowStep:
    action: Literal["click", "type", "navigate", "scroll", "select"]
    description: str                         # Human-readable, e.g. "Click the Submit button"
    timestamp: float
    selector: Optional[str] = None           # CSS selector or XPath
    coordinates: Optional[dict] = None       # {"x": int, "y": int}
    url: Optional[str] = None
    screenshot: Optional[str] = None         # Base64-encoded screenshot
    viewport_dimensions: Optional[dict] = None  # {"width": int, "height": int}
    speech_transcript: Optional[str] = None  # Voice narration, if captured
    value: Optional[str] = None              # For type actions

@dataclass
class SavedWorkflow:
    id: str
    name: str                                # e.g. "Submit expense report"
    steps: list[WorkflowStep] = field(default_factory=list)
    description: Optional[str] = None        # AI-generated summary of the workflow
    start_url: Optional[str] = None
    created_at: float = 0.0
    usage_count: int = 0
```

セレクタと座標の両方をキャプチャしているのは意図的です。セレクタはレイアウトの変更に強い一方、座標はセレクタが壊れたときに Claude が使える視覚的なフォールバックとなります。ビューポートの寸法を保存しておくのは、再生環境が記録環境と異なる場合に座標をスケーリングできるようにするためです。

### **記録：何をキャプチャするか**

最低限、クリックイベント、キーボード入力、ナビゲーションの変化、そして各アクション時のスクリーンショットをキャプチャします。各クリックについて、人間が読める説明を（aria-label、テキストコンテンツ、あるいは Claude への簡単な呼び出しによって）生成し、クリック位置に視覚的なマーカーを付けてスクリーンショットに注釈を加えます。

```
def on_click(event):
    step = WorkflowStep(
        action="click",
        selector=generate_selector(event.target),
        coordinates={"x": event.client_x, "y": event.client_y},
        url=current_url(),
        description=generate_description(event.target),
        timestamp=now(),
        viewport_dimensions=get_viewport_size(),
    )
    # Annotate screenshot with a circle at the click position
    screenshot = capture_screenshot()
    step.screenshot = annotate_with_circle(screenshot, event.client_x, event.client_y)
    workflow_steps.append(step)
```

注釈（クリック位置に描かれた色付きの円）には 2 つの目的があります。ユーザーが記録で正しい要素がキャプチャされたことを確認しやすくすること、そして再生時に Claude にアクションが行われた正確な場所を示すことです。再生用のプロンプトでは、これらのマーカーが記録時の産物であり、ライブの UI の一部ではないことを明確にしておく必要があります。

### **再生：プロンプトの構築**

ここが最も重要な部分です。ユーザーが保存済みのワークフローを起動したら、Claude へのメッセージを構築します。メッセージには、ユーザーの意図、実演の形式を説明するコンテキストブロック、そして記録されたスクリーンショットの 3 つを含めます。

コンテキストブロックは、注釈付きのスクリーンショットをどう解釈するか、そしてライブの UI が異なる場合にどう適応するかを Claude に伝えます。

```
def generate_playback_context(steps: list[WorkflowStep]) -> str:
    steps_description = "\n".join(
        f"Step {i+1}: {step.description}"
        for i, step in enumerate(steps)
    )

    return f"""<demonstration_context>
The user has recorded a demonstration showing how to perform this task.

RECORDED STEPS:
{steps_description}

ABOUT THE SCREENSHOTS:
- Each screenshot shows the screen state when an action was taken
- BLUE CIRCLES mark where the user clicked — these are recording annotations
- The blue highlighting is NOT part of the actual interface
- Your own screenshots will NOT have these markers

HOW TO USE THIS DEMONSTRATION:
1. Review all steps and screenshots to understand the complete workflow
2. Take your own screenshot to see the CURRENT page state
3. The blue highlights show which element to interact with — find it in your current view
4. Follow the same sequence of actions, adapting to any differences
5. If the UI has changed significantly, use judgment to find equivalent elements
</demonstration_context>"""
```

次に、ユーザーのプロンプト、コンテキストブロック、各ステップのスクリーンショットを画像として含めた完全なメッセージを組み立てます。

```
import anthropic

client = anthropic.Anthropic()

content = [
    {"type": "text", "text": user_prompt},
    {"type": "text", "text": generate_playback_context(workflow.steps)},
]

for i, step in enumerate(workflow.steps):
    if step.screenshot:
        content.append({"type": "text", "text": f"[Step {i+1}: {step.description}]"})
        content.append({
            "type": "image",
            "source": {"type": "base64", "media_type": "image/jpeg", "data": step.screenshot},
        })

response = client.beta.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    betas=["computer-use-2025-11-24"],
    messages=[{"role": "user", "content": content}],
    tools=[{
        "type": "computer_20251124",
        "name": "computer",
        "display_width_px": 1280,
        "display_height_px": 720,
    }],
)
```

### **再生モード**

すべてのワークフローが、記録された実演に同じ程度忠実である必要はありません。ワークフローによっては長すぎて大量の入力トークンを消費し、最終的にレイテンシの悪化とコストの増加を招きます。コンテキストプロンプトに含める厳密さ（strictness）のパラメータをサポートすることを検討してください。

**Strict（厳密）:** 手順に正確に従い、UI が大きく変わっている場合は停止して報告します。正確な手順が重要となる、コンプライアンス上の配慮が必要なワークフローに適しています。

**Adaptive（適応）:** 実演をガイドとして使いつつ、UI の変化に適応します。ほとんどのユースケースにとって最適なデフォルトで、軽微なレイアウトのずれ、更新されたボタンのラベル、再編成されたメニューにもスムーズに対応します。

**Goal-oriented（目標指向）:** 最終的な結果に焦点を当て、記録された手順を指示ではなくヒントとして扱います。UI は頻繁に変わるものの目標は変わらない場合に有用です。前述のコンテキスト管理のセクションで説明したものと同様の戦略を用いてモデルで記録された実演を要約し、その要約をコンピュータ操作用のモデルに渡します。

### **例：経費精算のエンドツーエンドのワークフロー**

保存されたワークフローが実際にどのようなものかを紹介します。このワークフローは 5 つのステップをキャプチャしています。経費フォームへの移動、経費の種類の選択、ドロップダウンからの「Travel」の選択、金額の入力、そして Submit のクリックです。

```
expense_workflow = SavedWorkflow(
    id="wf_abc123",
    name="Submit Expense Report",
    start_url="https://expenses.company.com/new",
    steps=[
        WorkflowStep(
            action="navigate",
            url="https://expenses.company.com/new",
            description="Navigate to new expense form",
            timestamp=1700000000,
        ),
        WorkflowStep(
            action="click",
            selector="#expense-type-dropdown",
            coordinates={"x": 400, "y": 200},
            description="Click on expense type dropdown",
            timestamp=1700000001,
        ),
        WorkflowStep(
            action="click",
            selector="[data-value='travel']",
            coordinates={"x": 400, "y": 280},
            description='Select "Travel" expense type',
            timestamp=1700000002,
        ),
        WorkflowStep(
            action="type",
            selector="#amount-input",
            value="150.00",
            description="Enter expense amount",
            timestamp=1700000003,
        ),
        WorkflowStep(
            action="click",
            selector="#submit-expense-btn",
            coordinates={"x": 1150, "y": 420},
            description="Click the Submit button",
            speech_transcript="Now I'll click submit to send the report for approval",
            timestamp=1700000004,
        ),
    ],
)
```

後日ユーザーが「チームランチ（$85.50）の経費精算を提出して」と言うと、再生サービスは、実演のコンテキスト、注釈付きの 5 枚のスクリーンショットすべて、そして新しいリクエストに含まれる具体的な値を使ってプロンプトを構築します。Claude はどこをクリックすべきか、どの順序で進めるべきかを正確に把握し、金額や説明を現在のタスクに合わせて調整します。入力トークン数の都合でワークフローが長すぎてこのアプローチが現実的でない場合は、例として使う前にまずワークフローをコンパクションすることを検討してください。コンテキスト管理のヒントについては、前述のセクションを参照してください。

## **コンピュータ操作・ブラウザ操作を始めるには**

これらのプラクティスは、本番環境でコンピュータ操作の統合を信頼性の高いものにするために何が重要かについての、現時点での私たちの最善の理解を反映したものです。Claude 4.6 モデルファミリーと Opus 4.7 に適用され、新しいモデルや手法の登場に応じて更新されます。

統合が成熟していくにつれて、最も重要となるパターンは、それぞれの環境、対象アプリケーション、信頼性の要件によって変わっていくでしょう。

*[コンピュータ操作のドキュメント](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)から始めるか、これらのベストプラクティスの新しい[デモ実装](https://github.com/anthropics/claude-quickstarts/tree/main/computer-use-best-practices)をご覧いただくか、あるいはこれらの機能がどのように構築され、今後どこへ向かうのかについての背景として、[コンピュータ操作に関する最初のリサーチ記事](https://www.anthropic.com/news/developing-computer-use)をあらためてお読みください。*

*謝辞：本記事と対応するデモは、Lucas Gonzalez と Luca Weihs が執筆しました。著者らは、Molly Vorwerck、Javier Rando、Maya Nielan、Gabe Mulley、Brigit Brown の貢献に感謝します。*
