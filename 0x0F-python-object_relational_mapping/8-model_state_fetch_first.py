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

    first = session.query(State.id, State.name).first()
    if (first is None):
        print("Nothing")
    else:
        print("{}: {}".format(first[0], first[1]))
