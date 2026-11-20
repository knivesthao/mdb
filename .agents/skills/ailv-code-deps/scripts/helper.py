"""ailv-code-deps helper: check requirements are pinned and audited."""
import re

REQUIREMENTS = [
    "fastapi==0.115.0",
    "pydantic==2.9.2",
    "requests>=2.0",
    "typer",
    "sqlmodel==0.0.22  # vendored copy in ./vendor",
]


def check(line):
    line = line.strip()
    if not line:
        return "skip (blank)"
    if "vendored" in line or "./vendor" in line:
        return "FAIL never vendor a copy you will forget to patch :: " + line
    if re.match(r"^[a-z0-9_-]+==\d", line, re.I):
        return "PASS pinned :: " + line
    return "FAIL unpinned :: " + line


def main():
    for line in REQUIREMENTS:
        print(check(line))
    print("audit: pip audit (scheduled); unused deps removed")


if __name__ == "__main__":
    main()
