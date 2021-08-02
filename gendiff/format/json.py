from gendiff import diff
import json


def get_json(data):
    sorting_content = sorted(data, key=lambda i: i[diff.KEY])
    return json.dumps(sorting_content)
