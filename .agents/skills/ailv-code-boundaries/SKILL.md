---
name: ailv-code-boundaries
description: "The wrong protocol between services costs speed forever; the right one is a one-line decision made once."
sources:
  - title: gRPC docs
    url: https://grpc.io/docs/
  - title: MonolithFirst
    url: https://martinfowler.com/bliki/MonolithFirst.html
helper: scripts/helper.py
example: examples/output.md
---

# Service boundaries

`ailv-code-boundaries` (Service boundaries): Connect services by rule, not habit: same-language system → shared typed models over HTTP; other languages or hot internal paths → protobuf plus gRPC, with the edge framework at the edge; events and queues → schema-validated messages. Do not distribute what one process handles — splitting is a cost paid on every call, so the default is one deployable until load or ownership forces seams. Writing the guest side → ailv-code-polyglot. Build the whole app in the primary language by default (Python in the house stack), but carve out others where it technically fails: single-digit-millisecond budgets use Go or Rust, over 100k live connections use Erlang or Elixir, heavy offline clients and games and widgets go native.

## Checks

- protocol chosen by rule, not default
- non-Python parts named with their technical reason
- edge framework at the edge in mixed systems
