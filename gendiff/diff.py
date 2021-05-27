from gendiff.format.parsing import get_type


def to_only_str(s):
    d = s.strip(' -+')
    a = d.split(':')
    return a[0]


def generate_diff(file_path1, file_path2):
    read_file1 = get_type(file_path1)
    print(type(read_file1))
    read_file2 = get_type(file_path2)
    file_before = read_file1.keys()
    file_after = read_file2.keys()
    diff_before = file_before - file_after
    diff_after = file_after - file_before
    intersect = file_before & file_after
    result = {'add': {}, 'remove': {}, 'change': {}, 'same': {}}
    for key in intersect:
        if read_file1[key] == read_file2[key]:
            result['same'][key] = read_file1[key]
        else:
            result['change'][key] = (read_file1[key], read_file2[key])
    for key in diff_before:
        result['remove'][key] = read_file1[key]
    for key in diff_after:
        result['add'][key] = read_file2[key]
    result1 = make_formatting(result)
    result2 = sorted(result1, key=to_only_str)
    result3 = ('{' + '\n  ' + '\n  '.join(result2) + '\n' + '}').lower()
    return result3


def make_formatting(data):
    output = []
    for key, value in data.items():
        for i, j in value.items():
            if key == 'add':
                output.append('+ ' + str(i) + ': ' + str(j))
            elif key == 'remove':
                output.append('- ' + str(i) + ': ' + str(j))
            elif key == 'same':
                output.append('  ' + str(i) + ': ' + str(j))
            elif key == 'change':
                output.append('- ' + str(i) + ': ' + str(j[0]))
                output.append('+ ' + str(i) + ': ' + str(j[1]))
    return output
