# flake8: noqa: C901
from gendiff import diff


def get_render(data, indent_level=1): 
    output = ""
    spaces = get_spaces(indent_level)
    sorting_content = sorted(data, key=lambda i: i[diff.KEY])
    for i in sorting_content:
        status = i[diff.TYPE]
        value = i[diff.VALUE]
        key = i[diff.KEY]
        if status == diff.ADDED:
            if type(value) == dict:
                output += f"\n{spaces}+ {key}: " \
                          f"{make_pack(value, indent_level)}"
            else:
                output += f"\n{spaces}+ {str(key)}: " \
                          f"{str(make_pack(value, indent_level))}"
        elif status == diff.REMOVED:
            if type(value) == dict:
                output += f"\n{spaces}- {key}: " \
                          f"{make_pack(value, indent_level)}"
            else:
                output += f"\n{spaces}- {str(key)}: " \
                          f"{str(make_pack(value, indent_level))}"
        elif status == diff.CHANGED:
            if type(value) == tuple:
                output += f"\n{spaces}- {key}: " \
                          f"{str(make_pack(value[0], indent_level))}"
                output += f"\n{spaces}+ {key}: " \
                          f"{str(make_pack(value[1], indent_level))}"
        elif status == diff.UNCHANGED:
            if type(value) == dict:
                output += f"\n{spaces}  {key}: " \
                          f"{make_pack(value, indent_level)}"
            else:
                output += f"\n{spaces}  {key}: " \
                          f"{make_pack(value, indent_level)}"
        elif status == diff.NESTED:
            output += f"\n{spaces}  {key}: " \
                      f"{get_render(value, indent_level + 1)}"
    if indent_level > 1:
        result = '{' + output + '\n' + get_spaces(indent_level - 1) + '  }'
    else:
        result = '{' + output + '\n' + get_spaces(indent_level - 1) + '}'
    return result


def make_pack(node, indent_level=0):
    if node is None:
        return 'null'
    if type(node) is bool:
        return 'true' if node else 'false'
    if isinstance(node, dict):
        output_text = '{'
        for key, value in node.items():
            spaces = get_spaces(indent_level + 1)
            if isinstance(value, dict):
                output_text += f'\n{spaces}  {key}: ' \
                    f'{make_pack(value, indent_level + 1)}'
            else:
                output_text += f'\n{spaces}  {key}: {value}'
        output_text += f'\n{get_spaces(indent_level)}  }}'
        return output_text
    else:
        return node


def get_spaces(depth):
    return ' ' * (depth * 4 - 2)
