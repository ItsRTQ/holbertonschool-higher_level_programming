#!/usr/bin/python3
"""This script will display all cities in acending order"""
import sys
import MySQLdb
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
        mysql_conn = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)
        cursor = mysql_conn.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
                       FROM cities INNER JOIN states \
                       ON cities.state_id = states.id ORDER BY cities.id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if cursor:
            cursor.close()
        if mysql_conn:
            mysql_conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, database = sys.argv[1:]
    cities_display(username, password, database)
