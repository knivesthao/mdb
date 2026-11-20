---
name: ailv-verify-scope
description: "A full suite per typo burns minutes for zero new proof — scope the run, keep the gate."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Match the check to the change

`ailv-verify-scope` (Match the check to the change): Match the verification to the change, never the habit. Behavior changes (endpoints, payments, webhooks, skills, tests) earn the full suite, once, after the final edit. Words and styling earn the fast path: a syntax check plus a smoke test of the touched route — no suite boot for copy. A fast path never weakens the gate: the repo's declared checks still run before ship, and anything the fast path cannot observe (script behavior, visual layout) goes to real eyes or the suite, never assumed. When unsure which lane a change belongs in, run the full suite — doubt means behavior.

## Checks

- behavior changes earn the full suite once
- words and styling earn syntax plus smoke
- fast path never skips the ship gate
- doubt runs the full suite
