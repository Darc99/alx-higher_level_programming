#!/usr/bin/python3
"""
This contains the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Init the rectangle
        Attributes:
          width, height, x, y, id        
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """Getters and Setters"""
    @property
    def width(self):
      """width getter"""
      return self.__width

    @width.setter
    def width(self, value):
      """width setter"""
      if type(value) is not int:
        raise TypeError("width must be an integer")
      if value <= 0:
        raise ValueError("width must be > 0")
      self.__width = value

    @property
    def height(self):
      """height getter"""
      return self.__height
    
    @height.setter
    def height(self, value):
      """height setter"""
      if type(value) is not int:
        raise TypeError("height must be an integer")
      if value <= 0:
        raise ValueError("height must be > 0")
      self.__height = value

    @property
    def x(self):
      """x getter"""
      return self.__x
    
    @x.setter
    def x(self, value):
      """x setter"""
      if type(value) is not int:
        raise TypeError("x must be an integer")
      if value < 0:
        raise ValueError("x must be >= 0")
      self.__x = value

    @property
    def y(self):
      """y getter"""
      return self.__y

    @y.setter
    def y(self, value):
      """y setter"""
      if type(value) is not int:
        raise TypeError("y must be an integer")
      if value < 0:
        raise ValueError("y must be >= 0")
      self.__y = value

    def area(self):
      """calculates the area of the rectangle"""
      return self.__width * self.__height

    def display(self):
      """prints the rectangle instance"""
      print(("\n" * self.__y) +
      "\n".join(((" " * self.__x) + ("#" * self.__width))
                for i in range(self.__height)))

    def __str__(self):
      """representation of the rectangle in string format"""
      return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
      """assigns an argument to each attribute"""
      attr_args = ["id", "width", "height", "x", "y"]
      i = 0
      length = len(args)
      if length > 0:
        for arg in range(length):
          setattr(self, attr_args[i], args[i])
          i += 1
      else:
        for key, value in kwargs.items():
          setattr(self, key, value)
