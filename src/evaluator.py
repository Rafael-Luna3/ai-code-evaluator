import argparse
import json

from src.evaluation_service import evaluate_submission


def print_report(result):
    print()
    print("AI CODE EVALUATOR")
    print("=" * 50)

    print(
        f'Problem: {result["problem"]}'
    )

    print(
        f'Analysis mode: '
        f'{result["analysis_mode"]}'
    )

    print()

    for index, test in enumerate(
        result["test_results"]["results"],
        start=1
    ):
        status = (
            "PASS"
            if test["passed"]
            else "FAIL"
        )

        print(
            f'Test {index}: {status} | '
            f'Args: {test["args"]} | '
            f'Expected: {test["expected"]} | '
            f'Actual: {test["actual"]}'
        )

    print()
    print("SCORES")
    print("-" * 50)

    for name, score in result[
        "scores"
    ].items():
        print(
            f"{name}: {score}"
        )

    feedback = result[
        "analysis"
    ].get(
        "feedback",
        []
    )

    if feedback:
        print()
        print("FEEDBACK")
        print("-" * 50)

        for item in feedback:
            print(
                f"- {item}"
            )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate Python candidate solutions"
        )
    )

    parser.add_argument(
        "file_path"
    )

    parser.add_argument(
        "--ai",
        action="store_true"
    )

    parser.add_argument(
        "--model",
        default=None
    )

    parser.add_argument(
        "--json",
        action="store_true"
    )

    args = parser.parse_args()

    with open(
        args.file_path,
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    result = evaluate_submission(
        data=data,
        use_ai=args.ai,
        ai_model=args.model
    )

    if args.json:
        print(
            json.dumps(
                result,
                indent=2,
                ensure_ascii=False,
                default=str
            )
        )

    else:
        print_report(
            result
        )


if __name__ == "__main__":
    main()