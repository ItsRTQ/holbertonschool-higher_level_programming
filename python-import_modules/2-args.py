#!/usr/bin/python3
from sys import argv
argc = len(argv)
if __name__ == "__main__":
    print("{} arguments.".format(argc - 1), end="")
    if argc - 1 != 0:
        print(':')
    else:
        print('.')
    for i in range(1, argc):
        print("{}: {}".format(i, argv[i]))
