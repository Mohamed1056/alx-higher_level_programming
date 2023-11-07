#!/usr/bin/python3
'''Module for class method.'''


class Student:
    """representaion of a student class."""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation."""
        try:
            for attr in self.attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in self.attrs:
                my_dict[key] = value
                return my_dict
