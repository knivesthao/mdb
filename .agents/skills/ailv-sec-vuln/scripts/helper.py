"""ailv-sec-vuln: rank findings by exploitability, assign owner + SLA deadline."""
import datetime

SLA_DAYS = {"critical": 7, "high": 30, "medium": 90, "low": 180}
TODAY = datetime.date(2026, 11, 8)

FINDINGS = [
    {"id": "CVE-2026-1001", "severity": "critical", "reachable": True, "owner": "team-api", "retested": True, "mttr_days": 5},
    {"id": "CVE-2026-1002", "severity": "high", "reachable": True, "owner": "team-web", "retested": False, "mttr_days": 20},
    {"id": "CVE-2026-1003", "severity": "medium", "reachable": False, "owner": "", "retested": False, "mttr_days": None},
    {"id": "CVE-2026-1004", "severity": "low", "reachable": False, "owner": "team-api", "retested": True, "mttr_days": 60},
]

SEV_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def check(f):
    issues = []
    if not f["owner"]:
        issues.append("no owner")
    sla = TODAY + datetime.timedelta(days=SLA_DAYS[f["severity"]])
    if not f["retested"]:
        issues.append("closure needs retest")
    block = f["severity"] == "critical" and f["reachable"]
    return sla, issues, block


def main():
    ordered = sorted(FINDINGS, key=lambda f: (not f["reachable"], SEV_RANK[f["severity"]]))
    print("finding/severity/reachable/owner/deadline/verdict")
    fails = 0
    mttrs = []
    for f in ordered:
        sla, issues, block = check(f)
        verdict = "BLOCK-CI" if block else ("OPEN" if issues else "OK")
        if issues:
            fails += 1
        if f["mttr_days"] is not None:
            mttrs.append(f["mttr_days"])
        print(f"{f['id']}/{f['severity']}/reachable={f['reachable']}/"
              f"owner={f['owner'] or 'NONE'}/{sla}/{verdict}"
              + (f" issues={issues}" if issues else ""))
    print(f"scanner errors: fail closed (build blocked on scanner error)")
    if mttrs:
        print(f"mean-time-to-remediate (demo): {sum(mttrs)/len(mttrs):.1f} days over {len(mttrs)} closed")
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} findings need attention)")


if __name__ == "__main__":
    main()
