def run_test_cases(function, test_cases):
    tests_passed = 0
    results = []

    for test_case in test_cases:
        input_value = test_case["input"]
        expected = test_case["expected"]

        try:
            actual = function(input_value)
            passed = actual == expected

        except Exception as error:
            actual = f"{type(error).__name__}: {error}"
            passed = False

        if passed:
            tests_passed += 1

        results.append({
            "input": input_value,
            "expected": expected,
            "actual": actual,
            "passed": passed
        })

    return {
        "tests_passed": tests_passed,
        "total_tests": len(test_cases),
        "results": results
    }