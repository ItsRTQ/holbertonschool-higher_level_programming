#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and a_dictionary:
        score_amount = 0
        for index, key in enumerate(a_dictionary):
            if index == 0:
                score = key
            if a_dictionary[key] > a_dictionary[score]:
                score = key
        if score:
            for key in a_dictionary:
                if a_dictionary[key] == a_dictionary[score]:
                    score_amount += 1
            if score_amount == 1:
                return score
        return None
    else:
        return None
