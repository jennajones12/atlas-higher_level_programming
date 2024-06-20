#!/usr/bin/python3
"""
Module containing the definition of the State class.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    """
    State class that inherits from Base.
    Links to the MySQL table 'states'.
    
    Attributes:
        id (int): Auto-generated, unique integer, can't be null, primary key.
        name (str): String with maximum 128 characters, can't be null.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
