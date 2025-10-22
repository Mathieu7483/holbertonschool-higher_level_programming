#!/usr/bin/python3
"""Script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
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
    # Execute the SQL query to fetch states matching the argument safely
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s", (sys.argv[4],))
    # Fetch all results
    query_rows = cursor.fetchall()
    # Print each row (state)
    for row in query_rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
