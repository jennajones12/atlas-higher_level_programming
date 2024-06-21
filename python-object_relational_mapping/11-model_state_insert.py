#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, db_name):
    """
    Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
    
    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.
    """
    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")
    
    # Add the new State object to the session
    session.add(new_state)
    
    # Commit the transaction
    session.commit()
    
    # Print the id of the new State
    print(new_state.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        add_state(username, password, db_name)
