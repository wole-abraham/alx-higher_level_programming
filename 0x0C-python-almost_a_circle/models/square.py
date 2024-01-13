#!/usr/bin/python3
"""Square subclass of traingle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """initialize parent clas attrb an"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, width=size, height=size)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
