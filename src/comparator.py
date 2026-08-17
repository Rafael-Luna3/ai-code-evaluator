def compare_evaluations(
    evaluation_a,
    evaluation_b
):
    score_a = evaluation_a[
        "scores"
    ]["final_score"]

    score_b = evaluation_b[
        "scores"
    ]["final_score"]

    difference = round(
        score_a - score_b,
        2
    )

    if difference > 0:
        winner = "A"

    elif difference < 0:
        winner = "B"

    else:
        winner = "tie"

    metrics = [
        "correctness",
        "readability",
        "code_quality",
        "instruction_following"
    ]

    differences = []

    for metric in metrics:
        value_a = evaluation_a[
            "scores"
        ][metric]

        value_b = evaluation_b[
            "scores"
        ][metric]

        if value_a > value_b:
            better = "A"

        elif value_b > value_a:
            better = "B"

        else:
            better = "tie"

        differences.append({
            "metric": metric,
            "candidate_a": value_a,
            "candidate_b": value_b,
            "better": better
        })

    return {
        "winner": winner,
        "candidate_a_score": score_a,
        "candidate_b_score": score_b,
        "score_difference": abs(
            difference
        ),
        "differences": differences
    }