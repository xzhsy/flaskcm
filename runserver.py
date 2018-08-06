"""
This script runs the FlaskWebProject2 application using a development server.
"""

from os import environ
import WebProject
import logging
from WebProject import app
from WebProject import setting,logger

if __name__ == '__main__':

    """输出配置信息"""
    # create logger
    logger.info('服务器配置数据:')
    for k in setting.REPOSITORY_SETTINGS.keys():
        logger.info('%s : %s', k, setting.REPOSITORY_SETTINGS[k])


    logger.info('开始启动网站服务..........')
    """启动服务"""
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 8080
    app.run(HOST, PORT)


