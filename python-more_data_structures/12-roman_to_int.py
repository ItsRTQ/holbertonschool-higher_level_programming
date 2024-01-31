#!/usr/bin/python3
def roman_to_int(roman_string):
    intervals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    if roman_string:
        result = 0
        second = 0
        for letter in reversed(roman_string):
            first = intervals.get(letter, 0)
            if first == 0:
                return 0
            if first < second:
                result -= first
            else:
                result += first
            second = first
        return result
    else:
        return 0
