"""ailv-code-legacy helper: strangler routing, slice by slice, no flag-day."""
import sys

# Traffic share on the replacement per slice; old interface wraps both.
SLICES = [0, 10, 50, 100]


def route(sku, pct_new):
    # Anti-corruption layer: legacy quirk ("-" SKUs) normalized before new path.
    sku = sku.replace("-", "_")
    dest = "new" if hash(sku) % 100 < pct_new else "old"
    return dest, sku


def main():
    for pct in SLICES:
        dests = [route(s, pct)[0] for s in ("A-1", "B-2", "C-3", "D-4")]
        print(f"slice new={pct}%: {dests}")
    print("existing patterns followed first; dead old path deleted after 100% + clean drills")
    print("flag-day rewrite: no")
    return 0


if __name__ == "__main__":
    sys.exit(main())
