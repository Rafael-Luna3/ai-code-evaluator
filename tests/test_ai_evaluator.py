import pytest

from pydantic import ValidationError

from src.ai_evaluator import (
    AIEvaluationResponse
)


def test_ai_response_schema():
    result = AIEvaluationResponse(
        readability=9,
        code_quality=8,
        instruction_following=10,
        feedback=[
            "Good solution"
        ]
    )

    assert result.readability == 9
    assert result.code_quality == 8
    assert (
        result.instruction_following
        == 10
    )


def test_ai_response_rejects_invalid_score():
    with pytest.raises(
        ValidationError
    ):
        AIEvaluationResponse(
            readability=15,
            code_quality=8,
            instruction_following=10,
            feedback=[]
        )