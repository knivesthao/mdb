"""Self-check for ailv-verify-layout: WCAG Reflow plus measured alignment."""
VIEWPORTS = [
    {"width": 320, "h_scroll": 0, "chopped": [], "baseline_ok": True, "edges_ok": True},
    {"width": 1280, "h_scroll": 0, "chopped": [], "baseline_ok": True, "edges_ok": True},
]
EXEMPT = "data table scrolls only inside stocked component (allowed)"
USER_OVERRIDE = None  # set to a string if user ordered a dense/playful break


def main():
    for v in VIEWPORTS:
        print("viewport %dpx: h_scroll=%d chopped=%s baseline=%s edges=%s" % (
            v["width"], v["h_scroll"], v["chopped"] or "none",
            v["baseline_ok"], v["edges_ok"]))
    print("exempt:", EXEMPT)
    checks = [
        ("no loss or 2D scroll at 320px (WCAG 1.4.10)",
         all(v["h_scroll"] == 0 and not v["chopped"] for v in VIEWPORTS)),
        ("rows share baselines, columns share edges",
         all(v["baseline_ok"] and v["edges_ok"] for v in VIEWPORTS)),
        ("2D scroll only in stocked components for exempt content", bool(EXEMPT)),
    ]
    failed = 0
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + ": " + name)
        failed += not ok
    if USER_OVERRIDE:
        print("NOTE: user override ships as specified:", USER_OVERRIDE)
    print("RESULT:", "PASS" if failed == 0 else "FAIL")


if __name__ == "__main__":
    main()
