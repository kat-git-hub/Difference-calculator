import json
import yaml
import os


def get_parsing(source):
    _, type = os.path.splitext(source)
    if type.lower() == '.json':
        return json.load(open(source))
    elif type.lower() == '.yml' or type.lower() == '.yaml':
        return yaml.load(open(source), Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown extension')
