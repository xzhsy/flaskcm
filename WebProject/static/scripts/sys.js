//字符串加上trim功能。（去掉两端空格）
String.prototype.trim = function () { return this.replace(/(^\s*)|(\s*$)/g, ""); };
// 对Date的扩展，将 Date 转化为指定格式的String 
// 月(M)、日(d)、小时(h)、分(m)、秒(s)、季度(q) 可以用 1-2 个占位符， 
// 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字) 
// 例子： 
// (new Date()).Format("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423 
// (new Date()).Format("yyyy-M-d h:m:s.S")      ==> 2006-7-2 8:9:4.18 
Date.prototype.format = function (fmt) { //author: meizz 
    var o = {
        "M+": this.getMonth() + 1,                 //月份 
        "d+": this.getDate(),                    //日 
        "h+": this.getHours(),                   //小时 
        "m+": this.getMinutes(),                 //分 
        "s+": this.getSeconds(),                 //秒 
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
        "S": this.getMilliseconds()             //毫秒 
    };
    if (/(y+)/.test(fmt))
        fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt))
            fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}
// A simple templating method for replacing placeholders enclosed in curly braces.  JS 字符串模板方法
if (!String.prototype.supplant) {
    String.prototype.supplant = function (o) {
        return this.replace(/{([^{}]*)}/g,
            function (a, b) {
                var r = o[b];
                // 如果未定义返回空字符串
                if (r === undefined || r == null)
                    return "";
                if (r === true || r === false || typeof r === 'string' || typeof r === 'number')
                    return r.toString();
                return a;
            }
        );
    };
}

/******
* 包含提示性信息的操作确认对话框
*****/
function bs_alert_Info(msg) {
    var template = '<div class="alert alert-success alert-dismissible" role="alert">'
        + '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
        + '<strong>消息</strong>' + msg
        + '</div>';
    $("#alertContainer").html(template);
}

/**** 封装 EASYUI 对话框 *****/
var sysMSG = {
    /******
    * 包含提示性信息的操作确认对话框
    *****/
    bs_alert_Info: function (msg) {
        var template = '<div class="alert alert-success alert-dismissible" role="alert">'
            + '<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
            + '<strong>消息</strong>' + msg
            + '</div>';
        $("#alertContainer").html(template);
    },
    /******
    * 包含提示性信息的操作确认对话框
    *****/
    Confirm: function (msgInfo, msgTips, fn, fnCancel) {
        // 根据需要处理消息
        var template = "<span class='HRMsg_Info'>" + msgInfo + "</span>";
        if (msgTips != null && msgTips != '') {
            template += "<br><div class='HRMsg_RemarkBlock'>" + msgTips + "</div>";
        }
        // 返回提示信息
        $.messager.confirm('操作确认', template, function (r) {
            if (r) {
                // 如果包含事件处理则调用
                if ($.isFunction(fn))
                    fn();
            }
            else {
                // 如果包含事件处理则调用
                if ($.isFunction(fnCancel))
                    fnCancel();
            }
        });
    },
    Alert: function (msgInfo, msgTips) {
        // 根据需要处理消息
        var template = "<span class='HRMsg_Info'>" + msgInfo + "</span>";
        if (msgTips != null && msgTips != '') {
            template += "<br><div class='HRMsg_RemarkBlock'>" + msgTips + "</div>";
        }
        // 弹出提示框
        $.messager.alert('提示', template, 'info');
    },
    Show: function (msgInfo, msgTips) {
        // 根据需要处理消息
        var template = "<span class='HRMsg_Info'>" + msgInfo + "</span>";
        if (msgTips != null && msgTips != '') {
            template += "<br><div class='HRMsg_RemarkBlock'>" + msgTips + "</div>";
        }
        $.messager.show({
            title: '系统消息',
            msg: template,
            timeout: 5000,
            showType: 'slide'
        });
    },
    /**********
    *将HTML内容原封不动地渲染到窗口
    ************/
    ShowHtml: function (htmlSegment, strTitle) {
        // 默认标题的名称
        var titleName = strTitle === undefined ? '系统消息' : strTitle;
        $.messager.show({
            title: titleName,
            msg: htmlSegment,
            timeout: 5000,
            showType: 'slide'
        });
    }
};