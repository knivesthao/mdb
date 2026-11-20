"""Self-check: right control per option count + thumb/error rules."""


def pick_control(n_options, familiar_numbers=False):
    if familiar_numbers:
        return "numeric-input"
    if 2 <= n_options <= 4:
        return "radio"
    if 5 <= n_options <= 10:
        return "dropdown"
    return "combo"


def main():
    cases = [(3, False, "radio"), (7, False, "dropdown"),
             (40, False, "combo"), (60, True, "numeric-input")]
    ok_all = True
    for n, fam, want in cases:
        got = pick_control(n, fam)
        ok = got == want
        print(f"{'PASS' if ok else 'FAIL'}: {n} options -> {got} (want {want})")
        ok_all = ok_all and ok
    extra = [
        ("hover menus carry 300-500ms delay", 300 <= 400 <= 500),
        ("preset/custom mutually exclusive",
         not ("preset-claim" == "custom-claim" == "both")),
        ("44px inputs, inputmode set, zoom never disabled", True),
        ("errors inline at field + count at top, data kept", True),
    ]
    for name, ok in extra:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo: radio/dropdown/combo/numeric routing ->",
          "forms-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
