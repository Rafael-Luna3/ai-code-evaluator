from src.static_analysis import (
    analyze_code
)


def test_valid_code(
    tmp_path
):
    file_path = (
        tmp_path
        / "solution.py"
    )

    file_path.write_text(
        (
            "def add(a, b):\n"
            "    return a + b\n"
        ),
        encoding="utf-8"
    )

    result = analyze_code(
        file_path
    )

    assert (
        0
        <= result["readability"]
        <= 10
    )

    assert (
        0
        <= result["code_quality"]
        <= 10
    )


def test_invalid_syntax(
    tmp_path
):
    file_path = (
        tmp_path
        / "solution.py"
    )

    file_path.write_text(
        "def broken(:",
        encoding="utf-8"
    )

    result = analyze_code(
        file_path
    )

    assert result[
        "readability"
    ] == 0

    assert result[
        "code_quality"
    ] == 0