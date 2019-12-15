#!/usr/bin/python3
""" Module 12-model_state_update_id_2 """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine, MetaData, Table, select)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(session.query(
        State.id).order_by(State.id).filter_by(name='Louisiana').first()[0])
    session.close()
