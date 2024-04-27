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
    exit = []
    def walk(tree1, tree2, file_extention, dept):
        print("tree1", tree1, "tree2", tree2, sep='\n')
        string = []
        visited = set()
        for key1 in  tree1.keys():
                print("for key1 in tree1.keys(): key1", i)
                visited.add(key1)
                if key1 in tree2.keys():
                    #print("if key1 in tree2.keys() key1", key1)
                    if isinstance(tree1[key1], dict) == True:
                        if isinstance(tree2[key1], dict) == True:
                            string["meta" + str(i)] = ["m", dept]
                            string["patents" + str(i)] = key1
                            string["children" + str(i)] = [walk(tree1[key1], tree2[key1], file_extention, dept + 1)]
                        else:
                        	string['parent' + str(i) + '1'] = key1
                        	string["child" + str(i) + "1"] = walk(tree1[key1], {}, file_extention, dept + 1)
                        	string["key" + str(i) + "2"] = key1
                        	string["meta" + str(i)] = ["u", dept]
                        	string["value" + str(i) + "2"] = tree2[key1]
                    else:
                        if isinstance(tree2[key1], dict) == True:
                        	string["key" + str(i) + "1"] = key1
                        	string["value" + str(i) + "1"] = tree1[key1]
                        	string["parent" + str(i) + "2"] = key1
                        	string["child" + str(i) + "2"] = walk({}, tree2[key1], file_extention, dept + 1)
                        	string["meta"] = ["u", dept]
                        	
                        else:
                            if tree1[key1] == tree2[key1]:
                            	string["keys" + str(i)] = key1
                            	string["values"+ str(i)] = tree1[key1]
                            	string["meta"+ str(i)] = ["m", dept]
                            else:
                            	#print("else else True")
                            	string["keys" + str(i)] = key1
                            	string["value" + str(i) + "1"] = tree1[key1]
                            	string["value" + str(i) + "2"] = tree2[key1]
                            	#print("tree1[key1], tree2[key1]",tree1[key1], tree2[key1])
                            	string["meta" + str(i)] = ["u", dept]
                else:
                    string["meta" + str(i)] = ["u", dept]
                    if isinstance(tree1[key1], dict) == True:
                            string["patent" + str(i) + "1"] = key1
                            string["child" + str(i) + "1"] = walk(tree1[key1], {}, file_extention, dept + 1)
                    else:
                            string["key" + str(i) + "1"] = key1
                            string["value" + str(i) + "1"] = tree1[key1]
        for key2 in tree2.keys():
            				string["meta" + str(i)] = ["u", dept]
            				if key2 in visited:
            					pass
            				if isinstance(tree2[key2], dict) == True:
            					string["patent" + str(i) + "2"] = key2
            					string["child" + str(i) + "2"] = walk({}, tree2[key2], file_extention, dept + 1)
            				else:
            					string["key" + str(i) + "2"] = key2
            					string["value" + str(i) + "2"] = tree2[key2]
        return string
        #print("string", string["parent1"], "dept", dept)
    exit = walk(data1, data2, file_extention, 1)
    return formatter1(exit)
