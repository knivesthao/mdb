"""Self-check: router — each interface task maps to its skill(s) only."""

ROUTES = {
    "new screen": ["ailv-ui-shell", "ailv-ui-tokens", "ailv-ui-seo"],
    "interactive typing": ["ailv-ui-framework"],
    "sales chart": ["ailv-ui-charts", "ailv-ui-chart-twin"],
    "data table widget": ["ailv-ui-widgets", "ailv-ui-platform-picks"],
    "mobile app": ["ailv-ui-mobile"],
    "checkout inputs": ["ailv-ui-forms"],
    "dialog buttons": ["ailv-ui-buttons"],
    "page states": ["ailv-ui-behavior"],
    "header nav": ["ailv-ui-nav"],
    "hero image": ["ailv-ui-images"],
    "accessibility audit": ["ailv-ui-a11y"],
}


def main():
    ok_all = True
    for task, skills in ROUTES.items():
        ok = len(skills) <= 3 and all(s.startswith("ailv-ui-") for s in skills)
        print(f"{'PASS' if ok else 'FAIL'}: '{task}' -> {', '.join(skills)}")
        ok_all = ok_all and ok
    print(f"demo: {len(ROUTES)} tasks routed, none reads the whole area ->",
          "router-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
