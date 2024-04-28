#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv[1:]
    host = "localhost@3306"
    user = args[0]
    passwd = args[1]
    dbname = args[2]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname)
    cur = db.cursor()
    cur.execute(f"SELECT id, name FROM states ORDER BY id DESC")
