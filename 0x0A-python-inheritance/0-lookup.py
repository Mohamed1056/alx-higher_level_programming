#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """Looks up for object attributes.
    Args:
        obj: The object list.
    Returns:
        list: the list of attributes.
    """
    return dir(obj)
