# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Current state

**Live at https://wiredforagents.com.** The landing page, `/spec`, all six badge cuts,
`og.png`, `robots.txt`, `sitemap.xml`, `llms.txt`, and `.well-known/security.txt` are
deployed. `wiredforagents.dev` and `www` 308 to the apex.

There is no package manifest, no build system, and no test suite, and that is deliberate
rather than an omission. Do not invent a toolchain. v1 is a zero-build static site: plain
HTML plus SVG, deployed to Vercel. If a task seems to want npm/Next.js/a bundler, that is
a scope change - raise it rather than introducing one.

**One exception:** `spec.html` is GENERATED from `SPEC.md` by `tools/build_spec.py`. Never
hand-edit `spec.html`. Edit `SPEC.md`, re-run `python tools/build_spec.py`, and commit
both. The generated output is committed precisely so Vercel still deploys with zero build.

Deploys currently run via `vercel deploy --prod --yes`. Push-to-deploy is not wired up
until the Vercel GitHub App is granted access to the repo.

> **A build spec exists at `docs/handoff.md` but is gitignored and local-only.** If you
> have it, read it first: it carries the locked decisions, canonical SVG source, file
> layout, and open blockers. If you are working from a clone and it is absent, this file
> plus `SPEC.md` and `README.md` are authoritative, and you should ask before inferring
> intent about anything they do not cover.

## What this project is

WIRED FOR AGENTS is a vendor-neutral badge plus mini-standard asserting that a product
can be discovered and **acted on programmatically** - proof line `API + MCP`. It is a
standalone shared brand asset: one host, one stable asset URL, embedded via a single
`<img>` footer line across several independent properties. Update the art once, every
consumer site updates.

Two consequences drive most decisions:

- **Asset URLs are a public contract.** `badge.svg` and its variants are hot-linked from
  other origins. Filenames and dimensions are stable, `vercel.json` must serve them with
  long cache headers and `Access-Control-Allow-Origin: *`, and renaming or restructuring
  an asset breaks live third-party pages.
- **The badge is only worth its criteria.** WFA-1 (documented API + OpenAPI), WFA-2 (MCP
  server), WFA-3 (programmatic scoped auth), WFA-4 (machine discovery). Each was chosen
  to be objectively verifiable in under a minute, because v2 turns this into an automated
  verifier issuing dynamic per-domain badges. Keep every criterion mechanically checkable;
  a criterion a crawler cannot test undermines the whole roadmap.

`SPEC.md` is the versioned source of truth for the criteria (starting at v0.1) and is the
file that must change, with a changelog entry, whenever a criterion moves. `index.html`
and `README.md` restate the criteria and must not drift from it.

## This is a capability badge, not a readability score

The nearby tools in this space check whether an agent can *read* a site: markdown
responses, `llms.txt`, crawlability. This certifies a stricter and different thing, that
programmatic **doors** exist and an agent can call them without reading the site at all.

**Never describe this project as a readiness, readability, or maturity score.** That
framing collapses it into an adjacent category it deliberately does not belong to, and
the distinction is the reason the project exists.

Related: the project was renamed on 2026-07-25 and the criteria codes moved from `AR-n`
to `WFA-n`. Any draft, write-up, or prototype predating that date carries the old name
and codes. Lift such a prototype's geometry, palette, and layout; never its text.

## Visual identity

Accent `#3DDC97` spring green over near-black `#0E1216`, with cyan `#56E1FF` used
sparingly. Monospace for the wordmark and data is a deliberate protocol/terminal choice,
not a fallback. The landing page commits to dark only; the *badge assets* ship in both
light and dark cuts because they land on host pages of unknown theme.

The mark's geometry - hexagon node, checkmark drawn as a routing line between two
endpoint dots, live status dot on the top vertex - is load-bearing meaning, not
decoration. It reads simultaneously as a check and as two connected endpoints. Reproduce
it from the canonical source rather than redrawing it.

The primary badge plate is **216x56** (compact 180x48, seal 150x150). Two constraints
travel together and must not be changed independently:

- The wordmark carries `textLength="131.5" lengthAdjust="spacingAndGlyphs"`. SVG text
  cannot be measured before render and the host page's monospace fallback is unknowable,
  so without this pin a wide fallback overflows the plate on someone else's site, silently.
- The plate width is derived from that pinned wordmark: it ends at 199.5, the left margin
  is 15, so 216 yields a matching 16.5 right margin.

Change the wordmark text, size, or letter-spacing and both values are invalid. Re-measure
in a browser and update them together.

**The mono cut must be inlined.** `currentColor` does not cross an `<img>` boundary; an
SVG loaded that way is an isolated document, so `badge-mono.svg` used as `<img>` renders
black on black. Inline it or use a colored cut.

## Outward actions require confirmation

Deploying to Vercel, DNS changes, publishing releases, and adding the footer badge to
live properties are outward-facing. Scaffold and commit locally as needed; confirm before
anything ships. Note that badge assets, once embedded by a third party, are effectively
permanent - treat the first deploy of an asset URL as a commitment.
