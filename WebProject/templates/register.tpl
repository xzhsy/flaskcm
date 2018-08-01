<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="Generator" content="EditPlus®">
  <meta name="Author" content="">
  <meta name="Keywords" content="">
  <meta name="Description" content="">
  <title>Document</title>
 </head>
 <body>
{% extends 'layout.tpl' %}
{% block title %}
SINGIN Page
{% endblock %}
{% block content %}
<h2>用户注册</h2>
<div id="alertContainer">
</div>
<script src="/static/scripts/sys.js"></script>
<script src="/static/scripts/jquery-1.10.2.js"></script>
<script type="text/javascript">
    $(function () {
        $("#btnSave").click(function (event) {
            // 阻止默认的表单请求
            event.preventDefault();

            $.ajax({
                type: "POST",
                url: "/register/adduser",
                data: {
                    'username': $("#txtusername").val(),
                    'password': $("#txtpassword").val(),
                    'email': $("#txtemail").val()
                },
                dataType: "json",
                success: function (data) {
                    if (data.state == 0) {
                        // 显示消息栏
                        bs_alert_Info(data.msg);
                    }
                }
            });
        });

    })
</script>
<form action="" method="POST" class="form-horizontal" role="form">
    <div class="form-group">
        <legend>请输入用户 密码</legend>
    </div>

    <div class="form-group">
        <label class="col-sm-2 control-label">用户名</label>
        <div class="col-sm-6">
            <input type="text" class="form-control" placeholder="UserName"  name="username" id="txtusername" >
        </div>
    </div>
	<div class="form-group">
        <label class="col-sm-2 control-label">密码</label>
        <div class="col-sm-6">
            <input type="text" class="form-control" placeholder="Password"  name="password" id ="txtpassword"  >
        </div>
    </div>
	<div class="form-group">
        <label class="col-sm-2 control-label">邮箱</label>
        <div class="col-sm-6">
            <input type="text" class="form-control" placeholder="Email"  name="email" id = "txtemail" >
        </div>
    </div>
    <div class="form-group">
        <div class="col-sm-6 col-sm-offset-2">
            <input type="submit" value="注册" id="btnSave">
        </div>
    </div>
    {% if error %}<div class="form-group">
    <div class="col-sm-6 col-sm-offset-2">
	<strong>Error:</strong> {{ error }}
	</div>
    </div>{% endif %}
</form>
{% endblock %}
 </body>
</html>
