from gendiff.diff.parse import get_data
from gendiff.diff.format.formatter1 import stylish
from gendiff.diff.format.formatter2 import plain


def generate_diff(file_path1, file_path2, format="stylish"):
    data1, data2 = get_data(file_path1, file_path2)
    """get paths to files, transfer them to the
    GET_DATA and receive files objects from
    GET_DATA. give files objects to the
    GET_DIFF_DICT and rerurn result string"""
    return get_diff_dict(data1, data2, format)


def walk(tree1, tree2, flag):
    """generate the list of difference recursive and"""
    """return his to GET DIFF DICT """
    if tree2 == {}:
        flag = "m"
    string = []
    visited = set()
    flag, string, visited = first_tree(tree1, tree2, flag, string, visited)
    string = second_tree(tree2, visited, string)
    return string


def if_key1_in_tree2(key1, tree1, tree2, flag, string):
    if isinstance(tree1[key1], dict):
        if isinstance(tree2[key1], dict):
            string.append({
                                         "m": {
                                                   "first": {"parent": key1,
                                                             "children":
                                                             walk(tree1[key1],
                                                                  tree2[key1],
                                                                  "u")}}})
        else:
            string.append({
                                        flag: {
                                                   "first": {"parent": key1,
                                                             "children":
                                                             walk(tree1[key1],
                                                                  {}, flag)},
                                                   "second": {
                                                                   "key": key1,
                                                                   "value":
                                                                   tree2[key1]
                                                                   }}})
    else:
        if isinstance(tree2[key1], dict):
            string.append({
                flag: {
                           "first": {
                                     "key": key1,
                                     "value": tree1[key1]},
                           "second": {
                                           "parent": key1,
                                           "children":
                                           walk(tree2[key1],
                                                {}, flag)}}})
        else:
            if tree1[key1] == tree2[key1]:
                string.append({
                                             "m": {
                                                   "first": {
                                                            "key": key1,
                                                            "value":
                                                            tree1[key1]}}})
            else:
                string.append({
                    flag: {
                               "first": {
                                         "key": key1,
                                         "value": tree1[key1]},
                               "second": {
                                               "key": key1,
                                               "value": tree2[key1]}}})
    return string, flag


def first_tree(tree1, tree2, flag, string, visited):
    """This function is the part of WALK to avoid linter complex error """
    for key1 in tree1.keys():
        visited.add(key1)
        if key1 in tree2.keys():
            string, flag = if_key1_in_tree2(key1, tree1, tree2, flag, string)
        else:
            if isinstance(tree1[key1], dict):
                string.append({
                            flag: {
                                   "first": {
                                             "parent": key1,
                                             "children":
                                             walk(tree1[key1],
                                                  {}, flag)}}})
            else:
                string.append({
                            flag: {
                                   "first": {
                                             "key": key1,
                                             "value": tree1[key1]}}})
    return flag, string, visited


def second_tree(tree2, visited, string):
    """This function is the part of WALK to avoid linter complex error """
    for key2 in tree2.keys():
        if key2 in visited:
            pass
        elif isinstance(tree2[key2], dict):
            string.append({
                        "u": {
                             "second": {
                                             "parent": key2,
                                             "children":
                                             walk(tree2[key2],
                                                  {}, "u")}}})
        else:
            string.append({
                            "u": {
                                 "second": {
                                                 "key": key2,
                                                 "value": tree2[key2]}}})
    return string


def get_diff_dict(data1, data2, formatter):
    """get files objects and transfer them for
    comparsion to WALK,
    then result of WALK transfer to FORMATTER
    Ready string from FORMATTER return to
    GENERATE_DICT"""
    dict_of_difference = walk(data1, data2, "u")
    if formatter == "plain":
        return plain(dict_of_difference)
    else:
        return stylish(dict_of_difference)
