#!/usr/bin/python3
import sys
argc = len(sys.argv)
args = sys.argv
print("{} arguments".format(argc - 1), end="")
if argc - 1 != 0:
    print(':')
else:
    print('.')
for i in range(1, argc):
    print("{}: {}".format(i, args[i]))