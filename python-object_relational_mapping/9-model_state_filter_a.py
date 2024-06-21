#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, db_name):
    # Create a database connection
    connection = "mysql://{}:{}@localhost:3306/{}"
    

    # Create an engine and connect to the MySQL server
    engine = create_engine(connection.format(username, password, db_name))
    Base.metadata.create_all(engine)


    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database for states containing 'a'
    states = session.query(State).order_by(State.id).\
            filter(State.name.like('%a%')).all()


    # Print the results
     for state in states_with_a:
         print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, db_name)
