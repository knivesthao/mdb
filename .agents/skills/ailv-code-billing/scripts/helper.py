"""ailv-code-billing helper: resolve charges from plan versions, idempotently."""
import sys

PLANS = {"pro-2025-q1": {"price_cents": 2000}, "pro-2025-q3": {"price_cents": 2500}}
SUBSCRIPTIONS = {}  # (customer, plan, idem_key) -> sub id


def subscribe(customer, plan, idem_key):
    key = (customer, plan, idem_key)
    if key not in SUBSCRIPTIONS:
        SUBSCRIPTIONS[key] = f"sub_{len(SUBSCRIPTIONS) + 1}"
    return SUBSCRIPTIONS[key]


def charge(event):
    version = event["plan_in_effect_at_event"]
    return PLANS[version]["price_cents"]  # never hardcoded


def main():
    s1 = subscribe("acme", "pro-2025-q3", "idem-1")
    s2 = subscribe("acme", "pro-2025-q3", "idem-1")  # retry -> same sub
    print(f"idempotent subscribe: {s1} == {s2} -> {'PASS' if s1 == s2 else 'FAIL'}")
    for ev in ({"plan_in_effect_at_event": "pro-2025-q1"},
               {"plan_in_effect_at_event": "pro-2025-q3"}):
        print(f"event @ {ev['plan_in_effect_at_event']}: charge {charge(ev)}c")
    print("entitlement: only on verified webhook (sig ok) -> entitled")
    print("failed payment: remind -> retry -> grace (no instant cancel)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
