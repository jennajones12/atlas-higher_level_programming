#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # search = sys.argv[4]
    sql = "SELECT `cities`.`id`, `cities`.`name`, `states`.`name` "
    sql += "FROM `states` INNER JOIN `cities` "
    sql += "ON `cities`.`state_id` = `states`.`id` "
    sql += "ORDER BY `cities`.`id`"

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute(sql)

    # Fetch all results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
