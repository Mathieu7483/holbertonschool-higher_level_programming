#!/usr/bin/python3
"""Scirpt that lists all State objects from the database hbtn_0e_6_usa"""
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
    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()
    # Print each State object
    for state in states:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
