#!/usr/bin/python3
"""Square subclass of traingle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """initialize parent clas attrb an"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
         return the size of the square

        """
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """updates the instance"""

        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

            except IndexError:
                pass
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Return the dictionary representation of the instance
            x, y, width, height and id

        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                "id": getattr(self, "id"), "size": getattr(self, "size")}
