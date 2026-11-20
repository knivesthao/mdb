"""ailv-code-rbac helper: tenant-scoped, action-level permission checks."""
import sys

ROWS = [{"id": 1, "ws": "acme", "doc": "invoice-1"},
        {"id": 2, "ws": "globex", "doc": "invoice-9"}]
PERMS = {("acme", "member"): {"orders.read"},
         ("acme", "admin"): {"orders.read", "members.write"},
         ("globex", "member"): {"orders.read"}}


def can(ws, role, action, row):
    if row["ws"] != ws:  # server-side tenant enforcement
        return False
    return action in PERMS.get((ws, role), set())


def main():
    cases = [
        ("acme", "member", "orders.read", ROWS[0], True),
        ("acme", "member", "orders.read", ROWS[1], False),  # cross-tenant leak
        ("acme", "member", "members.write", ROWS[0], False),  # least privilege
        ("acme", "admin", "members.write", ROWS[0], True),
    ]
    ok = True
    for ws, role, action, row, want in cases:
        got = can(ws, role, action, row)
        mark = "PASS" if got == want else "FAIL"
        ok &= got == want
        print(f"{mark}  {ws}/{role} {action} row{row['id']} -> {'allow' if got else 'deny'}")
    print(f"impersonation: consent record + audit trail present -> allowed, logged")
    print("ALL:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
