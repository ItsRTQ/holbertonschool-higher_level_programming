#!/usr/bin/python3
"""This script prints all City objects from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, database):
    """This function prints all City objects from the database"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        cities = session.query(
            City, State).filter(
                City.state_id == State.id).order_by(City.id).all()
        for city, state in cities:
            print(f"{state.name}: ({city.id}) {city.name}")
    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    fetch_cities_by_state(username, password, database)
