# ailv-sec-vuln — worked example

Input: demo findings baked into `scripts/helper.py` (4 CVEs of mixed
severity/reachability), run from inside the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
finding/severity/reachable/owner/deadline/verdict
CVE-2026-1001/critical/reachable=True/owner=team-api/2026-11-15/BLOCK-CI
CVE-2026-1002/high/reachable=True/owner=team-web/2026-12-08/OPEN issues=['closure needs retest']
CVE-2026-1003/medium/reachable=False/owner=NONE/2027-02-06/OPEN issues=['no owner', 'closure needs retest']
CVE-2026-1004/low/reachable=False/owner=team-api/2027-05-07/OK
scanner errors: fail closed (build blocked on scanner error)
mean-time-to-remediate (demo): 28.3 days over 3 closed
self-check: FAIL (2 findings need attention)
```

Reading it: reachable findings rank first, the critical reachable one blocks
CI, scanner errors fail closed, and two findings stay open (no owner / no
retest). Exit code 0.
