#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        result = a / b

    except (ZeroDivisionError):
        result = None

    finally:
        return (result)
        print("{}".format(result))