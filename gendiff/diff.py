from gendiff.format.parsing import get_parsing


def generate_diff(file_path1, file_path2):
    source1 = get_parsing(file_path1)
    source2 = get_parsing(file_path2)
    return diff(source1, source2)


def diff(source1, source2):
    file_before = source1.keys()
    file_after = source2.keys()
    diff_before = file_before - file_after
    diff_after = file_after - file_before
    intersect = file_before & file_after
    result = []
    for key in intersect:
        if isinstance(source1[key], dict) and isinstance(source2[key], dict):
            result.append({
                'key': key, 'value': diff(source1[key], source2[key]),
                'type': 'nested'})
        else:
            if source1[key] == source2[key]:
                result.append({
                    'key': key, 'value': source1[key],
                    'type': 'unchanged'})
            else:
                result.append({
                    'key': key, 'value': (source1[key], source2[key]),
                    'type': 'changed'})
    for key in diff_before:
        result.append({'key': key, 'value': source1[key], 'type': 'removed'})

    for key in diff_after:
        result.append({'key': key, 'value': source2[key], 'type': 'added'})
    return result
