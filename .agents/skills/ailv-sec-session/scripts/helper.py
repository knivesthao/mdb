"""ailv-sec-session: short-lived revocable sessions with absolute caps."""
# lifetimes in minutes
POLICY = {"access_min": 15, "absolute_max_min": 480, "rotation": True, "revocation": True}

SESSIONS = [
    {"id": "sess-ada-1", "age_min": 10, "lifetime_min": 15, "absolute_min": 480, "rotated": True, "revoked": False},
    {"id": "sess-bob-2", "age_min": 500, "lifetime_min": 60, "absolute_min": 480, "rotated": False, "revoked": False},
    {"id": "sess-eve-3", "age_min": 5, "lifetime_min": 15, "absolute_min": 480, "rotated": True, "revoked": True},
]


def verdict(s):
    if s["revoked"]:
        return "DEAD (revoked server-side)"
    if s["age_min"] > s["absolute_min"]:
        return "FAIL: past absolute cap -> kill"
    if s["age_min"] > s["lifetime_min"]:
        return "EXPIRED -> rotate"
    if not s["rotated"]:
        return "FAIL: no rotation"
    return "PASS: live, short-lived, revocable"


def main():
    print(f"policy: access<={POLICY['access_min']}m absolute<={POLICY['absolute_max_min']}m "
          f"rotation={POLICY['rotation']} revocation={POLICY['revocation']}")
    bad = 0
    for s in SESSIONS:
        v = verdict(s)
        print(f"[{('PASS' if v.startswith('PASS') or v.startswith(('DEAD', 'EXPIRED')) else 'FAIL')}] "
              f"{s['id']}: age={s['age_min']}m -> {v}")
        bad += v.startswith("FAIL")
    print(f"revocation kill-path: {'PASS' if POLICY['revocation'] else 'FAIL'}")
    print(f"self-check: {'FAIL' if bad else 'PASS'} ({bad} sessions violate policy)")


if __name__ == "__main__":
    main()
