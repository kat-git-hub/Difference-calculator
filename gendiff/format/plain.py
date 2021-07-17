
def get_plain(data, parent=""):
    output = ''
    sorting_content = sorted(data, key=lambda i: i['key'])
    for i in sorting_content:
        if i['type'] == 'changed':
            output += f"\nProperty \'{get_path(parent)}{(i['key'])}\'" \
                      f" was updated. " \
                      f"From \'{get_value(i['value'][0])}\' to " \
                      f"'{get_value(i['value'][1])}\' "
        elif i['type'] == 'added':
            output += f"\nProperty \'{get_path(parent)}{(i['key'])}'"\
                      f" was added with value: {get_value(i['value'])}"
        elif i['type'] == 'removed':
            output += f"\nProperty \'{get_path(parent)}{(i['key'])}'" \
                      f" was removed"
        elif i['type'] == 'nested':
            output += get_plain(i['value'], f"{get_path(parent)}{i['key']}")
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
        return f'{value}'
    if type(value) == dict or type(value) == list:
        return '[complex value]'
    else:
        return value
