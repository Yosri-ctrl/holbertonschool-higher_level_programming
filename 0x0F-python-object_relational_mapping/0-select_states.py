#!/usr/bin/python3
# script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()
    database = MySQLdb.Connect(
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
