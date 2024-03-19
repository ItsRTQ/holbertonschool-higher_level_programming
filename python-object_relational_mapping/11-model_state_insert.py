#!/usr/bin/python3
"""This script adds the State object Louisiana"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add(username, password, database):
    """This function adds the State object "Louisiana" to the database"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="Louisiana")
        session.add(new_state)
        session.commit()
        print(new_state.id)
    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    add(username, password, database)
