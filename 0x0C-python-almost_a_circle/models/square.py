#!/usr/bin/python3
"""
Module - "Square" subclass
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    subclass - Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Arguments:
        inherit from Rectangle public class attributes id, x & y
        public class attribute - size / int
        initializes the square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        encapsulate attribute size in getter for private use
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        mutator of attribute size, allows to change the data
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        override default private class method - __str__
        informal string representation of the Square subclass
        returns - [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """
        public class method - update
        assigns an argument to each attribute
        sets key/value argument to attributes to access by keywords
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        public class method - to_dictionary
        returns the dictionary representation of a Square
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
