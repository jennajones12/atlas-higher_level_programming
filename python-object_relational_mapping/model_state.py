#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base():
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL
    connection = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conection.format(username, password, db_name))
    Base.metadata.create_all(engine)
