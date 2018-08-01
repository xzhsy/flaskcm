import os
import time
from _datetime import datetime
from flask import render_template, request, flash,url_for,send_from_directory,redirect,abort
from WebProject import app
from WebProject.route import repository
from WebProject.common import json_helper, web_helper

ALLOWED_EXTENSIONS= set(['xls','xlsx'])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file_dir = app.config['UPLOAD_FOLDER']
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        if file and allowed_file(file.filename):
            ext = file.filename.rsplit('.', 1)[1]  # 获取文件后缀
            unix_time = int(time.time())
            new_filename = str(unix_time) + '.' + ext  # 修改了上传的文件名
            file.save(os.path.join(file_dir, new_filename))  # 保存文件到upload目录
            print(new_filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            flash("上传成功")
    return  redirect('/upload.html')


@app.route('/file/<filename>')
def download(filename):
    fpath = os.path.join(app.root_path,'xlsData')
    fname = filename
    print(os.path.join(fpath, filename))
    print(fname)
    return send_from_directory(fpath, fname, as_attachment=True)
    # return send_from_directory(fpath, fname, as_attachment=True)  # 返回要下载的文件内容给客户端
    # if os.path.isfile(os.path.join(fpath, fname)) and os.path.isdir(fpath):
    #     return send_from_directory(fpath, fname, as_attachment=True)  # 返回要下载的文件内容给客户端
    # else:
    #     return '{"msg":"参数不正确"}'