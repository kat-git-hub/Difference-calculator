from gendiff import diff


def get_plain(data, parent=""):
    path = get_path(parent)
    output = ''
    sorting_content = sorted(data, key=lambda i: i[diff.KEY])
    for i in sorting_content:
        key = i[diff.KEY]
        value = i[diff.VALUE]
        status = i[diff.TYPE]
        if status == diff.CHANGED:
            output += "\nProperty '{}{}' was updated. "\
                .format(path, key)
            output += "From {} to {}"\
                .format(get_value(value[0]), get_value(value[1]))
        elif status == diff.ADDED:
            output += "\nProperty '{}{}' was added with value: {}"\
                .format(path, key, get_value(value))
        elif status == diff.REMOVED:
            output += "\nProperty '{}{}' was removed"\
                .format(path, key)
        elif status == diff.NESTED:
            output += get_plain(value, f"{path}{key}")
    return output


def get_path(parent):
    if parent != '':
        return f'{parent}.'
    else:
        return ''


def get_value(value):
    if value is None:
        return 'null'
    if type(value) == bool:
        return 'true' if value else 'false'
    if type(value) == str:
        return f'\'{value}\''
    if type(value) == dict or type(value) == list:
        return '[complex value]'
    else:
        return value
