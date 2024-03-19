#!/usr/bin/python3
"""This script will take in an argument and display all value in state"""
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

    try:
        mysql_conn = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        query = "SELECT * FROM states WHERE name = '{}'".format(target)
        states = session.execute(query)
        for state in states:
            print((state.id, state.name))

    except Exception as e:
        print("Error:", e)
    finally:
        if mysql_conn:
            mysql_conn.close()
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, target = sys.argv[1:]
    display(username, password, database, target)
