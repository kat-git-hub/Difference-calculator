from gendiff.diff import generate_diff
from gendiff.format.stylish import get_render
#from gendiff.tests.fixtures import test_plain
import pytest
import os
import json
import yaml


path = './tests/fixtures'
checking_files = ['test_01_before.json','test_01_after.json',
                  'test_02_before.yml', 'test_02_after.yml',
                  'test_03_before.json', 'test_03_after.json'
                  'test_04_before.yml', 'test_04_after.yml']

answers = ['test_01_answer']
  #for i in checking_files:
#def load_params_from_json(path, checking_file):
#    with open(path, checking_file) as f:
        #return json.load(f)
#        return f.read()



#@pytest.fixture()


def test_generate_diff_json_yml():
  with open(os.path.join(path, 'test_01_answer.json')) as f:

    #for i in checking_files:

  


    check = json.load(f)
  check_json = generate_diff(os.path.join(path, 'test_01_before.json'),
                os.path.join(path, 'test_01_after.json'))
  check_yml = generate_diff(os.path.join(path, 'test_02_before.yml'),
                os.path.join(path, 'test_02_after.yml'))
  assert check == json.loads(check_json)
  assert check == yml.loads(check_yml)




#def test_generate_diff_json():
#  with open(os.path.join(path, checking_files[i]), "r") as f:
#      templates = json.load(f)
#    result_out = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
#    result = get_render(result_out, 1)
#    assert result == result_plane


#def test_generate_diff_yaml():
 # result_out = generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
  #result = get_render(result_out, 1)
  #assert result == result_plane


#def test_generate_diff_nested():
 # result_out = generate_diff('tests/fixtures/test_file1.json', 'tests/fixtures/test_file2.json')
  #result = get_render(result_out, 1)
  #assert result == result_nested


#def test_generate_diff_nested_yml():
#  result_out = generate_diff('tests/fixtures/test_02_file1.yml', 'tests/fixtures/test_02_file2.yml')
 # result = get_render(result_out, 1)
  #assert result == result_nested


#def test_generate_diff_plain():
#  result_out = generate_diff('tests/fixtures/test_02_file1.yml', 'tests/fixtures/test_02_file2.yml')
#  result = get_plain(result_out, 1)
#  assert result == test_plain