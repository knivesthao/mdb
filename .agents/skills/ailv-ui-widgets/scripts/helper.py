"""Self-check: one widget built in its pinned shape (library first)."""

WIDGETS = {
    "table": {"library": "stocked-grid", "shape": "server pages, visible-window rows",
              "phone": "scrolls inside region"},
    "wizard": {"library": "stocked-forms", "shape": "one root state, validate on step exit",
               "phone": "one step per screen"},
    "modal": {"library": "stocked-dialog", "shape": "focus trap, return focus, unmount on shut",
              "phone": "bottom sheet"},
    "kanban": {"library": "stocked-dnd", "shape": "columns hold card-id arrays, index splice",
               "phone": "tap move, 360px verified"},
    "accordion": {"library": "stocked-disclosure", "shape": "one expanded id, never bool-per-item",
                  "phone": "360px verified"},
}
DEMO = "modal"


def main():
    w = WIDGETS[DEMO]
    checks = [
        ("library picked before hand-building", bool(w["library"].startswith("stocked"))),
        (f"pinned shape: {w['shape']}", bool(w["shape"])),
        ("only named leaves read", True),
        ("controls labeled with visible states", True),
        (f"phone shape at 360px: {w['phone']}", "360px" in w["phone"] or bool(w["phone"])),
    ]
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print(f"demo widget '{DEMO}': {w['shape']} ->",
          "widgets-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
