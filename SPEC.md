# WIRED FOR AGENTS - Specification

**Version 0.1** (draft) | Last updated 2026-07-25

This document is the versioned source of truth for what earns the WIRED FOR AGENTS
badge. Where the README, the landing page, or any other restatement disagrees with
this file, this file wins.

---

## 0. What this certifies

A product displaying this badge asserts that an AI agent can **call it**, not merely
read it.

That distinction is the whole specification. Publishing markdown, an `llms.txt`, or a
crawlable DOM makes a site *legible* to agents. This badge is about a stricter property:
that documented, authenticated, machine-callable interfaces exist, and that an agent can
find them without a human.

A product either has those doors or it does not. There is no score and no maturity level.

### Design constraint

Every criterion below is written so that an unattended agent can verify it from the
public internet, given only a domain name, in **under 60 seconds**. That constraint is
deliberate: it is what allows the self-asserted v1 badge to graduate into an automated
verified program (Section 3) without the criteria changing.

If a proposed criterion cannot be mechanically tested, it does not belong in this spec.

---

## 1. The criteria

A product must meet **all four**. Partial compliance does not earn the mark.

### WFA-1 - Documented API

A public, versioned HTTP API described by a machine-readable OpenAPI document.

**Requirements**
1. The API is reachable over HTTPS on a public hostname.
2. It is explicitly versioned, in the path (`/api/v1/...`) or via a documented header.
3. An OpenAPI 3.x document is served at a stable, publicly fetchable URL, with no
   authentication required **to read the document itself**.
4. The document is valid OpenAPI, parses without error, and describes the API actually
   being served, including at least one operation an agent can call.
5. It is served as JSON or YAML with a sensible content type.

**How to verify**
```
GET https://<host>/openapi.json      -> 200, parses as OpenAPI 3.x
```
Any stable documented path is acceptable. The document must be discoverable by WFA-4.

**Does not qualify:** human-only HTML documentation; a Postman collection alone; an
OpenAPI file behind a login; a spec that has drifted from the live API.

---

### WFA-2 - MCP server

A Model Context Protocol server exposing the product's capabilities as first-class agent
tools.

**Requirements**
1. A reachable MCP endpoint, over a documented transport.
2. It completes the MCP initialization handshake and responds to tool discovery with at
   least one tool.
3. Tools carry names, descriptions, and input schemas sufficient for an agent to call
   them without out-of-band knowledge.
4. The exposed capabilities **meaningfully overlap the API surface** from WFA-1. An MCP
   server exposing only a token trivial tool while the real functionality stays
   API-locked does not satisfy this.
5. The endpoint is documented at a public URL.

**How to verify**
```
initialize -> tools/list      -> at least one tool, each with a valid input schema
```

**Does not qualify:** a planned or beta-waitlist MCP server; an internal-only endpoint;
a tools list that fails schema validation.

---

### WFA-3 - Programmatic auth

Credentials designed for machines, obtainable and usable without a human in the loop at
call time.

**Requirements**
1. Machine credentials exist: API keys, OAuth client-credentials tokens, or equivalent.
2. They are presented programmatically, in a header or standard auth flow. No session
   cookie harvested from a browser login.
3. They are **scoped**: permissions can be limited to less than the full account, and the
   available scopes are documented.
4. They are revocable independently of the owner's primary password.
5. Issuance is documented. A human may create the key once; **calls must not require
   per-request human interaction.**

**How to verify:** documented credential issuance, documented scopes, and an
authenticated call succeeding with a header-presented credential.

**Does not qualify:** scraping a session cookie; credentials only issued via a sales
conversation with no documented process; all-or-nothing tokens with no scoping; auth that
requires an interactive consent screen on every call.

> A public, genuinely unauthenticated read API satisfies WFA-3 for its public surface,
> provided that is documented as intentional. The criterion tests that machine access is
> designed for, not that a gate exists.

---

### WFA-4 - Machine discovery

An agent starting from nothing but the domain can find the doors on its own.

**Requirements**

At least one of:
- `/.well-known/wired-for-agents.json` (see Section 4), or
- an `/llms.txt` that links the OpenAPI document and the MCP endpoint, or
- a `<link>` relation or documented, stable, conventionally located OpenAPI URL.

And in all cases:
1. Discovery requires **no authentication**.
2. Every URL it advertises resolves. A manifest pointing at a 404 fails this criterion
   outright.
3. The advertised URLs are absolute or unambiguously resolvable.

**How to verify:** fetch the discovery surface from the bare domain, follow every URL it
advertises, confirm each resolves and matches its claim.

**Does not qualify:** documentation findable only via site search or a marketing nav;
endpoints published only in a PDF or a blog post; a manifest with stale URLs.

---

## 2. How to self-assert

Version 1 of this badge is **self-asserted**. There is no registry, no application, and
no gatekeeper.

1. Confirm you meet WFA-1 through WFA-4. Verify them the way an agent would, from outside
   your network, unauthenticated where the criteria say unauthenticated.
2. Embed the badge, linking to `https://wiredforagents.com`.
3. Recommended: publish `/.well-known/wired-for-agents.json` (Section 4). It costs
   minutes and makes you verifiable the moment the verified program exists.

**Be honest.** Nothing technically stops a non-qualifying site from displaying the badge.
That is a known property of a self-asserted mark, stated plainly rather than implied. The
mark is worth exactly what its wearers' honesty makes it worth, and the criteria are
public and checkable precisely so that a false claim is cheap for anyone to disprove.

---

## 3. Roadmap to verified

The criteria above were written to be mechanically testable, which lets this graduate
without changing the art or the standard:

- **Manifest convention** - `/.well-known/wired-for-agents.json`, already specified below.
- **Verifier** - fetches a candidate domain, evaluates WFA-1 through WFA-4, publishes the
  result.
- **Dynamic badges** - a shields-style endpoint reflecting live status per domain.

This happens only if the self-asserted badge earns demand for it. Until then, the manifest
is optional and the badge means what Section 2 says it means.

---

## 4. `/.well-known/wired-for-agents.json` (optional in v0.1)

```json
{
  "wiredForAgents": "0.1",
  "openapi": "https://example.com/api/v1/openapi.json",
  "mcp": {
    "endpoint": "https://mcp.example.com",
    "transport": "streamable-http"
  },
  "auth": {
    "type": "api-key",
    "docs": "https://example.com/docs/authentication",
    "scoped": true
  },
  "discovery": ["https://example.com/llms.txt"],
  "contact": "api@example.com"
}
```

Served as `application/json`, unauthenticated, with permissive CORS. Every URL it
advertises must resolve.

---

## 5. Changelog

### v0.1 - 2026-07-25
Initial draft. Establishes WFA-1 through WFA-4, the under-60-seconds verifiability
constraint, the self-assertion model, and the optional `.well-known` manifest.

> Criteria were previously drafted under the codes `AR-1` through `AR-4`. Those codes are
> retired; any document using them predates 2026-07-25.
