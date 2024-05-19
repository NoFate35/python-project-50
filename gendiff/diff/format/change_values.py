def make_value(value):
    """change some values"""
    if value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
        value = "null"
    return value
