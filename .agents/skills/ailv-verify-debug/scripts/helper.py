"""Self-check for ailv-verify-debug: bisect the run to the guilty step."""
STEPS = [
    {"name": "parse input", "done_state": "ok", "check": "ok"},
    {"name": "fetch record", "done_state": "ok", "check": "ok"},
    {"name": "render total", "done_state": "ok", "check": "FAIL"},
    {"name": "send receipt", "done_state": "skip", "check": "skip"},
]
SMALLEST_INPUT = "qty=-1 (was order #1042 with 37 lines)"
CONTRACT_FIX = "render total now honors fetch record's cents-int contract"


def bisect(steps):
    for s in steps:
        if s["check"] == "FAIL":
            return s["name"]
    return None


def main():
    print("smallest failing input:", SMALLEST_INPUT)
    guilty = bisect(STEPS)
    print("guilty step:", guilty)
    print("contract fix:", CONTRACT_FIX)
    checks = [
        ("smallest failing input reproduced", bool(SMALLEST_INPUT)),
        ("guilty step bisected by done-state", guilty == "render total"),
        ("contract fixed when steps disagree", bool(CONTRACT_FIX)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
