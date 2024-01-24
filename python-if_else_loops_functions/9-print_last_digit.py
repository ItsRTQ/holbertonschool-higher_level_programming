#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        number = abs(number) % 10
        print("{}".format(number), end="")
        return number
    elif isinstance(number, str) and number.isdigit():
        lastdigit = int(number) % 10
        print("{}".format(lastdigit), end="")
        return lastdigit
    else:
        return None
