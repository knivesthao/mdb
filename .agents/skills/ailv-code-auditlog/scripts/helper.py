"""ailv-code-auditlog helper: immutable actor-action-target trail + export."""
import json
import sys

TRAIL = []  # append-only: no edits, no deletes
RETENTION_DAYS = 365


def log(actor, action, target, day):
    TRAIL.append({"actor": actor, "action": action,
                  "target": target, "day": day})  # agent named in actor


def export(since_day):
    return [e for e in TRAIL if e["day"] >= since_day]  # retention window


def main():
    log("agent:checkout-fix", "members.write", "ws=acme user=bob->admin", 100)
    log("agent:checkout-fix", "data.export", "ws=acme orders.csv", 101)
    log("ops:ada", "impersonate.start", "ws=globex consent=ticket-5", 102)
    old = {"actor": "x", "action": "old", "target": "t", "day": 100 - RETENTION_DAYS - 1}
    kept = [e for e in TRAIL + [old] if e["day"] >= 100 - RETENTION_DAYS]
    print(f"append-only rows: {len(TRAIL)} (edits: none allowed)")
    print("export for auditors:")
    print(json.dumps(export(100), indent=1))
    print(f"retention {RETENTION_DAYS}d prunes 1 stale row -> kept {len(kept)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
