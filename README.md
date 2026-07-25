# WIRED FOR AGENTS

**A vendor-neutral badge and mini-standard for the agentic web.**

It tells a human or an AI agent one thing at a glance: this product can be
discovered, read, and acted on programmatically, via a documented API and an MCP
server. Not a screen an agent scrapes. Doors that were built for it.

> **Status: live at [wiredforagents.com](https://wiredforagents.com).** Specification
> v0.1, badge assets, and landing page are all deployed. The embed snippets below
> resolve today. The badge is self-asserted; see the note at the bottom.

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

One line in your footer:

```html
<a href="https://wiredforagents.com">
  <img src="https://wiredforagents.com/badge.svg" alt="Wired for Agents: API + MCP" height="40">
</a>
```

| File | Size | Notes |
|---|---|---|
| `badge.svg` | 216x56 | Primary, dark |
| `badge-light.svg` | 216x56 | Primary, for light grounds |
| `badge-compact.svg` | 180x48 | Mark + wordmark, no proof line |
| `badge-mono.svg` | 216x56 | Single color, inherits `currentColor` |
| `seal.svg` | 150x150 | Emblem for trust bars and heroes |
| `favicon.svg` | 48x48 | The mark alone |

> **The monochrome cut must be inlined**, not loaded via `<img>`. An SVG in an
> `<img>` is an isolated document, so `currentColor` never reaches it and the badge
> renders black on black. Paste the file into your markup, or use a colored cut.

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
