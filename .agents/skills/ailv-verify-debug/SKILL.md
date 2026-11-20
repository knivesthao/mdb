---
name: ailv-verify-debug
description: "A wrong agent needs a debugger, not a re-read; bisect the run to the guilty step."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Diagnose the run, not the intent

`ailv-verify-debug` (Diagnose the run, not the intent): When the output is wrong, reproduce first with the smallest input that still fails. Bisect the plan: re-run steps in order against their done-states until one lies — the guilty step is the first whose output fails its check. Read receipts, samples, and drill records, never the agent's explanation of what it meant. Fix the step, not the plan; if two steps disagree, the contract between them is the bug. Record the failure shape so the next run recognizes it.

## Checks

- smallest failing input reproduced
- guilty step bisected by done-state
- contract fixed when steps disagree
