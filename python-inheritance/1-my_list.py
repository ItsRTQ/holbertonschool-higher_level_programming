#!/usr/bin/python3
"""Module defines the classn MyList"""


class MyList(list):
    """MyList is a child of list
        Definitions:
            print_sorted(): prints MyList, sorted.
    """

    def print_sorted(self):
        one_shot = self.copy()
        one_shot.sort()
        print(one_shot)
