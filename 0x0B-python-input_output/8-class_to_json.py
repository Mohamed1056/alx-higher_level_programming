#!/usr/bin/python3
'''module for class_to_json function'''


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer, boolen)
    for json serilization """
    return obj.__dict__
