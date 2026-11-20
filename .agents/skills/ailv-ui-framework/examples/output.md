# ailv-ui-framework — worked example

Input: one Lit island (pinned CDN, light DOM) plus one HTMX static region targeting a plain div.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: no build step (pinned Lit CDN module)
PASS: hx-target never targets an island
PASS: light DOM (createRenderRoot returns this)
PASS: no React/Angular imports
PASS: islands tap-reachable (button inside island)
demo: 1 Lit island + HTMX static region -> islands-ok
```
