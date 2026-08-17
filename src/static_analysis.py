import ast
from pathlib import Path


def clamp(value, minimum=0, maximum=10):
    return max(minimum, min(maximum, value))


def analyze_code(file_path):
    source = Path(file_path).read_text(
        encoding="utf-8"
    )

    notes = []

    try:
        tree = ast.parse(source)

    except SyntaxError as error:
        return {
            "readability": 0,
            "code_quality": 0,
            "notes": [
                f"SyntaxError: {error}"
            ]
        }

    readability = 10.0
    code_quality = 10.0

    lines = source.splitlines()

    long_lines = [
        line
        for line in lines
        if len(line) > 100
    ]

    if long_lines:
        readability -= 1
        notes.append(
            "Contains lines longer than 100 characters."
        )

    if not ast.get_docstring(tree):
        readability -= 0.5
        notes.append(
            "Module has no docstring."
        )

    functions = [
        node
        for node in ast.walk(tree)
        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef
            )
        )
    ]

    if not functions:
        code_quality -= 2
        notes.append(
            "No function definitions found."
        )

    for function in functions:
        end_line = getattr(
            function,
            "end_lineno",
            function.lineno
        )

        function_length = (
            end_line
            - function.lineno
            + 1
        )

        if function_length > 40:
            readability -= 1
            notes.append(
                f"Function '{function.name}' is longer than 40 lines."
            )

    bare_except = any(
        isinstance(node, ast.ExceptHandler)
        and node.type is None
        for node in ast.walk(tree)
    )

    if bare_except:
        code_quality -= 2
        notes.append(
            "Contains a bare except statement."
        )

    dangerous_calls = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id in {
                    "eval",
                    "exec"
                }:
                    dangerous_calls.append(
                        node.func.id
                    )

    if dangerous_calls:
        code_quality -= 2
        notes.append(
            "Contains eval or exec."
        )

    wildcard_import = any(
        isinstance(node, ast.ImportFrom)
        and any(
            alias.name == "*"
            for alias in node.names
        )
        for node in ast.walk(tree)
    )

    if wildcard_import:
        code_quality -= 1
        notes.append(
            "Contains wildcard import."
        )

    return {
        "readability": round(
            clamp(readability),
            2
        ),
        "code_quality": round(
            clamp(code_quality),
            2
        ),
        "notes": notes
    }