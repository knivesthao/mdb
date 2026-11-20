# ailv-sec-index — worked example

Input: demo queries baked into `scripts/helper.py`, run from inside the
skill folder:

```
python3 scripts/helper.py
```

Real output:

```
router demo: one question -> one skill (never read them all)
[PASS] 'cve backlog of criticals' -> ailv-sec-vuln (want ailv-sec-vuln)
[PASS] 'enterprise sso rollout' -> ailv-sec-sso (want ailv-sec-sso)
[PASS] 'image scan failing' -> ailv-sec-scan (want ailv-sec-scan)
[PASS] 'leaked key in repo' -> ailv-sec-secretscan (want ailv-sec-secretscan)
[PASS] 'token lifetime policy' -> ailv-sec-session (want ailv-sec-session)
[PASS] 'siem alert flood' -> ailv-sec-siem (want ailv-sec-siem)
[PASS] 'waf rule tuning' -> ailv-sec-waf (want ailv-sec-waf)
[PASS] 'impossible travel login' -> ailv-sec-anomaly (want ailv-sec-anomaly)
[PASS] 'breach drill schedule' -> ailv-sec-runbooks (want ailv-sec-runbooks)
[PASS] 'os patch window' -> ailv-sec-patch (want ailv-sec-patch)
[PASS] 'audit evidence pack' -> ailv-sec-compliance (want ailv-sec-compliance)
[PASS] 'login form validation' -> ailv-code-auth (want ailv-code-auth)
[PASS] app basics stay in ailv-code-auth; humans verify counts/drills
self-check: PASS (0 misroutes)
```

Reading it: each question routes to exactly one skill, app basics stay in
ailv-code-auth. Exit code 0.
