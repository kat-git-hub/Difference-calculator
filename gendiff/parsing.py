import json
import yaml
import os


def get_data_type(source):
    _, type = os.path.splitext(source)
    type = type.lower()
    return type


def get_parsing(source):
    type = get_data_type(source)
    if type == '.json':
        return json.load(open(source))
    elif type == '.yml' or type == '.yaml':
        return yaml.load(open(source), Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown extension')
