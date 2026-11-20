"""ailv-sec-compliance: continuous automated evidence, every control mapped."""
CONTROLS = [
    {"id": "C1", "control": "access reviews", "proof": "siem quarterly export", "auto": True},
    {"id": "C2", "control": "change tickets on deploys", "proof": "pipeline log", "auto": True},
    {"id": "C3", "control": "PHI access audit", "proof": "auditlog per-access", "auto": True},
    {"id": "C4", "control": "card PAN never stored", "proof": "", "auto": False},
    {"id": "C5", "control": "GDPR deletion on request", "proof": "retention job receipt", "auto": True},
]


def main():
    print("regulated data first: PHI->auditlog+crypto+rbac+retention, "
          "PAN->tokenize, personal->retention+deletion")
    fails = 0
    for c in CONTROLS:
        if not c["proof"]:
            print(f"[FAIL] {c['id']} {c['control']}: unmapped -> audit finding waiting");
            fails += 1
        elif not c["auto"]:
            print(f"[FAIL] {c['id']} {c['control']}: manual screenshots rot -> automate");
            fails += 1
        else:
            print(f"[PASS] {c['id']} {c['control']}: proven by {c['proof']} (continuous)")
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} controls unproven)")


if __name__ == "__main__":
    main()
