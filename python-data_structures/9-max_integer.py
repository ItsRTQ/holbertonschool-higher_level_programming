#!/usr/bin/python3
def max_integer(my_list=[]):
    check = 0
    if not my_list:
        return None
    else:
        for i in my_list:
            if i > check:
                check = i
        return check
