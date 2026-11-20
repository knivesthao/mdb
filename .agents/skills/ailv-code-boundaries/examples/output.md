# ailv-code-boundaries — worked example

## Input

Demo service pairs baked into `scripts/helper.py`: same-stack billing,
Python-plus-Go hot path, and an order-events fan-out.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
billing + invoices (same Python stack) -> shared typed models over HTTP
python edge + go matcher -> protobuf + gRPC (edge framework at edge)
order events fan-out -> schema-validated messages (queue)
default: one deployable until load or ownership forces seams
non-Python carved out only for: single-digit-ms, 100k+ conns, native clients
```
