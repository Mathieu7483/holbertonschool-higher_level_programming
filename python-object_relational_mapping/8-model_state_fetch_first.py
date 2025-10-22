#!/usr/bin/python3
"""Scirpt that prints the first State object from the database hbtn_0e_6_usa"""
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
    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()
    # Print the State object or 'Nothing' if none found
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    # Close the session
    session.close()
