import json
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def execute_candidate(
    solution_file,
    function_name,
    args=None,
    kwargs=None,
    timeout_seconds=2
):
    args = args or []
    kwargs = kwargs or {}

    call_data = {
        "args": args,
        "kwargs": kwargs
    }

    command = [
        sys.executable,
        "-m",
        "src.candidate_worker",
        solution_file,
        function_name,
        json.dumps(call_data, ensure_ascii=False)
    ]

    try:
        completed_process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            cwd=PROJECT_ROOT
        )

    except subprocess.TimeoutExpired:
        return {
            "status": "timeout",
            "error_type": "TimeoutExpired",
            "message": f"Execution exceeded {timeout_seconds} seconds"
        }

    output_lines = [
        line.strip()
        for line in completed_process.stdout.splitlines()
        if line.strip()
    ]

    if not output_lines:
        message = completed_process.stderr.strip()

        if not message:
            message = (
                f"Worker exited with code "
                f"{completed_process.returncode}"
            )

        return {
            "status": "error",
            "error_type": "WorkerError",
            "message": message
        }

    try:
        return json.loads(output_lines[-1])

    except json.JSONDecodeError:
        return {
            "status": "error",
            "error_type": "InvalidWorkerOutput",
            "message": output_lines[-1]
        }