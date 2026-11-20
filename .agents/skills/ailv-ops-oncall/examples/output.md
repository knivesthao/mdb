# ailv-ops-oncall — worked example

Input: weekly rotation (amy, bo, cy) with primary->secondary->manager
escalation; 2 pages each linked to a runbook; blameless postmortem for
INC-7 filed 2 days later with both action items done.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: scheduled rotation with escalation
PASS: never a single hero with no notes
PASS: runbook per page
PASS: blameless postmortem within days
PASS: action items tracked to done
oncall: weekly rotation (amy,bo,cy), 2 pages, 1 reviews
```

Exit code: 0. No hero paging, every page has a runbook.
