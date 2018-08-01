"""
Routes and views for the bottle application.
用户登录和注册相关的内容
"""
import json
import os
import uuid
from datetime import datetime

from flask import (Flask, escape, flash, redirect, render_template, request,
                   session, url_for)
from flask_login import current_user, login_fresh, login_user, logout_user,login_required

import WebProject.common
from WebProject import app, login_manager
from WebProject.common import json_helper, web_helper
from WebProject.models.factory import create_repository
from WebProject.models.models import Rediscfg, User
from WebProject.setting import REPOSITORY_SETTINGS
from WebProject.xlsUtil.xls import orm
from WebProject.route import repository

# login_manager在INIT中初始化的Login_manager


@login_manager.user_loader
def user_loader(user_Id):
    db = repository.GetSession()
    return db.query(User).filter_by(userId=user_Id).first()


@app.route('/')
@app.route('/index.html')
def index():
    # current_user 是 flask_login 模块定义的全局对象
    """先判断是否已经登录"""
    if current_user.is_authenticated:
        return render_template('index.html', year=datetime.now().year)
    # 检查失败则返回匿名页
    return redirect('login.html')



@app.route('/login.html', methods=['POST'])
def Userlogin():
    error = None
    username = request.form['username']
    password = request.form['password']
    db = repository.GetSession()
    u = db.query(User).filter_by(username=username, password=password).first()
    if u is None:
        error = 'Invalid username'
    elif password is '':
        error = 'Invalid password'
    else:
        if u.password == password:
            login_user(u)
            return redirect(url_for('index'))
        else:
            error = 'wrong password'
    return render_template('login.html', year=datetime.now().year, error=error)


@app.route('/login.html', methods=['GET'])
def login():
    error = None
    return render_template('login.html', year=datetime.now().year, error=error)


@app.route("/logout.html",methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register.html')
def adduser():
    error = None
    return render_template('register.html', year=datetime.now().year, error=error)


@app.route('/register/adduser', methods=['POST'])
def register():
    error = None
    db = repository.GetSession()
    userid = str(uuid.uuid4())
    name = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    note = request.form.get('note')
    add = db.query(User).filter_by(username=name).first()
    print(type(name), name, password, email)
    if not add:
        if name and password and email:
            user = User(username=name, password=password,
                        email=email, userId=userid, Allowed=False)
            db.add(user)
            db.commit()
    else:
        return web_helper.return_msg(-1, '输入注册用户名已存在')

    if not name:
        return web_helper.return_msg(-1, '输入注册用户名为空')
    if not password:
        return web_helper.return_msg(-1, '输入注册密码为空')
    if not email:
        return web_helper.return_msg(-1, '输入注册邮箱为空')

    return web_helper.return_msg(0, '用户注册成功', data={"Id": userid})


@app.route('/register/msg/<userId>')
def registerMsg(userId):
    db = repository.GetSession()
    data = db.query(User).filter_by(userId=userId).first()
    return render_template("registerMessage.html", model=data)


"""
关于、联系信息和主页的内容
"""


@app.route('/home.html')
@login_required
def home():
    """Renders the home page."""
    return render_template('index.html', year=datetime.now().year)


@app.route('/404.html')
def err404():
    """Renders the contact page."""
    return render_template('404.html', year=datetime.now().year)

@app.route('/500.html')
def err500():
    """Renders the contact page."""
    return render_template('404.html', year=datetime.now().year)


@app.route('/setting.html')
@login_required
def setting():
    """Renders the contact page."""
    return render_template('setting.html', year=datetime.now().year)
"""
服务器资产信息
"""

@app.route('/assets.html')
def table():
    error = None
    return render_template('assets.html', year=datetime.now().year, error=error)

@app.route('/server.html')
def server():
    error = None
    return render_template('server.html', year=datetime.now().year, error=error)


@app.route('/tbatch.html')
def tbatch():
    error = None
    return render_template('tbatch.html', year=datetime.now().year, error=error)



@app.route('/plan.html')
def plan():
    error = None
    return render_template('plan.html', year=datetime.now().year, error=error)    


@app.route('/middleware.html')
def middleware():
    error = None
    return render_template('middleware.html', year=datetime.now().year, error=error)  


@app.route('/port.html')
def port():
    error = None
    return render_template('port.html', year=datetime.now().year, error=error)      


@app.route('/upload.html')
def up():
    files_list = os.listdir(app.config['UPLOAD_FOLDER'])
    file_url = app.config['UPLOAD_FOLDER']
    print(files_list)
    return render_template('upload.html', year=datetime.now().year,title='文件上传', files_list=files_list)