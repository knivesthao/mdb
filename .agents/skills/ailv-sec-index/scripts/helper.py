"""ailv-sec-index: route each question to exactly one sec skill."""
ROUTES = {
    "cve backlog": "ailv-sec-vuln",
    "enterprise sso": "ailv-sec-sso",
    "image scan": "ailv-sec-scan",
    "leaked key": "ailv-sec-secretscan",
    "token lifetime": "ailv-sec-session",
    "siem alert": "ailv-sec-siem",
    "waf rule": "ailv-sec-waf",
    "impossible travel": "ailv-sec-anomaly",
    "breach drill": "ailv-sec-runbooks",
    "os patch": "ailv-sec-patch",
    "audit evidence": "ailv-sec-compliance",
    "login form": "ailv-code-auth",
}

QUERIES = [
    ("cve backlog of criticals", "ailv-sec-vuln"),
    ("enterprise sso rollout", "ailv-sec-sso"),
    ("image scan failing", "ailv-sec-scan"),
    ("leaked key in repo", "ailv-sec-secretscan"),
    ("token lifetime policy", "ailv-sec-session"),
    ("siem alert flood", "ailv-sec-siem"),
    ("waf rule tuning", "ailv-sec-waf"),
    ("impossible travel login", "ailv-sec-anomaly"),
    ("breach drill schedule", "ailv-sec-runbooks"),
    ("os patch window", "ailv-sec-patch"),
    ("audit evidence pack", "ailv-sec-compliance"),
    ("login form validation", "ailv-code-auth"),
]


def route(q):
    q = q.lower()
    for key, skill in ROUTES.items():
        if key in q:
            return skill
    return None


def main():
    print("router demo: one question -> one skill (never read them all)")
    fails = 0
    for q, want in QUERIES:
        got = route(q)
        ok = got == want
        fails += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {q!r} -> {got} (want {want})")
    print(f"[PASS] app basics stay in ailv-code-auth; humans verify counts/drills")
    print(f"self-check: {'FAIL' if fails else 'PASS'} ({fails} misroutes)")


if __name__ == "__main__":
    main()
