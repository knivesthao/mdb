# ailv-sec-runbooks — worked example

Input: demo breach-class playbooks baked into `scripts/helper.py`, run from
inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
severity/escalation decided in advance: SEV1->page+exec notify, SEV2->page oncall, SEV3->ticket
[PASS] ransomware: drilled 2026-10-20 (19d ago), playbook updated=True, steps=3
[PASS] leaked-secret: drilled 2026-09-01 (68d ago), playbook updated=True, steps=3
[FAIL] phishing: never drilled -> improvisation risk
self-check: FAIL (1 playbooks need drilling/updating)
```

Reading it: containment per breach class, severity paths pre-decided, drills
update the playbook; the undrilled phishing playbook is flagged. Exit
code 0.
