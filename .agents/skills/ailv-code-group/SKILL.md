---
name: ailv-code-group
description: "One folder holds the whole component, so the agent reads once instead of hunting across layers."
sources:
  - title: Screaming Architecture
    url: https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html
helper: scripts/helper.py
example: examples/output.md
---

# Group by feature, drop the layers

`ailv-code-group` (Group by feature, drop the layers): Organize new code by feature, not by layer: a component's files sit together — checkout_routes.py, checkout_models.py, checkout_tests.py — named <feature>_<kind> so everything is found in one place. Keep model/view/controller separation inside the folder, not across the codebase. Put truly shared definitions (shared contracts) in one shared module every feature imports. If the codebase already uses a pattern like MVC, follow that pattern instead: restructuring working code costs tokens and every move risks new errors.

## Checks

- feature files sit together
- shared facts live in one module
- existing pattern followed over rewrites
