#!/usr/bin/python3
""" query to list out all states from hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    connectdb = MySQLdb.connect("localhost", user=sys.argv[1], password=sys.argv[2], database=sys.argv[3])
    obj = connectdb.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    obj.execute(query)
    entities = obj.fetchall()
    for row in entities:
        print(row)

    obj.close()
    connectdb.close()
