#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    amount = 0
    for amount, i in enumerate(range(x), start=1):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            print()
            return amount - 1
    print()
    return amount
