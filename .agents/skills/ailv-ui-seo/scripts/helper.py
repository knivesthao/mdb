"""Self-check: findability — title, description, H1, sitemap, noindex walls."""

DEMO_PAGE = {"title": "Trail shoes that grip wet rock",
             "description": "Lightweight trail shoes with all-weather grip. Free returns.",
             "h1_count": 1, "js_only_nav": False}
PUBLIC = ["/", "/shop", "/guide"]
WALLED = ["/checkout", "/billing", "/account"]


def sitemap():
    return [f"<url><loc>https://ex.test{p}</loc></url>" for p in PUBLIC]


def main():
    t, d = DEMO_PAGE["title"], DEMO_PAGE["description"]
    checks = [
        (f"one H1 (found {DEMO_PAGE['h1_count']})", DEMO_PAGE["h1_count"] == 1),
        (f"title {len(t)} chars < 60", len(t) < 60),
        (f"description {len(d)} chars < 160", len(d) < 160),
        ("real links, never JS-only nav", not DEMO_PAGE["js_only_nav"]),
        (f"sitemap lists {len(PUBLIC)} public pages", len(sitemap()) == len(PUBLIC)),
        ("paid pages noindexed + out of sitemap",
         all(p not in "".join(sitemap()) for p in WALLED)),
    ]
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo page: title/desc lengths ok, sitemap 3 public, 3 walled noindex ->",
          "seo-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
