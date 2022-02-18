#coding:utf-8

"""
desc:sqlalchemy使用总结
author: ben
time: 2018-05-11
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_, and_
from sqlalchemy import ForeignKey

# 创建一个SQLORM基类，之后创建的表必须得继承它
Modelbase = declarative_base()

# 连接数据库，使用session用于创建程序和数据库之间的会话
# echo=True 在控制台打印执行的sql
ENGINE = create_engine("mysql+mysqlconnector://root:272825@localhost:3306/testsqlalchemy",echo=True)
# sqlite 数据库
# ENGINE = create_engine('sqlite:///cookies.db', echo=True)

#创建Session对象
Session = sessionmaker(bind=ENGINE)

session = Session()

# 创建Users表
class Users(Modelbase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)
    age = Column(Integer)
    city_id = Column(Integer, ForeignKey("city.id"))
    def __init__(self, name, age):
        self.name = name
        self.age = age

#创建city表
class City(Modelbase):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    city = Column(String(30), unique=True)

#初始化数据库
def init_db():
    Modelbase.metadata.create_all(ENGINE)

def drop_db():
    Modelbase.metadata.drop_all(ENGINE)

#创建新的User对象
def insert_users():
    names = {'Jeny':22, 'Lisa':18, "Mark":19}
    for key, value in names.items():
        new_user = Users(key, value)
        new_user.city_id = 1
        session.add(new_user)
    session.commit()
    session.close()

def insert_city():
    city = City(city="Xian")
    session.add(city)
    session.commit()
    session.close()
# 简单查询
def easy_query():
    users = session.query(Users.name).all()
    for item in users:
        print(f'{item}')


# 查询所有
def query_all():
    users = session.query(Users).all()
    for item in users:
        print(f'id = {item.id},name = {item.name} , age = {item.age}')


# 条件查询1
def where_query():
    # users = session.query(Users).filter(Users.age==18).all()
    users = session.query(Users).filter_by(age=18).limit(1).all()
    for item in users:
        print(f'{item.name}')


# 模糊匹配like
def use_like_query():
    # users = session.query(Users).filter(Users.name.like('M%')).all()
    # users = session.query(Users).filter(Users.name.like('%M%')).filter(Users.name.like('%K%'))
    # users = session.query(Users).filter((Users.name.in_(['Mary','Jeny'])))
    users = session.query(Users).filter(or_(Users.name == 'Mark', Users.age == 19)).all()
    # print(session.query(User).filter(User.username.is_(None)).all())
    # print(session.query(User).filter(User.username.isnot(None)).all())
    for item in users:
        print(f'{item.name}')


# 聚合查询
def user_agg():
    from sqlalchemy import func
    users = session.query(Users.name, func.sum(Users.id)).group_by(Users.city_id).all()
    # for item in users:
    #     print(f'{item.name}')


# update
def update():
    user = session.query(Users).filter(Users.id == 1).update({Users.name, "ben"})
    session.add(user)
    session.commit()
    session.close()


"""
执行步骤:
1. init_db
2. insert_city
3. insert_users
4. 执行其他查询或更新操作
"""
if __name__ == "__main__":
    # drop_db()
    # init_db()
    # insert_city()
    # insert_users()
    # update()
    # 简单查询
    # easy_query()

    # 条件查询
    # where_query()
    # 查询所有
    # query_all()
    # 使用like
    # use_like_query()
    pass
