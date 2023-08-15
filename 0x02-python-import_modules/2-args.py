#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    print("{:d}".format(len(sys.argv) - 1), end=" ")
    if len(sys.argv) == 1:
        print("argument.")
    elif len(sys.argv) == 2:
        print("argument:")
    else:
        print("arguments:")

    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))

