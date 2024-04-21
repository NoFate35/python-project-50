from gendiff.diff.parse import get_data
from gendiff.diff.stylish import formatter1


def make_value(value, file_extention):
    if value is False:
        value = 'false'
    elif (value is True) and (file_extention == ".yml"):
        value = 'true'
    return value


def generate_diff(file_path1, file_path2):
    data1, data2, file_extention = get_data(file_path1, file_path2)
    """get paths to files and return difference of them fot .txt string"""
    return get_diff_dict(data1, data2, file_extention)
    
def get_diff_dict(data1, data2, file_extention):
    def walk(tree1, tree2, file_extention, dept):
        string = {}
        visited = set()
        for key1 in tree1.keys():
                visited.add(key1)
                if key1 in tree2.keys():
                    string['name'] = [key1]
                    string["meta"] = ["m", dept]
                    if isinstance(tree1[key1], dict) == True:
                        string["children"] = walk(tree1[key1], tree2[key1], file_extention, dept + 1)
                    else:
                        if tree1[key1] == tree2[key1]:
                            string["value"] = [tree1[key1]]
                        else:
                            string["value"] = [tree1[key1], tree2[key1]]
                            string["meta"] = ["u", dept]
                else:
                    string["name"] = [key1]
                    string["meta"] = ["u", dept]
                    if isinstance(tree1[key1], dict) == True:
                            
                            
    exit = walk(data1, data2, file_extention, 1)
    return formatter1(exit)
