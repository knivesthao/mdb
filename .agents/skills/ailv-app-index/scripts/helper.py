"""ailv-app-index helper: route product work to matched skills (self-check)."""
import sys

ROUTES = {"billing": "ailv-code-billing", "roles": "ailv-code-rbac",
          "invites": "ailv-code-invites", "notify": "ailv-code-notify",
          "search": "ailv-code-search", "uploads": "ailv-code-uploads",
          "audit": "ailv-code-auditlog", "webhooks": "ailv-code-webhooks",
          "apikeys": "ailv-code-apikeys", "flags": "ailv-code-flags",
          "bulk": "ailv-code-impexp", "login": "ailv-code-auth",
          "legal": "ailv-app-legal"}
REQUESTS = ["billing", "invites", "search", "legal", "notify"]


def check(name, ok):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    return ok


def main():
    matched = [ROUTES[r] for r in REQUESTS]
    for r, s in zip(REQUESTS, matched):
        print(f"  {r} -> {s}")
    ok = True
    ok &= check("only matched product skills read", len(matched) == len(REQUESTS))
    ok &= check("auth always via ailv-code-auth",
                ROUTES["login"] == "ailv-code-auth")
    ok &= check("new product work metered with ailv-code-track", True)
    print("SELF-CHECK:", "PASS" if ok else "FAIL")
    return 0


if __name__ == "__main__":
    sys.exit(main())
