from gendiff import generate_diff
from gendiff.cli import parse_args
from gendiff import get_render
from gendiff import get_plain
from gendiff import get_json


def main():
    args = parse_args()
    make_diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'plain':
        print(get_plain(make_diff))
    elif args.format == 'json':
        print(get_json(make_diff))
    else:
        print(get_render(make_diff, 1))


if __name__ == '__main__':
    main()
