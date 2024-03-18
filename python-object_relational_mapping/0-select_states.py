#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
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


def list_states(username, password, database):
    """Function to list all states from the database"""

    try:
        mysql_conn = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)
        cursor = mysql_conn.cursor()
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(state.name)

    except Exception as e:
        print("Error:", e)
    finally:
        if mysql_conn:
            mysql_conn.close()
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    list_states(username, password, database)
