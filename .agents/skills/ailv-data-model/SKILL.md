---
name: ailv-data-model
description: "Agents re-parse every structure on every read — nesting, abbreviations, and clever nulls tax all of them."
sources:
  - title: Pydantic docs
    url: https://docs.pydantic.dev/latest/
  - title: JSON Schema
    url: https://json-schema.org/
helper: scripts/helper.py
example: examples/output.md
---

# Data shaped for agent readers

`ailv-data-model` (Data shaped for agent readers): One canonical shape per concept: a User looks the same in the database, the API, and events — generated from one schema, never hand-mirrored. Flat over nested: nest at most two deep; deeper trees cost every reader a traversal, so lists of ids plus lookup beat giant trees. Names carry meaning: full words, units in names (amount_cents, created_at_utc), no tribal abbreviations. Explicit over clever: string enums spelled out, unions with a literal kind field, never null-means-something — use an explicit status instead. Time is ISO-8601 UTC strings, never local plus offset guessing. Validate at every boundary with the stack's typed models (Pydantic, Zod, or equivalent) so malformed data fails at the door with a message, not deep in logic. Denormalize for readers: store what queries read and recompute on write; joins across five tables cost the agent a reconstruction on every read. Respect the system it lands in: denormalization taxes writes, so keep hot write paths normalized; index what you filter, knowing each index taxes every write; events carry the change plus the id within the transport's size cap, never the whole entity; page everything bounded on read and write.

## Checks

- one canonical shape per concept
- nesting at most two deep
- no null-means-something, units in names
- denormalization pays its write cost
