#!/usr/bin/python3
"""This base will be the base of all other classes in this project"""

from models.base import Base

import sys


class Rectangle(Base):
    """Rectangel class inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises attributes int this subclass"""
        super().__init__(id)
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.getter
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    @property
    def width(self):
        return self.__width

    @width.getter
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.getter
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""

        return self.__height * self.__width

    def display(self):
        """Displays the triangle in with # """

        i = 0
        j = 0
        while(i < self.__height):
            while(j < self.__width):
                j += 1
                print("#", file=sys.stdout, end='')
            print("")
            j = 0
            i += 1

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def to_dictionary(self):
        """
            Return the dictionary representation of the instance
            x, y, width, height and id

        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                "id": getattr(self, "id"), "width": getattr(self, "width"),
                "height": getattr(self, "height")}

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            if kwargs:
                try:
                    self.id = kwargs['id']
                except KeyError:
                    pass
                try:
                    self.__width = kwargs['width']
                except KeyError:
                    pass
                try:
                    self.__height = kwargs['height']
                except KeyError:
                    pass
                try:
                    self.__x = kwargs['x']
                except KeyError:
                    pass
                try:
                    self.__y = kwargs['y']
                except KeyError:
                    pass
