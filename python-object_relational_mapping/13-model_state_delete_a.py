#!/usr/bin/python3
"""Script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa"""
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
    # Query all State objects that contain the letter 'a'
    states_to_delete = (session.query(State)
                        .filter(State.name.like('%a%'))
                        .all()
                        )
    # Delete each State object found
    for state in states_to_delete:
        session.delete(state)
    # Commit the session to save the changes to the database
    session.commit()
    # Close the session
    session.close()
