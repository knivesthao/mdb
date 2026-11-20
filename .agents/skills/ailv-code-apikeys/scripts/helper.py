"""ailv-code-apikeys helper: hashed, scoped, revocable keys (show once)."""
import hashlib
import hmac
import sys

STORE = {}  # key_id -> {hash, scopes, rate, revoked}
CALLS = {}  # key_id -> call count (metering/attribution)


def issue(key_id, secret, scopes, rate):
    STORE[key_id] = {"hash": hashlib.sha256(secret.encode()).hexdigest(),
                     "scopes": set(scopes), "rate": rate, "revoked": False}
    CALLS[key_id] = 0
    return secret  # shown once at creation, never again


def call(key_id, secret, scope):
    rec = STORE.get(key_id)
    if not rec or rec["revoked"]:
        return "deny: revoked/unknown"
    if not hmac.compare_digest(rec["hash"], hashlib.sha256(secret.encode()).hexdigest()):
        return "deny: bad secret"
    if scope not in rec["scopes"]:
        return "deny: out of scope"
    CALLS[key_id] += 1
    if CALLS[key_id] > rec["rate"]:
        return "deny: rate exceeded"
    return "allow"


def main():
    shown_once = issue("k1", "sk-live-ABC", ["orders.read"], 2)
    print(f"created k1, secret shown once: {shown_once} (stored: hash only)")
    print("good call:", call("k1", "sk-live-ABC", "orders.read"))
    print("wrong scope:", call("k1", "sk-live-ABC", "members.write"))
    print("rate 3rd call:", call("k1", "sk-live-ABC", "orders.read"),
          "/", call("k1", "sk-live-ABC", "orders.read"))
    STORE["k1"]["revoked"] = True
    print("after revoke:", call("k1", "sk-live-ABC", "orders.read"))
    print(f"metered calls attributed to k1: {CALLS['k1']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
