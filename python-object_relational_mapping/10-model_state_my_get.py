#!/usr/bin/python3
"""Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the State object with the name passed as argument
    state = (session.query(State)
             .filter(State.name == sys.argv[4])
             .first()
             )
    # Print the State object or "Not found" if it doesn't exist
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    # Close the session
    session.close()
