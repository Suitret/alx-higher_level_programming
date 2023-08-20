#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)
   from the database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    mydb = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cursor = mydb.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    mydb.close()
