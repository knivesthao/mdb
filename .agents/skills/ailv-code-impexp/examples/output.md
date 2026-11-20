# ailv-code-impexp — worked example

Input (demo, baked into `scripts/helper.py`): a 4-row CSV import with
two bad rows (`2,NOT-AN-EMAIL,xx` and `4,,40`), read in bounded
batches of 2.

Run: `python3 scripts/helper.py` (from the skill folder). Real output:

```
progress: 2/4 rows scanned
progress: 4/4 rows scanned
imported: 2, quarantined: 2
  quarantine: 2,NOT-AN-EMAIL,xx
  quarantine: 4,,40
notify: job complete + error report attached
```

Reading: the bulk move runs as a background-style job with progress,
bad rows are quarantined instead of failing the file, reads stay in
bounded batches, and completion notifies with the error report. Exit
code 0.
