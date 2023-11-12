#!/usr/bin/python3
'''Module for Rectangle class.'''


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width of the recatngule.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    '''height of the rectangule.'''
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x of the rectangule.'''
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of the rectangule.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
