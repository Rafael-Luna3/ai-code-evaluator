from pathlib import Path
from tempfile import TemporaryDirectory

from src.evaluation_service import (
    evaluate_submission
)


def evaluate_code(
    problem,
    code,
    function_name,
    test_cases,
    use_ai=False,
    ai_model=None,
    timeout_seconds=2
):
    with TemporaryDirectory(
        prefix="ai_code_evaluator_"
    ) as directory:
        solution_file = (
            Path(directory)
            / "candidate.py"
        )

        solution_file.write_text(
            code,
            encoding="utf-8"
        )

        data = {
            "problem": problem,
            "solution_file": str(
                solution_file
            ),
            "function_name": function_name,
            "test_cases": test_cases,
            "timeout_seconds": (
                timeout_seconds
            )
        }

        return evaluate_submission(
            data=data,
            use_ai=use_ai,
            ai_model=ai_model
        )