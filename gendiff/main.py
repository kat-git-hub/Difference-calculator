from gendiff.diff import make_diff
from gendiff.parsing import get_parsing
from gendiff.format.formatters import get_formatted_data


def get_file_diff(file_path):
    source = get_parsing(file_path)
    return source


def generate_diff(source1, source2, formatter='stylish'):
    data1 = get_file_diff(source1)
    data2 = get_file_diff(source2)
    diff = make_diff(data1, data2)
    result = get_formatted_data(diff, formatter)
    return result
