# ailv-ops-probes — worked example

Input: liveness checks process-alive (fail -> restart); readiness pings
db and queue with 2s timeouts (fail -> shed load); unready pod stays alive
but out of rotation; neither probe uses the user-serving handler.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: liveness split from readiness
PASS: probes check real deps with timeouts
PASS: unready pod alive but out of rotation
PASS: failing readiness sheds load, liveness restarts
PASS: no probe uses the user-serving handler
probes: liveness=['process alive'] readiness=['db ping', 'queue ping']
```

Exit code: 0. Restart and traffic decisions fully separated.
