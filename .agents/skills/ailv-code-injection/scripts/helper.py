"""ailv-code-injection helper: flag string-built queries/commands/markup."""
import re

DEMO = [
    "query = 'SELECT * FROM users WHERE name = \\'' + name + '\\''",
    "cursor.execute('SELECT * FROM users WHERE name = %s', (name,))",
    "os.system('convert ' + filename)",
    "subprocess.run(['convert', filename], check=True)",
    "page = mark_safe(user_bio)",
]


def check(line):
    if re.search(r"SELECT.*\+|\+.*SELECT|%.*%\s*%\s*\(|f['\"].*SELECT", line):
        return "UNSAFE query interpolation"
    if re.search(r"os\.system\s*\(.*\+|os\.popen|shell=True", line):
        return "UNSAFE shell command"
    if re.search(r"mark_safe\s*\(\s*user|innerHTML\s*=\s*user", line):
        return "UNSAFE unescaped markup"
    if re.search(r"execute\s*\(.*%s|subprocess\.run\s*\(\s*\[", line):
        return "safe (parameterized)"
    return "no pattern"


def main():
    for line in DEMO:
        print(check(line) + " :: " + line[:60])
    print("rule: ORM/parameters everywhere; user HTML never marked safe")


if __name__ == "__main__":
    main()
