#!/usr/bin/python3

"""
    CONNECTING TO THE DB using sqlalchemy

"""

from sqlalchemy import Column, Integer, String
from sqlchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
        state class:

        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The state id of the class
            name (str): The State name of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
