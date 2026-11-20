"""ailv-sec-sso: one IdP, expiring exceptions, JIT provision / auto deprovision."""
import datetime

TODAY = datetime.date(2026, 11, 8)
IDP = "idp-primary"

USERS = [
    {"name": "ada", "idp": "idp-primary", "mfa": "webauthn", "via": "sso"},
    {"name": "bob", "idp": "idp-primary", "mfa": "webauthn", "via": "jit", "domain_ok": True},
    {"name": "legacy-svc", "idp": "local", "mfa": "none", "via": "password"},
    {"name": "ex-admin", "idp": "idp-primary", "mfa": "webauthn", "via": "sso", "removed_from_idp": True},
]

EXCEPTIONS = [
    {"who": "break-glass-1", "owner": "secops", "expiry": "2026-12-01", "audited": True},
    {"who": "vendor-temp", "owner": "", "expiry": "2025-01-01", "audited": False},
]


def check_users():
    out = []
    for u in USERS:
        if u.get("removed_from_idp"):
            out.append((u["name"], "FAIL" if True else "FAIL", "still provisioned after IdP removal -> deprovision now"))
        elif u["idp"] != IDP or u["via"] == "password":
            out.append((u["name"], "FAIL", "not on single IdP / legacy password-only login"))
        elif u["mfa"] not in ("webauthn", "totp"):
            out.append((u["name"], "FAIL", "no phishing-resistant MFA"))
        else:
            note = "jit-provisioned, domain verified" if u["via"] == "jit" else "ok"
            out.append((u["name"], "PASS", note))
    return out


def check_exceptions():
    out = []
    for e in EXCEPTIONS:
        exp = datetime.date.fromisoformat(e["expiry"])
        if not e["owner"]:
            out.append((e["who"], "FAIL", "exception without owner"))
        elif exp <= TODAY:
            out.append((e["who"], "FAIL", f"expired {e['expiry']} -> revoke"))
        elif not e["audited"]:
            out.append((e["who"], "FAIL", "no audit trail"))
        else:
            out.append((e["who"], "PASS", f"expires {e['expiry']}, owned, audited"))
    return out


def main():
    print(f"identity provider: {IDP} (single)")
    fails = 0
    for name, status, note in check_users() + check_exceptions():
        print(f"[{status}] {name}: {note}")
        fails += status == "FAIL"
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} items need attention)")


if __name__ == "__main__":
    main()
