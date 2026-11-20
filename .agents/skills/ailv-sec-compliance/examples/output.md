# ailv-sec-compliance — worked example

Input: demo control map baked into `scripts/helper.py`, run from inside the
skill folder:

```
python3 scripts/helper.py
```

Real output:

```
regulated data first: PHI->auditlog+crypto+rbac+retention, PAN->tokenize, personal->retention+deletion
[PASS] C1 access reviews: proven by siem quarterly export (continuous)
[PASS] C2 change tickets on deploys: proven by pipeline log (continuous)
[PASS] C3 PHI access audit: proven by auditlog per-access (continuous)
[FAIL] C4 card PAN never stored: unmapped -> audit finding waiting
[PASS] C5 GDPR deletion on request: proven by retention job receipt (continuous)
self-check: FAIL (1 controls unproven)
```

Reading it: regulated data decides the control set, every control needs a
mapped continuous proof; the unmapped PAN control is an audit finding
waiting. Exit code 0.
