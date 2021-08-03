from gendiff import generate_diff
from gendiff.format import plain
from gendiff.format import json
import pytest
import os
import json
import yaml


path = 'tests/fixtures/'


@pytest.mark.parametrize('file1, file2, answer', 
                         [('test_01_before.json', 'test_01_after.json',
                           'test_answer_1.txt'),
                         ('test_02_before.yml', 'test_02_after.yml', 
                          'test_answer_1.txt'),
                         ('test_03_before.json', 'test_03_after.json', 
                          'test_answer_2.txt')]
                        )
def test_stylish(file1, file2, answer):
  with open(os.path.join(path, answer)) as f:
    expected_result = f.read()
  result = generate_diff(os.path.join(path, file1),
                         os.path.join(path, file2), None)
  assert result == expected_result


@pytest.mark.parametrize('file1, file2, answer', 
                         [('test_03_before.json', 'test_03_after.json', 
                           'test_answer_plain.txt'),
                         ('test_04_before.yml', 'test_04_after.yml', 
                          'test_answer_plain.txt')]
                        )
def test_plain(file1, file2, answer):
  with open(os.path.join(path, answer)) as f:
    expected_result = f.read()
  result = generate_diff(os.path.join(path, file1),
                         os.path.join(path, file2), 'plain')
  assert result == expected_result


@pytest.mark.parametrize('file1, file2, answer', 
                         [('test_01_before.json', 'test_01_after.json', 
                           'test_answer_json.json'),
                         ('test_02_before.yml', 'test_02_after.yml', 
                          'test_answer_json.json')]
                        )
def test_json(file1, file2, answer):
  with open(os.path.join(path, 'test_answer_json.json')) as f:
    check = json.load(f)
  check_json = generate_diff(os.path.join(path, file1), 
                             os.path.join(path, file2), 'json')
  check_yml = generate_diff(os.path.join(path, file1), 
                            os.path.join(path, file2), 'json')
  assert check == json.loads(check_json)
  assert check == json.loads(check_yml)