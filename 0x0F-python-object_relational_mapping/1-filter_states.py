#!/usr/bin/python3
""" script that lists all staets with a name starting with upper N """
import MySQLdb
import sys


if __name__ == "__main__":
    connectdb = MySQLdb.connect("localhost", user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3], port=3306)
    obj = connectdb.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER by id ASC"
    obj.execute(query)
    rows = obj.fetchall()
    for row in rows:
        print(row)
    obj.close
    connectdb.close
