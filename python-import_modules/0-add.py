#!/usr/bin/python3
a = 1
b = 2
exec(open('add_0').read())
result = add(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, result))
