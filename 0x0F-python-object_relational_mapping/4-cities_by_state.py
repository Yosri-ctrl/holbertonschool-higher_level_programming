#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host='localhost',
                         port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
        FROM states
        INNER JOIN cities ON states.id = cities.state_id
        ORDER BY cities.id ASC""")
    allCities = cursor.fetchall()

    for city in allCities:
        print(city)

    cursor.close()
    db.close()
