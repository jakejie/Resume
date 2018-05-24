# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:jobguanli
FileName = PyCharm
Version:1.0
CreateDay:2018/4/16 13:37
"""
# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, query

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'roottoor'
# PASSWORD = 'root'
HOST = '*'
# HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'movie'

engine = create_engine("{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE), pool_size=100)

Base = declarative_base()
Base.metadata.reflect(engine)
db_session = scoped_session(sessionmaker(bind=engine))



if __name__ == "__main__":
    pass

