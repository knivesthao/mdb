---
name: ailv-code-search
description: "Unscoped search leaks across customers; LIKE queries are the prototype, not the ship."
sources:
  - title: Typesense docs
    url: https://typesense.org/docs/
helper: scripts/helper.py
example: examples/output.md
---

# Tenant-scoped, ranked, typo-tolerant

`ailv-code-search` (Tenant-scoped, ranked, typo-tolerant): Scope every query by tenant first — unscoped search leaks across customers. Rank by relevance, not recency; maintain the index on writes, never with a nightly rebuild the product outgrows. Typo tolerance and filters are table stakes. Log dead searches — they are the roadmap.

## Checks

- tenant scoped, never global
- ranked, typo-tolerant
- index maintained on writes
