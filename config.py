# coding: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_POOL_SIZE = 50
    SQLALCHEMY_DATABASE_URI = 'mysql://msyqlusername:password@127.0.0.1/frpconfig'   ##USE MySQL DB  最后的frpconfig换成自己的数据库名
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/frpconfig' ##USE Postgresql DB
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///./frpc.db'  ##USE Postgresql DB not work
    SECRET_KEY = 'secret@key!to $pahjstect &from )csrf@'
    WTF_CSRF_SECRET_KEY = 'randomt f$or fbswor!m' # for csrf protection
    QQ_APP_ID = ''  #从connect.qq.com申请
    QQ_APP_KEY = ''
    @staticmethod
    def init_app(app):
        pass