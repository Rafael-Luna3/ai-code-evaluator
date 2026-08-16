import pytest

from src.scoring import calculate_scores


def test_perfect_score():
    result = calculate_scores(
        tests_passed=10,
        total_tests=10,
        readability=10,
        code_quality=10
    )

    assert result["correctness"] == 10
    assert result["readability"] == 10
    assert result["code_quality"] == 10
    assert result["final_score"] == 10

def test_partial_score():
    result = calculate_scores(
        tests_passed=8,
        total_tests=10,
        readability=9,
        code_quality=8
    )

    assert result["correctness"] == 8
    assert result["final_score"] == 8.33

def test_zero_total_tests():
    with pytest.raises(ValueError):
        calculate_scores(
            tests_passed=0,
            total_tests=0,
            readability=8,
            code_quality=8
        )