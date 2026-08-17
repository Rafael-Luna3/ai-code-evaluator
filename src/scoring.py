def validate_score(name, value):
    if value < 0 or value > 10:
        raise ValueError(
            f"{name} must be between 0 and 10"
        )


def calculate_scores(
    tests_passed,
    total_tests,
    readability,
    code_quality,
    instruction_following
):
    if total_tests <= 0:
        raise ValueError(
            "total_tests must be greater than zero"
        )

    if tests_passed < 0:
        raise ValueError(
            "tests_passed cannot be negative"
        )

    if tests_passed > total_tests:
        raise ValueError(
            "tests_passed cannot exceed total_tests"
        )

    validate_score(
        "readability",
        readability
    )

    validate_score(
        "code_quality",
        code_quality
    )

    validate_score(
        "instruction_following",
        instruction_following
    )

    correctness = (
        tests_passed
        / total_tests
    ) * 10

    final_score = (
        correctness * 0.55
        + readability * 0.15
        + code_quality * 0.15
        + instruction_following * 0.15
    )

    return {
        "correctness": round(
            correctness,
            2
        ),
        "readability": round(
            readability,
            2
        ),
        "code_quality": round(
            code_quality,
            2
        ),
        "instruction_following": round(
            instruction_following,
            2
        ),
        "final_score": round(
            final_score,
            2
        )
    }