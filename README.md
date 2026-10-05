# DiscCue website

DiscCue displays user-provided SRT subtitles on a separate Windows display or projector. Keep your player. Keep your disc. Add your subtitles.

This repository contains the static product website. It contains no application source or installer. Download official installers from [DiscCue Releases](https://github.com/maguwaidog/DiscCue-Releases).

## Product and downloads

- Windows 11 x64 (tested); Java runtime included, no separate JDK required.
- FREE Trial: 30 cumulative minutes of active subtitle projection in the same DiscCue app.
- Standard: ¥2,480 one-time purchase for customers in Japan, including applicable taxes, up to 2 activated devices, no subscription.
- Initial Standard activation and deactivation require internet access; normal use is offline after activation.
- [DiscCue v1.0.0 Release](https://github.com/maguwaidog/DiscCue-Releases/releases/tag/v1.0.0)
- [Download DiscCue-1.0.0.msi](https://github.com/maguwaidog/DiscCue-Releases/releases/download/v1.0.0/DiscCue-1.0.0.msi)
- [Buy Standard through Polar](https://buy.polar.sh/polar_cl_TDCBYYSAvUdgNv5AkaE9ONiixadWXCWjz7tw21eu6fU)
- [Demo on YouTube](https://www.youtube.com/watch?v=vQmIugiDq54)
- Support: mmd.apps303@gmail.com

The current installer is not digitally signed. DiscCue does not include movies, TV programs, Blu-ray/UHD content, or third-party subtitle files.

## Website structure

Plain HTML and CSS, with no build step, client-side JavaScript, trackers, external fonts, or embedded video.

- `index.html`: product, download, checkout, demo, requirements, FAQ, and support.
- `privacy.html`: local subtitle handling, online licensing, Polar checkout, and support.
- `terms.html`: product licensing, purchase and refund information.
- `tokushoho.html`: seller/provider roles, disclosure requests, Japan price, license delivery, and refund guidance.
- `404.html`: error page.
- `docs/commerce-operations.md`: disclosure and transaction-support procedures; no personal contact details or customer records.
- `assets/`: local stylesheet, favicon and lossless WebP product screenshots.
- `sitemap.xml` and `robots.txt`: crawl hints.

The CSS scene is labeled as a concept illustration, not a product screenshot.

## Preview and review

Run `python -m http.server 8000 --bind 127.0.0.1` from this directory. For the GitHub Pages project subpath, serve its parent and visit the checkout's directory URL.

Review at 320, 390, 768, and 1440 px, including keyboard focus, CTA links, FAQ, local assets, and policy pages. The canonical URL is https://maguwaidog.github.io/disccue/. A project-level robots.txt does not control the host-root robots policy.

Purchase disclosures follow the current official consumer and provider guidance. The owner must maintain the actual request-and-response operation described in `docs/commerce-operations.md`; wording alone does not complete disclosure. The real-product section uses owner-provided captures and keeps the separately labeled concept illustration. Changes on this branch are for review only; merging or deploying requires separate authorization.


## English website

The English landing page is `en/index.html`, with full English Terms, Privacy and purchase information. Japanese and English landing/policy pages use self-canonical URLs and reciprocal `ja`/`en`/`x-default` alternates. The English purchase information and Japan statutory disclosure have different purposes and are not declared interchangeable hreflang translations.

Language choice is explicit in headers and footers, with no automatic locale redirect or client-side storage. Both language versions use the same official v1.0.0 MSI and persistent production checkout link. International visitors review their final amount, currency and taxes in checkout; the Japan price is not advertised as a worldwide quote. The screenshots show Japanese UI. The v1.0.0 application implementation was checked for English and Japanese interface selection before adding the English-interface statement.

Product screenshots must come from the owner's original captures, receive a privacy/content audit and preserve the real UI. The concept illustration remains separately labeled. Do not use fabricated product imagery or upload private audit materials.


## Real product screenshots

Both landing pages show the control window, subtitle-only output and Current Line Sync in that order. Captions and alternative text are localized. Images retain their complete original frame, dimensions and decoded pixels; conversion is lossless WebP, with no UI or subtitle edits. No embedded source metadata is carried over.

| File in `assets/screenshots/` | Dimensions | Bytes |
| --- | --- | ---: |
| `disccue-operation-window.webp` | 1280 × 1392 | 16,482 |
| `disccue-subtitle-output.webp` | 2048 × 1152 | 10,842 |
| `disccue-current-line-sync.webp` | 1277 × 414 | 5,040 |

All three images total 32,364 bytes. They are lazy-loaded with explicit width and height to reserve space. Native image links open the same full-size assets without JavaScript. The captures contain owner-provided demo subtitles, not movie footage, credentials or personal paths.
