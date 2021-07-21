import json
import yaml


def get_parsing(source):
    type = source.split('.')
    if type[1] == 'json' or type[1] == 'JSON':
        return json.load(open(source))
    elif type[1] == 'yml' or type[1] == 'yaml' or type[1] == 'YML':
        return yaml.load(open(source), Loader=yaml.FullLoader)
