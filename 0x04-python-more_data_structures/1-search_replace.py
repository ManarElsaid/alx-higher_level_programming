#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        new_list = my_list.insert((my_list.index(search, i)), replace)
    return new_list
