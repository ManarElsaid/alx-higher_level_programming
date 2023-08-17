#!/usr/bin/python3
def number_keys(a_dictionary):
    nb_keys = 0
    list(a_dictionary)
    for i in a_dictionary:
        nb_keys += 1
    return nb_keys
