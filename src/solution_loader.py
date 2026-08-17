import importlib.util


def load_function_from_file(file_path, function_name):
    spec = importlib.util.spec_from_file_location(
        "candidate_module",
        file_path
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    function = getattr(module, function_name)

    if not callable(function):
        raise TypeError(
            f"'{function_name}' is not callable"
        )

    return function