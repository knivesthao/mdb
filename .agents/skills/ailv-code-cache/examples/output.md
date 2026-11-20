# ailv-code-cache — worked example

## Input

Demo key baked into `scripts/helper.py`: `report:7d` set, read via ETag,
then invalidated on write.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
get hit: computed-answer
etag: f6dbfe6c -> 304 Not Modified on match
after write invalidate, get: None
rule: never cache user secrets; invalidate on write, not timer alone
```
