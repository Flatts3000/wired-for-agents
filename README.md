# WIRED FOR AGENTS

**A vendor-neutral badge and mini-standard for the agentic web.**

It tells a human or an AI agent one thing at a glance: this product can be
discovered, read, and acted on programmatically, via a documented API and an MCP
server. Not a screen an agent scrapes. Doors that were built for it.

> **Status: in development.** The domains are registered and the specification is
> being written. The badge assets and landing page are not deployed yet, so the
> embed snippet below does not resolve. Watch this repo.

## What earns the mark

A product must meet **all four** criteria. Each is objective and verifiable by an
agent in under a minute, which is deliberate: it is what makes automated
verification possible later.

| Code | Criterion | |
|---|---|---|
| **WFA-1** | **Documented API** | A public, versioned REST API with a machine-readable OpenAPI spec at a known URL. |
| **WFA-2** | **MCP server** | A Model Context Protocol server exposing the same capabilities as first-class agent tools. |
| **WFA-3** | **Programmatic auth** | Scoped API keys or tokens built for machine access. No human-in-the-loop login required to get in. |
| **WFA-4** | **Machine discovery** | An agent can find the doors on its own: `llms.txt`, `/.well-known`, a linked OpenAPI document. |

Precise, testable definitions live in [`SPEC.md`](./SPEC.md), which is the
versioned source of truth. This README restates them for convenience; if the two
ever disagree, the spec wins.

## This is not a readability score

Several existing tools check whether an agent can *read* your site: whether you
serve markdown, publish `llms.txt`, or survive a crawl. Useful, and different from
this.

WIRED FOR AGENTS certifies a higher bar: that your product has **programmatic
doors**. An agent should not have to read your site at all. It should be able to
call you.

## Using the badge

Once the assets are live, one line in your footer:

```html
<a href="https://wiredforagents.com">
  <img src="https://wiredforagents.com/badge.svg" alt="Wired for Agents: API + MCP" height="40">
</a>
```

Variants will ship at stable URLs: primary dark and light, a compact cut, a
monochrome cut that inherits `currentColor`, and a seal for trust bars.

## Honesty about v1

This badge is **self-asserted**. Meeting the four criteria is on you, and nothing
currently stops a site that does not meet them from pasting the SVG. That is the
same trust model as "Works with" marks, and it is stated plainly rather than
implied.

Because the criteria are objectively checkable, the badge can graduate into a
verified program without changing the art: a published manifest, a crawler, and
per-domain badges reflecting live status. That happens if and when v1 earns the
demand for it.

## License

[MIT](./LICENSE). Note that a permissive license on the art is consistent with a
self-asserted v1: you can copy the badge, and the honest answer is that meeting
the criteria is what makes displaying it true.

## Security

See [SECURITY.md](./SECURITY.md). Because the SVGs are hot-linked by other sites,
asset-integrity issues are the highest-severity reports this project can receive.
