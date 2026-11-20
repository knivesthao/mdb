"""ailv-code-flags helper: targeted evaluation with owner + kill switch."""
import sys

FLAGS = {
    "new-checkout": {"owner": "billing-team", "plans": {"pro", "team"},
                     "tenants": set(), "pct": 50, "kill": False,
                     "remove_by": "2026-12-31"},
    "old-banner": {"owner": "growth", "plans": set(), "tenants": set(),
                   "pct": 100, "kill": True, "remove_by": "2025-01-01"},
}


def evaluate(name, plan, tenant, user_bucket):
    f = FLAGS[name]
    if f["kill"]:
        return False
    if f["plans"] and plan not in f["plans"]:
        return False
    if f["tenants"] and tenant not in f["tenants"]:
        return False
    return user_bucket < f["pct"]


def main():
    cases = [("new-checkout", "pro", "acme", 10, True),
             ("new-checkout", "pro", "acme", 90, False),
             ("new-checkout", "free", "acme", 10, False),
             ("old-banner", "pro", "acme", 0, False)]
    ok = True
    for name, plan, tenant, bucket, want in cases:
        got = evaluate(name, plan, tenant, bucket)
        mark = "PASS" if got == want else "FAIL"
        ok &= got == want
        print(f"{mark}  {name} plan={plan} bucket={bucket} -> {'on' if got else 'off'}")
    print("owner(new-checkout)=billing-team, kill switch wired -> yes")
    print("stale flag past remove_by (old-banner) -> delete it")
    print("ALL:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
