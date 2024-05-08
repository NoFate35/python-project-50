def make_value(value):
    """change some values in depend of file extention"""
    if value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
    	value = "null"
    return value

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
		

def formatter1(tree):
    """get the dirrerence tree and return string of difference"""
    dept = 0
    def walk(tree, dept):
    	exit = []
    	exit.append("{\n")
    	sorted_tree = sorted(tree, key=sort_tree)
    	for comparsion in sorted_tree:
    		str = []
    		match = get_match(comparsion)
    		strings = comparsion[match]
    		first = strings.get("first")
    		second = strings.get("second")
    		if (first is None) and (match == "u"):
    			second_key = get_key(second)
    			str.append("    " * dept )
    			str.append("  ")
    			str.append("+ ")
    			if second_key == "parent":
    				str.append(f"{second[second_key]}: ")
    				str.append("".join(walk(second['children'], dept + 1)))
    			else:
    				str.append(f"{second[second_key]}: ")
    				str.append(f"{make_value(second['value'])}")
    		elif (second is None) and (match == "u"):
    			first_key = get_key(first)
    			str.append("    " * dept )
    			str.append("  ")
    			str.append("- ")
    			if first_key == "parent":
    				str.append(f"{first[first_key]}: ")
    				str.append("".join(walk(first['children'], dept + 1)))
    			else:
    				str.append(f"{first[first_key]}: ")
    				str.append(f"{first['value']}")
    		elif (second is None) and (match == "m"):
    			first_key = get_key(first)
    			str.append("".join(["    " * (dept + 1), f"{first[first_key]}: "]))
    			if first_key == "parent":
    				str.append("".join(walk(first['children'], dept + 1)))
    			else:
    				str.append(f"{first['value']}")
    		else:
    				first_key = get_key(first)
    				second_key = get_key(second)
    				str.append("    " * dept )
    				str.append("  ")
    				str.append("- ")
    				str.append(f"{first[first_key]}: ")
    				if first_key == "parent":
    					str.append("".join(walk(first['children'], dept + 1)))
    					str.append("\n")
    				else: 
    				    str.append(f"{make_value(first['value'])}")
    				    str.append("\n")
    				
    				str.append("    " * dept )
    				str.append("  ")
    				str.append("+ ")
    				str.append(f"{second[second_key]}: ")
    				if second_key == "parent":
    					str.append(f"{walk(second['children'], dept + 1)}")
    				else: 
    				    str.append(f"{make_value(second['value'])}")
    		exit.append("".join(str))
    		exit.append("\n")
    	exit.append("    " * dept )
    	exit.append("}")
    	return exit
    return "".join(walk(tree, dept)) + "\n"