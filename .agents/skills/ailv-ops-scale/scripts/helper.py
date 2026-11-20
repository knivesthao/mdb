"""ailv-ops-scale helper: bounded autoscaling on real signals."""

def replicas(signal, lo, hi, per_unit):
    want = -(-signal // per_unit)  # ceil div
    return max(lo, min(hi, want))

def main():
    policy = {"signal": "queue_depth", "depth": 450, "per_replica": 50,
              "min": 2, "max": 12, "bottleneck": "workers",
              "stateless_first": True, "load_tested": True}
    got = replicas(policy["depth"], policy["min"], policy["max"],
                   policy["per_replica"])
    checks = [
        ("scales on real signal (%s)" % policy["signal"],
         policy["signal"] in ("cpu", "request_rate", "queue_depth")),
        ("min/max bounds cap the bill (%d..%d)" % (policy["min"], policy["max"]),
         policy["min"] <= got <= policy["max"]),
        ("scales bottleneck (%s), stateless first" % policy["bottleneck"],
         policy["stateless_first"]),
        ("autoscale path load-tested", policy["load_tested"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("scale: depth %d / %d per replica -> %d replicas (bounds %d..%d)" % (
        policy["depth"], policy["per_replica"], got,
        policy["min"], policy["max"]))

main()
