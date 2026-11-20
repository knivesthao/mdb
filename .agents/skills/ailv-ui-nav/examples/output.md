# ailv-ui-nav — worked example

Input: brand row + nav landmark with 2 links (Home `aria-current="page"`, Shop) and a Menu toggle.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Output:

```text
PASS: brand on its own row
PASS: real nav landmark
PASS: links in DOM (not JS-injected)
PASS: aria-current marks the page
PASS: toggle flips aria-expanded
PASS: no hand-written menu code (flowbite collapse)
demo nav: brand row + 2 links, Menu toggle narrow -> nav-ok
```
