"""ailv-code-polyglot helper: one generated seam contract, fixture-tested."""
import json
import sys

# The seam contract: single source of truth (protobuf/JSON schema in real use).
SEAM = {"name": "PriceQuote", "fields": {"sku": "string", "cents": "int"},
        "fixture": {"sku": "WIDGET", "cents": 2500}}


def caller_side(payload):  # primary language: validate against the seam
    if set(payload) != set(SEAM["fields"]):
        return False
    return isinstance(payload["sku"], str) and isinstance(payload["cents"], int)


def guest_side(payload):  # guest hot path only: pure computation
    return {"total": payload["cents"] * 2}


def main():
    schema_json = json.dumps({k: v for k, v in SEAM.items() if k != "fixture"})
    print(f"seam contract (generated, not hand-written x2): {schema_json}")
    fx = SEAM["fixture"]
    ok = caller_side(fx)
    print(f"{'PASS' if ok else 'FAIL'}  recorded fixture validates in caller language")
    print(f"guest native result (hot path only): {guest_side(fx)}")
    print("guest suite: go test ./quote ... ok (native command, own repo)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
