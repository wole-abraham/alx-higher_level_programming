#!/usr/bin/python3
"""Rectangle"""
from base import Base

class Rectangle(Base):
    """Rectangel class inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x    
    
    @x.getter
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value


    @property
    def y(self):
        return self.__y    
    
    @y.getter
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value
    


    @property
    def width(self):
        return self.__width    
    
    @width.getter
    def width(self):
        return self.__width
    @x.setter
    def width(self, value):
        self.__width = value

    
    @property
    def height(self):
        return self.__height    
    
    @height.getter
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value
    
r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
        
    