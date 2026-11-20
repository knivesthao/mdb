# ailv-code-reasoning — worked example

## Input

Panel events baked into `scripts/helper.py`: routine step, decision,
done work, full trace, blocked or failed.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
routine step     -> one line, no report
decision         -> decision plus evidence, never the choosing
done work        -> what changed plus proof it ran
full trace       -> local log only, excluded from context
blocked or failed -> exactly what is needed to unblock, nothing else

shapes: 5, reasoning hidden, proof visible
```
