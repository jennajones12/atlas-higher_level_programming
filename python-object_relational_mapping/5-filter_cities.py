#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        sys.exit(1)
    
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()
    except MySQLdb.Error as e:
        print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    
    # Construct SQL query with parameterized query for state name
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    
    # Execute query with user input
    try:
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()
        print(", ".join(city[0] for city in results))
    except MySQLdb.Error as e:
        print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    
    # Close cursor and database connection
    cursor.close()
    db.close()

