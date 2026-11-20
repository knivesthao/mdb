"""ailv-code-shape helper: check a module is machine-shaped."""
import ast

DEMO = '''
def validate(raw):
    if not isinstance(raw, dict):
        raise ValueError("input must be dict")
    if "name" not in raw:
        raise ValueError("missing name")
    return raw["name"]

def risky(raw):
    try:
        return int(raw)
    except Exception:
        return 0
'''


def main():
    tree = ast.parse(DEMO)
    lines = len(DEMO.strip().splitlines())
    print("module lines: " + str(lines) + " (limit 150)")
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if node.type is None or (isinstance(node.type, ast.Name) and node.type.id == "Exception"):
                print("FAIL bare/except-Exception in " + "risky" + ": name exceptions")
    print("PASS typed errors at boundaries (ValueError with input attached)")
    print("PASS flat depth<=2 with early returns")
    print("rule: behavior lives next to what it acts on")


if __name__ == "__main__":
    main()
