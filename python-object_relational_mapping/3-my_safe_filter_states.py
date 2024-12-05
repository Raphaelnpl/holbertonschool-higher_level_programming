#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument, safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()
    # Execute the SQL query with parameterized input to prevent SQL injection
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))

    # Fetch and display the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
