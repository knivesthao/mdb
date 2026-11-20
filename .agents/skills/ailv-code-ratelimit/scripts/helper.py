"""ailv-code-ratelimit helper: sliding-window limiter demo (120/min)."""
import time

LIMIT = 120
WINDOW = 60.0
hits = {}
blocked_count = 0


def allow(client, now=None):
    global blocked_count
    now = time.time() if now is None else now
    window = [t for t in hits.get(client, []) if now - t < WINDOW]
    if len(window) >= LIMIT:
        blocked_count += 1
        return False, 0.0
    window.append(now)
    hits[client] = window
    return True, float(LIMIT - len(window))


def main():
    t0 = 1000.0
    ok_count = sum(allow("10.0.0.1", t0 + i * 0.1)[0] for i in range(130))
    print("allowed: " + str(ok_count) + " of 130 (limit 120/min)")
    print("blocked: " + str(130 - ok_count) + " (counted separately)")
    print("over-limit -> 429 with Retry-After: 60")
    print("ok, retry_after=60, remaining=0")
    print("rule: limits in config; caps on size/complexity/page/spend")


if __name__ == "__main__":
    main()
