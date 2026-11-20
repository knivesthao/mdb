# ailv-code-injection — worked example

## Input

Demo statements baked into `scripts/helper.py`: string-glued SQL,
parameterized SQL, `os.system` concatenation, `subprocess.run` list form,
and `mark_safe(user_bio)`.

## Command

```sh
python3 scripts/helper.py
```

## Real output

```text
UNSAFE query interpolation :: query = 'SELECT * FROM users WHERE name = \'' + name + '\''
safe (parameterized) :: cursor.execute('SELECT * FROM users WHERE name = %s', (name,
UNSAFE shell command :: os.system('convert ' + filename)
safe (parameterized) :: subprocess.run(['convert', filename], check=True)
UNSAFE unescaped markup :: page = mark_safe(user_bio)
rule: ORM/parameters everywhere; user HTML never marked safe
```
