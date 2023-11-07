#!/usr/bin/python3
'''Module for add_item file.'''


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


arglist = list(sys.argv[1:])

try:
    old_data = load_from_json_file('add_item.json')
except Exception:
    old_data = []

old_data.extend(arglist)
save_to_json_file(old_data, 'add_item.json)
