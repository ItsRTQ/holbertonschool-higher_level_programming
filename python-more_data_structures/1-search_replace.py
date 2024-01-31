#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        new_list = my_list.copy()
        for index, value in enumerate(new_list):
            if value == search:
                new_list[index] = replace
        return new_list
    else:
        return None
