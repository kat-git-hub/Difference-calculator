from gendiff.diff import generate_diff
from gendiff.format.stylish import get_render
from gendiff.format.plain import get_plain
from gendiff.format.json import get_json

__all__ = ('generate_diff', 'get_render', 'get_plain', 'get_json')
