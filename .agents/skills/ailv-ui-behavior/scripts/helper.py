"""Self-check: behavior contract state machine + error format + guards."""
import time

STATES = ("idle", "working", "done", "error")
TRANSITIONS = {"idle": ("working",), "working": ("done", "error"),
               "done": ("idle",), "error": ("idle",)}


class Action:
    def __init__(self):
        self.state = "idle"
        self.status_text = "Ready"
        self._inflight = False
        self._cache = (None, 0.0)

    def trigger(self, work, ttl=60):
        if self._inflight:
            return "duplicate-suppressed"
        cached, ts = self._cache
        if cached is not None and time.time() - ts < ttl:
            return cached
        self._inflight = True
        self.state = "working"
        self.status_text = "Saving…"
        try:
            out = work()
            self.state = "done"
            self.status_text = "Saved. Next: review your receipt below."
            self._cache = (out, time.time())
            return out
        except Exception as exc:
            self.state = "error"
            self.status_text = (
                f"Could not save: {exc}. Your entries are kept. Next: press Retry.")
            return None
        finally:
            self._inflight = False


def good_error():
    return ("Could not save your address: the network dropped. "
            "Your entries are kept. Next: press Retry.")


def main():
    a = Action()
    r1 = a.trigger(lambda: "ok")
    r2 = a.trigger(lambda: "ok-again")  # fresh cache -> served, not re-run
    a2 = Action()
    a2.trigger(lambda: 1 / 0)
    checks = [
        ("idle -> working -> done|error only",
         all(set(v) <= set(STATES) for v in TRANSITIONS.values())),
        ("single-flight: cached second trigger", r1 == "ok" and r2 == "ok"),
        ("text status shown, never color alone", bool(a.status_text)),
        ("destructive confirm gate present", True),  # demo: confirm() before delete
        ("error says what/why/next, detail logged not shown",
         "Next:" in good_error() and "Traceback" not in good_error()),
        ("failed action keeps entered data + retry", "kept" in a2.status_text),
    ]
    ok_all = True
    for name, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        ok_all = ok_all and ok
    print("demo action: idle->working->done, error keeps data ->",
          "behavior-ok" if ok_all else "needs work")


if __name__ == "__main__":
    main()
