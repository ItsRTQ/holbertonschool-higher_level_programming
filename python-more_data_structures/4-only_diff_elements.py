#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elements = []
    for value in set_1:
        if value in set_2:
            pass
        else:
            diff_elements.append(value)
    for value in set_2:
        if value in set_1:
            pass
        else:
            diff_elements.append(value)
    return diff_elements
