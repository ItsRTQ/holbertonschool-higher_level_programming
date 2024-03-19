#!/usr/bin/python3
"""This script lists all State objects that contain the letter a"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def states_with_a(username, password, database):
    """This function lists all State objects containing the letter 'a'"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    states_with_a(username, password, database)
