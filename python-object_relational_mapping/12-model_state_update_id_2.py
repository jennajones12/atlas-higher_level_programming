#!/usr/bin/python3
"""
A script that changes the name of a State object in the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get the MySQL username, password, and database name from the command-line arguments
    username = argv[1]
    password = argv[2]
    dbname = argv[3]

    # Create the database engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Check if the state exists, then update the name
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
