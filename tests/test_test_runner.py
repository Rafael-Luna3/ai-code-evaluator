from src.test_runner import run_test_cases


def correct_function(numbers):
    return max(numbers)


def wrong_function(numbers):
    return numbers[0]

def sum_numbers(a, b):
    return a + b


def test_all_cases_pass():
    test_cases = [
        {
            "args": [[1, 2, 3]],
            "expected": 3
        },
        {
            "args": [[5, 10, 2]],
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
            "args": [[3, 1, 2]],
            "expected": 3
        },
        {
            "args": [[5, 10, 2]],
            "expected": 10
        }
    ]

    result = run_test_cases(
        function=wrong_function,
        test_cases=test_cases
    )

    assert result["tests_passed"] == 1
    assert result["total_tests"] == 2


def test_function_with_multiple_arguments():
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
        function=sum_numbers,
        test_cases=test_cases
    )

    assert result["tests_passed"] == 2
    assert result["total_tests"] == 2