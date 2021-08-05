KEY = 'key'
VALUE = 'value'
TYPE = 'type'
ADDED = '+ '
REMOVED = '- '
UNCHANGED = '  '
CHANGED = 'changed'
NESTED = 'nested'


def diff(source1, source2):
    removed = source1.keys() - source2.keys()
    added = source2.keys() - source1.keys()
    common = source1.keys() & source2.keys()
    result = []
    for key in common:
        if source1[key] == source2[key]:
            result.append({
                          KEY: key, VALUE: source1[key],
                          TYPE: UNCHANGED})
        elif isinstance(source1[key], dict) and isinstance(source2[key], dict):
            result.append({
                          KEY: key, VALUE: diff(source1[key], source2[key]),
                          TYPE: NESTED})
        else:
            result.append({
                          KEY: key, VALUE: (source1[key], source2[key]),
                          TYPE: CHANGED})
    for key in removed:
        result.append({KEY: key, VALUE: source1[key], TYPE: REMOVED})

    for key in added:
        result.append({KEY: key, VALUE: source2[key], TYPE: ADDED})
    return result
