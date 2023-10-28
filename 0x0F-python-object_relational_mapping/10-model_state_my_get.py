#!/usr/bin/python3
"""
    a script that lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database, state_searched = sys.argv[1:5]

    # Connect to the MySQL server using SQLAlchemy
    engine = create_engine(f"mysql://{username}:\
            {password}@localhost:3306/{database}")
    # Bind the engine to the base class
    Base.metadata.bind = engine

    # Create a session factory
    DBSession = sessionmaker(bind=engine)

    # Create a session factory
    session = DBSession()

    # Query
    state = session.query(State).filter(State.name == state_searched).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
