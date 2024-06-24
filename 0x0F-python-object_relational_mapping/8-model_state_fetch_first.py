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

    for i in session.query(State).filter_by(id=1):
        if i:
            print(f'{i.id}: {i.name}')
        else:
            print("Nothing")
