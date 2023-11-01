#!/usr/bin/python3
"""Deines a class Rectangle."""


class Rectangle:
    """represantion of the class Rectangle."""
    number_of_instance = 0
    """represnt te number of instances."""
    print_symbol = "#"
    """type: can print any type."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instance += 1

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returnes the area of the rectangul."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangule."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """returning string to the user."""
        if not self.__width or not self.__height:
            return ""
        return (str(self.print_symbol) * self.width + "\n") *
                self.height)[:-1]

    def __repr__(self):
        """returning a represntation to the designer."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every delete of a rectangule."""
        print("Bye rectangule...")
        Rectangle.number_of_instance -= 1
