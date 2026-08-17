import json
import sys

from src.solution_loader import load_function_from_file


def emit(payload):
    print(
        json.dumps(
            payload,
            ensure_ascii=False,
            default=str
        )
    )


def main():
    if len(sys.argv) != 4:
        emit({
            "status": "error",
            "error_type": "ArgumentError",
            "message": "Expected solution_file, function_name and call_data"
        })
        return

    solution_file = sys.argv[1]
    function_name = sys.argv[2]
    call_data = json.loads(sys.argv[3])

    args = call_data.get("args", [])
    kwargs = call_data.get("kwargs", {})

    try:
        function = load_function_from_file(
            file_path=solution_file,
            function_name=function_name
        )

        result = function(*args, **kwargs)

        emit({
            "status": "success",
            "result": result
        })

    except BaseException as error:
        emit({
            "status": "error",
            "error_type": type(error).__name__,
            "message": str(error)
        })


if __name__ == "__main__":
    main()