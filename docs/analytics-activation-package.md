# DiscCue / Umami Cloud activation package — NOT DEPLOYED

Prepared: 2026-10-12. Status: **HOLD**. No Umami account, site ID, live tracker, or real event test has been provided or verified.

## Decision record

Recommended initial provider: **Umami Cloud — Hobby**, subject to site-owner review.

- Pricing at review: $0/month, **1 website**, up to **100,000 events/month**, **6-month retention**.
- Custom events can be recorded with `data-umami-event` on an HTML anchor; no manual JavaScript callbacks needed.
- Caveat: **Cloud API and MCP access are not in Hobby**. Do not claim automatic weekly import of Umami statistics. The owner may review its dashboard and export data for the weekly DiscCue report. Do not upgrade to a trial or Pro without explicit approval.
- Cloud hosting and processing: consult Umami's live data-processing terms and privacy policy. Its documented server locations are US and EU/Germany. A cookie-free tracker does not by itself settle all notice, consent, or international-transfer requirements.
- Umami Cloud registration and the website UUID remain an **owner action**. The public website UUID is a non-secret setting; never put an API token or login credential into GitHub or chat.

Official sources (last checked 2026-10-12):
- https://umami.is/pricing
- https://docs.umami.is/docs/cloud/faq
- https://docs.umami.is/docs/add-a-website
- https://docs.umami.is/docs/track-events
- https://docs.umami.is/docs/tracker-configuration
- https://umami.is/privacy
- https://umami.is/terms

## Registration (manual, no automation)

1. Open https://cloud.umami.is/signup and select **Hobby / Free**, not a paid trial.
2. Inside Websites, register name `DiscCue` and domain `maguwaidog.github.io` **without** `https://` or the project path `/disccue/`.
3. Copy the tracking script from the Umami website settings and capture the **website ID only**. Do not share login, session tokens, or API keys.
4. Check current privacy, DPA and data location options; determine whether a consent mode/notice is required for the site's real audience before activation.

## Candidate script (documentation only: NEVER copy automatically to a live page)

The exact script host and attributes must be checked against the site's Umami dashboard snippet at implementation time:

```html
<script defer
  src="https://cloud.umami.is/script.js"
  data-website-id="REPLACE_WITH_UMAMI_WEBSITE_UUID"
  data-domains="maguwaidog.github.io"
  data-exclude-search="true"
  data-exclude-hash="true"
  data-do-not-track="true"></script>
```

Use `data-domains` to prevent stats from local previews or alternate preview hosts; the tracker **must not** be loaded in any production HTML before both language privacy notices, provider account and browser tests are ready. Keep Umami on the *website only*: do not instrument the Windows app, offline activation state, license keys, Polar hosted checkout, or customer portal.

**Privacy hygiene:** custom event names only, no custom event values. Exclude URL query/hash. Inspect the actual network requests to verify referrers do not expose private query parameters or identifiers; if they do, use a supported sanitizing strategy or stop rollout. Do not add `data-distinct-id` or fingerprint identifiers. Respect Do Not Track.

## Required proposed privacy replacement — Japanese

Replace the entire paragraph under `このウェブサイト / This website` **when activation is approved**, not beforehand:

> このウェブサイトでは、ページの閲覧状況や製品紹介の導線を改善するため、Umami Cloudによるアクセス解析を行います。閲覧ページ、流入元、閲覧日時、ブラウザー・端末種別、おおまかなアクセス地域、デモ動画・ダウンロード・購入案内リンクのクリックといった利用状況を統計的に確認します。サイトのアクセス解析コードはCookieやブラウザー保存領域への書き込みを行わず、URLのクエリ文字列・フラグメントを収集せず、ブラウザーのDo Not Track設定を尊重します。これらのクリックはダウンロード完了や購入完了を意味しません。解析イベントとしてメールアドレス、ライセンスキー、決済情報、映画・字幕データなどを送信しません。閲覧者の通信情報は解析サービスへのアクセス時に同サービス側で処理される場合があります。データの取扱い、保存期間、国外での処理についてはUmamiのPrivacy PolicyおよびTermsをご確認ください。YouTube動画は埋め込まず、リンクをクリックするとYouTubeへ移動します。

