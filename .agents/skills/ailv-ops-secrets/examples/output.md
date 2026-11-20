# ailv-ops-secrets — worked example

Input: repo with no committed secrets; 2 vault secrets runtime-injected,
per-env values, ages 12d/5d inside the 30d TTL; all reads from expected
places; vault seeded out of band with no agent-held root.

Command (run from inside the skill folder):

```
python3 scripts/helper.py
```

Actual output:

```
PASS: runtime injection only, never committed
PASS: no static value shared across envs
PASS: rotation automatic, none expired
PASS: reads audited, no unexpected readers
PASS: vault seeded out of band, no agent root
secret db/password (prod): age 12d/ttl 30d via runtime
secret api/key (staging): age 5d/ttl 30d via runtime
```

Exit code: 0. No committed secrets, rotation current, reads audited.
