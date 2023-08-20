#!/usr/bin/python3
"""script that takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    if len(sys.argv) != 5:
        sys.exit(1)
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (argv[4],))
        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        sys.exit(1)
