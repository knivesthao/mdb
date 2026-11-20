"""ailv-code-invites helper: single-use expiring tokens, never ownerless."""
import sys
import time

TOKENS = {}  # token -> {ws, role, exp, used}
OWNERS = {"acme": {"ada", "bob"}}  # workspace -> owner set


def issue(ws, role, ttl=3600):
    tok = f"inv-{len(TOKENS) + 1}"
    TOKENS[tok] = {"ws": ws, "role": role, "exp": time.time() + ttl, "used": False}
    return tok


def accept(tok, user):
    t = TOKENS.get(tok)
    if not t or t["used"] or time.time() > t["exp"]:
        return "deny: invalid/used/expired"
    t["used"] = True  # single-use
    return f"grant {t['role']} in {t['ws']} to {user} (logged)"


def remove_owner(ws, user):
    if len(OWNERS[ws]) <= 1 and user in OWNERS[ws]:
        return "blocked: workspace would be ownerless"
    OWNERS[ws].discard(user)
    return "removed"


def main():
    tok = issue("acme", "member")
    print("accept 1:", accept(tok, "carol"))
    print("accept 2 (reuse):", accept(tok, "dave"))
    old = issue("acme", "member", ttl=-1)
    print("expired:", accept(old, "erin"))
    print("remove bob:", remove_owner("acme", "bob"))
    print("remove ada (last owner):", remove_owner("acme", "ada"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
