# ailv-data-streams — worked example

Input: events at ts 61, 59 (within 10s horizon), 130 (advances
watermark), 85 (45s late, beyond horizon).

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
EVENT ts=61 advances watermark=61
EVENT ts=59 in-window (within horizon)
EVENT ts=130 advances watermark=130
EVENT ts=85 late -> side-channel
WINDOW emit trigger=watermark sum=6 side=[9]
WATERMARK lag=0s monitored -> PASS
PASS
```

Windows plus watermarks: in-horizon lates settle, beyond-horizon rides
the side channel, watermark lag is monitored.
