#!/usr/bin/python3
"""
    a script that that lists all cities from the database hbtn_0e_4_usa
    using only execute() once.
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
    sql_query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY id ASC
    """

    cursor.execute(sql_query)
    cities = cursor.fetchall()
    for city in cities:
        print(city)
    cursor.close()
    connection.close()
