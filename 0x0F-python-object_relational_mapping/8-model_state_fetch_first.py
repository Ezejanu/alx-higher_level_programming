#!/usr/bin/python3
"""
    a script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1:4]

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
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print ("Nothing")

    session.close()
