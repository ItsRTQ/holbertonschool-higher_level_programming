#!/usr/bin/python3
import hidden_4
all_names = dir(hidden_4)
toPrint = []
if __name__ == "__main__":
    for i in all_names:
        if i[0] != '_':
            toPrint.append(i)
    toPrint.sort()
    for j in toPrint:
        print(j)
