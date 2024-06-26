#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    search = sys.argv[4]
    sql = "SELECT `cities`.`name` "
    sql += "FROM `states` "
    sql += "INNER JOIN `cities` "
    sql += "ON `cities`.`state_id` = `states`.`id` "
    sql += "WHERE `states`.`name` = %s "
    sql += "ORDER BY `cities`.`id`;"

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute(sql, (search,))

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    first = True
    for row in results:
        if first:
            print(row[0], end="")
            first = False
        else:
            print(', ' + row[0], end="")
    print()

    # Close cursor and database connection
    cursor.close()
    db.close()
