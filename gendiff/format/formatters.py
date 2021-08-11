from gendiff.format.stylish import get_render
from gendiff.format.json import get_json
from gendiff.format.plain import get_plain


def get_formatted_data(data, formatter='stylish'):
    if formatter == 'stylish':
        return get_render(data)
    elif formatter == 'plain':
        return get_plain(data)
    elif formatter == 'json':
        return get_json(data)
    else:
        raise ValueError('Unknown formatter')
