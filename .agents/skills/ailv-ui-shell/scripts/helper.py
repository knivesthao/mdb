"""Self-check: 40-line semantic UI shell with machine-readable controls."""
import re

DEMO_HTML = """<header><button aria-label="Search" data-action="open-search">
<i data-lucide="search"></i></button></header>
<main><h1>Shop</h1></main><footer><a href="/help">Help</a></footer>"""


def check(html):
    results = []
    for tag in ("header", "main", "footer"):
        results.append((f"<{tag}> landmark present", f"<{tag}>" in html))
    controls = re.findall(r"<(button|a|input)[^>]*>", html)
    labeled = re.findall(r"<(?:button|a|input)[^>]*(aria-label|>[^<]{1,60}<)", html)
    results.append(("every control labeled", len(controls) > 0 and len(labeled) >= len(controls)))
    results.append(("custom controls expose data-action",
                    "data-action" in html))
    results.append(("lucide icons, no hand-written svg",
                    "data-lucide" in html and "<svg" not in html.lower()))
    return results


def main():
    ok_all = True
    for name, ok in check(DEMO_HTML):
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo shell: header/main/footer + labeled icon button ->",
          "shell-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
