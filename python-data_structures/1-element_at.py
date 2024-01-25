#!/usr/bin/python3
def element_at(my_list, idx):
    argc = 0
    if my_list:
        for number in my_list:
            if argc == idx:
                return number
            argc += 1
    return None
