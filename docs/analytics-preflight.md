# DiscCue website analytics preflight (2026-10-12)

Status: **DRAFT / NO TRACKING ACTIVE / DEPLOYMENT HOLD**

## Scope and rationale
Production uses GitHub Pages, static HTML/CSS, no browser analytics. Existing Japanese/English Privacy pages explicitly state there is no analytics. This branch **only** adds inert `data-umami-event` attributes to pre-existing anchors. No tracking JavaScript, cookie, pixel, outgoing request, or behavior-changing listener is included. Do not merge based solely on this preparation.

Potential provider: Umami Cloud (or equivalent privacy-oriented service), contingent on independent review of current terms, pricing/free quota, hosting region, personal data practices, consent obligations, and availability. No vendor selection or account configuration has been authorized or performed.

## Event contract
Analytics event identifiers are fixed, language-independent, and contain no visitor identifiers, search query parameters, subtitle contents, email, license key or purchase information.

| Event | Location | Counted action (NOT outcome) |
| --- | --- | --- |
| `download_hero_click` | JP/EN landing | user clicks top installer CTA |
| `download_pricing_click` | JP/EN landing | user clicks Trial section installer CTA |
| `checkout_hero_click` | JP/EN landing | user clicks top checkout CTA |
| `checkout_pricing_click` | JP/EN landing | user clicks Standard section checkout CTA |
| `demo_hero_click` | JP/EN landing | user clicks early YouTube demo link |
| `demo_section_click` | JP/EN landing | user clicks demo section link |
| `guide_intro_click` | JP/EN landing | user clicks external-subtitle guide |
| `trial_guide_click` | JP/EN guide | user clicks Trial link to landing pricing anchor |

Keep page path for Japanese/English separation. Never collect custom properties containing URL query strings or fragments. Do not use download clicks as confirmed MSI downloads, checkout clicks as sales, or MSI download_count as distinct people. Official GitHub Release asset counters and Polar verified sales remain independent sources.

## Pre-activation gates
1. Owner selects analytics provider, creates the project and confirms the provider-provided site ID; no secret API key is to be committed.
2. Confirm provider's current privacy and retention policies, data residency, EU/UK/Japan consent applicability and any DPA requirements. A cookie-free tool alone does not guarantee consent exemption.
3. Amend `privacy.html` and `en/privacy.html` together before any collector is loaded: provider, purposes, collected technical data and interactions, transfer/location, retention, controls/contact, links to vendor privacy; update `README.md` 'no trackers/no JavaScript' claim accurately.
4. Add one defer-loaded official analytics script to each tracked page, using configured site ID. No third-party script on checkout nor in the Windows app. No auto-loading YouTube embeds.
5. Tests: validate HTML, expected marker counts (7 JP + 7 EN + 1 JP guide + 1 EN guide = 16), no changes to href or localized copy, no console errors, mobile/desktop navigability, disabled/ad-blocked script fallback, manual event test and dashboard verification in separate browser sessions.
6. Verify no PII or secrets in emitted payloads; documented opt-out/consent handling if needed. Exclude own tests from production metrics when provider supports it.
7. Obtain explicit human authorization before merging or deploying. Existing site and purchasing journey must remain available.

## Weekly reporting
Use Search Console for organic impressions/clicks, provider for page views/visits and CTA click counts, GitHub **maguwaidog/DiscCue-Releases** for per-version MSI asset download_count, YouTube for video performance, and Polar for completed sales. Maintain date windows, report snapshot timestamps, source, previous cumulative, current cumulative and deltas. Distinguish unique visitors, event clicks, actual downloads and sales. Never calculate cross-source funnel conversion rates without cohort/session alignment.

## Rollback
Remove the injected collector scripts first; inert event attributes can be removed separately. Update privacy statements to accurately reflect active data processing and any continued data retention.
