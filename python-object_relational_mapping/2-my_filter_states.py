#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(
        port=3306,
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query to fetch states matching the argument
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = '{}'".format(sys.argv[4]))
    # Fetch all results
    query_rows = cursor.fetchall()
    # Print each row (state)
    for row in query_rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
