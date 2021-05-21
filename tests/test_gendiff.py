from gendiff.gendiff import generate_diff

result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

def test_generate_diff():
    result_out = generate_diff('tests/test_example/file1.json', 'tests/test_example/file2.json')
    assert result_out == result
