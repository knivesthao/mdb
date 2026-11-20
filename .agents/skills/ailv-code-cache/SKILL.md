---
name: ailv-code-cache
description: "A cache hit skips work entirely — the cheapest token is the one never spent."
sources:
  - title: MDN HTTP caching
    url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching
  - title: Redis docs
    url: https://redis.io/docs/latest/
helper: scripts/helper.py
example: examples/output.md
---

# Cache in layers, swap the store

`ailv-code-cache` (Cache in layers, swap the store): Cache in layers, nearest first: HTTP (ETag plus 304, Cache-Control per content type), in-process memo for hot reads, CDN edge in front. Hide every layer behind one tiny interface — get, set, invalidate — so the store swaps without touching callers: memory today, Redis or Memcached tomorrow. Cache computed answers, never user-specific secrets. Invalidate on write (data changed), not on a timer alone.

## Checks

- ETag and 304 on repeat reads
- one interface, swappable store
- invalidation tied to writes
