#!/usr/bin/python3
""" script to display city names in a specific state from the database """
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
    query = """SELECT cities.name FROM
               cities INNER JOIN states ON states.id=cities.state_id
               WHERE states.name=%s"""
    state_name = sys.argv[4]
    obj.execute(query, (state_name,))
    rows = obj.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    obj.close()
    connectdb.close()

