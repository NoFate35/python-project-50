import pytest
from gendiff.diff.get_diff import generate_diff


@pytest.fixture
def files_json():
    return (
                  "tests/fixtures/file1.json", # noqa: E126
                  "tests/fixtures/file2.json"
                 ) # noqa: E126


@pytest.fixture
def files_yml():
    return (
                  "tests/fixtures/file1.yml", # noqa: E126
                  "tests/fixtures/file2.yml"
                 ) # noqa: E126


@pytest.fixture
def result_stylish():
    return "tests/fixtures/result_stylish.txt"


@pytest.fixture
def result_plain():
    return "tests/fixtures/result_plain.txt"


@pytest.fixture
def result_json():
    return "tests/fixtures/result_json.txt"


def test_json_stylish(files_json, result_stylish):
    first_file, second_file = files_json
    with open(result_stylish, "r") as result:
        assert generate_diff(first_file, second_file) == result.read()


def test_yml_stylish(files_yml, result_stylish):
    first_file, second_file = files_yml
    with open(result_stylish, "r") as result:
        assert generate_diff(first_file, second_file) == result.read()


def test_json_plain(files_json, result_plain):
    first_file, second_file = files_json
    with open(result_plain, "r") as result:
        assert generate_diff(first_file, second_file, "plain") == result.read()


def test_yml_plain(files_yml, result_plain):
    first_file, second_file = files_yml
    with open(result_plain, "r") as result:
        assert generate_diff(first_file, second_file, "plain") == result.read()


def test_json_json(files_json, result_json):
    first_file, second_file = files_json
    with open(result_json, "r") as result:
        assert generate_diff(first_file, second_file, "json") == result.read()


def test_yml_json(files_yml, result_json):
    first_file, second_file = files_yml
    with open(result_json, "r") as result:
        assert generate_diff(first_file, second_file, "json") == result.read()
