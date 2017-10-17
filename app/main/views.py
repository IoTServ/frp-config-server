#coding:utf-8
from flask import request,render_template

from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/FreeFrpServer.html')
def FreeFrpServer():
    return render_template('FreeFrpServer.html')

@main.route('/FrpcConfig.html')
def FrpcConfig():
    return render_template('FrpcConfig.html')

@main.route('/FrpGithub.html')
def FrpGithub():
    return render_template('FrpGithub.html')

@main.route('/NAT-Download.html')
def Download():
    return render_template('NAT-Download.html')