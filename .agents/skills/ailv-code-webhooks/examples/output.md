# ailv-code-webhooks — worked example

Input (demo, baked into `scripts/helper.py`): an `order.paid` v2 event
`evt-1` delivered to `https://acme.example/hook` (fails once, retries
with backoff), then a customer replay of the same event.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
https://acme.example/hook: evt-1 ok after 2 tries (sig a49f07bf..), rx applied
https://acme.example/hook: evt-1 ok after 1 tries (sig a49f07bf..), rx duplicate-ignored (replay: safe resend)
delivery log (customer-visible): [{"event": "evt-1", "try": 1, "status": "5xx"}, {"event": "evt-1", "try": 2, "status": "ok"}, {"event": "evt-1", "try": 1, "status": "ok"}]
never fire-and-forget: retry with backoff + replay kept
```

Reading: the payload is signed and schema-versioned, failures retry
with backoff into a per-destination delivery log the customer can
replay, and the receiver dedups on the event id so resends are safe.
Exit code 0.
