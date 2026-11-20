---
name: ailv-code-impexp
description: "Synchronous bulk queries time out, and one bad row should not kill the file."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Bulk moves as background jobs

`ailv-code-impexp` (Bulk moves as background jobs): Run every bulk import and export as a background job with progress — never a synchronous request that times out. Validate encoding and schema row by row, quarantining bad rows instead of failing the file. Page reads in bounded batches; the export that loads the whole table is the outage. Notify on completion with the error report attached.

## Checks

- background jobs with progress
- bad rows quarantined, not fatal
- bounded batches
