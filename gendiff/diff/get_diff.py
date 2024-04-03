import json


def generate_diff(file_path1, file_path2):
    """get paths to files and return difference of them"""
    file_object1 = json.load(open(file_path1))
    file_object2 = json.load(open(file_path2))
    exit = []
    visited = set()
    for key1, value1 in file_object1.items():
        visited.add(key1)
        if key1 in file_object2.keys():
            if value1 == file_object2[key1]:
                exit.append(f"    {key1}: {value1}\n")
            else:
                exit.append(f"  - {key1}: {value1}\n")
                exit.append(f"  + {key1}: {file_object2[key1]}\n")
        else:
            exit.append(f"  - {key1}: {value1}\n")
            #print(f"- {key1}: {value1}\n ")
    for key2, value2 in file_object2.items():
        if key2 in visited:
            continue
        else:
            exit.append(f"  + {key2}: {value2}\n")
    exit.sort(key=lambda x: x[4])
    return ''.join(['{\n'] + exit + ['}'])
