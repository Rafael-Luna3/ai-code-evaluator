# AI Code Evaluator

A Python system for automatically testing, analyzing, scoring, and comparing candidate code solutions.

The project combines deterministic testing, static code analysis, optional AI-assisted evaluation, subprocess execution, solution comparison, automated testing, continuous integration, and a REST API.

## Features

- Dynamic Python solution loading
- Generic positional and keyword arguments
- Automated test execution
- PASS/FAIL reporting
- Execution timeout
- Separate candidate subprocess
- Static code analysis
- Weighted scoring
- Optional Gemini-assisted evaluation
- A/B solution comparison
- REST API with FastAPI
- pytest test suite
- GitHub Actions CI

## Architecture

```text
Input
  |
  v
Evaluation Service
  |
  +--> Test Runner
  |      |
  |      v
  |   Process Runner
  |      |
  |      v
  |   Candidate Worker
  |      |
  |      v
  |   Candidate Code
  |
  +--> Static Analysis
  |
  +--> Optional AI Evaluation
  |
  v
Scoring
  |
  v
Evaluation Result
```

## Installation

```bash
git clone <repository-url>
cd ai-code-evaluator

python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## CLI Evaluation

```bash
python -m src.evaluator examples/example.json
```

JSON output:

```bash
python -m src.evaluator examples/example.json --json
```

## AI-Assisted Evaluation

Set a Gemini API key.

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

Then:

```bash
python -m src.evaluator examples/example.json --ai
```

The default AI model is:

```text
gemini-3.6-flash
```

You can override it with:

```powershell
$env:GEMINI_MODEL="MODEL_ID"
```

## Compare Solutions

```bash
python -m src.compare examples/example.json examples/bad_example.json
```

With AI:

```bash
python -m src.compare examples/example.json examples/bad_example.json --ai
```

## REST API

Start the development server:

```bash
fastapi dev src/api.py
```

Open:

```text
http://127.0.0.1:8000/docs
```

### Health

```text
GET /health
```

### Evaluate

```text
POST /evaluate
```

Example request:

```json
{
  "problem": "Return the sum of two numbers.",
  "code": "def add(a, b):\n    return a + b",
  "function_name": "add",
  "test_cases": [
    {
      "args": [2, 3],
      "expected": 5
    }
  ],
  "use_ai": false,
  "timeout_seconds": 2
}
```

### Compare

```text
POST /compare
```

Compares two candidate implementations using the same problem and test cases.

## Testing

```bash
python -m pytest
```

## Scoring

The final score combines:

- Correctness: 55%
- Readability: 15%
- Code quality: 15%
- Instruction following: 15%

In static mode, automated correctness is used as a proxy for instruction following.

In AI mode, instruction following, readability, and code quality are evaluated by the configured Gemini model.

## Security

Candidate code runs in a separate subprocess with a timeout.

This is not a complete security sandbox.

Do not execute arbitrary untrusted code on a sensitive machine.

See `SECURITY.md`.

## Tech Stack

- Python
- pytest
- FastAPI
- Google GenAI SDK
- Gemini API
- GitHub Actions
- JSON
- Python AST
- subprocess
- Pydantic

## Status

Version 1.0.