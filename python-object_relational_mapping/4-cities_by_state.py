#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
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
    # Execute the SQL query to fetch all cities with their state names
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    # Fetch all results
    query_rows = cursor.fetchall()
    # Print each row (city)
    for row in query_rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
