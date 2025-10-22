#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
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
    # Execute the SQL query to fetch cities of the specified state
    cursor.execute( 
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )       
    # Fetch all results
    query_rows = cursor.fetchall()
    # Print each row (city)
    for row in query_rows:
        print(", ".join(row))
    # Close the cursor and database connection
    cursor.close()
    db.close()
