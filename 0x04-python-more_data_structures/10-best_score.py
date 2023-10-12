#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    new_list = list(a_dictionary.values())
    c = 0

    for i in new_list:
         if c <= i:
            c = i
    return (c)
