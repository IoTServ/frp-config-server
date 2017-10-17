#coding:utf-8
from flask_oauthlib.client import OAuth
import json

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect

from config import Config
from flask_admin import Admin


db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CsrfProtect()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
oauth = OAuth()
admin = Admin(name=u"后台管理系统",template_mode='bootstrap3')
def create_app():
    app = Flask(__name__)
    oauth.init_app(app)

    admin.init_app(app)
    from .modeviews import MyModelView
    from .models import User, FrpProxy_HTTP, FrpProxy_HTTPS, FrpProxy_PluginHttp, FrpProxy_PluginUnixSocket, \
        FrpProxy_TCP, FrpProxy_STCP, FrpProxy_STCPVistor, FrpProxy_UDP, FrpServiceCommon
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(FrpProxy_HTTP, db.session))
    admin.add_view(MyModelView(FrpProxy_HTTPS, db.session))
    admin.add_view(MyModelView(FrpProxy_PluginHttp, db.session))
    admin.add_view(MyModelView(FrpProxy_PluginUnixSocket, db.session))
    admin.add_view(MyModelView(FrpProxy_TCP, db.session))
    admin.add_view(MyModelView(FrpProxy_STCP, db.session))
    admin.add_view(MyModelView(FrpProxy_STCPVistor, db.session))
    admin.add_view(MyModelView(FrpProxy_UDP, db.session))
    admin.add_view(MyModelView(FrpServiceCommon, db.session))

    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app
