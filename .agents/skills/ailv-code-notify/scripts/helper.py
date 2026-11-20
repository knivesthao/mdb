"""ailv-code-notify helper: queued templated sends, deduped, unsubbed."""
import sys

QUEUE = []
SENT_KEYS = set()  # event-key dedup: retries never double-notify
PREFS = {"carol": {"channels": ["email"], "quiet": True},
         "dave": {"channels": ["email", "push"], "quiet": False}}
UNSUB = {"mallory"}  # working unsubscribe list


def enqueue(event_key, user, template, ctx):
    if user in UNSUB:
        return "suppressed: unsubscribed"
    QUEUE.append((event_key, user, template, ctx))
    return "queued"


def flush():
    for key, user, template, ctx in QUEUE:
        if key in SENT_KEYS:
            print(f"  {key} -> {user}: deduped (already sent)")
            continue
        body = template.format(**ctx)
        chans = PREFS[user]["channels"]
        if PREFS[user]["quiet"]:
            print(f"  {key} -> {user}: digested batch {chans}: {body}")
        else:
            print(f"  {key} -> {user}: send {chans}: {body}")
        SENT_KEYS.add(key)
    QUEUE.clear()


def main():
    print(enqueue("order-7:paid", "carol", "Order {n} paid.", {"n": 7}))
    print(enqueue("order-7:paid", "carol", "Order {n} paid.", {"n": 7}), "(retry)")
    print(enqueue("order-8:paid", "dave", "Order {n} paid.", {"n": 8}))
    print(enqueue("promo-1", "mallory", "Sale!", {}), "(marketing path separate)")
    flush()
    print("provider caps absorbed by queue; transactional/marketing paths split")
    return 0


if __name__ == "__main__":
    sys.exit(main())
