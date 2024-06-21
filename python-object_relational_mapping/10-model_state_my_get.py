#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_states(username, password, db_name, search):
    """
    Prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
    """

    # Create an engine and connect to the MySQL server
    connection = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(connection.format(username, password, db_name))


    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database for the state with the given name
    state = session.query(State).\
    filter(State.name == search).first()

    # Print the result
    if states:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()


    if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    search = sys.argv[4]
    print_states(username, password, db_name, search)
