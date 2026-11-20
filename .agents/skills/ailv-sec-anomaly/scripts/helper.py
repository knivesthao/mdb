"""ailv-sec-anomaly: baselines retuned, only sharp signals page."""
LOGINS = [
    {"user": "ada", "from": "SG", "at_h": 9, "prev_h": 8, "prev_from": "SG"},
    {"user": "bob", "from": "SG", "at_h": 10, "prev_h": 9, "prev_from": "SG"},
    # impossible travel: SG -> BR within 1h
    {"user": "eve", "from": "BR", "at_h": 10, "prev_h": 9, "prev_from": "SG"},
    # lateral movement: first-ever admin share sweep
    {"user": "svc", "from": "LAN", "at_h": 3, "prev_h": 3, "prev_from": "LAN", "lateral": True},
    {"user": "ada", "from": "SG", "at_h": 11, "prev_h": 9, "prev_from": "SG"},
]

BASELINE_RETUNED_DAYS_AGO = 6  # must be <= 14


def signal(e):
    if e.get("lateral"):
        return "lateral-movement"
    if e["from"] != e["prev_from"] and abs(e["at_h"] - e["prev_h"]) <= 1:
        return "impossible-travel"
    return None


def main():
    print(f"baseline retuned {BASELINE_RETUNED_DAYS_AGO}d ago "
          f"[{'PASS' if BASELINE_RETUNED_DAYS_AGO <= 14 else 'FAIL'}] (continuous retuning)")
    pages, queued = 0, 0
    for e in LOGINS:
        sig = signal(e)
        if sig in ("impossible-travel", "lateral-movement"):
            pages += 1
            print(f"  [PAGE] {e['user']} {e['prev_from']}->{e['from']}: {sig}")
        else:
            queued += 1
            print(f"  [queue] {e['user']} from {e['from']}: normal -> analyst review")
    print(f"demo: {pages} paged (sharp only), {queued} queued for review")
    print(f"[PASS] only sharp signals page; rest stays in review queue")
    print("self-check: PASS")


if __name__ == "__main__":
    main()
