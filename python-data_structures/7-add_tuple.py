#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aLen = len(tuple_a)
    bLen = len(tuple_b)
    if aLen == 2 and bLen == 2:
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return result
    newTA = (tuple_a[0] if aLen >= 1 else 0, tuple_a[1] if aLen == 2 else 0)
    newTB = (tuple_b[0] if bLen >= 1 else 0, tuple_b[1] if bLen == 2 else 0)

    result = (newTA[0] + newTB[0], newTA[1] + newTB[1])
    return result
