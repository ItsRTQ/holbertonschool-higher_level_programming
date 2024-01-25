#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    argc = 0
    if new_list:
        for number in new_list:
            if argc == idx:
                new_list[argc] = element
                return new_list
            argc += 1
    return new_list
