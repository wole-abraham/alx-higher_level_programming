#!/usr/bin/python3

"""
    python script that print the states
    of the object
    the database in the system
"""
if __name__ == "__main__":

    from sys import argv
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    engine = create_engine(f'mysql+mysqldb://{username}:\
{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    i = session.query(State).filter_by(name=state_name).first()
    if i:
        print(i.id)
    else:
        print("Not found")
