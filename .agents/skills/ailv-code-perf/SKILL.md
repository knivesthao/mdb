---
name: ailv-code-perf
description: "Users feel milliseconds and megabytes; everything else is invisible."
sources:
  - title: web.dev on LCP
    url: https://web.dev/articles/lcp
helper: scripts/helper.py
example: examples/output.md
---

# Fast by budget

`ailv-code-perf` (Fast by budget): Set a budget first: page weight, endpoint milliseconds, query count — then measure before changing anything. Page budgets name user-centric milestones (first paint, interactive), not just bytes — quantity metrics alone never capture felt speed. Cache first (see ailv-code-cache): repeated work should never recompute. Shrink the payload: paginate lists, select only needed columns, compress images, ship less JavaScript. Push heavy work out of the request into background jobs (see ailv-code-async for the handoff), and turn N+1 reads into single joined or batched reads on indexed columns. Re-measure after every change; speed you can't see is a guess.

## Checks

- budgets set before optimizing
- repeat work cached, not recomputed
- N+1 reads batched or joined
