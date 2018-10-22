from sqlalchemy import Table, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from grocerapp import Config

Base = declarative_base()

class Grocery(Base):
    __tablename__= 'groceries'
    id = Column(Integer, primary_key=True)
    keyword = Column(String(64), index=True, unique=True)
    name = Column(String(120), index=True, unique=True)
    price = Column(Float())

    def __repr__(self):
        return self.keyword


class DB:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine


    def add_kw(self, kw):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        new_item = Grocery(keyword=kw)
        session.add(new_item)
        session.commit()

    def query(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        return session.query(Grocery).all()