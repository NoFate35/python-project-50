from gendiff.diff.format.change_values import make_value


def get_match(comparsion):
    """abstract level function"""
    char = comparsion.get("m")
    if char is None:
        return "u"
    return "m"


def get_key(string):
    """abstract level function"""
    key = string.get("key")
    if key is None:
        return "parent"
    return "key"


def sort_tree(ls):
    """sort values of the difference list by alphabet in formatter function"""
    comparsion = ls[get_match(ls)]
    first = comparsion.get("first")
    second = comparsion.get("second")
    if first:
        parent = first.get("parent")
        if parent:
            return parent
        else:
            return first["key"]
    else:
        parent = second.get("parent")
        if parent:
            return parent
        else:
            return second["key"]


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
            str = if_in_stylish(first, second, str, dept)
        elif (second is None) and (match == "u"):
            str = elif_in_stylish(first, second, str, dept)
        elif (second is None) and (match == "m"):
            first_key = get_key(first)
            str.append("".join(["    " * (dept + 1), f"{first[first_key]}: "]))
            if first_key == "parent":
                str.append("".join(stylish(first['children'], dept + 1)))
            else:
                str.append(f"{first['value']}")
        else:
            str = else_in_stylish(first, second, str, dept)
        exit.append("".join(str))
        exit.append("\n")
    exit.append("    " * dept)
    exit.append("}")
    return "".join(exit)


def if_in_stylish(first, second, str, dept):
    """This function is the part of STYLISH to
    avoid the linter problems"""
    second_key = get_key(second)
    str.append("    " * dept)
    str.append("  ")
    str.append("+ ")
    if second_key == "parent":
        str.append(f"{second[second_key]}: ")
        str.append("".join(stylish(second['children'], dept + 1)))
    else:
        str.append(f"{second[second_key]}: ")
        str.append(f"{make_value(second['value'])}")
    return str


def elif_in_stylish(first, second, str, dept):
    """This function is the part of STYLISH, to
    avoid the linter problems"""
    first_key = get_key(first)
    str.append("    " * dept)
    str.append("  ")
    str.append("- ")
    if first_key == "parent":
        str.append(f"{first[first_key]}: ")
        str.append("".join(stylish(first['children'], dept + 1)))
    else:
        str.append(f"{first[first_key]}: ")
        str.append(f"{first['value']}")
    return str


def else_in_stylish(first, second, str, dept):
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
    str.append(f"{make_value(second['value'])}")
    return str