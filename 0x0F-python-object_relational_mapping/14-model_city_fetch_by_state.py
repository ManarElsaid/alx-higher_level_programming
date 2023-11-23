#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    url = 'mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State)\
        .join(State).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
