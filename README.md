# DiscCue official website — Launch Website v1

DiscCue（ディスクキュー）— **External Subtitles for Physical Media**

**Keep your player. Keep your disc. Add your subtitles.**

DiscCue is a Windows External Subtitle Projection System for home theaters. Users load their own authorized SRT and output subtitles through a separate display/projector in the movie viewing field. The existing disc player and video signal remain untouched. No movies, subtitles, ripping, or movie playback are included.

## Scope and review status

This change implements the launch site in `maguwaidog/disccue` and stops at a **Draft PR**. Do not merge main, deploy Pages, create an application Release, or enable sales as part of this task. `maguwaidog/movie-glass-subtitles` is a read-only specification reference, not a dependency or deployment target.

Confirmed terms: **Standard ¥2,480**, one-time purchase, no subscription, up to two activated devices. Initial online activation; normal offline use without periodic online revalidation. FREE Trial provides **30 cumulative minutes of active projection playback**, not 30 minutes per session. Standard additionally provides unlimited projection playback and Current Line Sync.

The real production download and Polar Checkout URLs are not available. Both actions are native disabled buttons with visible explanations, in the Hero and plan cards. No guessed, sandbox, or placeholder URL is shipped. The launch checklist records exactly how to replace the buttons with verified links and which related notices must change.

- [Pre-change audit and product evidence](docs/launch-audit.md)
- [Required external information and launch checklist](docs/launch-checklist.md)
- [Local validation record](docs/launch-validation.md)

## Structure

```text
index.html                 Problem-led Hero, two signal paths, features, demo,
                           trial/Standard plans and comparison, requirements,
                           FAQ, support, policy links
privacy.html               Verified local/activation/site privacy behavior;
                           full policy still needs completion before checkout
terms.html                 Confirmed terms; refund/seller/full terms review gate
404.html                   Self-contained noindex error page
assets/styles.css          Existing palette plus responsive launch sections
assets/favicon.svg         Existing original DiscCue mark
robots.txt                 Crawl hints for a future root domain
sitemap.xml                Canonical homepage, Privacy, Terms URLs
docs/                      Audit, checklist, and validation notes
.nojekyll                  Static GitHub Pages serving
.gitignore                 Local system-file exclusions
```

Plain HTML/CSS, no JavaScript or build step. Japanese main copy retains concise English explanations. Local system fonts; no analytics, embedded videos, external font requests, or third-party asset dependencies. The original CSS scene is explicitly a concept, not a product screenshot. The supplied demo opens YouTube only when clicked. The actual support address is `mmd.apps303@gmail.com`.

## Local preview

From this repository:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/> and stop with Ctrl+C. Use `python3` if required by your environment. To exercise the project path, serve the parent directory instead and open <http://127.0.0.1:8000/disccue/> with the checkout named `disccue`.

Validate at **320, 390, 768, and 1440 px**: Hero/CTA, table, demo, FAQ, nav, links, CSS/favicon, Privacy/Terms/404, horizontal overflow and keyboard focus. Test FAQ Enter/Space and reduced-motion. Check public pages for broken paths or fake URLs and inspect canonical/OG/Twitter metadata and sitemap. Python's server does not simulate Pages' custom 404 response; open `404.html` directly locally and check a missing nested route only after an authorized deployment.

## GitHub Pages and review workflow

Existing production URL: **https://maguwaidog.github.io/disccue/**.

Publication source is `main`, repository root, using GitHub Pages' **Deploy from a branch** with `.nojekyll`. No custom workflow is necessary. Changes pushed to this feature branch are for review; do not push this launch change directly to main.

For a future explicitly authorized deployment:

1. Resolve all launch blockers in the checklist; verify actual download and production checkout destinations and complete legal pages.
2. Review and merge the PR into main only when authorized. If Pages is already enabled, its main deployment follows automatically.
3. If Pages needs initial configuration, use Settings → Pages → Deploy from a branch → main → /(root). Do not change that configuration during the current Draft PR task.
4. Wait for successful deployment and open the actual production URL. Repeat viewport/link/asset checks; test Privacy, Terms, and a missing nested route returning the custom 404 with working home/favicon paths.

Official source configuration guide: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

The existing official Website URL remains suitable as a reference for seller onboarding, but a website change does not enable a store or guarantee provider approval. This Draft PR changes neither Lemon Squeezy nor Polar settings.

## Future expansion and custom domain

Add real screenshots and verified downloads/checkout after evidence is supplied. Extend Support as needed without adding a framework. Shared presentation stays in `assets/styles.css`; keep the small headers/footers consistent across HTML pages.

No domain purchase, DNS change, or `CNAME` is part of this work. If **disccue.com** is acquired later and migration is authorized, keep this repository as the site source. Configure domain ownership, Pages, DNS, and HTTPS according to GitHub's current documentation:

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

Normal pages use relative links/assets. Update canonical/OG, sitemap/robots, 404's absolute home URL and project-root favicon path, and any onboarding URLs during migration. A `CNAME` alone does not configure DNS. Crawlers request robots.txt at the host root; this repository's `/disccue/robots.txt` is not authoritative for the entire github.io host.
