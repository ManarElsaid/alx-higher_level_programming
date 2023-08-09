#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a == ord('e') || a == ord('q'):
        break
    else:
        print("{:c}".format(a), end = "")
