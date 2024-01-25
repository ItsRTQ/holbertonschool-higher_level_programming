#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    argc = 0
    if my_list:
        for number in my_list:
            if argc == idx:
                del (my_list[argc])
                return my_list
            argc += 1
    return my_list
