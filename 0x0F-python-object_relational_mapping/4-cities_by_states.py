#!/usr/bin/python3

"""
    Python script list all the cities
    from the db hbtn_0e_4_usa
"""

import MySQLdb
import sys


db = MySQLdb.connect(user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     port=3306,
                     host='localhost',
                     )

cur = db.cursor()

cur.execute("SELECT cities.id, cities.name, \
        states.name FROM cities\
        JOIN states ON cities.state_id=states.id")

res = cur.fetchall()

for i in res:
    print(i)
