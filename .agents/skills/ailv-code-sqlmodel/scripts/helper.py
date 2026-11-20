"""SQLModel router demo: fetch only on stack match. Stdlib only."""

MATCHED = ["order_by ignore-first", "no init validation asserts", "model_validate dict tests"]
UNMATCHED = "skip entirely when the stack has no SQLModel"

for rule in MATCHED:
    print(f"stack=sqlmodel -> {rule}")
print(f"stack=other     -> {UNMATCHED}")
print(f"\nrules: {len(MATCHED)}, gated, never default")
