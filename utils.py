from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(db_name):
    if db_name:
        # connect to database
        engine = create_engine(f'sqlite:///{db_name}')
    else:
        engine = create_engine('sqlite:///:memory:')

    # create a session
    session = sessionmaker(bind=engine)
    return session()


