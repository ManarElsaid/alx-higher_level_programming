#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(url, pool_pre_ping=True)
if __name__ = "__main__":
    Session = sessionmaker(bend=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name)
