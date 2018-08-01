"""
Routes and views for the bottle application.
xexcel 表格路由
"""

from _datetime import datetime
from flask import render_template, request, flash
from WebProject import app
from WebProject.xlsUtil.xls import orm
from flask_login import current_user, login_fresh, login_user, logout_user,login_required
from WebProject.models.models import User,procfg
from WebProject.route import repository
from sqlalchemy import func, or_
from WebProject.xlsUtil.page import Pagination




@app.route('/zk.html')
def zk():
    """Renders the about page."""
    hostList = []
    a = orm()
    item = a.zkinfo()
    hostList = item
    print(hostList)
    hostList = item
    data = {
        'title': '配置信息',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'args': hostList
    }
    return render_template('zkList.html', args=hostList, title='配置信息', year=datetime.now().year,message='Your application description page.')


@app.route('/redis.html')
def redisList():
    """Renders the about page."""
    hostList = []
    a = orm()
    item = a.redisinfo()
    hostList = item
    # print(item)
    data = {
        'title': '配置信息',
        'message': 'Your application description page.',
        'year': datetime.now().year,
        'args': hostList
    }
    return render_template('redisList.html',args=hostList,title='配置信息', year=datetime.now().year,message='Your application description page.')


@app.route('/project.html', methods=['POST','GET'])
def do_pos():
    prj = request.form.get('prjname')
    if prj is None:
        prj = request.args.get('prjname')
    print('args',prj)
    # print(request.args['prjname'])
    # prj = prj.encode('latin1').decode('utf-8')
    # a = orm()
    # item = a.main(prj)
    # appList = item
    # # print(appList)
    # data = {
    #     'title': '配置信息',
    #     'message': 'Your application description page.',
    #     'year': datetime.now().year,
    #     'args': appList
    # }
    # flash('查询成功')
    # return render_template('project.html',args=appList,title='配置信息', year=datetime.now().year,message='Your application description page.')
    li = []
    db = repository.GetSession()
    # print('prj:',prj)
    if prj == None:
        projects = db.query(procfg).limit(2).all()
    else:
        projects = db.query(procfg).filter(or_(procfg.proname == prj, procfg.project == prj))
    # print("projects:",projects,"prj:",prj)
    for i in projects:
        # print(i.proname)
        li.append(i)
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=10)
    print(request.path)
    print(request.args)
    print(li)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("project.html", index_list=index_list, html=html,title='配置信息', year=datetime.now().year,message='Your application description page.')
