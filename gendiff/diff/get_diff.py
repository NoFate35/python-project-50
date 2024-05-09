from gendiff.diff.parse import get_data
from gendiff.diff.stylish import formatter1


def generate_diff(file_path1, file_path2):
    data1, data2 = get_data(file_path1, file_path2)
    """get paths to files and return difference of them fot .txt string"""
    return get_diff_dict(data1, data2)


def get_diff_dict(data1, data2):
	def walk(tree1, tree2, flag):
		def first_tree(tree1, tree2, flag, string, visited):
			for key1 in  tree1.keys():
				visited.add(key1)
				if key1 in tree2.keys():
					if isinstance(tree1[key1], dict) == True:
						if isinstance(tree2[key1], dict) == True:
							string.append({
                	           	"m": {
                	           	"first": {"parent": key1,
                	           	"children": walk(tree1[key1], tree2[key1], "u")}}})
						else:
							string.append({
                                	flag: {
                                	"first": {"parent": key1, "children": walk(tree1[key1], {}, flag)}, 
                                	"second": {"key": key1, "value": tree2[key1] }}})
					else:
						if isinstance(tree2[key1], dict) == True:
							string.append({
                                		flag: {
                                		"first": {"key": key1, "value": tree1[key1]}, 
                                		"second": {"parent": key1, "children": walk(tree2[key1], {}, flag) }}})
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
				else:
					if isinstance(tree1[key1], dict) == True:
						string.append({
                            	flag: {
                            	"first": {"parent": key1, "children": walk(tree1[key1], {}, flag)}}})
					else:
						string.append({
                            	flag: {
                            	"first": {"key": key1, "value": tree1[key1]}}})
			return (flag, string, visited)
		def second_tree(tree2, visited, string):
			for key2 in tree2.keys():
				if key2 in visited:
					pass
				elif isinstance(tree2[key2], dict) == True:
					string.append({
                            "u": {
                            "second": {"parent": key2, "children": walk(tree2[key2], {}, flag) }}})
				else:
					string.append({
                            "u": {
                            "second": {"key": key2, "value": tree2[key2]}}})
			return string
		if tree2 == {}:
			flag = "m"
		string = []
		visited = set()
		flag, string, visited = first_tree(tree1, tree2, flag, string, visited)
		string = second_tree(tree2, visited, string)
		return string
	exit = walk(data1, data2, "u")
	return formatter1(exit)
