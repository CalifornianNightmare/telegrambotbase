from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_DEFAULT

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)

class Database:
    def __init__(self, db_name=DATABASE_DEFAULT):
        self.engine = create_engine(db_name)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, user_id, username, first_name, last_name):
        session = self.Session()
        user = User(user_id=user_id, username=username, first_name=first_name, last_name=last_name)
        session.add(user)
        session.commit()
        session.close()
