---
name: ailv-ui-tokens
description: "Fixing palette and spacing to tokens removes an entire category of per-element decisions."
sources:
  - title: Apple Human Interface Guidelines
    url: https://developer.apple.com/design/human-interface-guidelines
  - title: Material Design 3
    url: https://m3.material.io
helper: scripts/helper.py
example: examples/output.md
---

# Tokens + Tailwind

`ailv-ui-tokens` (Tokens + Tailwind): Style with Tailwind utilities for layout and spacing, on top of three color tokens (--ink, --paper, --accent) and a 4/8/16/32 scale. Keep preflight on as the consistent baseline — describe every margin, bullet, and underline explicitly, never rely on browser defaults. Two neutrals plus one accent, 1px borders, radii 6px/10px. Contrast >= 4.5:1 so the human eyeball verdict works. Color with meaning and measure: green confirms, red destroys or errors, blue informs — never subvert these. Hold roughly 60% neutral background, 30% structure and text, 10% high-contrast accent on interactive elements only. Layer tokens: raw option palettes stay private, decisions (accent, text) and component tokens are what code reads (Fowler, Material).  If the project already uses a different design system, do not create this skill at all — skip it. Theme with tokens, not branches: dark mode rides inverted tokens (same names, swapped values) behind prefers-color-scheme — never a second stylesheet, never color literals in components. Scale down, never break: the 4/8/16/32 spacing holds at 360px, and every interactive element offers at least a 44px touch target.

## Checks

- palette is 3 colors max
- no per-element color decisions
- contrast >= 4.5:1
- prose lines stay within 45–75 characters
- spacing scale holds and touch targets reach 44px at 360px
