import argparse


def parse_args():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Generate diff')
    parser.add_argument('-f FORMAT', '--format FORMAT',
                        action='store_true', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args
