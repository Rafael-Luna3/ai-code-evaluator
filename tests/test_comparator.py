from src.comparator import (
    compare_evaluations
)


def create_evaluation(
    final_score,
    correctness
):
    return {
        "scores": {
            "correctness": correctness,
            "readability": 9,
            "code_quality": 9,
            "instruction_following": 9,
            "final_score": final_score
        }
    }


def test_candidate_a_wins():
    evaluation_a = create_evaluation(
        9.5,
        10
    )

    evaluation_b = create_evaluation(
        7,
        6
    )

    result = compare_evaluations(
        evaluation_a,
        evaluation_b
    )

    assert result[
        "winner"
    ] == "A"


def test_tie():
    evaluation_a = create_evaluation(
        9,
        10
    )

    evaluation_b = create_evaluation(
        9,
        10
    )

    result = compare_evaluations(
        evaluation_a,
        evaluation_b
    )

    assert result[
        "winner"
    ] == "tie"