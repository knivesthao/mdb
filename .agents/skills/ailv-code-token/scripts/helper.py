"""ailv-code-token helper: check nesting depth and dead exports on demo code."""
import ast

DEMO = '''
def route(kind):
    table = {"a": 1, "b": 2}
    if kind not in table:
        return 0
    return table[kind]

def unused_helper():
    return 99

def nested(x):
    if x:
        if x > 1:
            if x > 2:
                return "deep"
    return "shallow"
'''


def max_depth(node, depth=0):
    depths = [depth]
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.If, ast.For, ast.While, ast.With)):
            depths.append(max_depth(child, depth + 1))
        else:
            depths.append(max_depth(child, depth))
    return max(depths)


def main():
    tree = ast.parse(DEMO)
    names = {n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)}
    called = {n.func.id for n in ast.walk(tree)
              if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    dead = sorted(names - called - {"route", "nested"})
    print("functions: " + ", ".join(sorted(names)))
    print("dead exports: " + (", ".join(dead) if dead else "none"))
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            print("depth " + n.name + ": " + str(max_depth(n)))
    print("rule: nesting>2 fails; dead code deleted; one pattern per job")


if __name__ == "__main__":
    main()
