#!/usr/bin/python3
from sys import argv
argc = len(argv)
result = 0
if argc == 2:
    print('0')
else:
    for i in range(1, argc):
        result += int(argv[i])
    print(f"{result}")
