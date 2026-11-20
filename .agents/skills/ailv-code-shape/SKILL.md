---
name: ailv-code-shape
description: "Small typed modules fit in a single read, so the agent holds the whole unit in context at once."
sources: []
helper: scripts/helper.py
example: examples/output.md
---

# Machine-shaped modules

`ailv-code-shape` (Machine-shaped modules): Write small flat modules: one file, one job, <150 lines. Typed inputs and outputs (Pydantic in, response_model out — or the stack's equivalent), no hidden globals, no clever abstractions. Flat over nested (depth <= 2, early returns). Raise typed transport errors at boundaries (HTTPException in FastAPI); never leak tracebacks or raw errors. Name files by what they do: skills.py, validate.py, render.py. Locality of behavior: put the behavior next to what it acts on — never in a distant shared layer (examples live in ailv-code-group). Fail typed, catch narrow: raise typed errors with the failing input attached; catch only expected exceptions at trust boundaries (OSError, ValueError) — never bare `except`; retry only the transient (timeouts, 429/503), surface the rest typed.

## Checks

- module <150 lines
- no global mutation
- tracebacks never reach clients
- behavior lives next to what it acts on
- no bare except Exception; every catch names its exceptions
