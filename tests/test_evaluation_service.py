import json

from src.evaluation_service import (
    evaluate_submission
)


def test_complete_evaluation():
    with open(
        "examples/sum_example.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    result = evaluate_submission(
        data,
        use_ai=False
    )

    assert result[
        "test_results"
    ]["tests_passed"] == 4

    assert result[
        "analysis_mode"
    ] == "static"

    assert result[
        "scores"
    ]["correctness"] == 10