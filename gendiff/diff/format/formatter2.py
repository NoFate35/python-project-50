from gendiff.diff.format.supporting import make_value, get_match, get_key
from gendiff.diff.format.supporting import sort_tree


def plain(tree):    # noqa: C901
    """FORMATTER PLAIN get the tree of
    difference and return the diffefence in string
    format"""
    out = []

    def walk(tree, prop):
        sorted_tree = sorted(tree, key=sort_tree)
        for comparsion in sorted_tree:
            match = get_match(comparsion)
            strings = comparsion[match]
            first = strings.get("first")
            second = strings.get("second")
            if first and second:
                first_key = get_key(first)
                second_key = get_key(second)
                prop.append(f"{first[first_key]}")
                propertie = ".".join(prop)
                text = " was updated. From "
                if first_key == "parent":
                    text += "[complex value]"
                else:
                    text += f"{make_value(first['value'], 'f2')}"
                text += " to "
                if second_key == "parent":
                    text += "[complex value]"
                else:
                    text += f"{make_value(second['value'], 'f2')}"
                out.append("Property " + "'" + propertie + "'" + text + "\n")
            elif (first is None) and (match == "u"):
                key = get_key(second)
                prop.append(f"{second[key]}")
                propertie = ".".join(prop)
                text = " was added with value: "
                if key == "parent":
                    text += "[complex value]"
                else:
                    text += f"{make_value(second['value'], 'f2')}"
                out.append("Property " + "'" + propertie + "'" + text + "\n")
            elif (second is None) and (match == "m"):
                first_key = get_key(first)
                prop.append(f"{first[first_key]}")
                if first_key == "parent":
                    walk(first['children'], prop)
                else:
                    pass
            elif (second is None) and (match == "u"):
                key = get_key(first)
                prop.append(f"{first[key]}")
                propertie = ".".join(prop)
                text = " was removed"
                out.append("Property " + "'" + propertie + "'" + text + "\n")
            prop.pop()
    walk(tree, prop=[])
    return "".join(out)
