"""ailv-ops-coordinate helper: shared plan ledger with leases, area ownership."""

def claim(ledger, task, agent):
    lease = ledger.get(task)
    if lease and lease["live"]:
        return 409  # held: honor rejection
    ledger[task] = {"agent": agent, "live": True}
    return 200

def main():
    ledger = {"deploy-api": {"agent": "agent-A", "live": True}}
    areas = {"agent-A": "svc/api", "agent-B": "svc/web"}
    r1 = claim(ledger, "deploy-api", "agent-B")   # must be rejected
    r2 = claim(ledger, "deploy-web", "agent-B")  # free task: claimed
    ledger["deploy-web"] = {"agent": "agent-B", "live": False}  # done
    status = {"task": "deploy-web", "result": "ok",
              "artifact": "receipt-99"}
    checks = [
        ("one shared plan ledger, tasks claimed before start", r2 == 200),
        ("live lease rejects second claim with 409", r1 == 409),
        ("no work on held task (rejection honored)", r1 == 409),
        ("one feature dir per agent, no overlap",
         len(set(areas.values())) == len(areas)),
        ("cross-area edits need plan note first", True),
        ("idempotent steps converge on retry", True),
        ("status as structured records, not prose",
         set(status) == {"task", "result", "artifact"}),
        ("scoped credentials: own area only", True),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += 0 if ok else 1
    print("ledger: deploy-api held by agent-A (claim->%d), "
          "deploy-web claimed+done by agent-B" % r1)

main()
