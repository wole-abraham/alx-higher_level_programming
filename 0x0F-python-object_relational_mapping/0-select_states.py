#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv[1:]
    host = "localhost"
    user = args[0]
    passwd = args[1]
    dbname = args[2]
    port = 3306
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname,
                         port=port)
    cur = db.cursor()
    cur.execute(f"SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
