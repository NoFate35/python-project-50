#!/usr/bin/env python 

import argparse

def main():
        parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
        parser.add_argument('first_file', type = str, help="in file")
        parser.add_argument('second_file', type = str, help="out file")
        args = parser.parse_args()
        print(args. first_file, args.second_file)
        print("Hello!")

if __name__ == "main":
    main()