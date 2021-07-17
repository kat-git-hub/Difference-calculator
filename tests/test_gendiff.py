from gendiff.diff import generate_diff
from gendiff.format import STYLISH, PLAIN, JSON
#from gendiff.tests.fixtures import test_plain
import pytest
import os
import json
import yaml



fixtures_path = 'tests/fixtures/'
checking_files = ['test_01_before.json',
                                  'test_01_after.json'
                  'test_02_before.yml', 'test_02_after.yml',
                  #'03_before.json', '03_after.json'
                  #'04_before.yml', '04_after.yml'
                  ]

answers = ['test_01_answer.json']

res = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

#@pytest.fixture()


def test_generate_diff_json_yml():
  with open('tests/fixtures/test_01_answer.txt') as f:
    check = f.read()
  check_json = generate_diff('tests/fixtures/test_01_before.json',
                            'tests/fixtures/test_01_after.json')
  check_yml = generate_diff(os.path.join(fixtures_path, 'test_02_before.yml'),
                            os.path.join(fixtures_path, 'test_02_after.yml'))
  assert check == get_render(check_json, 1)
  #assert check == check_yml
