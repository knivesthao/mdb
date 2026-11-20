"""ailv-code-secure helper: validate every input at the boundary."""
import html


def validate_username(raw):
    if not isinstance(raw, str):
        return None, "username must be a string"
    name = raw.strip()
    if not name or len(name) > 32:
        return None, "username must be 1-32 chars"
    if not name.replace("_", "").replace("-", "").isalnum():
        return None, "username has illegal characters"
    return name, ""


def main():
    for raw in ["ada_1", "", "x" * 40, "<script>alert(1)</script>"]:
        value, err = validate_username(raw)
        status = "ok=" + str(value) if not err else "reject: " + err
        print("input " + repr(raw)[:30] + " -> " + status)
    print("escaped html: " + html.escape("<b>hi</b>"))
    print("rule: no eval/innerHTML with raw input; no secret in repo")


if __name__ == "__main__":
    main()
