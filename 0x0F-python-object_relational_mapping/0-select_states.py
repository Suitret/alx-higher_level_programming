#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb as mysql
import sys

args = sys.argv[1:]

if __name__ == "__main__":
    mydb = mysql.connect(
        host="localhost",
        user=args[0],
        passwd=args[1],
        db=args[2],
        port="3306"
    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    mydb.close()
