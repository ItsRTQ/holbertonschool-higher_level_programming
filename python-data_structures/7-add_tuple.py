#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aLen = len(tuple_a)
    bLen = len(tuple_b)
    a1, a2 = tuple_a[0] if aLen > 0 else 0, tuple_a[1] if aLen > 1 else 0
    b1, b2 = tuple_b[0] if bLen > 0 else 0, tuple_b[1] if bLen > 1 else 0
    total = (a1 + b1, a2 + b2)
    return total
