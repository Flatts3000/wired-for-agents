#!/usr/bin/env python3
"""Render SPEC.md into spec.html using the site's visual language.

SPEC.md remains the single source of truth. spec.html is GENERATED - never edit
it by hand. Re-run this after any change to SPEC.md:

    python tools/build_spec.py

The output is committed so the site keeps its zero-build deploy on Vercel.
"""
import pathlib
import re
import sys

import markdown

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "SPEC.md"
OUT = ROOT / "spec.html"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Specification - Wired for Agents</title>
<meta name="description" content="The versioned Wired for Agents specification: WFA-1 documented API, WFA-2 MCP server, WFA-3 programmatic auth, WFA-4 machine discovery.">
<link rel="canonical" href="https://wiredforagents.com/spec">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Wired for Agents">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="Specification - Wired for Agents">
<meta property="og:description" content="Four criteria certifying that a product has programmatic doors. Each verifiable by an agent in under 60 seconds.">
<meta property="og:url" content="https://wiredforagents.com/spec">
<meta property="og:image" content="https://wiredforagents.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Wired for Agents: API + MCP">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://wiredforagents.com/og.png">
<meta name="theme-color" content="#0E1216">
<style>
  :root{{
    --ink:#0E1216; --ink-2:#151C23; --accent:#3DDC97; --accent-2:#56E1FF;
    --txt:#EAF0F2; --muted:#8B98A3; --line:rgba(255,255,255,.13);
    --mono:ui-monospace,"JetBrains Mono",Menlo,Consolas,monospace;
    --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  }}
  *{{box-sizing:border-box}}
  body{{
    margin:0; background:var(--ink); color:var(--txt); font-family:var(--sans);
    line-height:1.65; -webkit-font-smoothing:antialiased;
  }}
  .wrap{{max-width:760px; margin:0 auto; padding:0 24px 96px}}
  a{{color:var(--accent)}}
  a:hover{{text-decoration:underline}}
  :focus-visible{{outline:2px solid var(--accent-2); outline-offset:3px; border-radius:4px}}
  .skip{{
    position:absolute; left:-9999px; top:8px; z-index:10; background:var(--ink-2);
    color:var(--txt); border:1px solid var(--accent); border-radius:8px;
    padding:10px 16px; font-family:var(--mono); font-size:13px;
  }}
  .skip:focus{{left:24px}}
  .topbar{{
    display:flex; align-items:center; justify-content:space-between; gap:16px;
    padding:24px 0 40px; flex-wrap:wrap;
  }}
  .topbar a{{
    font-family:var(--mono); font-size:12px; letter-spacing:.12em;
    text-transform:uppercase; text-decoration:none; display:inline-block; padding:4px 2px;
  }}
  h1{{
    font-family:var(--mono); font-size:clamp(26px,5vw,38px); font-weight:700;
    letter-spacing:.01em; line-height:1.15; margin:0 0 8px;
  }}
  h2{{
    font-family:var(--mono); font-size:15px; font-weight:700; letter-spacing:.14em;
    text-transform:uppercase; color:var(--muted);
    margin:56px 0 14px; padding-top:24px; border-top:1px solid var(--line);
  }}
  h3{{font-size:19px; margin:36px 0 8px; font-weight:650}}
  h4{{
    font-family:var(--mono); font-size:13px; letter-spacing:.06em;
    color:var(--accent); margin:24px 0 6px;
  }}
  p,li{{color:#C7D1D6}}
  strong{{color:var(--txt)}}
  blockquote{{
    margin:20px 0; padding:2px 0 2px 18px; border-left:2px solid var(--line);
    color:var(--muted);
  }}
  code{{
    font-family:var(--mono); font-size:.88em; background:var(--ink-2);
    border:1px solid var(--line); border-radius:5px; padding:1px 5px; color:var(--txt);
  }}
  pre{{
    background:var(--ink-2); border:1px solid var(--line); border-radius:12px;
    padding:16px; overflow-x:auto; margin:20px 0;
  }}
  pre:focus-visible{{outline:2px solid var(--accent-2); outline-offset:3px}}
  pre code{{background:none; border:0; padding:0; font-size:12.5px; white-space:pre}}
  hr{{border:0; border-top:1px solid var(--line); margin:48px 0}}
  /* SPEC.md uses --- before most section headings; the h2 already draws a rule,
     so collapse the pair instead of rendering two lines. */
  hr + h2{{border-top:0; padding-top:0; margin-top:28px}}
  hr:has(+ h2){{display:none}}
  table{{border-collapse:collapse; width:100%; margin:20px 0; font-size:15px}}
  th,td{{border:1px solid var(--line); padding:9px 12px; text-align:left}}
  th{{font-family:var(--mono); font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted)}}
  ul,ol{{padding-left:22px}}
  li{{margin:5px 0}}
  footer{{
    border-top:1px solid var(--line); margin-top:64px; padding-top:28px;
    color:var(--muted); font-size:13px; display:flex; gap:16px;
    justify-content:space-between; flex-wrap:wrap;
  }}
  footer a{{display:inline-block; padding:4px 2px}}
  @media (prefers-reduced-motion:reduce){{*{{transition:none!important}}}}
</style>
</head>
<body>
<a class="skip" href="#content">Skip to the specification</a>
<div class="wrap">
  <nav class="topbar">
    <a href="/">&#8592; Wired for Agents</a>
    <a href="https://github.com/Flatts3000/wired-for-agents/blob/main/SPEC.md">Source on GitHub</a>
  </nav>
  <main id="content">
{body}
  </main>
  <footer>
    <span>Generated from <code>SPEC.md</code>, the versioned source of truth.</span>
    <span><a href="/">Home</a> &middot; <a href="/llms.txt">llms.txt</a></span>
  </footer>
</div>
</body>
</html>
"""


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1

    text = SRC.read_text(encoding="utf-8")

    # The page supplies its own <h1> chrome; drop the document's leading title
    # line so the rendered page has exactly one h1.
    text = re.sub(r"^# .*?\n", "", text, count=1)

    html = markdown.markdown(
        text,
        extensions=["extra", "sane_lists", "toc"],
        output_format="html5",
    )

    # Scrollable code blocks must be reachable by keyboard (WCAG 2.1.1).
    html = html.replace("<pre>", '<pre tabindex="0" role="region" aria-label="Code sample, scrollable">')

    heading = (
        '<h1>Wired for Agents<br><span style="color:var(--muted);'
        'font-size:.62em">Specification</span></h1>\n'
    )
    page = TEMPLATE.format(body=heading + html)
    OUT.write_text(page, encoding="utf-8")

    print(f"  wrote {OUT.relative_to(ROOT)}  ({len(page) / 1024:.1f} KB)")
    print(f"  h1 count: {page.count('<h1')}   pre blocks: {page.count('<pre')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
