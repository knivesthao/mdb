---
name: ailv-verify-types
description: "Tests pass while types lie: both benchmark arms shipped type errors that green suites never caught."
---

# Type-check before you test

`ailv-verify-types` (Type-check before you test): Run the project's static type checker before the test suite on every build step that writes code — mypy or pyright for Python, tsc for TypeScript, the compiler's own checks everywhere else. Zero errors is the gate: fix or waive each one with a reason logged beside it, never silence the checker to make the run green. Project means the whole project: run the checker over app AND tests (e.g. `mypy app tests` with `--check-untyped-defs`), never scope the gate to the app package to get green — the costliest recent misses hid in tests/. Suppress known-idiom false positives once in config (e.g. FastAPI Depends-in-defaults warnings), never per line. If no checker is installable (offline vendored bank, no network), run `python -m compileall` as a smoke gate and log an explicit waiver naming the missing checker — a waived gate is logged, never silent, and never claimed as a passed check. A waiver is verification debt: waived code is not type-clean until a real checker runs over it, so re-check at the first opportunity. Known-framework false positives get targeted ignores on the first attempt — SQLModel metaclass columns are invisible to static analysis, so `order_by`/`desc` take `# type: ignore` immediately; never burn attempts on `__table__.c` workarounds. New code adds no untyped boundaries — public function signatures carry types, nullables are explicit, and `Any` needs a comment naming why. When the language has no checker, say so in the log and move on; an absent gate is a logged gap, not a silent pass.

## Checks

- type checker runs before the test suite
- zero errors, waivers logged with reasons
- no new untyped public signatures
- offline falls back to compileall plus a logged waiver
- waived code re-checked at first opportunity, never reported type-clean
- framework false positives ignored on first attempt, no workaround loops
- checker runs over app and tests, untyped defs checked
- idiom false positives suppressed in config, not inline
