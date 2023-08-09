#!/usr/bin/python3
for n in range(100):
    if n == 99:
        print("{:2d}".format(n))
    else:
        print("{:2d}".format(n), end=", ")
