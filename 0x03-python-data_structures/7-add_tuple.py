#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    aa, ab = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    ba, bb = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)
    out1 = aa + ba
    out2 = ab + bb

    return (out1, out2)
