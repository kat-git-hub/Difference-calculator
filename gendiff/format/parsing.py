import json
import yaml


def get_parsing(source):
    file_type = source.split('.')
    if file_type[1] == 'json' or file_type[1] == 'JSON':
        return json.load(open(source))
    if file_type[1] == 'yml' or file_type[1] == 'yaml' or file_type[1] == 'YML':
        return yaml.load(open(source), Loader=yaml.FullLoader)
