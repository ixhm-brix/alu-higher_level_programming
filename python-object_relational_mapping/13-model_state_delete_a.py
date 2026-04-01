#!/usr/bin/python3
"""Script that deletes all State objects with a name containing letter a."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    to_delete = [s for s in session.query(State).all() if 'a' in s.name]
    for state in to_delete:
        session.delete(state)
    session.commit()
    session.close()
