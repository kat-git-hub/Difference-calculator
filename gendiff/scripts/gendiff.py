from gendiff.diff import generate_diff
from gendiff.cli import parse_args
from gendiff.format.stylish import stylish


def main():
    args = parse_args()
    make_diff = generate_diff(args.first_file, args.second_file)
    result = stylish(make_diff, 1)
    print(result)


if __name__ == '__main__':
    main()
