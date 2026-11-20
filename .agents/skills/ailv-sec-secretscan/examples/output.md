# ailv-sec-secretscan — worked example

Input: demo 5-line push diff baked into `scripts/helper.py`, run from inside
the skill folder:

```
python3 scripts/helper.py
```

Real output:

```
push-time scan of 5 lines: 3 hit(s)
  line 2 [aws-key]: aws_access = 'AKIAIOSFODNN7EXAMPLE'...
  line 3 [private-key]: -----BEGIN RSA PRIVATE KEY-----...
  line 4 [api-token]: api_key = 'sk-live-abc123XYZ789qrs'...
verdict: BLOCK PUSH
response order: 1) revoke secret now 2) investigate 3) purge history+forks
              4) rotate everything the secret could reach
post-merge detection is backup, not the plan
```

Reading it: push blocked on secret shapes, revoke-first ordering shown
(all three hits are synthetic demo strings, not live secrets). Exit code 0.
