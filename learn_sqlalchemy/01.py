# coding:utf-8
"""
sqlalchemy基本用法
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
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
session = DbSession()

# 添加
add_user = Users("test", "test123@qq.com")
session.add(add_user)
session.commit()
print("-" * 5 + "Add: test" + "-" * 5 + "\n")

# 更新1
session.query(Users).filter_by(id=1).update({'name': "Jack"})
session.commit()

update_user = session.query(Users.name).filter(Users.name == "test").first()
print("-" * 5 + "Update1: update test to %s" % update_user.name)

# 更新2
update_users = session.query(Users).filter_by(name="Jack").all()
for user in update_users:
    user.name = "test"
    session.add(user)
session.commit()

users = session.query(Users).filter_by(name="test").all()
if users:
    for user in users:
        print("-" * 5 + "Update2: update test to %s" % update_user.name)

# 删除1
delete_users = session.query(Users).filter(Users.name == "test").first()
if delete_users:
    session.delete(delete_users)
    session.commit()
    print("-" * 5 + "Delete1: test")

# 删除2
add_user = Users("test2", "test1234@qq.com")
session.add(add_user)
session.commit()
print("-" * 5 + "Add: test2" + "-" * 5)

session.query(Users).filter(Users.name == "test2").delete()
session.commit()
print("-" * 5 + "Delete1: test")
