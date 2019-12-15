#!/usr/bin/python3
""" Module 9-model_state_fetch_all """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine, MetaData, Table, select)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_q = session.query(
        State).filter(State.name.like('%a%')).order_by(State.id)
    for state in state_q:
        print("{}: {}".format(state.id, state.name))
    session.close()
