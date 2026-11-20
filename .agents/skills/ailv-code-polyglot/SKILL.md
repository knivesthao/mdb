---
name: ailv-code-polyglot
description: "Guest code fails at the seam and in language-specific traps the Python-trained agent walks into."
sources:
  - title: Protocol Buffers docs
    url: https://protobuf.dev/
helper: scripts/helper.py
example: examples/output.md
---

# Own guest-language code safely

`ailv-code-polyglot` (Own guest-language code safely): Use this only for code the primary language technically cannot carry — it remains the default everywhere else (Python in the house stack). Define the seam first: the contract lives in one repo as protobuf or JSON schema, and both sides generate from it — never hand-write both ends. Test the seam with recorded fixtures in the caller's language; the guest service proves itself with its own native tests, run with its native command (go test, cargo test, mix test). Keep guest code small and boring — the hot path only, everything else stays in the primary language. Agent pitfalls per guest: Rust — restructure ownership instead of cloning to satisfy the borrow checker. Go — propagate context and wrap errors; never swallow err. Erlang and Elixir — supervision trees own restarts, so don't defensively trap what the supervisor replays; keep state in processes.

## Checks

- seam defined as generated contract
- seam tests with recorded fixtures
- guest code minimal, hot path only
