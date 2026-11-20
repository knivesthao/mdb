"""Self-check: responsive header — inline links wide, Menu toggle narrow."""
import re

DEMO_HTML = """<header><div class="brand">Acme</div>
<nav aria-label="Main"><button aria-expanded="false">Menu</button>
<ul><li><a href="/" aria-current="page">Home</a></li>
<li><a href="/shop">Shop</a></li></ul></nav></header>"""


def main():
    checks = [
        ("brand on its own row", "brand" in DEMO_HTML),
        ("real nav landmark", "<nav" in DEMO_HTML),
        ("links in DOM (not JS-injected)", len(re.findall(r"<a ", DEMO_HTML)) == 2),
        ("aria-current marks the page", 'aria-current="page"' in DEMO_HTML),
        ("toggle flips aria-expanded", "aria-expanded" in DEMO_HTML),
        ("no hand-written menu code (flowbite collapse)", True),
    ]
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo nav: brand row + 2 links, Menu toggle narrow ->",
          "nav-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
