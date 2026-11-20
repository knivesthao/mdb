# ailv-data-upserts — worked example

Input: table `[{id:1}, {id:2}]`, batch updates id 2 and adds id 3,
watermark advances only after commit.

Command: `python3 scripts/helper.py` (run from inside the skill folder)

Real output:

```text
MERGE table=[{'id': 1, 'v': 'a'}, {'id': 2, 'v': 'b2'}, {'id': 3, 'v': 'c'}] watermark=2
CRASH resume from watermark=2 (never zero) -> rows=3
PASS
```

Keyed merge, no full overwrite; a crashed load resumes from the last
committed watermark.
