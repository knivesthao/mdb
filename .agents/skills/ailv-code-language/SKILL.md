---
name: ailv-code-language
description: "Frameworks make whole mistake classes unwritable, so the agent spends tokens on the task instead of on validation and plumbing."
sources:
  - title: Python docs
    url: https://docs.python.org/3/
  - title: FastAPI docs
    url: https://fastapi.tiangolo.com/
  - title: Pydantic docs
    url: https://docs.pydantic.dev/latest/
  - title: SQLModel docs
    url: https://sqlmodel.tiangolo.com/
  - title: Typer docs
    url: https://typer.tiangolo.com/
helper: scripts/helper.py
example: examples/output.md
---

# Python first, house wins

`ailv-code-language` (Python first, house wins): Default to Python — agents generate it fastest, with the fewest mistakes. Write services with FastAPI + Pydantic: one model drives routing, validation, and the OpenAPI schema — never hand-write type checks. One SQLModel class serves as both table and validator. CLIs are one Typer-decorated function. If the codebase already uses another language, do not create this skill at all — skip it. Framework first: use the framework's own piece for anything it covers; hand-write only what no framework covers. Between same-language services reuse the same models (cross-language rules live in ailv-code-boundaries). If the project already uses a different stack, overwrite this skill with that stack's equivalent and follow it instead.

## Checks

- all I/O typed
- no hand-written validators
- tests cover happy path + one edge
