#!/usr/bin/env python
import argparse
import json


def only_str(s):
    return s.strip(' -+')


def generate_diff(file_path1, file_path2):
    read_file1 = json.load(open(file_path1))
    read_file2 = json.load(open(file_path2))
    file_before = read_file1.items()
    file_after = read_file2.items()
    diff_before = file_before - file_after
    diff_after = file_after - file_before
    intersect = file_before & file_after
    output_file = make_formatting(diff_before, diff_after, intersect)
    return output_file


def make_formatting(file1, file2, file3):
    format_file1 = [' - ' + str(i[0]) + ': ' + str(i[1]) for i in file1]
    format_file2 = [' + ' + str(i[0]) + ': ' + str(i[1]) for i in file2]
    format_file3 = ['   ' + str(i[0]) + ': ' + str(i[1]) for i in file3]
    concatination = format_file1 + format_file2 + format_file3
    merging_files = sorted(concatination, key=only_str)
    output = ('{' + '\n' + '\n'.join(merging_files) + '\n' + '}').lower()
    return output


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Generate diff')
    parser.add_argument('-f FORMAT', '--format FORMAT', action='store_true',
                        help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()
    generate_diff(file_path1, file_path2)


if __name__ == '__main__':
    main()
