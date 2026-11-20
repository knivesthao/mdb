---
name: ailv-ops-probes
description: "Instant-healthy sends traffic to broken pods mid-deploy; conflated probes restart what should drain."
sources:
  - title: Kubernetes probes
    url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/
helper: scripts/helper.py
example: examples/output.md
---

# Liveness split from readiness

`ailv-ops-probes` (Liveness split from readiness): Separate liveness (restart me) from readiness (send me traffic): a pod that cannot serve stays alive but out of rotation. Probes check real dependencies with timeouts — instant-healthy sends traffic to broken pods mid-deploy. Failing readiness sheds load; failing liveness restarts. Never probe with the same handler that serves users.

## Checks

- liveness split from readiness
- probes check real deps
- no user-handler probes
