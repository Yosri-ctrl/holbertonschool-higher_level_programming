#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter(State.name == argv[4])

    if (state_id.first() is None):
        print("Not found")
    else:
        print(state_id[0][0])
