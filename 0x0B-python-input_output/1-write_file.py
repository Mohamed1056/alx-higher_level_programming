#!/usr/bin/python3
'''Module for write_file function'''


def write_file(filename="", text=""):
    '''reads file with utf-8'''
    with open(filename, "w", encoding="utf-8") as MyFile:
        return MyFile.write(text)
