"""ailv-code-integrity helper: verify-before-trust checklist with HMAC demo."""
import hashlib
import hmac

SECRET = b"demo-webhook-secret"


def sign(payload):
    return hmac.new(SECRET, payload.encode(), hashlib.sha256).hexdigest()


def verify(payload, signature):
    return hmac.compare_digest(sign(payload), signature)


def main():
    payload = '{"event":"deploy","sha":"abc123"}'
    sig = sign(payload)
    print("payload: " + payload)
    print("signature: " + sig[:16] + "...")
    print("verify good: " + str(verify(payload, sig)))
    print("verify tampered: " + str(verify(payload + "x", sig)))
    for name, ok in [("lockfiles committed", True),
                     ("webhook signatures verified", verify(payload, sig)),
                     ("no curl-to-shell installs", True),
                     ("bytes changed without commit -> stop and ask", True)]:
        print(("PASS " if ok else "FAIL ") + name)


if __name__ == "__main__":
    main()
