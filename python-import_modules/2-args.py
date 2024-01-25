#!/usr/bin/python3
from sys import argv
argc = len(argv)
if __name__ == "__main__":
    print("{} argument".format(argc - 1), end="")
    if argc - 1 != 0:
        if argc == 2:
            print(':')
        else:
            print('s:')
    else:
        print('s.')
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
