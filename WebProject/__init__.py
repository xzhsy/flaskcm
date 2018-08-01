"""
The flask application package.
"""
import os
from flask import Flask
import logging
from flask_login import LoginManager

# create logger
logger = logging.getLogger('CMD_APP')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

logger.info("创建 Flask 对象")
app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = 'WebProject/xlsData'
basedir = os.path.abspath(os.path.dirname(__file__))
logger.info("初始化 LoginManager")
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
logger.info("为 Session 指定 secret_key ")
app.secret_key = os.urandom(24)

logger.info("加载路由设置")
import WebProject.route



