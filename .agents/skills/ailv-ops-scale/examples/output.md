# ailv-ops-scale — worked example

Input: queue depth 450, 50 messages per replica, bounds 2..12 replicas,
bottleneck is stateless workers, autoscale path load-tested.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: scales on real signal (queue_depth)
PASS: min/max bounds cap the bill (2..12)
PASS: scales bottleneck (workers), stateless first
PASS: autoscale path load-tested
scale: depth 450 / 50 per replica -> 9 replicas (bounds 2..12)
```

Exit code: 0. 9 replicas: inside bounds, driven by queue depth.
