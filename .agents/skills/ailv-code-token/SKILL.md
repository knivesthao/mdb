---
name: ailv-code-token
description: "Every token spent writing or re-reading code is a token not spent on the task; cheap code compounds across sessions."
---

# Token-efficient code

`ailv-code-token` (Token-efficient code): Write code that's cheap to generate and cheap to re-read: type everything, one canonical pattern per job (a route, a model, a command). Early returns, table-driven branches over nested ifs, JSON-first data. Delete dead code — every dead line taxes every future read. Prefer 20 lines of plain code over 5 lines of clever code. Fix by smallest edit: never rewrite a whole file for a local fix — patch the function, keep the rest. Every rewritten-but-unchanged line is pure output tax. Templates get smallest edits too: never whole-file-rewrite an HTML template for a local fix — the file writer is byte-literal, but a model regenerating the file tidies tags and corrupts it (probed). Patch the block, keep the rest.

## Checks

- no nested depth >2
- no dead exports
- single pattern per job
- fixes are smallest edits, never whole-file rewrites
- templates patched by block, never whole-file rewrites
