KEY = 'key'
VALUE = 'value'
TYPE = 'type'
ADDED = 'added+ '
REMOVED = 'removed- '
UNCHANGED = 'unchanged  '
CHANGED = 'changed  '
NESTED = 'nested  '


def make_diff(source1, source2):
    removed = source1.keys() - source2.keys()
    added = source2.keys() - source1.keys()
    common = source1.keys() & source2.keys()
    result = []
    for key in common:
        value1 = source1[key]
        value2 = source2[key]
        if value1 == value2:
            result.append({
                          KEY: key, VALUE: value1,
                          TYPE: UNCHANGED})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            result.append({
                          KEY: key, VALUE: make_diff(value1, value2),
                          TYPE: NESTED})
        else:
            result.append({
                          KEY: key, VALUE: (value1, value2),
                          TYPE: CHANGED})
    for key in removed:
        result.append({KEY: key, VALUE: source1[key], TYPE: REMOVED})
    for key in added:
        result.append({KEY: key, VALUE: source2[key], TYPE: ADDED})
    return result
