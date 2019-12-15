#!/usr/bin/python3
""" Module 10-model_state_my_get """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine, MetaData, Table, select)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(
        State.id).order_by(State.id).filter(State.name == str(argv[4])).all()
    if state:
        print(state[0][0])
    else:
        print("Not found")
    session.close()
