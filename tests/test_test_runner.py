from src.test_runner import run_test_cases


def test_all_cases_pass():
    test_cases = [
        {
            "args": [5, 10],
            "expected": 15
        },
        {
            "args": [-2, 7],
            "expected": 5
        }
    ]

    result = run_test_cases(
        solution_file=(
            "examples/sum_solution.py"
        ),
        function_name="sum_numbers",
        test_cases=test_cases
    )

    assert result[
        "tests_passed"
    ] == 2

    assert result[
        "total_tests"
    ] == 2


def test_some_cases_fail():
    test_cases = [
        {
            "args": [[3, 1, 2]],
            "expected": 3
        },
        {
            "args": [[5, 10, 2]],
            "expected": 10
        }
    ]

    result = run_test_cases(
        solution_file=(
            "examples/bad_solution.py"
        ),
        function_name="find_largest",
        test_cases=test_cases
    )

    assert result[
        "tests_passed"
    ] == 1