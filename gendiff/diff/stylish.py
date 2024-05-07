def make_value(value, file_extention):
    if value is False:
        value = 'false'
    elif value is True:
        value = 'true'
    elif value is None:
    	value = "null"
    return value

def get_match(comparsion):
	char = comparsion.get("m")
	if char is None:
		return "u"
	return "m"
	
	
def get_key(string):
	#print("string", string)
	key = string.get("key")
	if key is None:
		return "parent"
	return "key"
	
	
def sort_tree(ls):
	#print("la", ls)
	comparsion = ls[get_match(ls)]
	first = comparsion.get("first")
	second = comparsion.get("second")
	if first:
		parent = first.get("parent")
		if parent:
			#print("parent[0]", parent[0])
			return parent
		else:
			#print("first['key''][0]", first["key"][0])
			return first["key"]
	else:
		parent = second.get("parent")
		if parent:
			#print("parent[0]", parent[0])
			return parent
		else:
			#print("second['key''][0]", second["key"][0])
			return second["key"]
		

def formatter1(tree, file_extention):
    dept = 0
    def walk(tree, file_extention, dept):
    	#print("tree", tree)
    	exit = []
    	exit.append("{\n")
    	sorted_tree = sorted(tree, key=sort_tree)
    	#print("sorted_yree", sorted)
    	for comparsion in sorted_tree:
    		#print("compartion",  comparsion)
    		str = []
    		match = get_match(comparsion)
    		strings = comparsion[match]
    		first = strings.get("first")
    		second = strings.get("second")
    		#print(" second", second)
    		if (first is None) and (match == "u"):
    			second_key = get_key(second)
    			str.append("    " * dept )
    			str.append("  ")
    			str.append("+ ")
    			if second_key == "parent":
    				str.append(f"{second[second_key]}: ")
    				str.append("".join(walk(second['children'], file_extention, dept + 1)))
    				#str.append("".join(["    " * (dept + 1),  "}"]))
    				#str.append("\n")
    			else:
    				str.append(f"{second[second_key]}: ")
    				str.append(f"{make_value(second['value'], file_extention)}")
    				#str.append("\n")
    		elif (second is None) and (match == "u"):
    			first_key = get_key(first)
    			str.append("    " * dept )
    			str.append("  ")
    			str.append("- ")
    			if first_key == "parent":
    				str.append(f"{first[first_key]}: ")
    				str.append("".join(walk(first['children'], file_extention, dept + 1)))
    				#str.append("".join(["    " * (dept + 1), "}"]))
    				#str.append("\n")
    			else:
    				str.append(f"{first[first_key]}: ")
    				str.append(f"{first['value']}")
    				#str.append("\n")
    		elif (second is None) and (match == "m"):
    			#print(" elif (second is None) and (match == 'm'):")
    			first_key = get_key(first)
    			str.append("".join(["    " * (dept + 1), f"{first[first_key]}: "]))
    			if first_key == "parent":
    				str.append("".join(walk(first['children'], file_extention, dept + 1)))
    				#str.append("".join(["    " * (dept + 1), "}"]))
    				#str.append("\n")
    			else:
    				#print("first_key not 'parent")
    				str.append(f"{first['value']}")
    				#str.append("\n")
    				#print("str", str)
    		else:
    				first_key = get_key(first)
    				second_key = get_key(second)
    				str.append("    " * dept )
    				str.append("  ")
    				str.append("- ")
    				str.append(f"{first[first_key]}: ")
    				if first_key == "parent":
    					str.append("".join(walk(first['children'], file_extention, dept + 1)))
    					#str.append("".join(["    " * (dept + 1), "}"]))
    					str.append("\n")
    				else: 
    				    str.append(f"{make_value(first['value'], file_extention)}")
    				    str.append("\n")
    				
    				str.append("    " * dept )
    				str.append("  ")
    				str.append("+ ")
    				str.append(f"{second[second_key]}: ")
    				if second_key == "parent":
    					str.append(f"{walk(second['children'], file_extention, dept + 1)}")
    					#str.append("".join(["\n", "    " * (dept - 1), "  ", "}"]))
    					#str.append("\n")
    				else: 
    				    str.append(f"{make_value(second['value'], file_extention)}")
    				    #str.append("\n")
    		exit.append("".join(str))
    		#print("str", "".join(str))
    		exit.append("\n")
    	exit.append("    " * dept )
    	exit.append("}")
    	return exit
    print("".join(walk(tree, file_extention, dept)))
    return "".join(walk(tree, file_extention, dept)) + "\n"