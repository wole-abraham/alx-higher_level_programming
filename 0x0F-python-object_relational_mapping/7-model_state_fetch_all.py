#!/usr/bin/python3

"""
   script list all State Object from  the database

"""


def list_objects():

    """

        list objects in the database table

    """

    from sys import argv
    import sqlalchemy
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

    for data in session.query(State).order_by(State.id):
        print(f"{data.id}: {data.name}")


if __name__ == "__main__":
    list_objects()
