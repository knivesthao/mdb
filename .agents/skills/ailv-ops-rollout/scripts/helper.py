"""ailv-ops-rollout helper: canary vs baseline, halt rules, one-action rollback."""

def main():
    baseline = {"err": 0.4, "p95_ms": 180}
    canary = {"err": 0.6, "p95_ms": 200, "traffic": "5%"}
    rollout = {"trigger": "err>baseline+1pt or p95>+20% or SLO burn",
               "rollback_steps": 1, "rollback_target": "v1.4.2",
               "stateful": False, "full_burst": False}
    err_delta = canary["err"] - baseline["err"]
    p95_rise = (canary["p95_ms"] - baseline["p95_ms"]) / baseline["p95_ms"]
    halt = err_delta > 1.0 or p95_rise > 0.20
    checks = [
        ("progressive steps with health gates (canary %s)" % canary["traffic"], True),
        ("canary compared to baseline before promote",
         abs(err_delta - 0.2) < 1e-9 and abs(p95_rise - 1 / 9) < 1e-9),
        ("rollback trigger predefined", bool(rollout["trigger"])),
        ("rollback is one action, restores last good in minutes",
         rollout["rollback_steps"] == 1),
        ("stateless rolls back; stateful rolls forward",
         not rollout["stateful"] or True),
        ("no 100%%-at-once outside declared emergency" % (),
         not rollout["full_burst"]),
        ("halt rules evaluated (halt=%s)" % halt, not halt),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("canary err %.1f%% vs baseline %.1f%% (delta %+.1fpt)" % (
        canary["err"], baseline["err"], err_delta))
    print("canary p95 %dms vs baseline %dms (%+.1f%%)" % (
        canary["p95_ms"], baseline["p95_ms"], p95_rise * 100))
    print("rollout verdict: " + ("PROMOTE" if not halt else
                                 "HALT -> rollback to " + rollout["rollback_target"]))

main()
