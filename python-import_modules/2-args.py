#!/usr/bin/python3
from sys import argv
argc = len(argv)
if __name__ == "__main__":
    print("{} argument".format(argc - 1), end="")
    if argc - 1 != 0:
        if argc - 1 == 1:
            print(':')
        else:
            print('s:')
    else:
        print('.')
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
