---
name: ailv-verify-visual
description: "A screenshot settles in one glance what no code review can prove about a UI."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Visual confirmation

`ailv-verify-visual` (Visual confirmation): Humans judge UI by looking. Every screen needs a settled screenshot state with real data (no lorem, no empty list), shot twice: desktop and 360px phone width — most sessions arrive on a phone. List the 3 things to eyeball: layout, labels, error state. Save verification screenshots to the project's shots/ folder (gitignored), named for what they show — never /tmp. Never trust a headless screenshot alone: use it for a quick first look only, and treat a real browser or the user's own screenshot as proof; when they disagree, believe the user's screen. If it cannot be seen, it does not ship.

## Checks

- seeded demo data present
- 3 eyeball items listed
- error state visible
- desktop and 360px shots saved
