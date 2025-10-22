#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py username password database_name
"""
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
    cur = db.cursor()
    # Execute the SQL query to fetch all states ordered by id
    query_rows = cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all results
    # query_rows = cur.fetchall()
    # Print each row (state)
    for row in query_rows:
        print(row)
    # Close the cursor and database connection
    cur.close()
    db.close()
