import json
import sys

from src.scoring import calculate_scores
from src.solution_loader import load_function_from_file
from src.test_runner import run_test_cases


def main():
    file_path = sys.argv[1]

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    candidate_function = load_function_from_file(
        file_path=data["solution_file"],
        function_name=data["function_name"]
    )

    test_results = run_test_cases(
        function=candidate_function,
        test_cases=data["test_cases"]
    )

    scores = calculate_scores(
        tests_passed=test_results["tests_passed"],
        total_tests=test_results["total_tests"],
        readability=data["readability"],
        code_quality=data["code_quality"]
    )


    print("\n=== TEST RESULTS ===\n")

    for index, result in enumerate(test_results["results"], start=1):
        status = "PASS" if result["passed"] else "FAIL"

        print(
            f'Test {index}: {status} | '
            f'Input: {result["input"]} | '
            f'Expected: {result["expected"]} | '
            f'Actual: {result["actual"]}'
        )


    print("\n=== CODE EVALUATION ===\n")

    print(f'Problem: {data["problem"]}\n')

    print(f'Correctness: {scores["correctness"]}/10')
    print(f'Readability: {scores["readability"]}/10')
    print(f'Code Quality: {scores["code_quality"]}/10')

    print(f'\nFinal Score: {scores["final_score"]}/10')


if __name__ == "__main__":
    main()