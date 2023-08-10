#!/usr/bin/python3
def pow(a, b):
    for n in range(0, b - 1):
        if b == 0:
            a = 1
        elif b < 0:
            a = a / a
    return a
