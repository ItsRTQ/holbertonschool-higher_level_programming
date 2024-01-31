#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    if my_list:
        skip = []
        for value in my_list:
            if value in skip:
                pass
            else:
                result += value
                skip.append(value)
        return result
    else:
        return result
