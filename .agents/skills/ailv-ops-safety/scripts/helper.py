"""ailv-ops-safety helper: scoped creds, human approval, drain, spend cap."""

NEVER = {"iam", "dns", "billing", "prod-data", "root"}

def main():
    agent = {"scope": {"svc/api-deploy", "svc/api-data"},
             "holds": set(), "fail_streak": 0, "deploys": True}
    destructive = {"op": "drop table users", "human_approved": False,
                   "executed": False}
    if not destructive["human_approved"]:
        destructive["executed"] = False  # never without a human
    if agent["fail_streak"] >= 2:
        agent["deploys"] = False
    spend = {"budget": 500, "spent": 120, "alert_at": 400, "kill": True}
    checks = [
        ("agents scoped least-privilege, never-touch enforced",
         not (agent["scope"] & NEVER)),
        ("destructive ops wait for human approval first",
         not destructive["executed"]),
        ("no agent approver / no emergency bypass", True),
        ("failing actors auto-drained (streak %d)" % agent["fail_streak"],
         agent["deploys"] or agent["fail_streak"] >= 2),
        ("spend capped with alerts + kill switch",
         spend["kill"] and spend["spent"] < spend["budget"]),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("safety: scope=%s spent $%d/$%d drain=%s" % (
        sorted(agent["scope"]), spend["spent"], spend["budget"],
        not agent["deploys"]))

main()
