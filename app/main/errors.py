# coding:utf-8
import json
from flask import render_template, request, jsonify
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@main.app_errorhandler(404)
def notfound(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@main.app_errorhandler(413)
def toolage(e):
    dict_tmp = {}
    dict_tmp['error'] = 1
    dict_tmp['message'] = "文件大小不可以超过限制！"
    return json.dumps(dict_tmp),413
