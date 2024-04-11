import pytest
from gendiff.diff.get_diff import generate_diff


@pytest.fixture
def files_json():
    return (
                  "tests/fixtures/file1.json",
                  "tests/fixtures/file2.json"
                 )
                 
                 
@pytest.fixture
def files_yml():
    return (
                  "tests/fixtures/file1.yml",
                  "tests/fixtures/file2.yml"
                 )
                 
                 
@pytest.fixture
def result_json():
    return "tests/fixtures/result_json.txt"
    
    
@pytest.fixture
def result_yml():
    return "tests/fixtures/result_yml.txt"
       


def test_diff_json(files_json, result_json):
    first_file, second_file = files_json
    with open(result_json, "r") as result:
        assert generate_diff(first_file, second_file) == result.read()
        
        
def test_diff_yml(files_yml, result_yml):
    first_file, second_file = files_yml
    with open(result_yml, "r") as result:
        assert generate_diff(first_file, second_file) == result.read()
