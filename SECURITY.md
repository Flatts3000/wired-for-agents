# Security Policy

## Scope

This repository publishes a badge, its SVG assets, and a written specification.
It is a static site with no backend, no database, and no user accounts, so the
realistic attack surface is narrow. The things worth reporting:

- **Asset tampering or supply-chain risk.** The SVGs are hot-linked directly by
  third-party sites. Anything that could cause a malicious payload to be served
  from a badge URL is the highest-severity issue this project can have. SVG is an
  active format; script content, external references, or `foreignObject` in a
  published asset are all bugs.
- **Header or CORS misconfiguration** in `vercel.json` that weakens the sites
  embedding the badge.
- **Specification flaws** where a criterion in `SPEC.md` could be satisfied by an
  implementation that is not actually safe to expose to agents, or where meeting
  the criteria would push an adopter toward an insecure configuration.
- **Redirect or domain issues** across `wiredforagents.com` and
  `wiredforagents.dev`.

## Reporting a vulnerability

Please use **GitHub Private Vulnerability Reporting** on this repository
(Security tab, "Report a vulnerability"). That keeps the report private until a
fix ships.

Do not open a public issue for a vulnerability.

Expect an acknowledgement within 7 days. Because embedded badge assets affect
third-party sites, asset-integrity reports are triaged first.

## Supported versions

The specification is versioned (see `SPEC.md`). Only the latest published
version of the spec and the currently deployed assets are supported.

## A note on the badge itself

Version 1 of this badge is **self-asserted**. Anyone can copy the SVG onto a site
that does not meet the criteria. That is a known and accepted property of v1, not
a vulnerability. The verified program that would close it is future work, tracked
in the project handoff.
