#!/usr/bin/python3
""" Write a script that lists all states with a name starting with upper N """

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

    # Define the SQL query with a case-sensitive LIKE clause using BINARY
    sql_query = ("SELECT * FROM states WHERE BINARY name "
                 "LIKE 'N%' ORDER BY id ASC")
    cursor.execute(sql_query)
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    connection.close()
