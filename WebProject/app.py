"""
This script runs the application using a development server.
"""

from flask import Flask, render_template, session,redirect,request,flash
from datetime import datetime
import os,uuid
import routes
from setting import REPOSITORY_SETTINGS
from models.factory import create_repository
from models.models import User, Rediscfg
from common import web_helper, encrypt_helper
# routes contains the HTTP handlers for our server and must be imported.
# import routes
#
# if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
#     # Debug mode will enable more verbose output in the console window.
#     # It must be set at the beginning of the script.
#     bottle.debug(True)


# def wsgi_app():
#     """Returns the application to make available through wfastcgi. This is used
#     when the site is published to Microsoft Azure."""
#     return bottle.default_app()

app = Flask(__name__)

app.secret_key=routes.app.secret_key

repository = create_repository(REPOSITORY_SETTINGS)
if __name__ == '__main__':
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080


    @app.route('/')
    def index():
        db = repository.GetSession()
        u = db.query(User).filter_by(username = session.get('username'),password=session.get('password')).first()
        if u is not  None:
            return redirect('/home')
        return render_template('login.tpl', year=datetime.now().year)


    @app.route('/register')
    def adduser():
        error = None
        return render_template('register.tpl', year=datetime.now().year, error=error)
    @app.route('/register/adduser', methods=['GET', 'POST'])
    def register():
        error = None
        db = repository.GetSession()
        userid = str(uuid.uuid4())
        name=request.form.get('username')
        password=request.form.get('password')
        email=request.form.get('email')
        add = db.query(User).filter_by(username=name).first()
        print(type(name),name,password,email)
        if not add:
           if   name  and   password  and  email :
                user = User(username=name, password=password,email=email,userId=userid)
                db.add(user)
                db.commit()
                flash('注册成功')
        else:
            return web_helper.return_msg(0,'输入注册用户名已存在')

        if  not name :
            return web_helper.return_msg(0,'输入注册用户名为空')
        if not password :
            return web_helper.return_msg(0, '输入注册密码为空' )
        if not email :
            return web_helper.return_msg(0, '输入注册邮箱为空' )
        return web_helper.return_msg(0 ,'用户注册成功')

    @app.route('/login',methods=['POST','GET'])
    def login():
        error = None
        username = request.form['username']
        password = request.form['password']
        db = repository.GetSession()
        u = db.query(User).filter_by(username = username,password=password).first()
        if u is None:
            error = '用户名或密码错误'
        if not u.IsLogin :
            error = "未审核通过"
        else:
            if u.password == password:
                session['userId'] = u.userId
                session['IsAdmin'] = u.IsAdmin
                session['IsLogin'] = u.IsLogin

                return redirect('/home')
            else:
                error = 'wrong password'
        return render_template('login.tpl', year=datetime.now().year,error = error)


    @app.route("/logout")
    def logout():
        if session:
            session.pop('userId', None)
            session.pop('IsAdmin', None)
            session.pop('IsLogin', None)
            flash('退出登录')
        return redirect('/')
    @app.route('/<path:filepath>',methods=['POST','GET'])
    def server_static(filepath):
        db = repository.GetSession()
        u = db.query(User).filter_by(userId = session.get('userId'),IsLogin = 1).first()
        if u is  None:
            return redirect('/')
        return routes.app

    """修改模板文件参数，将相对路径(./)修改为工程路径"""
    views = PROJECT_ROOT+"/views"
    app.TEMPLATE_PATH = [PROJECT_ROOT, views]
    app.PROJECT_ROOT = PROJECT_ROOT
    # Starts a local test server.
    app.run(debug='true', host='0.0.0.0', port=PORT)

