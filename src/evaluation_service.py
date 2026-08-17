from src.ai_evaluator import evaluate_with_ai
from src.scoring import calculate_scores
from src.static_analysis import analyze_code
from src.test_runner import run_test_cases


def evaluate_submission(
    data,
    use_ai=False,
    ai_model=None
):
    problem = data["problem"]
    solution_file = data["solution_file"]
    function_name = data["function_name"]
    test_cases = data["test_cases"]

    timeout_seconds = data.get(
        "timeout_seconds",
        2
    )

    test_results = run_test_cases(
        solution_file=solution_file,
        function_name=function_name,
        test_cases=test_cases,
        timeout_seconds=timeout_seconds
    )

    total_tests = test_results[
        "total_tests"
    ]

    tests_passed = test_results[
        "tests_passed"
    ]

    if total_tests <= 0:
        raise ValueError(
            "At least one test case is required"
        )

    correctness = (
        tests_passed
        / total_tests
    ) * 10

    static_analysis = analyze_code(
        solution_file
    )

    analysis = {
        "readability": static_analysis[
            "readability"
        ],
        "code_quality": static_analysis[
            "code_quality"
        ],
        "instruction_following": round(
            correctness,
            2
        ),
        "feedback": static_analysis[
            "notes"
        ]
    }

    analysis_mode = "static"

    if use_ai:
        analysis = evaluate_with_ai(
            problem=problem,
            solution_file=solution_file,
            test_results=test_results,
            model=ai_model
        )

        analysis_mode = "ai"

    scores = calculate_scores(
        tests_passed=tests_passed,
        total_tests=total_tests,
        readability=analysis[
            "readability"
        ],
        code_quality=analysis[
            "code_quality"
        ],
        instruction_following=analysis[
            "instruction_following"
        ]
    )

    return {
        "problem": problem,
        "solution_file": solution_file,
        "function_name": function_name,
        "analysis_mode": analysis_mode,
        "test_results": test_results,
        "analysis": analysis,
        "scores": scores
    }