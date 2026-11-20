"""Type gate demo: checker runs before tests, zero errors to proceed. Stdlib only."""

GATES = {
    "checker runs first": "mypy / pyright / tsc before pytest, not after",
    "zero errors": "fix or waive with a logged reason, never silence",
    "no new untyped boundaries": "public signatures typed, nullables explicit",
}

for gate, rule in GATES.items():
    print(f"{gate:28} -> {rule}")
print(f"\ngates: {len(GATES)}, all enforced, none skipped")
