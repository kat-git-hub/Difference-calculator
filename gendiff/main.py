from gendiff.diff import diff
from gendiff.parsing import get_parsing
from gendiff.format.formatters import get_right_formatter


def get_file_diff(file_path1, file_path2):
    source1 = get_parsing(file_path1)
    source2 = get_parsing(file_path2)
    return source1, source2


def generate_diff(source1, source2, formatter='stylish'):
    source1, source2 = get_file_diff(source1, source2)
    make_diff = diff(source1, source2)
    result = get_right_formatter(make_diff, formatter)
    return result
