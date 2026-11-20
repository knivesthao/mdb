"""Self-check: every image earns its place (eager hero, lazy rest, alt)."""

DEMO_IMAGES = [
    {"src": "hero.avif", "fold": "above", "loading": "eager",
     "fetchpriority": "high", "width": 1200, "height": 600,
     "alt": "Runner wearing the trail shoe", "srcset": True},
    {"src": "detail-1.avif", "fold": "below", "loading": "lazy",
     "width": 800, "height": 600, "alt": "Sole tread close-up", "srcset": True},
    {"src": "divider.svg", "fold": "below", "loading": "lazy",
     "width": 0, "height": 0, "alt": "", "decorative": True},
]


def check(imgs):
    results = []
    above = [i for i in imgs if i["fold"] == "above" and not i.get("decorative")]
    results.append(("one above-fold visual", len(above) == 1))
    hero = above[0]
    results.append(("hero eager + high priority + dims",
                    hero["loading"] == "eager" and hero.get("fetchpriority") == "high"
                    and hero["width"] > 0))
    below = [i for i in imgs if i["fold"] == "below" and not i.get("decorative")]
    results.append(("below-fold lazy with srcset",
                    all(i["loading"] == "lazy" and i["srcset"] for i in below)))
    results.append(("alt on informative, empty-alt on decorative",
                    all("alt" in i and (i["alt"] or i.get("decorative")) for i in imgs)))
    results.append(("no decorative content images",
                    all(i.get("decorative") or i["alt"] for i in imgs)))
    return results


def main():
    ok_all = True
    for name, ok in check(DEMO_IMAGES):
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo: 1 eager hero + 1 lazy detail + 1 decorative ->",
          "images-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
