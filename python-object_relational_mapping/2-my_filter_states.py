#!/usr/bin/python3
"""This script will take in an argument and display all value in state"""
import MySQLdb
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, MetaData
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
    connection = engine.connect()
    metadata = MetaData()
    states = Table('states', metadata, autoload=True, autoload_with=engine)
    query = states.select().where(
        states.columns.name == target).order_by(states.columns.id)
    result = connection.execute(query)
    for row in result:
        print(row)
    connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, target = sys.argv[1:]
    display(username, password, database, target)
