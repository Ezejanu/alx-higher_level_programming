#!/usr/bin/python3

import MySQLdb
import sys

username, password, database = sys.argv[1:4]
connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
cursor = connection.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
states = cursor.fetchall()
for state in states:
    print(state)

cursor.close()
connection.close()
