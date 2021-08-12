# flake8: noqa: C901
from gendiff import diff


INDENT = 4
SIGN = 2


def get_render(data, indent_level=1):
    output = []
    spaces = get_spaces(indent_level)
    sorting_content = sorted(data, key=lambda i: i[diff.KEY])
    for i in sorting_content:
        status = i[diff.TYPE]
        value = i[diff.VALUE]
        key = i[diff.KEY]
        if status == diff.NESTED:
            output.append(f"\n{spaces}  {key}: "
                          f"{get_render(value, indent_level + 1)}")
        elif status == diff.ADDED:
            output.append(f"\n{spaces}+ {key}: "
                          f"{value_to_string(value, indent_level)}")
        elif status == diff.REMOVED:
            output.append(f"\n{spaces}- {key}: "
                          f"{value_to_string(value, indent_level)}")
        elif status == diff.CHANGED:
            old, new = value
            output.append(f"\n{spaces}- {key}: "
                          f"{value_to_string(old, indent_level)}")
            output.append(f"\n{spaces}+ {key}: "
                          f"{value_to_string(new, indent_level)}")
        elif status == diff.UNCHANGED:
            output.append(f"\n{spaces}  {key}: "
                          f"{value_to_string(value, indent_level)}")
    if indent_level > 1:
        result = (f"{{"
                  f"{''.join(output)}\n{get_spaces(indent_level - 1)}"
                  f"  }}")
    else:
        result = (f"{{"
                  f"{''.join(output)}\n{get_spaces(indent_level - 1)}"
                  f"}}")
    return result


def value_to_string(node, indent_level=0):
    if node is None:
        return 'null'
    if type(node) is bool:
        return 'true' if node else 'false'
    if isinstance(node, dict):
        return render_dict(node, indent_level)
    else:
        return node


def render_dict(node, indent_level):
    output_text = '{'
    for key, value in node.items():
        spaces = get_spaces(indent_level + 1)
        if isinstance(value, dict):
            output_text += (f"\n{spaces}  {key}: "
                            f"{value_to_string(value, indent_level + 1)}")
        else:
            output_text += f"\n{spaces}  {key}: {value}"
    output_text += f"\n{get_spaces(indent_level)}  }}"
    return output_text


def get_spaces(depth):
    return ' ' * (depth * INDENT - SIGN)
