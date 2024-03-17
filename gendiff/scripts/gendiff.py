#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help="in file")
    parser.add_argument('second_file', type=str, help="out file")
    parser.add_argument("-f", "--format", type=str, help="set format of output")
    parser.parse_args()


if __name__ == "main":
    main()
