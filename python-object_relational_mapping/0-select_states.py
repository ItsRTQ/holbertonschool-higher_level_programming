#!/usr/bin/python3
"""This module list all states from database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database):
    """This function connects to database to list data
        ARGS:
            username: user
            password: passcode
            database: targeted database
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(0)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
