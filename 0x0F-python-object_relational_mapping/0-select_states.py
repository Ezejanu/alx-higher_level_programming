#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

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

if __name__ == "__main__":

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
    cursor.close()
    connection.close()
