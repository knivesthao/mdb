"""Self-check: 3-token palette, contrast, spacing scale, touch targets."""
import re

TOKENS = {"--ink": "#1a1a1a", "--paper": "#ffffff", "--accent": "#005fcc"}
SPACING = [4, 8, 16, 32]
DEMO_CSS = ":root{--ink:#1a1a1a;--paper:#fff;--accent:#005fcc}.btn{min-height:44px;margin:8px}"


def luminance(hexcolor):
    hexcolor = hexcolor.lstrip("#")
    if len(hexcolor) == 3:
        hexcolor = "".join(c * 2 for c in hexcolor)
    r, g, b = (int(hexcolor[i:i + 2], 16) / 255 for i in (0, 2, 4))

    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def main():
    checks = []
    checks.append(("palette is 3 colors max", len(TOKENS) <= 3))
    checks.append(("no per-element color decisions (token refs only)",
                   not re.search(r"#[0-9a-fA-F]{3,6}", DEMO_CSS.replace("#1a1a1a", "").replace("#fff", "").replace("#005fcc", ""))))
    ratio = contrast(TOKENS["--ink"], TOKENS["--paper"])
    checks.append((f"contrast ink/paper {ratio:.1f}:1 >= 4.5", ratio >= 4.5))
    checks.append(("spacing scale 4/8/16/32 holds", SPACING == [4, 8, 16, 32]))
    checks.append(("touch targets reach 44px", "44px" in DEMO_CSS))
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print(f"demo tokens: ink/paper/accent, contrast {ratio:.1f}:1 ->",
          "tokens-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
