#!/usr/bin/python3
"""
Module - "Rectangle" subclass
"""


from models.base import Base


class Rectangle(Base):
    """
    subclass - Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Arguments:
        public class attribute - width / int
        public class attribute - height / int
        public class attribute - x (axys coordinate) /int
        public class attribute - y (axys coordinate) /int
        public class attribute - id (axys coordinate) /int
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        encapsulate attribute width in getter for private use
        """
        return self.__width


    @property
    def height(self):
        """
        encapsulate attribute height in getter for private use
        """
        return self.__height

    @property
    def x(self):
        """
        encapsulate attribute x in getter for private use
        """
        return self.__x

    @property
    def y(self):
        """
        encapsulate attribute y in getter for private use
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        mutator of attribute width, allows to change the data
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @height.setter
    def height(self, value):
        """
        mutator of attribute height, allows to change the data
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        mutator of attribute x, allows to change the data
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        mutator of attribute y, allows to change the data
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public class method - area
        returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        public class method - display
        prints in stdout the Rectangle instance with the character #
        calculates coodinates where to print based on x & y
        """
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """
        override default private class method - __str__
        informal string representation of the rectangle subclass
        returns - [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)
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
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        public class method - to_dictionary
        returns the dictionary representation of a Rectangle
        """
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
