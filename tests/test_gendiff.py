from gendiff import generate_diff
from gendiff.format import plain
from gendiff.format import json
import pytest
import os
import json
import yaml


fixtures_path = 'tests/fixtures/'
checking_files = {
  'test_answer_1.txt': ('test_01_before.json', 'test_01_after.json',
                        'test_02_before.yml', 'test_02_after.yml', None), 
  'test_answer_2.txt': ('test_03_before.json', 'test_03_after.json',
                        'test_04_before.yml', 'test_04_after.yml', None),
  'test_answer_plain.txt': ('test_03_before.json', 'test_03_after.json',
                            'test_04_before.yml', 'test_04_after.yml', 'plain'),
                 }


#@pytest.mark.parametrize(item[], file2, formatter)

def test_stylish_plain():
  for key, item in checking_files.items():
    with open(os.path.join(fixtures_path, key)) as f:
      check = f.read()
    check_json = generate_diff(os.path.join(fixtures_path, item[0]),
                              os.path.join(fixtures_path, item[1]), item[4])
    check_yml = generate_diff(os.path.join(fixtures_path, item[2]),
                             os.path.join(fixtures_path, item[3]), item[4])
    assert check == check_yml
    assert check == check_json


def test_json():
  with open(os.path.join(fixtures_path, 'test_answer_json.json')) as f:
    check = json.load(f)
  check_json = generate_diff(os.path.join(fixtures_path, 'test_01_before.json'), 
                              os.path.join(fixtures_path, 'test_01_after.json'), 'json')
  check_yml = generate_diff(os.path.join(fixtures_path, 'test_02_before.yml'), 
                              os.path.join(fixtures_path, 'test_02_after.yml'), 'json')
  assert check == json.loads(check_json)
  assert check == json.loads(check_yml)