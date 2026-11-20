---
name: ailv-data-contracts
description: "A breaking rename with no contract silently breaks every downstream reader."
sources:
  - title: AsyncAPI
    url: https://www.asyncapi.com/
helper: scripts/helper.py
example: examples/output.md
---

# Versioned schemas, additive only

`ailv-data-contracts` (Versioned schemas, additive only): Version every event and table schema in one registry with compatibility checks on publish. Additive changes only — new optional fields, never renames or type changes without a new version. Consumers pin the version they read; producers support the last N versions through a dual-write window. Promise freshness too: each feed declares how late is too late and what happens on breach — a contract without an SLA is a handshake.

## Checks

- schemas versioned in one registry
- additive-only evolution
- consumers pin versions
