"""ailv-code-boundaries helper: pick protocol by rule."""
CASES = [
    {"name": "billing + invoices (same Python stack)", "langs": 1, "hot": False},
    {"name": "python edge + go matcher", "langs": 2, "hot": True},
    {"name": "order events fan-out", "langs": 2, "hot": False, "events": True},
]


def pick(case):
    if case.get("events"):
        return "schema-validated messages (queue)"
    if case["langs"] == 1 and not case["hot"]:
        return "shared typed models over HTTP"
    return "protobuf + gRPC (edge framework at edge)"


def main():
    for case in CASES:
        print(case["name"] + " -> " + pick(case))
    print("default: one deployable until load or ownership forces seams")
    print("non-Python carved out only for: single-digit-ms, 100k+ conns, native clients")


if __name__ == "__main__":
    main()
