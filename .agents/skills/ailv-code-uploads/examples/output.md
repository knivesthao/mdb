# ailv-code-uploads — worked example

Input (demo, baked into `scripts/helper.py`): a PNG payload lyingly
named `cute.png.exe`, plus an over-cap file. (The storage key is a fresh
uuid each run; this is the output of the recorded run.)

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
direct PUT https://storage.local/uploads/14f516bee2cd48b4be22f4e13e2e1160?exp=300&sig=bbdd1328c97a354c [image/png, private] (lied name 'cute.png.exe' ignored)
reject: size capped at edge
serve: signed URL, minutes TTL, private bucket (no public reads)
suspect file -> async scan -> quarantine on hit (clean here)
```

Reading: the file goes direct to storage on a short-lived signed URL
(the app server never sees the bytes), MIME comes from content sniffing
not the filename, sizes are capped at the edge, each upload gets a
unique key, and everything stays private by default. Exit code 0.
