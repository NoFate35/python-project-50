import argparse
from gendiff.diff.get_diff import generate_diff


"""Get arguments and call generate_diff function"""


def main():
    descript = 'Compares two configuration files and shows a difference.'
    parser = argparse.ArgumentParser(description=descript)
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument("-f", "--format", type=str, help="set format of output")
    args = parser.parse_args()
    if args.format == "one":
        print("privettt")
    else:
        print(generate_diff(args.first_file, args.second_file))
