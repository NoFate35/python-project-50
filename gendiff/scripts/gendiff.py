#!/usr/bin/env python

import argparse
from gendiff.diff.get_diff import generate_diff


"""Get arguments and call generate_diff function"""


def main():
    descript = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=descript)
    parser.add_argument('first_file', type=str, help="in file")
    parser.add_argument('second_file', type=str, help="out file")
    parser.add_argument("-f", "--format", type=str, help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == "main":
    main()
