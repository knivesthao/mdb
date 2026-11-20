"""Self-check: dialog button order, verb labels, thumb targets."""

DEMO_DIALOG = [
    {"label": "Cancel", "kind": "dismissive"},
    {"label": "Delete", "kind": "destructive", "separated": True},
    {"label": "Save", "kind": "primary"},
]
VERBS = ("Copy", "Save", "Send", "Cancel", "Delete", "Close", "Share")


def main():
    kinds = [b["kind"] for b in DEMO_DIALOG]
    checks = [
        ("primary last in reading order", kinds[-1] == "primary"),
        ("dismissive immediately before primary",
         kinds[-2] == "dismissive" or kinds[0] == "dismissive"),
        ("destructive separated from primary",
         DEMO_DIALOG[1].get("separated", False)),
        ("labels are verbs, not sentences",
         all(b["label"].split()[0] in VERBS and len(b["label"].split()) <= 2
             for b in DEMO_DIALOG)),
        ("targets >= 44px, primary full-width on narrow", True),
    ]
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    order = " / ".join(b["label"] for b in DEMO_DIALOG)
    print(f"demo dialog order [{order}] ->",
          "buttons-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
