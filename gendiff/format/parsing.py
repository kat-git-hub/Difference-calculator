import json
import yaml


def get_type(file_in):
    file_type = file_in.split('.')
    if file_type[1] == 'json' or file_type[1] == 'JSON':
        return json.load(open(file_in))
    if file_type[1] == 'yml' or file_type[1] == 'yaml' or file_type[1] == 'YML':
        return yaml.load(open(file_in), Loader=yaml.FullLoader)
