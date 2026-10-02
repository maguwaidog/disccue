# Launch Website v1: pre-change audit

Audit date: 2026-10-03 (Asia/Tokyo).

## Sources and repository boundaries

- Website base: `maguwaidog/disccue`, `main`, `49586aa7b68445e2f6b0fb0174203961719541df`.
- Public website: https://maguwaidog.github.io/disccue/ (HTTP 200).
- Reference application latest main: `d762ccdd4d2ab91525a1a3bee67d8fce5ea2dd73`, merge of PR #34.
- PR #34 is merged. Its main tree `0964a2866354b6e72c9e0f89106a5ea9e7d5d836` is identical to the available read-only reference checkout at `e37f969e44763e91a6b8ad2e15a45095351625fe`.
- The application checkout, its branch, files, and references are not modified by this task. No application branch, commit, or PR is created.

## Current website issues

- Hero and metadata say “IN DEVELOPMENT” / “現在開発中”.
- Hero says public download and sales have not started.
- Product and feature notes use development/release-pending language.
- Status says release date and price are undecided.
- STANDARD and FREE Trial are described only as planned.
- Contact details are placeholders, including the Privacy page.
- Terms describe pricing and licensing as unfinalized, which conflicts with the new confirmed brief.
- No problem-led imported Blu-ray/UHD entry point, trial/download CTA, pricing/comparison, demo, requirements, or FAQ.
- No purchase or download URL is configured.
- Site contains only HTML/CSS, a custom 404, and original vector/CSS concept art. There are no real product screenshots.
- Favicon, semantic sections, focus visibility, responsive rules, and reduced-motion support exist.
- SEO has title/description but no canonical, Open Graph, Twitter card, robots.txt, or sitemap.
- Existing source branch is `main`; this task uses `launch/disccue-website-v1` and stops at Draft PR.

## Verified product facts

- User-confirmed commercial terms: Standard ¥2,480, one-time purchase, no subscription, up to two devices.
- Application README, `LicenseUiStrings.kt`, and `docs/polar-license-activation-v1.md`: initial online Standard activation; normal offline use without periodic online revalidation; online deactivation releases a slot.
- `ProductEntitlements.kt` and `docs/commercialization-step3c-free-trial.md`: FREE trial is 30 cumulative minutes of active projection playback. SRT loading, configuration, and paused playback do not consume it. Remaining usage persists across restarts.
- Baseline SRT loading/rendering/playback, separate display, style/geometry and manual timing are available in FREE. Standard enables unlimited projection playback and Current Line Sync.
- `docs/commercialization-step3d-current-line-sync.md`: Current Line Sync aligns the current displayed cue's SRT start to the subtitle playback clock by correcting global offset; it does not modify the source SRT and is not automatic movie/audio synchronization.
- `desktop/build.gradle.kts`: Windows MSI/EXE packaging, DiscCue 1.0.0. README: packaged Java runtime; end users do not need Gradle/JDK.
- `docs/step2-windows-design.md`: Windows 11 is the documented design target. The existing MSI's read-only Windows Installer summary reports `x64;1033`, and its bundled Java runtime PE machine type is `0x8664` (x64). The local MSI SHA-256 is `C8D674B7514BE33A07074CCFEC5EDFF29B12B37D8C22E36AE726ECFCE78701BA`, matching the acceptance record. This is evidence of x64 packaging, not a published download or a complete supported OS matrix. Minimum OS version and the formally supported list still need confirmation.
- Display selection uses connected Windows/AWT displays; a separate subtitle display/projector is required for the described two-output setup.

## External dependencies and launch gaps

- Production checkout: `LicenseCheckoutConfiguration.standardCheckoutUrl` defaults to null. No verified official checkout URL was found in site or tracked reference source/docs.
- Distribution: GitHub's application Releases list is empty at audit time. An acceptance-tested local MSI is not a published production download.
- Images: no suitable tracked real UI/projection/setup images found in either repository. Existing conceptual artwork must stay labeled as a concept.
- Demo: user-provided https://www.youtube.com/watch?v=vQmIugiDq54; use a direct Watch Demo link, without third-party frames or thumbnail downloads.
- Support: user-confirmed `mmd.apps303@gmail.com`.
- Full seller information, refund conditions, and final product/privacy legal policies are not supplied. Do not invent them.
- App acceptance docs retain release-only actual-version-upgrade and physical multi-device tests as NOT RUN. This website task does not clear those gates.

## Implementation direction

Preserve the static website and brand. Add a problem-led Hero, separate trial/purchase actions, two-path how-it-works, confirmed FREE/Standard comparison, direct demo link, requirements, FAQ, and real support contact. Add SEO metadata and crawl files. Disable unavailable checkout/download actions with clear user-facing explanations; document launch blockers. Do not merge, publish, release, create products, change seller settings, obtain keys, or add tokens.
