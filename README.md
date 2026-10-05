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
- `assets/`: local stylesheet and favicon.
- `sitemap.xml` and `robots.txt`: crawl hints.

The CSS scene is labeled as a concept illustration, not a product screenshot.

## Preview and review

Run `python -m http.server 8000 --bind 127.0.0.1` from this directory. For the GitHub Pages project subpath, serve its parent and visit the checkout's directory URL.

Review at 320, 390, 768, and 1440 px, including keyboard focus, CTA links, FAQ, local assets, and policy pages. The canonical URL is https://maguwaidog.github.io/disccue/. A project-level robots.txt does not control the host-root robots policy.

Purchase disclosures follow the current official consumer and provider guidance. The owner must maintain the actual request-and-response operation described in `docs/commerce-operations.md`; wording alone does not complete disclosure. Product screenshots are recommended before launch and can be added later without replacing the labeled concept illustration. Changes on this branch are for review only; merging or deploying requires separate authorization.


## English website

The English landing page is `en/index.html`, with full English Terms, Privacy and purchase information. Japanese and English landing/policy pages use self-canonical URLs and reciprocal `ja`/`en`/`x-default` alternates. The English purchase information and Japan statutory disclosure have different purposes and are not declared interchangeable hreflang translations.

Language choice is explicit in headers and footers, with no automatic locale redirect or client-side storage. Both language versions use the same official v1.0.0 MSI and persistent production checkout link. International visitors review their final amount, currency and taxes in checkout; the Japan price is not advertised as a worldwide quote. English website content does not claim the application has an English UI mode.

Product screenshots must come from the owner's original captures, receive a privacy/content audit and preserve the real UI. The concept illustration remains separately labeled. Do not use fabricated product imagery or upload private audit materials.
