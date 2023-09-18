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

    def __str__(self):
        """srt method that returns the square data"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """return the square size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets the square size"""
        self.width = value
        self.height = value
