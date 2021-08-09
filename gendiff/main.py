from gendiff.diff import make_diff
from gendiff.parsing import get_parsing
from gendiff.format.formatters import get_right_formatter


def get_file_diff(file_path1, file_path2):
    source1 = get_parsing(file_path1)
    source2 = get_parsing(file_path2)
    return source1, source2


def generate_diff(source1, source2, formatter='stylish'):
    data1, data2 = get_file_diff(source1, source2)
    diff = make_diff(data1, data2)
    result = get_right_formatter(diff, formatter)
    return result
