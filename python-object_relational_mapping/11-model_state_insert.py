#!/usr/bin/python3
"""Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
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
    # Create a new State object with the name "Louisiana"
    new_state = State(name="Louisiana")
    # Add the new State object to the session
    session.add(new_state)
    # Commit the session to save the new State to the database
    session.commit()
    # Print the id of the new State object
    print("{}".format(new_state.id))
    # Close the session
    session.close()
