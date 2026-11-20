"""ailv-code-webhooks helper: signed payloads, retry+replay, receiver dedup."""
import hashlib
import hmac
import json
import sys

SECRET = b"whsec-demo"
LOG = {}  # destination -> [deliveries]; receivers dedup on event ids
SEEN = set()


def sign(payload):
    body = json.dumps(payload, sort_keys=True).encode()
    return hmac.new(SECRET, body, hashlib.sha256).hexdigest(), body


def deliver(dest, event_id, payload, fail_first=True):
    sig, body = sign(payload)
    attempts = 0
    while True:
        attempts += 1
        ok = attempts > 1 or not fail_first  # backoff then success
        LOG.setdefault(dest, []).append({"event": event_id, "try": attempts,
                                        "status": "ok" if ok else "5xx"})
        if ok:
            recv = "duplicate-ignored" if event_id in SEEN else "applied"
            SEEN.add(event_id)
            return f"{dest}: {event_id} ok after {attempts} tries (sig {sig[:8]}..), rx {recv}"


def main():
    print(deliver("https://acme.example/hook", "evt-1", {"type": "order.paid", "v": 2}))
    print(deliver("https://acme.example/hook", "evt-1", {"type": "order.paid", "v": 2},
                  fail_first=False), "(replay: safe resend)")
    print("delivery log (customer-visible):", json.dumps(LOG["https://acme.example/hook"]))
    print("never fire-and-forget: retry with backoff + replay kept")
    return 0


if __name__ == "__main__":
    sys.exit(main())
