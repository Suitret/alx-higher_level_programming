#!/usr/bin/python3
"""script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument.
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
    query = "SELECT * FROM states WHERE name='%s' ORDER BY id ASC;"
    cursor.execute(query, (argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    mydb.close()
