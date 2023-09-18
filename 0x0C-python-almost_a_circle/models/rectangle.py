#!/usr/bin/python3
"""defines the class rectangle inherits
from Base class"""
from models.base import Base


class Rectangle(Base):
    """represents subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the rectangle
        Args:
            width: the width of the rectangle
            height: the rectangle height
        Raises:
            TypeError: if width or height not integer
            ValueError: if width or height <= 0"""
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")

        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")

        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)
    
    @property
    def width(self):
        """get rectangle width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """set rectangle width"""
        if (not isinstance(width, int)):
            raise TypeError("width must be an integer")
        elif (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get rectangle height"""
        return (self.__height)
    @height.setter
    def height(self, height):
        """set rectangle height"""
        if (not isinstance(height, int)):
            raise TypeError("height must be an integer")
        elif (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x value"""
        return (self.__x)
    @x.setter
    def x(self, x):
        """set x value"""
        if (not isinstance(x, int)):
            raise TypeError("x must be an integer")
        elif (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y value"""
        return (self.__y)
    @y.setter
    def y(self, y):
        """set y value"""
        if (not isinstance(y, int)):
            raise TypeError("y must be an integer")
        elif (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """returns the area value of the Rectangle instance"""
        return (self.__width * self.__height)


    def __str__(self):
        """__str__ method so that it returns rectangle data"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def display(self):
        """prints in stdout the Rectangle
        instance with the character # with taking care of position"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def update(self, *args):
        """a method that assigns an argument to each attribute"""
        attr = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
           setattr(self, attr[i], arg)
