# ailv-data-cdc — worked example

Input: WAL log with insert, update, delete (id 1), then insert (id 2);
consumer resumes from checkpoint.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
OFFSET 1 insert id=1
OFFSET 2 update id=1
OFFSET 3 delete id=1 propagated
OFFSET 4 insert id=2
STATE {2: 'c'} checkpoint=4
PASS
CHECK no polling: source=wal-log -> PASS
```

Deletes propagate, ordered offsets checkpoint so restarts resume.
