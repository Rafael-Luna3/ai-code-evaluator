import subprocess
import sys


def test_cli_static_evaluation():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.evaluator",
            "examples/example.json"
        ],
        capture_output=True,
        text=True,
        timeout=10
    )

    assert result.returncode == 0
    assert "AI CODE EVALUATOR" in result.stdout
    assert "Analysis mode: static" in result.stdout
    assert "Test 1: PASS" in result.stdout
    assert "final_score:" in result.stdout