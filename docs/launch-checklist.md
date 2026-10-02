# Launch Website v1: review and activation checklist

This branch is a **Draft PR only**. Do not merge, deploy, publish an application release, or enable sales as part of this task. The current GitHub Pages production site stays on main. Product evidence and the pre-change audit are in [launch-audit.md](launch-audit.md).

## Confirmed public facts

- DiscCue / External Subtitles for Physical Media; Windows subtitle-only display/projection, user-supplied legal SRT and media.
- Standard ¥2,480, one-time, no subscription, up to two activated devices.
- Initial online activation; normal offline use without periodic online revalidation; online deactivation returns a slot.
- FREE: 30 cumulative minutes of active projection playback; paused/stopped/setup time excluded; remaining trial survives restart.
- FREE and Standard: local SRT, separate output, styling/geometry, manual timing/Seek/Jump. Standard additionally enables unlimited projection playback and Current Line Sync.
- Windows 11 design target; existing artifact is x64 MSI with a bundled runtime. Minimum supported OS remains unconfirmed.
- Support: mmd.apps303@gmail.com. Demo: https://www.youtube.com/watch?v=vQmIugiDq54.

## Required external information

- **DOWNLOAD_URL_REQUIRED**: supply the real production distribution URL and verify the published installer, identity/version, signing, and supported Windows matrix. No application GitHub Releases were present during the audit. A local MSI is not a distribution URL.
- **POLAR_CHECKOUT_URL_REQUIRED**: supply the verified production Polar Checkout URL and confirm that it represents Standard ¥2,480 / one-time / two devices. The reference checkout configuration defaults to null. Do not substitute sandbox or test URLs.
- **SCREENSHOT_REQUIRED**: supply cleared real UI and actual subtitle projection/setup images with useful alt text. No suitable tracked images were found. The existing homepage CSS illustration is explicitly a concept; it is not an app screenshot. The provided Watch Demo link is usable independently.
- **WINDOWS_SUPPORT_CONFIRMATION_REQUIRED**: confirm the minimum supported version and tested Windows versions. Do not infer Windows 10, ARM, or x86 compatibility from the MSI format.
- **LEGAL_POLICY_CONFIRMATION_REQUIRED**: finalize seller identity/details, full product license/terms, refund eligibility/period/procedure, and privacy purposes/retention/request procedures. Confirm any checkout tax/currency presentation. Do not invent a refund window, lifetime updates, or a legal operator.

## Connect the two actions after verification

1. Verify the production URLs and destination content; document the evidence in the follow-up PR.
2. In `index.html`, replace **both** Download Free Trial disabled buttons (Hero and FREE card) with `<a class="button">` elements whose `href` is the verified distribution URL. Replace their unavailable notes with accurate version/platform/install information. Remove `disabled` and obsolete `aria-describedby` references.
3. Replace **both** Buy Standard disabled buttons (Hero and Standard card) with anchors to the verified production checkout. Keep Hero's `button-outline` style if appropriate. Replace the unavailable notes with accurate checkout information.
4. Update the unavailable-link notices in `#pricing`, the price FAQ, `privacy.html`, and `terms.html`. Complete the legal pages before enabling purchase. Do not merely remove their review notices.
5. Add cleared screenshots if supplied. Keep demo content separate from included product assets.
6. Confirm the application's independent release gates, including the actual-version-upgrade and physical multi-device tests currently marked NOT RUN in the reference acceptance docs. This website change does not claim those tests pass.
7. Repeat the validation below, seek review, and deploy only when separately authorized.

## Validation before review or deployment

- Serve the parent directory and visit `/disccue/` to exercise the GitHub Pages subpath. No build step is required.
- Check index, Privacy, Terms, and 404 at 320, 390, 768, and 1440 px: no horizontal overflow, legible hero/CTA/table/FAQ, local CSS and favicon loads.
- Inspect heading hierarchy, duplicate IDs, image alt attributes, metadata/canonical/OG/Twitter, all internal anchors and routes, and sitemap.
- Use the keyboard for skip link, navigation, demo/support links, and FAQ (Enter/Space). Check focus visibility, text contrast, and reduced-motion.
- Confirm unavailable actions remain native disabled buttons with explanatory text until their real URLs exist; no fake href, localhost, sandbox, or test URL in public pages.
- Check direct external links (YouTube, provider policies), and the exact support mailto. HTTP success is a reachability check, not proof that media rights or provider settings are cleared.
- Local Python servers do not emulate the GitHub Pages custom 404 response. Preview `404.html` locally; after an authorized deployment also test a nonexistent nested URL and its home/favicon paths.
- After a future authorized merge, validate the actual production URL and HTTPS. For this Draft PR, verify main and the public homepage remain unchanged.

## Search and custom-domain notes

Canonical, OG, and sitemap URLs use `https://maguwaidog.github.io/disccue/`. `robots.txt` is included for a future root domain; crawlers request robots at the **host root**, so `/disccue/robots.txt` alone is not authoritative for github.io. The existing host robots policy remains outside this repository's control. Sitemap can be submitted at its project URL.

No custom domain or DNS is configured. If `disccue.com` is acquired and a migration is authorized, update canonical/OG URLs, sitemap/robots, and 404's absolute home/project-root favicon path as well as GitHub Pages and DNS. The ordinary pages retain relative assets and internal links.
