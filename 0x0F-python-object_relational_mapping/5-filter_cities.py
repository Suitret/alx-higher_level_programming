#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
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
    query = "SELECT cities.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id;"
    cursor.execute(query, (argv[4],))
    query_rows = cursor.fetchall()
    cities = ', '.join(row[0] for row in query_rows)
    print(cities)
    cursor.close()
    mydb.close()
