def diff(source1, source2):
    removed = source1.keys() - source2.keys()
    added = source2.keys() - source1.keys()
    common = source1.keys() & source2.keys()
    result = []
    for key in common:
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
    for key in removed:
        result.append({'key': key, 'value': source1[key], 'type': 'removed'})

    for key in added:
        result.append({'key': key, 'value': source2[key], 'type': 'added'})
    return result
