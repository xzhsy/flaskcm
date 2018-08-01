"""
Routes and views for the bottle application.
用户数据管理部分
"""
from datetime import datetime
from flask import (render_template, request)
from flask_login import current_user, login_required

from WebProject import app
from WebProject.common import web_helper
from WebProject.models.models import User
from WebProject.route import repository
from WebProject.xlsUtil.page import Pagination

@app.route('/user.html')
@login_required
def userIndex():
    """Renders the about page."""
    # 创建session对象:
    db = repository.GetSession()
    users = db.query(User).all()
    isadmin = current_user.IsAdmin
    id = current_user.userId
   
    for u in users:
        print(u.username,u.password,u.email,u.IsAdmin)
    return render_template('user/userIndex.html', title='用户管理',
                           message='Your application description page.',
                           year=datetime.now().year,
                           data=users, admin=isadmin, id=id)


@app.route('/profile.html')
@login_required
def profile():
    """Renders the about page."""
    # 创建session对象:
    db = repository.GetSession()
    users = db.query(User).filter_by(userId=current_user.userId).first()
    isadmin = current_user.IsAdmin
    id = current_user.userId
   
 
    return render_template('profile.html', title='个人信息',
                           message='Your application description page.',
                           year=datetime.now().year,
                           data=users, admin=isadmin, id=id)

@app.route('/user/delete_View/<userId>', methods=['GET'])
def userDeleteView(userId):
    # 创建session对象:
    db = repository.GetSession()
    userdata = db.query(User).get(userId)

    return render_template('user/userdel.html', title='用户编辑',
                           year=datetime.now().year,
                           model=userdata)                          


@app.route('/user/delete', methods=['POST'])
def delete():
    db = repository.GetSession()
    userId = request.form.get('userId')
    userdata = db.query(User).get(userId)
    db.delete(userdata)
    db.commit()
    db.close()
    return web_helper.return_msg(0, "删除成功！")


@app.route('/user/edit/<userId>', methods=['POST', 'GET'])
# @view('useredit')
def userEdit(userId):
    # 创建session对象:
    db = repository.GetSession()
    user = db.query(User).get(userId)
    dict(title='用户编辑',
         year=datetime.now().year,
         model=user)
    return render_template('user/useredit.html', title='用户编辑',
                           year=datetime.now().year,
                           model=user)


@app.route('/user/update', methods=['POST'])
# @view('useredit')
def userUpdate():
    userId = request.form.get('userId')
    username = request.form.get('username')
    note = request.form.get('note').encode()
    note = note.decode('utf-8')
    email = request.form.get('email')
    password = request.form.get('password')
    # 创建session对象:
    # print(userId,username,email,note)
    db = repository.GetSession()
    db.query(User).filter(User.userId == userId).update(
        {"username": username, "note": note, "email": email, "password": password}, synchronize_session=False)
    db.commit()
    return web_helper.return_msg(0, "保存成功！")


@app.route('/test')
def test():
    li = []
    for i in range(1, 100):
        li.append(i)
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=10)
    print(request.path)
    print(request.args)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("test.html", index_list=index_list, html=html)
    
