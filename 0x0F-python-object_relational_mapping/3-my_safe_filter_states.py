#!/usr/bin/python3
""" script to display all values in the table of the db where name matches the args """
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
    search_pattern = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    obj.execute(query, (search_pattern,))
    rows = obj.fetchall()
    for row in rows:
        print(row)
    obj.close()
    connectdb.close()

