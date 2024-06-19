#!/usr/bin/python3
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
    
    # Construct SQL query
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute query with user input
    try:
        cursor.execute(query, ('%' + state_name + '%',))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("MySQLdb Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
    
    # Close cursor and database connection
    cursor.close()
    db.close()