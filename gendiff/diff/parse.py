import os
import json
import yaml
from yaml.loader import SafeLoader


def get_data(file_path1, file_path2):
    """This function accepts file path's,
    choose the extention
    and load the files objects (based on extention)"""
    file_path, file_extention = os.path.splitext(file_path1)
    if file_extention == ".json":
        data1 = json.load(open(file_path1))
        data2 = json.load(open(file_path2))
    else:
        with open(file_path1) as file_object1:
            with open(file_path2) as file_object2:
                data1 = yaml.load(file_object1, Loader=SafeLoader)
                data2 = yaml.load(file_object2, Loader=SafeLoader)
    return data1, data2
