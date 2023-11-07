#!/usr/bin/python3
'''Module for from_json_string function'''


import json


def from_json_string(my_str):
    '''function to return from json to dict'''
    return json.loads(my_str)
