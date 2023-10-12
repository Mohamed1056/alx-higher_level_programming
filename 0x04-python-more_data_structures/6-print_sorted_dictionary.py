#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    list_dir = list(a_dictionary.keys())
    list_dir.sort()
    for i in list_dir:
        print("{}: {}".format(i, a_dictionary.get(i)))
