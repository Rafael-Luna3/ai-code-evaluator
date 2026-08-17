import pytest

from src.solution_loader import load_function_from_file


def test_load_existing_function():
    function = load_function_from_file(
        file_path="examples/candidate_solution.py",
        function_name="find_largest"
    )

    result = function([1, 5, 3])

    assert result == 5


def test_missing_function():
    with pytest.raises(AttributeError):
        load_function_from_file(
            file_path="examples/candidate_solution.py",
            function_name="function_that_does_not_exist"
        )

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        load_function_from_file(
            file_path="examples/file_that_does_not_exist.py",
            function_name="find_largest"
        )

def test_non_callable_attribute():
    with pytest.raises(TypeError):
        load_function_from_file(
            file_path="examples/candidate_solution.py",
            function_name="author"
        )