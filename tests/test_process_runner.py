from src.process_runner import (
    execute_candidate
)


def test_successful_execution(
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

    result = execute_candidate(
        solution_file=str(
            file_path
        ),
        function_name="add",
        args=[2, 3]
    )

    assert result[
        "status"
    ] == "success"

    assert result[
        "result"
    ] == 5


def test_missing_function(
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

    result = execute_candidate(
        solution_file=str(
            file_path
        ),
        function_name="missing",
        args=[2, 3]
    )

    assert result[
        "status"
    ] == "error"

    assert result[
        "error_type"
    ] == "AttributeError"


def test_timeout(
    tmp_path
):
    file_path = (
        tmp_path
        / "solution.py"
    )

    file_path.write_text(
        (
            "def loop():\n"
            "    while True:\n"
            "        pass\n"
        ),
        encoding="utf-8"
    )

    result = execute_candidate(
        solution_file=str(
            file_path
        ),
        function_name="loop",
        timeout_seconds=1
    )

    assert result[
        "status"
    ] == "timeout"