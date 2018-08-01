from datetime import datetime
from sqlalchemy import Column, String, DateTime, create_engine, Boolean, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin,login_user
import uuid

# 创建对象的基类:
Base = declarative_base()
# 定义User对象:


class User(Base,UserMixin):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    userId = Column(String(36), primary_key=True)
    username = Column(String(20))
    email = Column(String(20))
    password = Column(String(20))
    note = Column(String(20))
    create_time = Column(DateTime(), default=datetime.now)
    updated_time = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now)
    IsAdmin = Column(Boolean(), default=False)
    IsLogin = Column(Boolean(), default=False)
    # Allowed = Column(Boolean(), default=False)
    
    def get_id(self):
        return self.userId

class Rediscfg(Base):
    # 表的名字:
    __tablename__ = 'rediscfg'
    # 表的结构:
    Redis_Id = Column(Integer(), primary_key=True, autoincrement=True)
    DomainName = Column(String(36), nullable=False)
    IPAddress = Column(String(36), nullable=False)
    Username = Column(String(36), nullable=False)
    Password = Column(String(36)),
    Note = Column(String(36)),
    Used = Column(Boolean(), default=False)
    create_time = Column(DateTime(), default=datetime.now)
    updated_time = Column(
        DateTime(), default=datetime.now, onupdate=datetime.now)

    def __init__(self):
        self.DomainName = ''
        self.IPAddress = ''
        self.Username = ''
        self.Used = False
        self.Password = ''
        self.Note = ''

class procfg(Base):
    # 表的名字:
    __tablename__ = 'procfg'
    # 表的结构:
    proid = Column(Integer(), primary_key=True, autoincrement=True)
    proname = Column(String(36), nullable=False)
    project = Column(String(36), nullable=False)
    IPAddress = Column(String(36), nullable=False)
    node = Column(String(36))
    gr = Column(String(36))
    http = Column(Integer())
    https = Column(Integer())
    ajp = Column(Integer())
    shutdown = Column(Integer())
    jmx = Column(Integer())
    dubbo = Column(Integer())
    path = Column(String(36))
    create_time = Column(DateTime(), default=datetime.now)
    updated_time = Column(DateTime(), default=datetime.now)

    def __init__(self):
        self.http = ''
        self.IPAddress = ''
        self.https = ''
        self.ajp = ''
        self.shutdown = ''
        self.dubbo = ''
        self.jmx = ''
        self.proname = ''
        self.node = ''
        self.proid = ''
        self.project = ''
        self.group = ''
        self.path = ''