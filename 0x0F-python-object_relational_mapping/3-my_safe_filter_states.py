#!/usr/bin/python3

""" Python script to execute query the query below """

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306,
                         )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY id ASC", {'name': argv[4]})

    res = cur.fetchall()

    for ress in res:
        print(ress)
