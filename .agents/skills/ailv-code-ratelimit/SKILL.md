---
name: ailv-code-ratelimit
description: "An unthrottled endpoint is a counter-inflation and outage tool for anyone with a loop."
sources:
  - title: IETF RateLimit RFC 9339
    url: https://www.rfc-editor.org/rfc/rfc9339.html
helper: scripts/helper.py
example: examples/output.md
---

# Throttle the expensive doors

`ailv-code-ratelimit` (Throttle the expensive doors): Throttle expensive endpoints per client: a sliding window (for example 120 requests per minute per IP on API routes) — public reads get room, writes and beacons get less. Throttle more than pace: cap payload size, query complexity, records per page, and third-party spend per call — a slow drip of giant queries is still abuse (OWASP API4). Answer over-limit with 429 plus a Retry-After header, never a crash page. Keep limits in config, not code, so they change without a deploy. Count blocked requests separately so attacks show up in stats instead of hiding in totals. Behind a CDN, prefer its edge rules; the built-in limiter is the second layer, not the first.

## Checks

- expensive routes throttled per client
- 429 carries Retry-After
- limits live in config
- caps cover size, complexity, page size, spend
