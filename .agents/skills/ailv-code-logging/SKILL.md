---
name: ailv-code-logging
description: "You can't respond to an attack you never recorded or never noticed."
sources:
  - title: NIST SP 800-92 log management
    url: https://csrc.nist.gov/pubs/sp/800/92/final
helper: scripts/helper.py
example: examples/output.md
---

# Logs that catch break-ins

`ailv-code-logging` (Logs that catch break-ins): Log the events that catch break-ins: failed logins, validation failures, permission denials, and spikes in costly endpoints. Keep logs structured (who, what, when) and secret-free — logs get copied and shared. Watch them with an alert, not just storage: an unread log is decoration.

## Checks

- auth and deny events logged
- no secrets in logs
- alerts on spikes, not just storage
