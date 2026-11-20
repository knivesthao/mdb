"""Router self-check: route each task to exactly one legal leaf."""
LEAVES = {
    "pages": ("ailv-app-legal-pages", ("privacy", "terms", "refund", "returns policy", "subprocessor")),
    "card": ("ailv-app-card-scope", ("card number", "pci", "saq", "card entry", "checkout iframe")),
    "tax": ("ailv-app-tax", ("vat", "tax rate", "oss", "nexus", "charge tax")),
    "mail": ("ailv-app-legal-mail", ("newsletter", "marketing mail", "opt-out", "unsubscribe", "transactional")),
}
DEMOS = [
    ("publish refund policy page", "ailv-app-legal-pages"),
    ("card entry iframes for SAQ A", "ailv-app-card-scope"),
    ("EU VAT on digital sale", "ailv-app-tax"),
    ("newsletter opt-out wording", "ailv-app-legal-mail"),
]


def route(task):
    t = task.lower()
    scored = {}
    for leaf, keys in LEAVES.values():
        scored[leaf] = sum(1 for k in keys if k in t)
    best = [leaf for leaf, s in scored.items() if s == max(scored.values()) and s > 0]
    return best[0] if len(best) == 1 else None


def main():
    ok = True
    for task, want in DEMOS:
        got = route(task)
        line = "PASS" if got == want else "FAIL"
        if got != want:
            ok = False
        print(f"{line}: {task!r} -> {got} (want {want})")
    print("PASS: exactly one leaf per task" if ok else "FAIL: routing ambiguous")
    print("RESULT:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
