from gendiff.diff.format.supporting import make_value, get_match, get_key
from gendiff.diff.format.supporting import sort_tree


def stylish(tree, dept=0):
    exit = []
    exit.append("{\n")
    sorted_tree = sorted(tree, key=sort_tree)
    for comparsion in sorted_tree:
        str = []
        match = get_match(comparsion)
        strings = comparsion[match]
        first = strings.get("first")
        second = strings.get("second")
        if (first is None) and (match == "u"):
            str = add(second, str, dept, "+ ")
        elif (second is None) and (match == "u"):
            str = add(first, str, dept, "- ")
        elif (second is None) and (match == "m"):
            first_key = get_key(first)
            str.append("".join(["    " * (dept + 1), f"{first[first_key]}: "]))
            if first_key == "parent":
                str.append("".join(stylish(first['children'], dept + 1)))
            else:
                str.append(f"{first['value']}")
        else:
            str = difference(first, second, str, dept)
        exit.append("".join(str))
        exit.append("\n")
    exit.append("    " * dept)
    exit.append("}")
    return "".join(exit)


def add(tree, str, dept, char):
    """This function is the part of STYLISH to
    avoid the linter problems"""
    key = get_key(tree)
    str.append("    " * dept)
    str.append("  ")
    str.append(char)
    if key == "parent":
        str.append(f"{tree[key]}: ")
        str.append("".join(stylish(tree['children'], dept + 1)))
    else:
        str.append(f"{tree[key]}: ")
        str.append(f"{make_value(tree['value'])}")
    return str


def difference(first, second, str, dept):
    """This function is the part of STYLISH, to
    avoid the linter problems"""
    first_key = get_key(first)
    second_key = get_key(second)
    str.append("    " * dept)
    str.append("  ")
    str.append("- ")
    str.append(f"{first[first_key]}: ")
    if first_key == "parent":
        str.append("".join(stylish(first['children'], dept + 1)))
        str.append("\n")
    else:
        str.append(f"{make_value(first['value'])}")
        str.append("\n")
    str.append("    " * dept)
    str.append("  ")
    str.append("+ ")
    str.append(f"{second[second_key]}: ")
    if second_key == "parent":
        str.append("".join(stylish(second['children'], dept + 1)))
    else:
        str.append(f"{make_value(second['value'])}")
    return str
