#!/usr/bin/python3

""" python script dislays all values in the states table """

if __name__ == "__main__":

    import sys
    import MySQLdb

    arg = sys.argv[1:]
    host = 'localhost'
    user = arg[0]
    passwd = arg[1]
    db = arg[2]
    name = arg[3]
    port = 3306

    db = MySQLdb.connect(host=host, user=user,
                         passwd=passwd, db=db,
                         port=port)
    cur = db.cursor()
    query = f"SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(name)
    cur.execute(query)

    states = cur.fetchall()

    for state in states:
        print(state)
