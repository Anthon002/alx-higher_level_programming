#!/usr/bin/python3
""" script to display all values from a join between cities and states """
import MySQLdb
import sys

if __name__ == "__main__":
    connectdb = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )
    obj = connectdb.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM
               cities INNER JOIN states ON states.id=cities.state_id"""
    obj.execute(query)
    rows = obj.fetchall()
    for row in rows:
        print(row)
    obj.close()
    connectdb.close()

