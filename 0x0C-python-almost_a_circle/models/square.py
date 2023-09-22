#!/usr/bin/python3
"""defines the class square inherits
from rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represents subclass square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialization the square
        Args:
            size: the size of the square"""

        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """return the square size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets the square size"""
        self.width = value
        self.height = value

    def __str__(self):
        """srt method that returns the square data"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """a method that assigns attributes"""
        attr = ["id", "size", "x", "y"]

        if (args):
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)

        else:
            for key, value in kwargs.items():
                if (key == "height" or key == "width"):
                    key = "size"
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        s_dic = {'id': self.id,
                 'x': self.x,
                 'size': self.width,
                 'y': self.y}
        return s_dic
