import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,create_engine,INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    idUser = Column(INT,primary_key=True)
    email = Column(String(45))
    sex = Column(INT)
    username = Column(String(45))
    password = Column(String(45))

engine = create_engine('mysql+pymysql://root:Zhaoyun0218@localhost:3306/world')
DBSession = sessionmaker(bind=engine)


session = DBSession()
user1 = User(idUser='10000001',email='277168645@qq.com',sex='1',username='zhaoting',password='123456')
session.add(user1)
session.commit()
session.close()
