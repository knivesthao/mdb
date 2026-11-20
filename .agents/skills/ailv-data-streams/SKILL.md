---
name: ailv-data-streams
description: "Batch logic on streams mishandles late events; a stalled watermark is a silent outage."
sources:
  - title: Apache Kafka docs
    url: https://kafka.apache.org/documentation/
helper: scripts/helper.py
example: examples/output.md
---

# Windows plus watermarks

`ailv-data-streams` (Windows plus watermarks): Transform unbounded streams with windows plus watermarks so late and out-of-order events settle per policy. Watermarks trade latency for completeness: events later than the horizon drop or ride a side channel — name the horizon, never assume every event arrives. Never batch logic on a stream — every unbounded grouping needs a trigger for when it emits. Track watermark lag as the health metric; a stalled watermark is the outage.

## Checks

- windows plus watermarks
- every grouping has an emit trigger
- watermark lag monitored
