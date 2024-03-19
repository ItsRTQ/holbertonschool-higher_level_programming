#!/usr/bin/python3
"""This script deletes all State objects that containing the letter 'a'"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, database):
    """This function deletes all State objects with the targeted name"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        states_to_delete = session.query(
            State).filter(State.name.like('%a%')).all()
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)
            session.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    delete_states_with_a(username, password, database)
