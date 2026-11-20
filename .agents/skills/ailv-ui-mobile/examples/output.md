# ailv-ui-mobile — worked example

Input: server-rendered cart fragment (HTMX button + count span, viewport meta, narrow container).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: zero hand-written fetch calls
PASS: no client-side state store
PASS: htmx drives interaction
PASS: layout verified at 360px (viewport + narrow container)
demo: server-rendered fragment, no fetch, no store -> mobile-ready
```
