"""ailv-code-logging helper: structured, secret-free security logging demo."""
import json
import re

SECRET_PAT = re.compile(r"(password|api[_-]?key|token|secret)\s*=\s*\S+", re.I)


def redact(text):
    return SECRET_PAT.sub(r"\1=***", text)


def log(event, **fields):
    record = {"event": event, **fields}
    print(redact(json.dumps(record, sort_keys=True)))


def main():
    log("login_failed", who="bob", when="2026-01-01T00:00:00Z", reason="bad password")
    log("validation_failed", who="anon", field="age", reason="negative")
    log("permission_denied", who="bob", action="delete")
    log("costly_spike", endpoint="/api/report", rpm=900)
    print("redaction demo: " + redact("login with password=hunter2 ok"))
    print("rule: auth+deny events logged; no secrets; alerts on spikes")


if __name__ == "__main__":
    main()
