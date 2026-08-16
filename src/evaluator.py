import json
import sys

from src.scoring import calculate_scores


def main():
    file_path = sys.argv[1]

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    scores = calculate_scores(
        tests_passed=data["tests_passed"],
        total_tests=data["total_tests"],
        readability=data["readability"],
        code_quality=data["code_quality"]
    )

    print("\n=== CODE EVALUATION ===\n")

    print(f'Problem: {data["problem"]}\n')

    print(f'Correctness: {scores["correctness"]}/10')
    print(f'Readability: {scores["readability"]}/10')
    print(f'Code Quality: {scores["code_quality"]}/10')

    print(f'\nFinal Score: {scores["final_score"]}/10')


if __name__ == "__main__":
    main()