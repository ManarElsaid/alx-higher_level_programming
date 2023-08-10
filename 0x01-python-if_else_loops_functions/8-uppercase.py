#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) >= 97 and ord(n) <= 122:
            print("{:c}".format(ord(n) - 32), end="")
        else:
            print("{:s}".format(n), end="")
    print("\n")
