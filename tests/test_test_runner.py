from src.test_runner import run_test_cases


def correct_function(numbers):
    return max(numbers)


def wrong_function(numbers):
    return numbers[0]


def test_all_cases_pass():
    test_cases = [
        {
            "input": [1, 2, 3],
            "expected": 3
        },
        {
            "input": [5, 10, 2],
            "expected": 10
        }
    ]

    result = run_test_cases(
        function=correct_function,
        test_cases=test_cases
    )

    assert result["tests_passed"] == 2
    assert result["total_tests"] == 2


def test_some_cases_fail():
    test_cases = [
        {
            "input": [3, 1, 2],
            "expected": 3
        },
        {
            "input": [5, 10, 2],
            "expected": 10
        }
    ]

    result = run_test_cases(
        function=wrong_function,
        test_cases=test_cases
    )

    assert result["tests_passed"] == 1
    assert result["total_tests"] == 2