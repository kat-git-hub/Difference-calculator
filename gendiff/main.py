from gendiff.diff import diff
from gendiff.format.stylish import get_render
from gendiff.format.parsing import get_parsing
from gendiff.format.json import get_json
from gendiff.format.plain import get_plain


def get_file_diff(file_path1, file_path2):
    source1 = get_parsing(file_path1)
    source2 = get_parsing(file_path2)
    return source1, source2


def generate_diff(source1, source2, formatter=None):
    source1, source2 = get_file_diff(source1, source2)
    make_diff = diff(source1, source2)
    if formatter == 'plain':
        return get_plain(make_diff)
    elif formatter == 'json':
        return get_json(make_diff)
    else:
        return get_render(make_diff)
