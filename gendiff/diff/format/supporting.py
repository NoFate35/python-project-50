def make_value(value, formatter="f1"):
    """change some values"""
    if value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
        value = "null"
    elif formatter == "f2":
    	value = "'" + value + "'"
    return value


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
