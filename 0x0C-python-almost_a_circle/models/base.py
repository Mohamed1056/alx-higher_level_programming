#!/usr/bin/python3
'''Module for Base class'''


class Base:
    '''representaion of class Base'''
    __nb_objects = 0
    
    def __init__(self, id=None):
        '''constructor.'''
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id    
