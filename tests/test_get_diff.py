import pytest
from gendiff.diff.get_diff import generate_diff


@pytest.fixture
def files():
    return (
                  "tests/fixtures/file1.json",
                  "tests/fixtures/file2.json",
                  "tests/fixtures/result.txt"
                 )


def test_generate_diff(files):
    first_file, second_file, result = files
    with open(result, "r") as result:
        assert generate_diff(first_file, second_file) == result.read()
