
def get_render(data, nesting_level):
    output = ""
    spaces = get_spaces(nesting_level)
    sorting_content = sorted(data, key=lambda i: i['key'])
    for i in sorting_content:
        if i['type'] == 'added':
            if type(i['value']) == dict:
                output += '\n' + spaces + '+ ' + (i['key']) + ': '\
                    + make_pack(i['value'], nesting_level)
            else:
                output += '\n' + spaces + '+ ' + str(i['key']) + ': '\
                    + str(make_pack(i['value'], nesting_level))
        elif i['type'] == 'removed':
            if type(i['value']) == dict:
                output += '\n' + spaces + '- ' + (i['key']) + ': '\
                    + (make_pack(i['value'], nesting_level))
            else:
                output += '\n' + spaces + '- ' + str(i['key']) + ': '\
                    + str(make_pack(i['value'], nesting_level))
        elif i['type'] == 'changed':
            if type(i['value']) == tuple:
                output += '\n' + spaces + '- ' + (i['key']) + ': '\
                    + str(make_pack(i['value'][0], nesting_level))
                output += '\n' + spaces + '+ ' + (i['key']) + ': '\
                    + str(make_pack(i['value'][1], nesting_level))
        elif i['type'] == 'unchanged':
            if type(i['value']) == dict:
                output += '\n' + spaces + '  ' + (i['key']) + ': '\
                    + make_pack(i['value'], nesting_level)
            else:
                output += '\n' + spaces + '  ' + (i['key']) + ': '\
                    + make_pack(i['value'], nesting_level)
        elif i['type'] == 'nested':
            output += '\n' + spaces + '  ' + (i['key']) + ': '\
                + get_render(i['value'], nesting_level + 1)
    if nesting_level > 1:
        result = '{' + output + '\n' + get_spaces(nesting_level - 1) + '  }'
    else:
        result = '{' + output + '\n' + get_spaces(nesting_level - 1) + '}'
    return result


def make_pack(node, nesting_level=0):
    if node is None:
        return 'null'
    if type(node) is bool:
        return 'true' if node else 'false'
    if isinstance(node, dict):
        output_text = '{'
        for key, value in node.items():
            spaces = get_spaces(nesting_level + 1)
            if isinstance(value, dict):
                output_text += f'\n{spaces}  {key}: ' \
                    f'{make_pack(value, nesting_level + 1)}'
            else:
                output_text += f'\n{spaces}  {key}: {value}'
        output_text += f'\n{get_spaces(nesting_level)}  }}'
        return output_text
    else:
        return node


def get_spaces(depth):
    return ' ' * (depth * 4 - 2)
