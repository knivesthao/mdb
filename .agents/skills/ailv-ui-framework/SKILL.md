---
name: ailv-ui-framework
description: "Standard web components with no build step; every new interactive region starts as one."
sources:
  - title: Lit docs
    url: https://lit.dev/
  - title: Flowbite docs
    url: https://flowbite.com/docs/getting-started/introduction/
helper: scripts/helper.py
example: examples/output.md
---

# Islands first, house wins

`ailv-ui-framework` (Islands first, house wins): Default to Lit islands for interactive regions, loaded from the pinned Lit CDN module — no build step, no framework lock-in. Lit ships no ready-made pieces, so keep Flowbite for those (menu, dialog, dropdown) and never rebuild one just to own it; if an island needs pieces, use WebAwesome over CDN; never React or Angular. Render into the light DOM (never shadow) so utilities and icons keep working; HTMX never targets an island or anything inside one. Islands work the same on phones: no hover-only island behavior, everything reachable by tap, payloads kept small for mobile networks. If the codebase already uses another framework, do not create this skill at all — skip it. If the project already uses a different stack, overwrite this skill with that stack's equivalent and follow it instead.

## Checks

- no build step for components
- hx-target never targets an island
- light DOM so utilities keep working
- islands tap-reachable with small payloads on phones If the prescribed stack has no island runtime (no HTMX, no Lit), fall back to plain fetch plus server-rendered HTML — never hand-build a framework to replace one.
