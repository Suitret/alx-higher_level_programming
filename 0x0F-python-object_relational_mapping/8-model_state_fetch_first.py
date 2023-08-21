#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}\
                '.format(username, password, db_name), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        first_state = session.query(State).order_by(State.id).first()
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        session.close()

    except Exception as e:
        sys.exit(1)
