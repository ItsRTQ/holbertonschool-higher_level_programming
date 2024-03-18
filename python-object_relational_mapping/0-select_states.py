
import MySQLdb
import sys
"""This script list all states from database hbtn_0e_0_usa"""


def list_states(username, password, database):
    """This function connects to database to list data
        ARGS:
            username: user
            password: passcode
            database: targeted database
    """
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("Error connecting to the MySQL server:", e)
        sys.exit(1)

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
    except MySQLdb.Error as e:
        print("Error fetching states:", e)
        db.close()
        sys.exit(1)

    print("States:")
    for state in states:
        print(state)

    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(0)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
