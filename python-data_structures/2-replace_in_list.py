#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    argc = 0
    if my_list:
        for number in my_list:
            if argc == idx:
                my_list[argc] = element
                return my_list
            argc += 1
    return my_list
