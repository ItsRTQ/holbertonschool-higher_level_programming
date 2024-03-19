#!/usr/bin/python3
"""This module print cities and state"""
import sys
import MySQLdb


def list_cities(username, password, database, state_name):
    """This call will representent each row of the table citie"""

    try:
        mysql_conn = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)

        cursor = mysql_conn.cursor()
        cursor.execute("SELECT cities.id, cities.name FROM cities \
                        INNER JOIN states ON cities.state_id = states.id \
                        WHERE states.name = %s \
                        ORDER BY cities.id ASC", (state_name,))
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
    if len(sys.argv) != 5:
        sys.exit(1)
    username, password, database, state_name = sys.argv[1:]
    list_cities(username, password, database, state_name)
