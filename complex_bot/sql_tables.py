import sqlalchemy
from sqlalchemy import Column, String, Integer, Date, create_engine, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

DIALCT = "mysql"  # 数据库类型

DRIVER = "pymysql"  # 数据库驱动

USERNAME = "root"  # 数据库用户名

PASSWORD = ""  # 数据库密码

HOST = "127.0.0.1"  # 服务器IP地址

PORT = "3306"  # 端口号，默认3306

DATABASE = "botsql"  # 数据库名

DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    user_id = Column(String(15), primary_key=True)
    name = Column(String(30))
    sex = Column(Enum("male", "female"))
    age = Column(Integer)
    credit_all = Column(Integer)


class Credit(Base):
    # 表的名字
    __tablename__ = 'credit'

    user_id = Column(String(10), primary_key=True)
    credit_type = Column(String(20), primary_key=True)
    credit = Column(Integer)
    time = Column(Date)


# class Punching_card(Base):
#     # 表的名字
#     __tablename__ = 'punching_card'
#
#     credit_id = Column(String(10), primary_key=True)
#     credit_type = Column(String(20))


def add_uesr(u_id, u_name, u_sex, u_age):
    user = User(user_id=u_id, name=u_name, sex=u_sex, age=u_age, credit_all=0)
    session.merge(user)
    session.commit()


def add_record(u_id, c_type, c_credit, c_time):
    # yesterday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    today = datetime.date.today()
    if c_time == today:
        credit = Credit(user_id=u_id, credit_type=c_type, credit=c_credit, time=c_time)
        session.merge(credit)
        session.commit()


def select_record():
    pass


def select_user():
    pass


def up_user():
    pass

Base.metadata.drop_all()
Base.metadata.create_all()


# today=datetime.date.today()

# print(today)
# credit = Credit(user_id=123, credit_id=123, credit=123, time='2020-02-02')
# session.add(credit)
# session.commit()

# add_Record(123, 123, 12, today)

# add_Uesr(12,12,12,12)


# Base.metadata.drop_all()
# S=session()
# objects = [
#     Punching_card(credit_id="20181001", credit_type="Math"),
#     Punching_card(credit_id="20181002",credit_type="English"),
#     Punching_card(credit_id="20181003",credit_type="Politics"),
#     Punching_card(credit_id="20181004",credit_type="Professional")]
# session.add_all(objects)
# session.commit()
