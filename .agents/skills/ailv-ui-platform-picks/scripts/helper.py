"""Self-check: library names per framework + standalone setup gates."""

PICKS = {
    ("react", "table"): "TanStack Table", ("react", "kanban"): "dnd-kit",
    ("react", "dialog"): "Radix", ("vue", "table"): "TanStack Vue",
    ("vue", "combo"): "Headless UI Combobox", ("angular", "table"): "Material table",
    ("angular", "dialog"): "Material dialog",
}
STANDALONE = {"react": "Vite/CRA client-only: skip server clauses",
              "vue": "standalone Vite client-only: skip Nuxt clauses"}


def resolve(framework, widget, setup="full"):
    name = PICKS.get((framework, widget), "native-media-api")
    if setup == "standalone" and framework in STANDALONE:
        return f"{name} ({STANDALONE[framework]})"
    return name


def main():
    cases = [(("react", "table", "full"), "TanStack Table"),
             (("vue", "combo", "full"), "Headless UI Combobox"),
             (("react", "table", "standalone"), "TanStack Table"),
             (("angular", "dialog", "full"), "Material dialog")]
    ok_all = True
    for args, want in cases:
        got = resolve(*args)
        ok = want in got
        if args[2] == "standalone":
            ok = ok and "skip" in got.lower()
        print(f"{'PASS' if ok else 'FAIL'}: {args} -> {got}")
        ok_all = ok_all and ok
    print("demo: 4 resolves incl. standalone gate ->",
          "picks-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
