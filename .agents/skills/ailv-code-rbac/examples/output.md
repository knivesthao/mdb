# ailv-code-rbac — worked example

Input (demo, baked into `scripts/helper.py`): two rows in different
workspaces (acme invoice-1, globex invoice-9); member vs admin roles;
four allow/deny probes plus an impersonation case.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
PASS  acme/member orders.read row1 -> allow
PASS  acme/member orders.read row2 -> deny
PASS  acme/member members.write row1 -> deny
PASS  acme/admin members.write row1 -> allow
impersonation: consent record + audit trail present -> allowed, logged
ALL: PASS
```

Reading: the cross-tenant read is denied server-side (row2), the member
cannot escalate to `members.write`, and impersonation only passes with
consent + audit. Exit code 0.
