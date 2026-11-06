---
date: '2026-11-05'
final_url: https://claude.com/resources/articles/claude-enterprise-security-updates
number: 166
selector_used: article
slug: claude-enterprise-security-updates
source_url: https://claude.com/blog/claude-enterprise-security-updates
title: More visibility and control over Claude Enterprise for security teams
title_ja: セキュリティチーム向けに Claude Enterprise の可視性と制御を強化
---

Claude Enterprise に、新しいセキュリティ機能と管理機能が加わりました。セキュリティセンター、一般提供となった推論フック、一元管理、そして追加のアクセス制御です。

Claude がどのように設定されているかを把握するために、セキュリティセンターでは組織の Claude 設定を Anthropic の推奨構成と比較して表示します。自社のポリシーを適用するために、推論フックはプロンプトやツール呼び出しをデータセキュリティツールに送り、チェックを行います。アクセスを管理するために、一元管理では全社的な設定を 1 つの管理コンソールで扱えるようになります。さらに新しいアクセス制御により、Admin API を通じたメンバーのサインアウト、IP 許可リストの自己管理、そして管理対象コンピューター上の Claude Desktop で個人アカウントやその他の外部 Claude アカウントをブロックすることによるシャドー IT の防止が可能になります。

また先日、Endpoint Detection and Response（EDR）との連携も発表しました。これにより、ユーザーのコンピューター上で動作する [unified Claude](https://claude.com/resources/articles/unified-claude-enterprise) および Cowork の仮想マシン内で、組織のセンサーを実行できます。

セキュリティチームは、Claude がどのように設定されているか、社内のデバイス上で何を行っているか、そして従業員が作業する中でデータがどのように扱われているかを把握する必要があります。今回の機能は、そのための可視性と制御を提供します。

## セキュリティセンター：Claude のセキュリティ設定を 1 か所で確認

![Claude の Organization settings にあるセキュリティポスチャのダッシュボード。16 項目中 13 項目のコントロールが合格している。](https://assets.claude.com/893acaa9f8b564cda630ed280d69e5c7d2bca5f7.png)

セキュリティチームは、チャット、Cowork、Claude Code における Claude のセキュリティ設定を、設定ごとに個別に確認するのではなく、1 つのページでまとめて確認できるようになりました。セキュリティセンターは Organization settings に新しく追加されたページで、現在の設定を Anthropic の推奨構成と比較します。これにより、チームは何をどこで変更すべきかを把握できます。

各コントロールについて、セキュリティセンターは現在の値、推奨値（存在する場合）、そして変更できる設定へのリンクを表示します。また、新しく追加された設定や最近変更された設定も示します。セキュリティセンターはページを読み込むたびに構成をチェックするため、自動チェックされるコントロールには常に現在の設定が反映されます。Compliance API を利用している組織は、同じ結果を API 経由で取得することもできます。

アテステーション（attestation）機能は、管理者がセキュリティレビューを行うための共有ワークスペースです。管理者はプロセスを一度一緒に進めるだけで、各コントロールの現状の記録、リスクの受容、問題のフラグ付けを 1 か所で行えます。

セキュリティセンターのページはレポートとしてダウンロードでき、監査人や関係者と共有できます。レポートには、どのコントロールがページによって自動チェックされたか、どれが Owner によって確認されたかが明記されます。なお、セキュリティセンターは Anthropic の推奨事項に基づくガイダンスであり、いかなる法律や基準への準拠を認証・保証するものではありません。

## 推論フック

推論フック（inference hooks）は、組織がすでに利用しているデータセキュリティツールと Claude を接続します。これにより、従業員が作業する中で、データ損失防止（DLP）やセキュリティのポリシーをプロンプトやツール呼び出しに適用できます。

フックには 2 種類あり、いずれも一般提供（GA）となりました。

- プロンプトフックは、対応する Claude プロダクトからのプロンプトをセキュリティツールに送り、チェックを行います。
- ツール呼び出し前フック（pre-tool-call hooks）は、対応する Claude プロダクトでのツール呼び出しを実行前にチェックします。

フックはセキュリティベンダーの製品と連携して動作します。チームはすでに作成済みのポリシーをそのまま使い、Claude に適用できます。

## 一元管理：組織全体のアイデンティティとアクセスを 1 つのコンソールで

一元管理（centralized management）では、親組織に専用の管理コンソール（admin.claude.com）が用意されます。親組織とは、Claude Enterprise および Claude Platform の各組織にまたがって会社全体を表す組織です。管理者は、個々の組織の設定から操作するのではなく、親組織配下の組織に対する全社的な設定をこのコンソールで一度に管理できます。対象となる設定には、シングルサインオン、ディレクトリ同期（SCIM）、ドメイン検証、グループ、Compliance API キーが含まれます。

コンソールでは親組織配下のすべての組織を 1 か所で確認でき、2 つのロールが追加されます。親組織のオーナー（Parent organization owners）は、オーナーや管理者のロールを誰に付与するかを含め、親組織レベルのすべてを管理できます。親組織の管理者（Parent organization admins）は、それらのロール割り当てを除くすべてを管理できます。

また、複数のアイデンティティプロバイダーを接続し、それぞれに個別のシングルサインオンおよび SCIM 構成を持たせることも可能になりました。買収した企業が既存のプロバイダーを使い続けることも、チームが 1 ドメインずつ新しいプロバイダーへ移行することもできます。

各組織は、それぞれのメンバー、ロール、設定、そして IP 許可リスト、テナント制限、セッション期間といった組織レベルのセキュリティコントロールを引き続き保持します。親組織のロールは、デフォルトでは個々の組織内へのアクセス権を付与しません。ただし、親組織で作成された Compliance API キーは、組織をまたいでデータを読み取ることができます。

## アクセス制御：メンバーのサインアウトとシャドー IT の防止

セキュリティチームは、Admin API を 1 回呼び出すだけで、メンバーを組織から削除することなく Claude からサインアウトさせられるようになりました。この呼び出しにより、そのメンバーのすべてのブラウザとデバイスでのサインインセッションが終了し、Claude Code などのアプリでは再度サインインが必要になります。ただし、API キー、すでに実行中のクラウドセッション、スケジュールされたルーティンは終了せず、メンバーは後から再びサインインできます。

Enterprise の管理者は、Anthropic を介さずに IP 許可リストを自分で設定・管理できるようになりました。IP 許可リストは、ほとんどの Claude プロダクトへのアクセスを、組織が承認した IP アドレスに制限します。

管理者は、デバイス管理によるプッシュを行わずに、Claude Desktop のよく使われる設定を構成できるようになりました。シャドー IT の防止に役立てるため、管理対象コンピューター上の Claude Desktop で、個人アカウントやその他の外部 Claude アカウントをブロックすることもできます。さらに Owner は、従業員が Claude で使用できるワークスペースフォルダーを制限することもできます。

## Cowork と unified Claude における Endpoint Detection and Response（EDR）

Cowork と unified Claude がローカルで動作する場合、保護を強化するため、シェルコマンドやコードはユーザーのコンピューター上の隔離された仮想マシン内で実行されます。この隔離はデバイスの保護に役立ちますが、セキュリティチームからは、エンドポイントの他の場所と同様に、この仮想マシン内についても可視性がほしいという要望が寄せられていました。

管理者は、組織の EDR センサーを Cowork の仮想マシン内で実行できるようになりました。センサーは仮想マシン内のアクティビティを、セキュリティチームがすでに監視しているのと同じコンソールに報告します。対象となるのはユーザーのコンピューター上の仮想マシンであり、クラウド上の Cowork セッションは含まれません。

管理者は、macOS および Windows のデバイス管理を通じて連携を設定します。仮想マシンが起動するたびに、Claude は EDR ベンダーによるセンサーパッケージの署名を検証してからインストールします。センサーは検知モードで動作し、アクティビティをセキュリティチームに報告しますが、ブロックはしません。この連携は対応する EDR ベンダーで利用でき、対応ベンダーは [ヘルプセンター](https://support.claude.com/en/articles/17828685-run-your-endpoint-detection-and-response-edr-sensor-in-claude-cowork-on-claude-desktop) に掲載されています。

## はじめに

これらの機能は Claude Enterprise で利用できます。ベータ期間中の一部例外については [ヘルプセンター](https://support.claude.com/en) をご覧ください。

[セキュリティセンター](https://support.claude.com/en/articles/18246629-review-your-organization-s-security-posture-with-the-security-center) はベータ版です。プロンプトフックとツール呼び出し前フックを含む [推論フック](https://support.claude.com/en/articles/16059458-inference-hooks-overview) は一般提供されています。管理者は、推論フックとセキュリティセンターのどちらも Organization settings で管理できます。

[一元管理](https://support.claude.com/en/articles/18232924) もベータ版です。セットアップを開始するには、親組織配下のいずれかの組織の管理者が admin.claude.com にアクセスし、親組織の管理者を提案します。他の組織の管理者がレビューして承認し、最後の承認によってセットアップが完了します。セットアップは取り消せないため、開始前に親組織の管理者を決めておいてください。

Admin API による [メンバーのサインアウト](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans#h_3cba7d14e5) と [セルフサービスの IP 許可リスト](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting) はベータ版です。Owner は Organization settings で [Claude Desktop の設定](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop#h_21135034c8) を管理できます。こちらもベータ版です。

Cowork における [Endpoint Detection and Response](https://support.claude.com/en/articles/17828685-run-your-endpoint-detection-and-response-edr-sensor-in-claude-cowork-on-claude-desktop) は、macOS および Windows 上の Claude Team と Enterprise、ならびに Amazon Bedrock、Google Cloud Vertex AI、Microsoft Foundry 上の Claude デスクトップアプリ向けにベータ版として提供されており、対応ベンダーについては MDM を通じて展開されます。
