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
            output.append("Property '{}{}' was updated.".format(path, key))
            output.append(" From {} to {}\n"
                          .format(get_value(value[0]), get_value(value[1])))
        elif status == diff.ADDED:
            output.append("Property '{}{}' was added with value: {}\n"
                          .format(path, key, get_value(value)))
        elif status == diff.REMOVED:
            output.append("Property '{}{}' was removed\n"
                          .format(path, key))
        elif status == diff.NESTED:
            output.append(get_plain(value, f"{path}{key}"))
    return ''.join(output)


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
