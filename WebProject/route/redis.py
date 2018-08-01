"""
Routes and views for the bottle application.
REDIS数据管理部分
"""
from datetime import datetime
from flask import (render_template, request)

from WebProject import app
from WebProject.common import web_helper
from WebProject.models.models import Rediscfg
from WebProject.route import repository


@app.route('/redis')
def redisIndex():
    """Renders the about page."""
    # 创建session对象:
    session = repository.GetSession()
    items = session.query(Rediscfg).all()
    return render_template('/redis/redis_index.html',
                           data=items,
                           year=datetime.now().year)


@app.route('/redis/append')
def redisAppend():
    # 创建对象
    data = Rediscfg()

    return render_template('/redis/redis_edit.html',
                           title='Redis 信息',
                           year=datetime.now().year,
                           model=data
                           )


@app.route('/redis/update')
def redisUpdate():

    # 创建session对象
    session = repository.GetSession()
    data = Rediscfg()
    data.Redis_Id = request.forms.get('Redis_Id')
    data.DomainName = request.forms.get('DomainName')
    data.IPAddress = request.forms.get('IPAddress')
    data.Username = request.forms.get('Username')
    data.Note = request.forms.get('Note')

    if(data.Redis_Id == 'None' or data.Redis_Id == None):
        data.Redis_Id = None
        session.add(data)
        session.commit()
    else:
        session.query(Rediscfg).filter(Rediscfg.Redis_Id == data.Redis_Id).update(
            {"DomainName": data.DomainName, "IPAddress": data.IPAddress, "Username": data.Username, "Note": data.Note, }, synchronize_session=False)
        session.commit()

    return web_helper.return_msg(0, "保存成功！")


@app.route('/redis/edit/<redisId>')
def redisEdit(redisId):
    # 创建session对象:
    session = repository.GetSession()
    redis = session.query(Rediscfg).get(redisId)
    return render_template('/redis/redis_edit.html', year=datetime.now().year, model=redis)
