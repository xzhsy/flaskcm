"""
Routes and views for the bottle application.
xexcel restfull
"""

from WebProject import app
from WebProject.common import web_helper
import json
from WebProject.xlsUtil.xls import orm
from WebProject.xlsUtil.xlsTdb import xlsTdb
from flask_login import current_user, login_fresh, login_user, logout_user,login_required
from WebProject.models.models import User
from WebProject.route import repository
from datetime import datetime
from flask import render_template


@app.route('/api')
@login_required
def re():
    return('/index.html')

@app.route('/api/applist/<prjname>')
def do_api(prjname):
    if prjname == None:
        return web_helper.return_msg(400,"输入工程名为空")
    a = orm()
    item = a.main(prjname)
    appList= item
    return json.dumps(appList)

@app.route('/data')
def x2data():
    b=xlsTdb()
    b.main('test.xlsx')
    return('2 data')