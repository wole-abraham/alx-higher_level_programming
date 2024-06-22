#!/usr/bin/env python3

""" Python script to execute query """

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     host='localhost',
                     )

cur = db.cursor()

cur.execute("SELECT * from states ORDER BY id ASC")

res = cur.fetchall()

for ress in res:
    print(ress)
