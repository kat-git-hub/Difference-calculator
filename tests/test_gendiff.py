from gendiff.diff import generate_diff

result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def test_generate_diff_json():
    result_out = generate_diff('tests/test_example/file1.json', 'tests/test_example/file2.json')
    assert result_out == result


def test_generate_diff_yaml():
  result_out = generate_diff('tests/test_example/file1.yml', 'tests/test_example/file2.yml')
  assert result_out == result


