import json
import yaml
import os


def get_extension(source):
    _, type = os.path.splitext(source)
    extension = type.lower()
    return extension


def get_parsing(source):
    extension = get_extension(source)
    if extension == '.json':
        return json.load(open(source))
    elif extension == '.yml' or extension == '.yaml':
        return yaml.load(open(source), Loader=yaml.FullLoader)
    else:
        raise ValueError('Unknown extension')
