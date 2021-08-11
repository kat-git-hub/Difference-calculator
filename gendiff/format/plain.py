from gendiff import diff


def get_plain(data, parent=""):
    path = get_path(parent)
    output = []
    sorting_content = sorted(data, key=lambda i: i[diff.KEY])
    for i in sorting_content:
        key = i[diff.KEY]
        value = i[diff.VALUE]
        status = i[diff.TYPE]
        if status == diff.CHANGED:
            old, new = value
            output.append("Property '{}{}' was updated. From {} to {}"
                          .format(path, key, get_value(old),
                                  get_value(new)))
        elif status == diff.ADDED:
            output.append("Property '{}{}' was added with value: {}"
                          .format(path, key, get_value(value)))
        elif status == diff.REMOVED:
            output.append("Property '{}{}' was removed"
                          .format(path, key))
        elif status == diff.NESTED:
            output.append(get_plain(value, f"{path}{key}"))
    return '\n'.join(output)


def get_path(parent):
    if parent != '':
        return f'{parent}.'
    else:
        return ''


def get_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        return f'\'{value}\''
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    else:
        return value
