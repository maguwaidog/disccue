# Launch Website v1 validation

Date: 2026-10-03 (Asia/Tokyo). Website base: `49586aa7b68445e2f6b0fb0174203961719541df`.

## Local source and browser checks

Static HTML/CSS: no build or package installation is needed. The project was served from its parent directory at `/disccue/` to exercise the GitHub Pages project path. Validation tooling and screenshots remain in the task workspace, outside this website repository.

- HTML structural checks passed for index, Privacy, Terms, and 404: balanced tags, one h1 per page, heading hierarchy, unique IDs, local paths and fragments, image alt attributes, canonical/description/OG/Twitter metadata, 404 noindex, and safe URL inspection. This is a structural audit, not a W3C validator certification.
- XML sitemap parsed and its three canonical pages matched the HTML. robots.txt sitemap hint matched; host-root robots limitations are documented in the checklist.
- Chrome/Playwright: **92 checks passed, zero errors**, across **320, 390, 768, and 1440 px**, including all four HTML pages. CSS parsed through the browser with local asset routes returning 200. No horizontal page overflow, clipped inspected text, unloaded images, failed local resources, or console/page errors were found.
- Native disabled Download/Buy actions appear twice each (Hero and plan cards), with explanatory text. No fake checkout/download URL is present.
- Navigation destinations, all 13 FAQ entries, and expanded FAQ widths passed. Keyboard skip link and navigation work; focus indicators are visible; Enter/Space opens and closes native FAQ details. Demo and support point to the exact user-supplied destinations.
- Computed text contrast checks passed for rendered text on all four pages using the actual solid ancestor backgrounds (4.5:1 normal / 3:1 large text). Original decorative artwork is not a product screenshot; contrast checks are not an automated accessibility certification.
- Reduced-motion sets smooth scrolling to auto. No automatic external requests occur: fonts, CSS, favicon, and artwork are local; YouTube is a direct link.
- **32 screenshots** were captured: all pages at each requested width, expanded FAQs, Hero/how-it-works/pricing/demo section captures on mobile and desktop, and four initial viewport captures. The hero, two signal paths, pricing/table, and overall tablet/mobile layouts were visually reviewed. The product explanation and trial/price summary fit in the initial viewport at 320×740, 390×844, 768×1024, and 1440×1000.
- `git diff --check` passed.

## Links and current production site

- All five HTTPS destinations used by the pages returned **HTTP 200**: supplied YouTube demo, Polar Privacy Policy, GitHub Privacy Statement, Google Privacy Policy, and the official homepage. YouTube oEmbed returned 200 with title **DiscCue_DEMO**, confirming the supplied video identifier resolves. Reachability is not a media-rights or provider-configuration review.
- The current **main production site**, not the launch branch, returned 200 for homepage, Privacy, Terms, CSS, favicon, and direct 404.html. A nonexistent nested route returned the DiscCue custom **404** with its home link.
- The public homepage exactly matched the pre-change bytes (SHA-256 `130e51ec9682fc5d171f7e529d10b1b3d80af0eb06f82025d78a3705dbeafb27`). The launch version has **not** been deployed or validated as live production.
- Local Python's server does not emulate Pages custom-404 handling. The new 404 page uses inline styling and a project-root favicon path so nested URLs do not require relative CSS. Repeat the live nested-404 test after an independently authorized deployment.

## Boundaries and remaining gates

The application reference checkout remains on `codex/polar-license-activation`, SHA `e37f969e44763e91a6b8ad2e15a45095351625fe`, clean and unchanged. Its tree matches merged PR #34 / latest main `d762ccdd4d2ab91525a1a3bee67d8fce5ea2dd73`. Only the website feature branch is committed/pushed. No application release, license activation, product/seller change, merge, Pages publication, domain purchase, or DNS change is performed.

Real download/production checkout URLs, cleared screenshots, formal Windows support matrix, seller/refund/full policy details, and the application's independent release acceptance gates remain open. See [launch-checklist.md](launch-checklist.md). Safe disconnected actions are intentional; this validation does not declare the commercial launch ready.
