#!/usr/bin/python3
"""
    a script that takes in an argument and
    displays all values matching the argument
"""

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
        sys.argv[4]: state name searched

    Returns:
        None
"""

if __name__ == "__main__":

    username, password, database, state_searched = sys.argv[1:5]
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = connection.cursor()
    sql_query = ("SELECT * FROM states "
                 "WHERE BINARY name = '{}'".format(state_searched))

    cursor.execute(sql_query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()
