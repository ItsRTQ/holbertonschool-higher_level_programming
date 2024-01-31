#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        ordered_keys = list(a_dictionary.keys())
        ordered_keys.sort()
        for key in ordered_keys:
            print("{}: {}".format(key, a_dictionary[key]))
