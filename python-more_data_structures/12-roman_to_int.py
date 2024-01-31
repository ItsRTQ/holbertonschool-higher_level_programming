#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string:
        result = 0
        skip = False
        invalids = [
            "IIII",
            "VV",
            "XXXX",
            "LL",
            "CCCC",
            "DD",
            "MMMM"
        ]
        intervals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        for invalid in invalids:
            if invalid in roman_string:
                return 0
        for index, letter in enumerate(roman_string, start=1):
            if letter in intervals.keys():
                if skip:
                    skip = False
                    continue
                first = intervals[letter]
                if index < len(roman_string):
                    second = intervals[roman_string[index]]
                else:
                    second = None
                if second:
                    if first >= second:
                        result += (lambda a, b: a + b)(first, second)
                        skip = True
                    elif first < second:
                        result += (lambda a, b: a - b)(second, first)
                        skip = True
                else:
                    result += first
            else:
                return 0
        return result
    else:
        return 0
