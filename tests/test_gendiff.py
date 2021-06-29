from gendiff.diff import generate_diff
from gendiff.format.stylish import stylish

result_plane = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

result_inner = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

def test_generate_diff_json():
    result_out = generate_diff('tests/test_example/file1.json', 'tests/test_example/file2.json')
    result = stylish(result_out, 1)
    assert result == result_plane


def test_generate_diff_yaml():
  result_out = generate_diff('tests/test_example/file1.yml', 'tests/test_example/file2.yml')
  result = stylish(result_out, 1)
  assert result == result_plane


def test_generate_diff_inner():
  result_out = generate_diff('tests/test_example/test_file1.json', 'tests/test_example/test_file2.json')
  #make_diff = generate_diff(args.first_file, args.second_file)
  result = stylish(result_out, 1)
  assert result == result_inner