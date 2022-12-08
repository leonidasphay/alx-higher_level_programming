#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, passwd, db, argument = argv[1:]

    db_setting = {
            'host': 'localhost',
            'port': 3306,
            'user': user,
            'passwd': passwd,
            'db': db,
            'charset': "utf8"
            }

    conn = MySQLdb.connect(**db_setting)
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"\
            .format(argument)

    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
