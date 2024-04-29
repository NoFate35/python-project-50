def formatter1(exit, file_extention):
    dept = 1
    def walk(exit, file_extention, dept):
    	for comparsion in exit:
    		str = []
    		str.append("...." * dept)
    		match = comparsion.get("m")
    		if match is None:
    			match = comparsion["u"]
    			str.append("-")
    		else: str.append("+")
    		#print("match", match)
    		first = match.get("first")
    		second = match.get("second")
    		print("first", first, "second", second)
    		"""
    		parent = comparsion[match].get("parent")
    		if parent is None:
    			parent = "key"
    		value =
    		"""
    	return
    return walk(exit, file_extention, dept)