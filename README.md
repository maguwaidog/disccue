# DiscCue official website

DiscCue（ディスクキュー）— **External Subtitles for Physical Media**

This repository contains the official product website (v0.2 positioning update). The application repository `maguwaidog/movie-glass-subtitles` is separate and is not a dependency or deployment target.

**Keep your eyes on the movie.**

DiscCue is an **External Subtitle Projection System for Windows Home Theater**, currently in development. The brand descriptor remains **External Subtitles for Physical Media**. User-supplied SRT subtitles are output through a separate subtitle display or projector positioned in the same viewing field as the movie. Existing movie playback equipment remains untouched; DiscCue does not modify the video signal or digitally composite subtitles into it.

The subtitle workflow is local/offline, with subtitle styling, position/geometry adjustment, precise timing/offset controls, Seek/Jump, and Current Line Sync. Current Line Sync uses the current subtitle line as a reference for manual alignment with the dialogue. These capabilities are implemented or confirmed for v1 STANDARD; the website does not imply that the product is released or that synchronization is automatic.

Users provide their own subtitle files and must use legally obtained media and subtitle files they are authorized to use. DiscCue does not provide, host, stream, or distribute movies or copyrighted video content, and does not supply subtitles.

## Structure

```text
index.html             Hero, product, features, how it works, status, contact
privacy.html           Current website privacy information; product policy pending
terms.html             Pre-launch terms, license, and refund status
404.html               Self-contained missing-page page
assets/styles.css      Responsive styles; local system fonts
assets/favicon.svg     Original DiscCue mark
.nojekyll              Serve static files without Jekyll processing
.gitignore             Ignore local system files
README.md              Local preview, deployment, and expansion notes
```

Plain HTML/CSS. No JavaScript, build tooling, external fonts, analytics, cookies, purchase forms, or third-party asset dependencies. The homepage artwork is an original CSS concept illustration, not a screenshot of the application. Japanese descriptions include English explanations for international visitors.

## Local preview

From this repository directory, run:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/>. `python3` can be used on systems where Python is named `python3`. Stop the server with Ctrl+C. The homepage and policy pages also work as static files.

To check the GitHub Pages project subdirectory locally, run the server from the parent directory and open <http://127.0.0.1:8000/disccue/>. Keep the checkout directory named `disccue` for this check. Python's default server does not emulate GitHub Pages' custom 404 behavior; directly open `404.html` to preview its appearance, then check a nonexistent nested URL on the live Pages site after deployment.

Check both narrow mobile and wide desktop viewports, anchor links, policy pages, the home links, and asset loading. No deployment credentials belong in this repository.

For a positioning or layout update, verify widths **320, 390, 768, and 1440 pixels** locally and on the live Pages URL. Check the hero and viewing-field illustration, the How it works anchor, all navigation, Privacy/Terms/home links, CSS/favicon paths, and the custom 404 page. Confirm that no horizontal overflow occurs and that the copy remains readable. The illustration shows separate physical outputs in one viewing field, not subtitle compositing into the video signal.

## GitHub Pages publication

1. Create the independent public repository `maguwaidog/disccue` and push these files to `main`.
2. Open repository **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/(root)**, then Save.
4. Wait for the Pages deployment to succeed, then open **https://maguwaidog.github.io/disccue/**.
5. Confirm `privacy.html`, `terms.html`, stylesheet, favicon, anchors, and a nonexistent nested path. Confirm HTTPS and the mobile layout.

Publication source: `main`, repository root. `.nojekyll` keeps the site independent of Jekyll. A custom workflow is not required.

For subsequent updates, inspect local changes, fetch `origin/main`, and fast-forward the clean `main` branch before editing. Review the diff and run local checks before committing. Push the reviewed update to `main`, wait for Pages to reflect that commit, and repeat the live checks above. Update only this website repository.

GitHub's source configuration guide: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

Use **https://maguwaidog.github.io/disccue/** in the Lemon Squeezy Seller onboarding **Website URL** field after the live site has been verified. Creating this website does not create a store, change seller settings, issue licenses, or guarantee seller approval.

## Before sales begin

- Replace the contact placeholder with actual contact and support details.
- Publish the product Privacy Policy based on the implemented data handling.
- Publish full terms, licensing, refund procedures, and seller information.
- Confirm Windows requirements, supported subtitle formats, and trial details.
- Add genuine application screenshots, verified downloads, final pricing, and purchase information when ready.

Do not add fixed pricing, checkout links, unsupported capability claims, fabricated contact details, or claims of a released product while development is ongoing. Every purchase-related page must reflect the actual released product and sales arrangements.

Keep STANDARD's one-time purchase and FREE Trial wording at the planned stage until the commercial terms are finalized. Internal pricing hypotheses do not belong in this public repository. Focus public feature descriptions on the confirmed v1 scope; do not present future synchronization assistance, glasses, subtitle-provider integrations, translation, or cloud search as current capabilities. Avoid competitor comparisons and unsupported uniqueness claims.

## Future expansion

Add Screenshots, Download, Pricing, Purchase, and Support as new sections or standalone HTML pages when their content is available. Shared presentation is centralized in `assets/styles.css`; update the small shared header/footer on each HTML page when navigation changes. Maintain relative links and asset URLs so the site works under `/disccue/` and at a domain root. Add genuine screenshots with useful alternative text; never imply the concept artwork is the product UI.

## Future custom domain: disccue.com

No domain has been purchased or configured by this project, and no `CNAME` file is included. If `disccue.com` is obtained later, this repository can remain the source of the official website.

When explicitly authorized at that time, verify ownership and configure the custom domain in GitHub Pages Settings, set the required DNS records at the domain provider, wait for the certificate, and enable HTTPS. Follow the current GitHub documentation rather than hardcoding DNS addresses here:

https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

The normal pages use relative links and assets. Update the absolute home URL in `404.html` to the new official domain as part of that migration, and update onboarding/reference URLs. A CNAME file alone is not a substitute for configuring and verifying the domain in Pages settings.
