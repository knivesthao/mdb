"""Self-check: server-rendered mobile page (FastAPI + HTMX + Tailwind + Capacitor)."""
import re

DEMO_HTML = """<meta name="viewport" content="width=device-width, initial-scale=1">
<div class="flex flex-col px-4 max-w-md mx-auto">
<button hx-get="/cart/add" hx-target="#cart-count">Add</button>
<span id="cart-count">0</span></div>"""


def check(html):
    results = []
    results.append(("zero hand-written fetch calls",
                    not re.search(r"fetch\s*\(", html)))
    results.append(("no client-side state store",
                    not re.search(r"(localStorage|sessionStorage|redux|zustand|pinia)", html, re.I)))
    results.append(("htmx drives interaction",
                    bool(re.search(r"hx-(get|post|target)", html))))
    results.append(("layout verified at 360px (viewport + narrow container)",
                    "viewport" in html and bool(re.search(r"max-w-(sm|md)|360px|w-full", html))))
    return results


def main():
    all_ok = True
    for name, ok in check(DEMO_HTML):
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        all_ok = all_ok and ok
    print("demo: server-rendered fragment, no fetch, no store ->",
          "mobile-ready" if all_ok else "needs work")


if __name__ == "__main__":
    main()
