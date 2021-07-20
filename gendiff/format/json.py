import json


def get_json(data):
    sorting_content = sorted(data, key=lambda i: i['key'])
    return json.dumps(sorting_content)
