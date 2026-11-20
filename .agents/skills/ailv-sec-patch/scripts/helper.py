"""ailv-sec-patch: fleet-wide patching with CIS baselines, no exemptions."""
FLEET = [
    {"host": "web-01", "os_days": 5, "browser_days": 3, "agent_ok": True, "exempt": False, "owner": "ops"},
    {"host": "db-01", "os_days": 12, "browser_days": 12, "agent_ok": True, "exempt": False, "owner": "dba"},
    {"host": "exec-laptop", "os_days": 120, "browser_days": 90, "agent_ok": False, "exempt": True, "owner": "ops"},
    {"host": "legacy-pos", "os_days": 200, "browser_days": 200, "agent_ok": True, "exempt": True, "owner": "retail"},
]

WINDOW_DAYS = 14


def main():
    print(f"patch window: {WINDOW_DAYS}d, baseline: CIS")
    fails = 0
    for h in FLEET:
        worst = max(h["os_days"], h["browser_days"])
        problems = []
        if h["exempt"]:
            problems.append("EXEMPT -> persistent foothold, include it")
        if worst > WINDOW_DAYS:
            problems.append(f"straggler ({worst}d > {WINDOW_DAYS}d) -> page {h['owner']}")
        if not h["agent_ok"]:
            problems.append("no agent -> unmanaged")
        if problems:
            fails += 1
            print(f"[FAIL] {h['host']}: " + "; ".join(problems))
        else:
            print(f"[PASS] {h['host']}: patched ({worst}d), agent ok, no exemption")
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} hosts need attention)")


if __name__ == "__main__":
    main()
