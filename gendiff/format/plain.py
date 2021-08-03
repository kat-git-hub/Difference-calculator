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
            output.append("\nProperty '{}{}' was updated.".format(path, key))
            output.append(" From {} to {}"
                          .format(get_value(value[0]), get_value(value[1])))
        elif status == diff.ADDED:
            output.append("\nProperty '{}{}' was added with value: {}"
                          .format(path, key, get_value(value)))
        elif status == diff.REMOVED:
            output.append("\nProperty '{}{}' was removed"
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
