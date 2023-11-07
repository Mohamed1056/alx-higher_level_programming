#!/usr/bin/python3
'''Module for append_write funcion'''


def append_write(filename="", text=""):
    '''function to return the nuber of letters in this str'''
    with open(filename, "a", encoding="utf-8") as MyFile:
        return MyFile.write(text)
