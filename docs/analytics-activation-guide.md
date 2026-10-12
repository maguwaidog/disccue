# DiscCue analytics activation guide / 計測導入ガイド

Status: **DRAFT ONLY / NEVER DEPLOY WITHOUT REVIEW**. Owner action is required to create a Umami Cloud site and obtain a public website ID. No site ID, analytics collector or privacy-policy changes are active on production.

## Provider and plan considerations (2026-10-12)
- Proposed provider: Umami Cloud, Hobby plan. Check the current pricing and terms before creating the account: https://umami.is/pricing
- The free plan does not provide analytics API/MCP access. Do not imply ChatGPT's scheduled weekly report can automatically fetch Umami data. Instead export dashboard data manually and supply it for reconciliation, or use a separately vetted automation source.
- Umami's cookie-free design does not, by itself, resolve all jurisdiction-specific notice or consent requirements. Check provider privacy, retention, location, transfer details and whether a consent control is required before activating: https://umami.is/privacy
- Avoid placing tracking on checkout pages (hosted by Polar) or in the Windows application.

## Setup (human account step)
1. In Umami Cloud, register/sign in, add website with URL `https://maguwaidog.github.io/disccue/`, and retain the provider-issued **website ID**. It is a site identifier, not a secret token.
2. Using the provider's documented embed snippet (not an invented endpoint), create a second Draft PR commit that injects its script with `defer` into exactly the four event-labelled pages. Consider other site policy pages only after reviewing the data-scope and notice requirements.
3. Keep existing anchor URLs and all 16 `data-umami-event` markers. Verify external-link navigation works normally even if the collector is blocked or offline.
4. Replace the current incorrect “no analytics” sections in **both** `privacy.html` and `en/privacy.html` with the approved copy below, adjusted to reflect verified provider behavior. Update README's “no JS/trackers” statement before deployment.
5. Browser tests with consent/opt-out requirements satisfied: JP/EN desktop/mobile, pageviews, unique event names, double-click/reload behavior, no personal data, 3rd-party blocking, price and download links, policy and accessibility.
6. Human approves final PR; only then merge/deploy. No live analytics has been configured or verified yet.

## Japanese privacy copy (draft, do not publish verbatim without checking provider settings)
### このウェブサイト・アクセス解析
本サイトでは、サイトの利用状況を把握し、説明や導線を改善するため、[提供事業者名]のアクセス解析を利用します。[確認済みの具体的な技術情報・処理内容]および閲覧ページやダウンロード・購入ページへのリンクのクリック状況を取り扱います。クリック数は実際のファイル取得や購入完了を意味しません。取り扱う情報、保存期間（[確認済みの期間]）、保存・移転先（[確認済みの所在地]）、利用停止・同意に関する設定（[適用する仕組み]）については[事業者プライバシーポリシーURL]をご確認ください。購入は引き続きPolarの外部サイトで行い、本サイトで決済情報を取得しません。動画は埋め込まず、クリックした場合のみYouTubeへ移動します。

## English privacy copy (draft, do not publish verbatim without checking provider settings)
### Website analytics
We use [provider] analytics to understand visits and improve website content and navigation. The service processes [confirmed technical data and collection details], page views, and clicks on download and checkout links. Click events do not confirm completed downloads or purchases. See [provider policy URL] for data handling, retention ([confirmed retention]), location and transfers ([confirmed information]), and available privacy or consent controls ([verified mechanism]). Purchases continue through Polar's external checkout; this website does not collect payment-card details. Demo videos remain external YouTube links and are not embedded or loaded automatically.

## Acceptance checklist
- [ ] User account + production website identifier created
- [ ] Verified analytics provider plan / TOS / retention / privacy
- [ ] Japanese & English privacy texts validated against actual data collection
- [ ] Current README claims updated in same deployment as collector
- [ ] Collector added only to planned pages with no personal-information fields
- [ ] Every CTA and each page path tested on a preview / local host
- [ ] No analytics sent until disclosures and applicable privacy choices are in effect
- [ ] No data interpreted as purchases or distinct users without source corroboration
- [ ] Explicit owner sign-off / normal merge only after review

## Weekly measurement process without an API
- Umami dashboard: save date range, timezone, unique visitors, page views, referrers, device/country (only if available), event counts separated by JP/EN path and screen location; export available reports or attach screenshots; omit unavailable fields rather than estimating.
- GSC: organic search impressions/clicks for the settled period; state any API inconsistency rather than forcing totals.
- GitHub: sum **all MSI assets** under `maguwaidog/DiscCue-Releases` (not the application source repository); save per-release cumulative counts and snapshot timestamp.
- YouTube: save the reporting date range and separate total lifetime snapshots from time-bounded performance.
- Polar: only report verified completed orders/revenue; unknown ≠ zero.
- Weekly comparison: current cumulative - previous cumulative for matching definitions; never compute a funnel conversion rate from differently scoped data.

## Security/rollback
Never commit a secret key, Polar credentials, any customer/license data, visitor IP or raw data export into this public GitHub repository. If analytics fails, remove collector references; event labels are inert without it. Update notices to match the actual processing and retained historical data.
