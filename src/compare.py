import argparse
import json

from src.comparator import (
    compare_evaluations
)

from src.evaluation_service import (
    evaluate_submission
)


def load_json(file_path):
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Compare two candidate solutions"
        )
    )

    parser.add_argument(
        "candidate_a"
    )

    parser.add_argument(
        "candidate_b"
    )

    parser.add_argument(
        "--ai",
        action="store_true"
    )

    parser.add_argument(
        "--model",
        default=None
    )

    args = parser.parse_args()

    data_a = load_json(
        args.candidate_a
    )

    data_b = load_json(
        args.candidate_b
    )

    evaluation_a = evaluate_submission(
        data_a,
        use_ai=args.ai,
        ai_model=args.model
    )

    evaluation_b = evaluate_submission(
        data_b,
        use_ai=args.ai,
        ai_model=args.model
    )

    comparison = compare_evaluations(
        evaluation_a,
        evaluation_b
    )

    result = {
        "candidate_a": evaluation_a,
        "candidate_b": evaluation_b,
        "comparison": comparison
    }

    print(
        json.dumps(
            result,
            indent=2,
            ensure_ascii=False,
            default=str
        )
    )


if __name__ == "__main__":
    main()