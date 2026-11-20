---
name: ailv-ui-nav
description: "Links stay one tap away on phones, inline on desktop."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Responsive headers

`ailv-ui-nav` (Responsive headers): Put the brand on its own centered row. Show inline links on wide screens; below about 640px collapse them behind a Menu button (Flowbite collapse toggle) that opens a stacked list — the links stay in the DOM on every breakpoint, one tap away on phones, since most visitors arrive on mobile. Use a real nav landmark, mark the current page with aria-current, and let the toggle flip aria-expanded. No hand-written menu code, keyboard reachable.

## Checks

- inline links on wide screens, Menu button below ~640px
- links in the DOM on every breakpoint, stacked when open
- aria-current marks the page, aria-expanded flips on toggle
