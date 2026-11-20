"""ailv-code-track helper: one emit helper, JSONL today, warehouse tomorrow."""
import json
import os

SINK = "/tmp/ailv-track-demo.jsonl"
FORBIDDEN = ("name", "email", "api_key", "password")


def emit(action, **fields):
    for key in fields:
        if key in FORBIDDEN:
            raise ValueError("identity in event: " + key)
    record = {"action": action, **fields}
    with open(SINK, "a") as fh:
        fh.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def main():
    if os.path.exists(SINK):
        os.remove(SINK)
    for args in [("used", {"feature": "search"}), ("copied", {"feature": "snippet"}),
                 ("failed", {"feature": "checkout"}), ("slow", {"feature": "report"})]:
        print("emit: " + json.dumps(emit(args[0], **args[1]), sort_keys=True))
    try:
        emit("used", email="a@x.com")
    except ValueError as exc:
        print("blocked: " + str(exc))
    print("sink today: " + SINK + " (swap to warehouse without touching callers)")


if __name__ == "__main__":
    main()
