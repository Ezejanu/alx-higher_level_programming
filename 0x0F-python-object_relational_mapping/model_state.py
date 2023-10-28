#!/usr/bin/python3
"""
    a python file that contains the class definition of a State and an instance
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class State(Base):
    """ links to the MySQL table states """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
