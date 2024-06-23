#!/usr/bin/python3

"""
    python script takes the name
    of a state as an argument and list all cities of that state
    using the database

"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost',
                         )
    cur = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT cities.name FROM cities WHERE\
            state_id = (SELECT id FROM states WHERE name = %s)\
            ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()
    em = []

    for i in rows:
        for r in i:
            em.append(r)

print(*em, sep=', ')
