#!/usr/bin/python3
'''Module for load_from_json_string function'''


import json


def load_from_json_file(filename):
    '''function to reverse to object'''
    with open(filename, encoding="utf-8") as MyFile:
        return json.load(MyFile)
