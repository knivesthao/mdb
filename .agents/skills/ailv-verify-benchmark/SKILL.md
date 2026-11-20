---
name: ailv-verify-benchmark
description: "Savings nobody measured are marketing; one protocol turns claims into numbers."
---

# Measure the task, not the skill

`ailv-verify-benchmark` (Measure the task, not the skill): Prove savings with a with/without trial on a real task: run it once with only matched skills installed, once with the whole bank, once with no skills. Record tokens burned, wall time, and defect count per run; report all three, never tokens alone. Match the task first with the bank map — the no-skills run still follows the plan rules (inline if five steps or fewer, file if longer). Publish the method and the raw numbers with the result; a claim without both is marketing. Log which skills and fields were fetched per step (skill id plus fields= value), so repeat reads can move to slim fields and totals stay auditable. Log defects in defects[], never only in gaps: a defect described only in prose did not happen for tally purposes. Reconcile before rendering: assert rendered row count equals the log's row count and rendered totals equal recomputed sums; keep a self-referential final row out of the same pass — tally before appending it, or exclude it from the title claim.

## Checks

- with/without/no-skill trial run
- tokens, time, defects all reported
- method plus raw numbers published
- fetched skill fields logged per step
- rendered totals reconciled against the log before publishing
