#!/usr/bin/python3
'''Module for save_to_json_file function'''


import json


def save_to_json_file(my_obj, filename):
    '''function to save json to file'''
    with open(filename, "w", encoding="utf-8") as MyFile:
        json.dump(my_obj, MyFile)
