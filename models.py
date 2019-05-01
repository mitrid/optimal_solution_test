from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Table(Base):
    __tablename__ = 'table'

    pk = Column(Integer, primary_key=True)
    A = Column(String)
    B = Column(String)
    C = Column(String)
    D = Column(String)
    E = Column(String)
    F = Column(String)
    G = Column(String)
    H = Column(String)
    I = Column(String)
    J = Column(String)

    def __repr__(self):
        return f'{self.A} {self.B}'