Under `外部サービス / External services`, **add** (do not remove hosting, YouTube or Polar references):

> アクセス解析にはUmami Cloudを使用します。統計情報は日本国外（米国または欧州を含む）のサーバーで処理される場合があります。詳しくは https://umami.is/privacy と https://umami.is/terms をご確認ください。アクセス解析に関するお問い合わせは本ページ記載の窓口へご連絡ください。

Check actual data retention and data-subject rights with the vendor at publication time. The live policy's statement that analytics is *not installed* MUST be replaced at the same deployment as the live script.

## Required proposed privacy replacement — English

Replace the entire paragraph under `This website` **when activation is approved**, not beforehand:

> This website uses Umami Cloud to understand aggregate page visits and improve product navigation. Metrics may include visited pages, referring sources, times of access, browser and device types, approximate geographic region, and clicks on demo, download and purchase links. The analytics code does not set cookies or write to browser storage. We configure it to omit URL query strings and fragments and to respect browser Do Not Track settings. A recorded click is not confirmation of a download or completed purchase. We do not send email addresses, license keys, payment information, movie or subtitle content as analytics event properties. The provider may process technical connection information when receiving analytics requests. See Umami's privacy policy and terms for details of processing, retention and international transfers. YouTube videos are linked, not embedded or automatically loaded.

Under `External services`, **add** (preserve existing provider descriptions):

> Umami Cloud processes aggregate website analytics and may process data on servers outside Japan, including the US and EU. For details, see https://umami.is/privacy and https://umami.is/terms. Direct privacy enquiries about DiscCue website analytics to the support contact on this page.

## Activation gates

1. Verify free plan, owner account and website UUID.
2. Review current provider policy/terms and consent requirements for audiences reached, with notice requirements resolved.
3. Place approved script in exactly **four pages**: `index.html`, `en/index.html`, `guides/blu-ray-external-subtitles/index.html`, `en/guides/blu-ray-external-subtitles/index.html`. If site-wide coverage is desired, explicitly audit and include additional policy/legal pages as a separate scope decision.
4. Replace appropriate Japanese/English live privacy paragraphs in the **same** PR before any script becomes active, with exact HTML escaping and real links; update README's 'no JavaScript/no trackers' claims. Include page footer access to privacy.
5. Check native hyperlink navigation (including relative links). A past Umami Cloud issue reported relative anchors with `data-umami-event` interfering with navigation; if reproduced, do not deploy the blocker. Reference: https://github.com/umami-software/umami/issues/3144
6. Exercise both languages on desktop and mobile: each expected event once, pageview once, target href still navigates, script-blocked case still navigates, no duplicate events, no personal info in network payloads. Never rely on simulated code tests as proof of real reporting.
7. Confirm event counts in owner dashboard, check monthly limits and exclude administrator testing where possible.
8. Explicit owner review/approval is required before merge or deployment; keep PR **Draft** until then.

## Reporting model

Weekly cadence: Japan Monday 09:00, windows exactly defined and same-length comparisons.

- **GSC**: organic impressions, clicks, CTR, ranking, query/page breakdown, known data lag.
- **Umami Hobby dashboard/export**: visits, pageviews, referrers, languages via paths, and eight specific click event names. **Manual import while on Hobby**; do not fabricate when data is absent.
- **GitHub**: `maguwaidog/DiscCue-Releases` asset `download_count` by installer version, cumulative snapshots and deltas, not distinct installers/users.
- **YouTube**: independently measured video impressions/views and sources.
- **Polar**: confirmed purchases/revenue only when a legitimate connected or owner-reported source exists.

Never claim that an outbound click proves an actual MSI download, an installed/activated Trial, or a Standard sale. Cross-platform click-to-purchase CVR is **not** measurable without accurately linked cohorts and legal privacy review.
