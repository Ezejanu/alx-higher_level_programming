#!/usr/bin/python3
"""
 a script that deletes all State objects with a name
 containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == " __main__":

    username, password, database = sys.argv[1:4]
    # Create an engine to connect to the database
    engine = create_engine(f'mysql://{username}:\
            {password}@localhost:3306/{database}')

    # Bind the engine to the Base class
    Base.metadata.bind = engine

    # Create a session factory
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Delete states whose name contain the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
