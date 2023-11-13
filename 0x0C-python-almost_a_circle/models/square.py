#!/usr/bin/python3
'''Module for square class.'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''representaion of the class.'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''represent string for the user.'''
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        '''Size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
