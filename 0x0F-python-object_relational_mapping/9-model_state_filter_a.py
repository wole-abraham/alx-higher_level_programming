#!/usr/bin/python3

"""
    pyhton script that print
    the query values:

"""

if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:\
{password}@localhost:3306/{db_name}')

    Session = sessionmaker(bind=engine)
    session = Session()

    i = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc())
    for inn in i:
        if inn:
            print(f'{inn.id}: {inn.name}')
        else:
            print("Nothing")
