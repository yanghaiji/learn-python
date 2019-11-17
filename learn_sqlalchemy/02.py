# coding:utf-8
"""
session操作
"""
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@localhost/learn_sqlalchemy?")


# 用户表模型
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(64))

    def __init__(self, name, email):
        self.name = name
        self.email = email


# 创建表，如果表存在则忽视
Base.metadata.create_all(engine)

# 创建session
DbSession = sessionmaker(bind=engine)
session = scoped_session(DbSession)

# 线程安全


@contextmanager
def session_maker(session=session):
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def update_user():
    with session_maker() as db_session:
        db_session.query(Users).filter_by(name='test2').update({'email': 'test2@qq.com'})


if __name__ == '__main__':
    update_user()
