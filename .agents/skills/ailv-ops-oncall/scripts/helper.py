"""ailv-ops-oncall helper: rotation, runbooks, tracked postmortems."""

def main():
    rotation = {"schedule": "weekly", "members": ["amy", "bo", "cy"],
                "escalation": ["primary->secondary->manager"],
                "single_hero": False}
    pages = [{"symptom": "checkout errors", "runbook": "rb/checkout-errors"},
             {"symptom": "db failover", "runbook": "rb/db-failover"}]
    reviews = [{"incident": "INC-7", "days_after": 2, "blameless": True,
                "actions": [{"t": "add runbook", "done": True},
                            {"t": "fix alert threshold", "done": True}]}]
    checks = [
        ("scheduled rotation with escalation",
         bool(rotation["schedule"]) and bool(rotation["escalation"])),
        ("never a single hero with no notes", not rotation["single_hero"]),
        ("runbook per page", all(p["runbook"] for p in pages)),
        ("blameless postmortem within days",
         all(r["days_after"] <= 7 and r["blameless"] for r in reviews)),
        ("action items tracked to done",
         all(a["done"] for r in reviews for a in r["actions"])),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("oncall: %s rotation (%s), %d pages, %d reviews" % (
        rotation["schedule"], ",".join(rotation["members"]),
        len(pages), len(reviews)))

main()
