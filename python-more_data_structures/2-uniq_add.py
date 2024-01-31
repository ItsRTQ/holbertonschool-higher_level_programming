#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        skip = []
        result = 0
        for value in my_list:
            if value in skip:
                pass
            else:
                result += value
                skip.append(value)
        return result
    else:
        return my_list
