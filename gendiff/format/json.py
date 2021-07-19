import json


def get_json(data):
    return json.dumps(data, sort_keys=True)
