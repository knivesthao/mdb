# ailv-code-secure — worked example

## Input

Demo usernames baked into `scripts/helper.py`: `ada_1`, empty string,
a 40-char string, and `<script>alert(1)</script>`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
input 'ada_1' -> ok=ada_1
input '' -> reject: username must be 1-32 chars
input 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx -> reject: username must be 1-32 chars
input '<script>alert(1)</script>' -> reject: username has illegal characters
escaped html: &lt;b&gt;hi&lt;/b&gt;
rule: no eval/innerHTML with raw input; no secret in repo
```
