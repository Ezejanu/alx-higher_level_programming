#!/usr/bin/python3

import MySQLdb
import sys

def main():
    """
    Connects to a MySQL database using provided credentials and retrieves
    and prints all rows from the 'states' table in ascending order of 'id'.

    Usage: python script_name.py <username> <password> <database_name>

    Args:
        sys.argv[1]: MySQL username
        sys.argv[2]: MySQL password
        sys.argv[3]: MySQL database name

    Returns:
        None
    """
    try:
        username, password, database = sys.argv[1:4]
        connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
