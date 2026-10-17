# ZQM brand and README conventions

This is a practical default for new and refreshed repositories. It is a consistency guide, not a claim that every repository has already adopted it.

## Brand families

- **ZQM Labs:** cream `#fff7ea`, ink `#2b2118`, orange `#e07b24`, evergreen/night-sky accents. Use for games, community experiences, and studio resources.
- **ZQM Computing:** dark navy, cyan/teal, and mint with restrained topographic/grid motifs. Use for geospatial engineering, scientific computing, and infrastructure patterns.
- **Dr. Z:** cinematic laboratory imagery and analog/scientific motifs. Use as a character/brand ambassador in selected landing pages and campaign artwork; do not replace technical diagrams, maps, or project-specific visualizations with character art.

Avoid combining all palettes in one interface. Keep each repository's purpose immediately legible.

## Asset rules

- Prefer self-hosted SVG for simple scalable marks, banners, diagrams, and decorative line art. Use raster formats for photographic artwork.
- Recommended profile banner canvas: `1200×320` (or another documented fixed aspect ratio). Game/website hero art may use `1200×340`; preserve its aspect ratio responsively.
- Recommended standalone mark canvas: `512×512`.
- Include `<title>` and `<desc>` in SVGs where meaningful, use descriptive alt text for informative images, and empty alt text for purely decorative images.
- Keep documentation-only art under `docs/assets/` or another clearly documented docs path. Do not place it under runtime asset folders such as `assets/img/` if tests or service-worker manifests treat those paths as deployable game assets.
- Never add documentation-only art to an offline precache just to satisfy a broad test. Refine the test's scope or correct the path classification.
- Avoid embedded external fonts, external image hosts, unnecessary filters, and complex SVG effects that fail in common renderers.
- Check SVG XML well-formedness, explicit `viewBox`, intrinsic dimensions, clipping, contrast, and legibility at actual display widths (desktop and mobile). A successful parse is not a substitute for visual inspection.

## README structure

Recommended order:

1. Project name and one-sentence purpose.
2. Optional self-hosted banner with descriptive alt text.
3. Status: experimental, active, archived, or production-supported—only if accurate.
4. What it does and what it does not do.
5. Quick start with prerequisites and tested commands.
6. Verification: exact tests/builds actually run and their status.
7. Configuration, security/privacy, offline behavior, accessibility, and limitations where relevant.
8. Project map and links to directly related repositories or live resources.
9. License and contribution guidance.

Keep the README focused on that repository's purpose. A badge is useful only when it points to a real workflow or service and its status is meaningful. Remove stale, broken, or redundant badges; do not add coverage, release, deployment, or language badges without an authoritative source.

## Claims and cross-links

- Prefer verifiable descriptions: name the command, test, interface, file, or release that demonstrates the claim.
- Distinguish files present from capabilities verified. Locale files do not prove full translation; a service worker does not prove every flow works offline; a deployment workflow does not prove production health.
- Label plans, prototypes, imported project history, and archived/superseded repositories plainly.
- Link to the canonical implementation, public docs, issue tracker, or deployment. Avoid linking internal/private repositories from public marketing copy unless access and intent are explicitly appropriate.
- Check links when updating READMEs and do not imply that a related repo is maintained, secure, or production-ready solely because it exists.
- Preserve existing license notices and never imply all ZQM repositories share a license.

## Pull-request checklist

- [ ] Does the banner/mark belong to this brand family and repo purpose?
- [ ] Are all factual feature, maturity, localization, offline, security, and availability claims supported?
- [ ] Do all badges point to current workflows/services?
- [ ] Are cross-links valid, canonical, and appropriate for the repository's visibility?
- [ ] Is documentation-only artwork outside runtime/deployment asset inventories?
- [ ] Have applicable lint, test, build, link, and SVG checks been run?
- [ ] Is visual rendering checked at the actual target size and on mobile?
- [ ] Does the PR state what remains untested?
