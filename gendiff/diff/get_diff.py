from gendiff.diff.parse import get_data
from gendiff.diff.stylish import formatter1


def generate_diff(file_path1, file_path2):
    data1, data2, file_extention = get_data(file_path1, file_path2)
    """get paths to files and return difference of them fot .txt string"""
    return get_diff_dict(data1, data2, file_extention)
    
def get_diff_dict(data1, data2, file_extention):
    def walk(tree1, tree2, file_extention, flag):
        #print("tree1", tree1, "tree2", tree2, sep='\n')
        if tree2 == {}:
        	flag = "m"
        #print("flag", flag)
        string = []
        visited = set()
        for key1 in  tree1.keys():
                #print("for flag", flag)
                #print("for key1 in tree1.keys(): key1")
                visited.add(key1)
                if key1 in tree2.keys():
                    #print("if key1 in tree2.keys() key1", key1)
                    if isinstance(tree1[key1], dict) == True:
                        if isinstance(tree2[key1], dict) == True:
                            
                            string.append({
                            "m": {
                           "first": {"parent": key1,
                            "children": walk(tree1[key1], tree2[key1], file_extention, "u")}}})
                        else:
                        	string.append({
                            flag: {
                            "first": {"parent": key1, "children": walk(tree1[key1], {}, file_extention, flag)}, 
                            "second": {"key": key1, "value": tree2[key1] }}})
                    else:
                        if isinstance(tree2[key1], dict) == True:
                        	string.append({
                            flag: {
                            "first": {"key": key1, "value": tree1[key1]}, 
                            "second": {"parent": key1, "children": walk(tree2[key1], {}, file_extention, flag) }}})
                        else:
                            if tree1[key1] == tree2[key1]:
                            	string.append({
                            "m": {
                            "first": {"key": key1, "value": tree1[key1]}}})
                            else:
                            	string.append({
                            flag: {
                            "first": {"key": key1, "value": tree1[key1]}, 
                            "second": {"key": key1, "value": tree2[key1]}}})
        
                            	#print("tree1[key1], tree2[key1]",tree1[key1], tree2[key1])
                else:
                    if isinstance(tree1[key1], dict) == True:
                            string.append({
                            flag: {
                            "first": {"parent": key1, "children": walk(tree1[key1], {}, file_extention, flag)}}})
                    else:
                            #print("ffflllaaggg", flag, "value", tree1[key1])
                            string.append({
                            flag: {
                            "first": {"key": key1, "value": tree1[key1]}}})
        flag = "u"
        for key2 in tree2.keys():
            if key2 in visited:
            				pass
            elif isinstance(tree2[key2], dict) == True:
                            string.append({
                            flag: {
                            "second": {"parent": key2, "children": walk(tree2[key2], {}, file_extention, flag) }}})
            else:
                            string.append({
                            flag: {
                            "second": {"key": key2, "value": tree2[key2]}}})
        #print("string", string["parent1"], "dept", dept)
        return string
    exit = walk(data1, data2, file_extention, "u")
    #print("get_diff", exit)
    return formatter1(exit, file_extention)
