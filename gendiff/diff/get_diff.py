from gendiff.diff.parse import get_data


def make_value(value, file_extention):
    if value is False:
        value = 'false'
    elif (value is True) and (file_extention == ".yml"):
        value = 'true'
    return value


def generate_diff(file_path1, file_path2):
    data1, data2, file_extention = get_data(file_path1, file_path2)
    """get paths to files and return difference of them fot .txt string"""
    exit = []
    visited = set()
    for key1, value1 in data1.items():
        value1 = make_value(value1, file_extention)
        visited.add(key1)
        if key1 in data2.keys():
            if value1 == data2[key1]:
                exit.append(f"    {key1}: {value1}\n")
            else:
                exit.append(f"  - {key1}: {value1}\n")
                exit.append(f"  + {key1}: {data2[key1]}\n")
        else:
            exit.append(f"  - {key1}: {value1}\n")
    for key2, value2 in data2.items():
        value2 = make_value(value2, file_extention)
        if key2 in visited:
            continue
        else:
            exit.append(f"  + {key2}: {value2}\n")
    exit.sort(key=lambda x: x[4])
    return ''.join(['{\n'] + exit + ['}\n'])
