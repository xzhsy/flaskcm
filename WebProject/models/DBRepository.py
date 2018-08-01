from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker


class Repository(object):
    """description of class"""

    def __init__(self, settings):
        """Initializes the repository with the specified settings dict.
        Required settings are:
         - HOST
         - DATABASE
         - USERNAME
         - PASSWORD
        """
        self.name = 'MySql'
        self.host = settings['HOST']
        self.database = settings['DATABASE']
        self.username = settings['USERNAME']
        self.password = settings['PASSWORD']
        self.port = settings['PORT']

    """description of class"""

    def GetSession(self):
        """"数据库连接字符串"""
        ConnectionString = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}?charset=utf8".format(
            user=self.username, pwd=self.password, host=self.host, port=self.port, db=self.database)
        """初始化Sqlalchery""" 'mysql+mysqlconnector://root:123456@localhost:3306/od_appconf'
        engine = create_engine(ConnectionString, pool_recycle=3600)
        DBSession = sessionmaker(bind=engine)
        return DBSession()
