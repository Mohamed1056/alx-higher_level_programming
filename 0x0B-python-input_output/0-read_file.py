#!/usr/bin/python3
'''Module for read_file function'''


def read_file(filename=""):
    '''reads file name with utf-8'''
    with open(filename, encoding="utf-8") as MyFile:
        print(MyFile.read())
