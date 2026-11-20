"""ailv-sec-runbooks: containment playbooks per breach class, drilled."""
import datetime

TODAY = datetime.date(2026, 11, 8)
PLAYBOOKS = [
    {"cls": "ransomware", "steps": ["isolate host", "rotate creds", "notify customers"],
     "drilled": "2026-10-20", "updated_after_drill": True},
    {"cls": "leaked-secret", "steps": ["revoke key", "purge history", "rotate reach"],
     "drilled": "2026-09-01", "updated_after_drill": True},
    {"cls": "phishing", "steps": ["kill sessions", "force reset"], "drilled": "",
     "updated_after_drill": False},
]

SEVERITY_PATH = {"SEV1": "page+exec notify", "SEV2": "page oncall", "SEV3": "ticket"}


def main():
    print("severity/escalation decided in advance: "
          + ", ".join(f"{k}->{v}" for k, v in SEVERITY_PATH.items()))
    fails = 0
    for p in PLAYBOOKS:
        if not p["steps"]:
            print(f"[FAIL] {p['cls']}: no containment steps");
            fails += 1
            continue
        if not p["drilled"]:
            print(f"[FAIL] {p['cls']}: never drilled -> improvisation risk");
            fails += 1
            continue
        age = (TODAY - datetime.date.fromisoformat(p["drilled"])).days
        stale = age > 90
        upd = p["updated_after_drill"]
        ok = not stale and upd
        fails += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {p['cls']}: drilled {p['drilled']} "
              f"({age}d ago), playbook updated={upd}, steps={len(p['steps'])}")
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} playbooks need drilling/updating)")


if __name__ == "__main__":
    main()
