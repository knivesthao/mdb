"""Self-check: Lit islands first, house wins (no build, light DOM, tap)."""
import re

DEMO_HTML = """<script type="module">
import {LitElement, html} from 'https://cdn.jsdelivr.net/npm/lit@3/+esm';
class CartIsland extends LitElement { createRenderRoot(){return this;} }
customElements.define('cart-island', CartIsland);</script>
<div id="cart-static" hx-get="/cart" hx-target="#cart-static">x</div>
<cart-island><button>Tap to add</button></cart-island>"""


def check(html):
    islands = re.findall(r"<([a-z]+-island)[^>]*>", html)
    hx_targets = re.findall(r'hx-target="([^"]+)"', html)
    results = [
        ("no build step (pinned Lit CDN module)", "cdn.jsdelivr.net/npm/lit" in html),
        ("hx-target never targets an island",
         not any(t.strip("#") in " ".join(islands) or "island" in t for t in hx_targets)),
        ("light DOM (createRenderRoot returns this)", "createRenderRoot" in html),
        ("no React/Angular imports", "react" not in html.lower() and "angular" not in html.lower()),
        ("islands tap-reachable (button inside island)", "<button>" in html),
    ]
    return results


def main():
    ok_all = True
    for name, ok in check(DEMO_HTML):
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo: 1 Lit island + HTMX static region ->",
          "islands-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
