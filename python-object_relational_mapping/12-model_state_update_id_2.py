#!/usr/bin/python3
"""script that changes the name of a
State object from the database hbtn_0e_6_usa"""
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
    # Query the State object with id = 2
    state = session.query(State).get(2)
    # Change the name of the State object to "New Mexico"
    if state:
        state.name = "New Mexico"
        # Commit the session to save the changes to the database
        session.commit()
    # Close the session
    session.close()
