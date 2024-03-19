#!/usr/bin/python3
"""This script will take in an argument and display all values in state"""
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


Base = declarative_base()


class State(Base):
    """This class is going to represent each row from the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))


def display(username, password, database, target):
    """This function will do the search to find the states"""
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(
        State.name.like(target)).order_by(State.id)
    for state in query.all():
        print((state.id, state.name))


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, target = sys.argv[1:]

    display(username, password, database, f"%{target}%")
