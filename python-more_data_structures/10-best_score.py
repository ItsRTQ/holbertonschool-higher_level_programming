#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict):
        for index, key in enumerate(a_dictionary):
            if index == 0:
                score = key
            if a_dictionary[key] > a_dictionary[score]:
                score = key
        if score:
            return score
        else:
            return None
    else:
        return None
