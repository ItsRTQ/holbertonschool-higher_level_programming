#!/usr/bin/python3
"""This script prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def find_state(username, password, database, state_name):
    """This function prints the State object with the given name"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == state_name).first()
        if state:
            print(state.id)
        else:
            print("Not found")
    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    find_state(username, password, database, state_name)
