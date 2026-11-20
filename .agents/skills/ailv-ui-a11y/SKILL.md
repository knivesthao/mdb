---
name: ailv-ui-a11y
description: "Contrast ratios are the beginning of accessibility, not the end."
sources:
  - title: WCAG overview
    url: https://www.w3.org/WAI/standards-guidelines/wcag/
  - title: axe-core
    url: https://github.com/dequelabs/axe-core
  - title: MDN prefers-reduced-motion
    url: https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
helper: scripts/helper.py
example: examples/output.md
---

# Audit with keyboard, ears, motion off

`ailv-ui-a11y` (Audit with keyboard, ears, motion off): Walk every flow keyboard-only: tab order matches visual order, every control reachable and operable, focus always visible, traps only where intended with escape hatches. Run a screen-reader pass on each template: landmarks set, headings in order, live regions announce state changes, charts expose their data twin. Honor reduced motion fully — no essential animation without a static equivalent. Audit on a schedule, not once.

## Checks

- keyboard-only walkthrough passes
- screen-reader pass per template
- reduced motion fully honored
