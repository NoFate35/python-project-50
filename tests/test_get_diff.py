#!/usr/bin/env python
import pytest
from gendiff.diff.get_diff import generate_diff

    
@pytest.fixture
def files():
    return ("tests/fixtures/file1.json", "tests/fixtures/file2.json")
        
        
def test_generate_diff(files):
    first_file, second_file = files
    with open(first_file, "r") as file1:
        print(file1.read())
    with open(second_file, "r") as file2:
        print(file2.read())