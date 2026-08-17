from src.process_runner import execute_candidate


def run_test_cases(
    solution_file,
    function_name,
    test_cases,
    timeout_seconds=2
):
    tests_passed = 0
    results = []

    for test_case in test_cases:
        args = test_case.get("args", [])
        kwargs = test_case.get("kwargs", {})
        expected = test_case["expected"]

        execution = execute_candidate(
            solution_file=solution_file,
            function_name=function_name,
            args=args,
            kwargs=kwargs,
            timeout_seconds=timeout_seconds
        )

        if execution["status"] == "success":
            actual = execution["result"]
            passed = actual == expected

        else:
            error_type = execution.get(
                "error_type",
                execution["status"]
            )

            message = execution.get(
                "message",
                ""
            )

            actual = f"{error_type}: {message}"
            passed = False

        if passed:
            tests_passed += 1

        results.append({
            "args": args,
            "kwargs": kwargs,
            "expected": expected,
            "actual": actual,
            "passed": passed,
            "execution_status": execution["status"]
        })

    return {
        "tests_passed": tests_passed,
        "total_tests": len(test_cases),
        "results": results
    }