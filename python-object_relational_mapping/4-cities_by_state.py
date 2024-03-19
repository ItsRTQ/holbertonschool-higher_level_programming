#!/usr/bin/python3
"""This script will display all cities in acending order"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class City(Base):
    """This call will representent each row of the table citie"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state = Column(String(128))


def cities_display(username, password, database):
    """This function will list the cities in acending order"""
    try:
        engine = create_engine(
            f"mysql://{username}:{password}@localhost:3306/{database}")
        Session = sessionmaker(bind=engine)
        session = Session()
        cities = session.query(City).order_by(City.id).all()
        for city in cities:
            print("({}, '{}', '{}')".format(city.id, city.name, city.state))

    except Exception as e:
        print("Error:", e)
    finally:
        if session:
            session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    cities_display(username, password, database)
