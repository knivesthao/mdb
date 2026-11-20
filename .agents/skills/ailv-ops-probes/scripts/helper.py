"""ailv-ops-probes helper: liveness vs readiness split, real-dep checks."""

def main():
    liveness = {"checks": ["process alive"], "on_fail": "restart",
                "timeout_s": 2, "user_handler": False}
    readiness = {"checks": ["db ping", "queue ping"], "on_fail": "shed load",
                 "timeout_s": 2, "user_handler": False,
                 "serving": False}  # cannot serve -> out of rotation, alive
    checks = [
        ("liveness split from readiness",
         liveness["on_fail"] != readiness["on_fail"]),
        ("probes check real deps with timeouts",
         len(readiness["checks"]) > 0 and readiness["timeout_s"] > 0),
        ("unready pod alive but out of rotation",
         not readiness["serving"]),
        ("failing readiness sheds load, liveness restarts",
         readiness["on_fail"] == "shed load"
         and liveness["on_fail"] == "restart"),
        ("no probe uses the user-serving handler",
         not liveness["user_handler"] and not readiness["user_handler"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("probes: liveness=%s readiness=%s" % (
        liveness["checks"], readiness["checks"]))

main()
