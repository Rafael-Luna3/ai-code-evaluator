from fastapi.testclient import (
    TestClient
)

from src.api import app


client = TestClient(
    app
)


def test_health():
    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok"
    }


def test_evaluate():
    response = client.post(
        "/evaluate",
        json={
            "problem": (
                "Return the sum "
                "of two numbers."
            ),
            "code": (
                "def add(a, b):\n"
                "    return a + b\n"
            ),
            "function_name": "add",
            "test_cases": [
                {
                    "args": [2, 3],
                    "expected": 5
                },
                {
                    "args": [10, -2],
                    "expected": 8
                }
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data[
        "test_results"
    ]["tests_passed"] == 2


def test_compare():
    response = client.post(
        "/compare",
        json={
            "problem": (
                "Return the largest "
                "number in a list."
            ),
            "candidate_a": {
                "code": (
                    "def find_largest(numbers):\n"
                    "    return max(numbers)\n"
                ),
                "function_name": (
                    "find_largest"
                )
            },
            "candidate_b": {
                "code": (
                    "def find_largest(numbers):\n"
                    "    return numbers[0]\n"
                ),
                "function_name": (
                    "find_largest"
                )
            },
            "test_cases": [
                {
                    "args": [[1, 5, 2]],
                    "expected": 5
                },
                {
                    "args": [[9, 1, 3]],
                    "expected": 9
                }
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data[
        "comparison"
    ]["winner"] == "A"