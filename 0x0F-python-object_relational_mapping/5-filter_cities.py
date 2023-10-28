#!/usr/bin/python3
"""
    Write a script that takes in the name of a state as an argument
    and lists all cities of that state, using the database
"""

import sys
import MySQLdb

"""
    Connects to a MySQL database using provided credentials and retrieves
    and prints all rows from the 'states' table in ascending order of 'id'

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
    sql_query = """
        SELECT cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    params = (state_searched, )

    cursor.execute(sql_query, params)
    cities = cursor.fetchall()
    city_list = ", ".join(city[0] for city in cities)
    print(city_list)

    cursor.close()
    connection.close()
