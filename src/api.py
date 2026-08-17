from typing import Any

from fastapi import FastAPI
from fastapi import HTTPException

from pydantic import BaseModel
from pydantic import Field

from src.comparator import (
    compare_evaluations
)

from src.submission_service import (
    evaluate_code
)


app = FastAPI(
    title="AI Code Evaluator API",
    version="1.0.0",
    description=(
        "Evaluate and compare Python "
        "candidate solutions."
    )
)


class TestCase(BaseModel):
    args: list[Any] = Field(
        default_factory=list
    )

    kwargs: dict[str, Any] = Field(
        default_factory=dict
    )

    expected: Any


class EvaluateRequest(BaseModel):
    problem: str
    code: str
    function_name: str
    test_cases: list[TestCase]
    use_ai: bool = False
    ai_model: str | None = None
    timeout_seconds: float = 2


class Candidate(BaseModel):
    code: str
    function_name: str


class CompareRequest(BaseModel):
    problem: str
    candidate_a: Candidate
    candidate_b: Candidate
    test_cases: list[TestCase]
    use_ai: bool = False
    ai_model: str | None = None
    timeout_seconds: float = 2


@app.get("/")
def root():
    return {
        "name": "AI Code Evaluator",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/evaluate")
def evaluate(
    request: EvaluateRequest
):
    try:
        test_cases = [
            test_case.model_dump()
            for test_case
            in request.test_cases
        ]

        return evaluate_code(
            problem=request.problem,
            code=request.code,
            function_name=(
                request.function_name
            ),
            test_cases=test_cases,
            use_ai=request.use_ai,
            ai_model=request.ai_model,
            timeout_seconds=(
                request.timeout_seconds
            )
        )

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error


@app.post("/compare")
def compare(
    request: CompareRequest
):
    try:
        test_cases = [
            test_case.model_dump()
            for test_case
            in request.test_cases
        ]

        evaluation_a = evaluate_code(
            problem=request.problem,
            code=request.candidate_a.code,
            function_name=(
                request
                .candidate_a
                .function_name
            ),
            test_cases=test_cases,
            use_ai=request.use_ai,
            ai_model=request.ai_model,
            timeout_seconds=(
                request.timeout_seconds
            )
        )

        evaluation_b = evaluate_code(
            problem=request.problem,
            code=request.candidate_b.code,
            function_name=(
                request
                .candidate_b
                .function_name
            ),
            test_cases=test_cases,
            use_ai=request.use_ai,
            ai_model=request.ai_model,
            timeout_seconds=(
                request.timeout_seconds
            )
        )

        comparison = compare_evaluations(
            evaluation_a,
            evaluation_b
        )

        return {
            "candidate_a": evaluation_a,
            "candidate_b": evaluation_b,
            "comparison": comparison
        }

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error