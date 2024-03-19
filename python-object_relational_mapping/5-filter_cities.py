#!/usr/bin/python3
"""This module prints cities of a given state"""
import sys
import MySQLdb


def display_cities(username, password, database, state_name):
    """This function lists all cities of a given state"""

    try:
        mysql_conn = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=database)
        cursor = mysql_conn.cursor()
        cursor.execute("SELECT cities.name FROM cities \
                        INNER JOIN states ON cities.state_id = states.id \
                        WHERE states.name = %s\
                        ORDER BY cities.id ASC", (state_name,))
        cities = cursor.fetchall()
        cities_str = ', '.join(city[0] for city in cities)
        print(cities_str)
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
    display_cities(username, password, database, state_name)
