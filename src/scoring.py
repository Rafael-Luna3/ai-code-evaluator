def calculate_scores(tests_passed, total_tests, readability, code_quality):
    if total_tests <= 0:
        raise ValueError("total_tests must be greater than zero")

    correctness = (tests_passed / total_tests) * 10

    final_score = (correctness + readability + code_quality) / 3

    return {
        "correctness": round(correctness, 2),
        "readability": readability,
        "code_quality": code_quality,
        "final_score": round(final_score, 2)
    }