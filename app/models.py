#coding: utf-8
import hashlib,urllib2,json
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin, current_user
from . import db, login_manager
from flask import current_app

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    qq_openid = db.Column(db.String(64))
    services = db.relationship('FrpServiceCommon', backref='webuser', lazy='dynamic')

    # proxies
    tcp_s = db.relationship('FrpProxy_TCP', backref='webuser', lazy='dynamic')  # TCP
    udp_s = db.relationship('FrpProxy_UDP', backref='webuser', lazy='dynamic')  # UDP
    http_s = db.relationship('FrpProxy_HTTP', backref='webuser', lazy='dynamic')  # HTTP
    https_s = db.relationship('FrpProxy_HTTPS', backref='webuser', lazy='dynamic')  # HTTPS
    pusocket_s = db.relationship('FrpProxy_PluginUnixSocket', backref='webuser', lazy='dynamic')  # PluginUnixSocket
    phttp_s = db.relationship('FrpProxy_PluginHttp', backref='webuser', lazy='dynamic')  # PluginHttp
    stcp_s = db.relationship('FrpProxy_STCP', backref='webuser', lazy='dynamic')  # stcp
    stcpvistor_s = db.relationship('FrpProxy_STCPVistor', backref='webuser', lazy='dynamic')  # stcpVistor

    @staticmethod
    def insert_user(qq_openid):
        user = User(qq_openid=qq_openid)
        db.session.add(user)
        db.session.commit()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def is_administrator(self):
        return self.id==1

    def __repr__(self):
        return '<User %r>' % self.id

    def getallcomm(self):
        return [(t.id, t.name) for t in self.services]

class AnonymousUser(AnonymousUserMixin):
    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser

# callback function for flask-login extentsion
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class FrpServiceCommon(db.Model):
    __tablename__ = 'frp_services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    server_addr = db.Column(db.String(16))     #0.0.0.0
    server_port = db.Column(db.String(16))     #7000
    log_file =db.Column(db.String(64))         # ./ frpc.log
    log_level = db.Column(db.String(16))       #info
    log_max_days = db.Column(db.String(16))     #3
    privilege_token = db.Column(db.String(64)) # 12345678
    admin_addr = db.Column(db.String(64))       # 127.0.0.1
    admin_port = db.Column(db.String(16))     #7400
    admin_user = db.Column(db.String(64))       #admin
    admin_pwd = db.Column(db.String(64))        #admin
    pool_count = db.Column(db.String(16))     #5
    tcp_mux = db.Column(db.String(16))      #true
    user = db.Column(db.String(64),unique=True,index=True)         #your_name
    login_fail_exit = db.Column(db.String(16))#true
    protocol = db.Column(db.String(16))     #tcp
    start = db.Column(db.String(128))        #ssh,dns
    heartbeat_interval = db.Column(db.String(16))     #30
    heartbeat_timeout = db.Column(db.String(16))     #90
    #web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    #proxies
    tcp_s = db.relationship('FrpProxy_TCP', backref='servcomm', lazy='dynamic')   #TCP
    udp_s = db.relationship('FrpProxy_UDP', backref='servcomm', lazy='dynamic')   #UDP
    http_s = db.relationship('FrpProxy_HTTP', backref='servcomm', lazy='dynamic')   #HTTP
    https_s = db.relationship('FrpProxy_HTTPS', backref='servcomm', lazy='dynamic')   #HTTPS
    pusocket_s = db.relationship('FrpProxy_PluginUnixSocket', backref='servcomm', lazy='dynamic')   #PluginUnixSocket
    phttp_s = db.relationship('FrpProxy_PluginHttp', backref='servcomm', lazy='dynamic')   #PluginHttp
    stcp_s = db.relationship('FrpProxy_STCP', backref='servcomm', lazy='dynamic')   #stcp
    stcpvistor_s = db.relationship('FrpProxy_STCPVistor', backref='servcomm', lazy='dynamic')   #stcpVistor

    def __repr__(self):
        return '<FrpService %r>' % self.name


class FrpProxy_TCP(db.Model):
    __tablename__ = 'frp_tcp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    local_ip = db.Column(db.String(16))#127.0.0.1
    local_port = db.Column(db.String(16))#22
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#false
    remote_port = db.Column(db.String(16))#6001
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_TCP %r>' % self.name

class FrpProxy_UDP(db.Model):
    __tablename__ = 'frp_udp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    local_ip = db.Column(db.String(16))#114.114.114.114
    local_port = db.Column(db.String(16))#53
    remote_port = db.Column(db.String(16))#6002
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#false
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_UDP %r>' % self.name


class FrpProxy_HTTP(db.Model):
    __tablename__ = 'frp_http'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    local_ip = db.Column(db.String(16))#127.0.0.1
    local_port = db.Column(db.String(16))#80
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#true
    http_user = db.Column(db.String(16))#admin
    http_pwd = db.Column(db.String(16))#admin
    subdomain = db.Column(db.String(16))#web01
    custom_domains = db.Column(db.String(16))#web02.yourdomain.com
    locations = db.Column(db.String(16))#/, / pic
    host_header_rewrite = db.Column(db.String(16))#example.com
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_HTTP %r>' % self.name

class FrpProxy_HTTPS(db.Model):
    __tablename__ = 'frp_https'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    local_ip = db.Column(db.String(16))#127.0.0.1
    local_port = db.Column(db.String(16))#8000
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#false
    subdomain = db.Column(db.String(16))#web01
    custom_domains = db.Column(db.String(16))#web02.yourdomain.com
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_HTTPS %r>' % self.name

class FrpProxy_PluginUnixSocket(db.Model):
    __tablename__ = 'frp_PluginUnixSocket'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    remote_port = db.Column(db.String(16))#6003
    plugin_unix_path = db.Column(db.String(16))#/ var / run / docker.sock
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_PluginUnixSocket %r>' % self.name

class FrpProxy_PluginHttp(db.Model):
    __tablename__ = 'frp_PluginHttp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    remote_port = db.Column(db.String(16))#6004
    plugin_http_user = db.Column(db.String(16))#abc
    plugin_http_passwd = db.Column(db.String(16))#abc
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_PluginHttp %r>' % self.name

class FrpProxy_STCP(db.Model):
    __tablename__ = 'frp_stcp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    sk = db.Column(db.String(16))#abcdefg
    local_ip = db.Column(db.String(16))#127.0.0.1
    local_port = db.Column(db.String(16))#22
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#false
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_STCP %r>' % self.name

class FrpProxy_STCPVistor(db.Model):
    __tablename__ = 'frp_stcpVistor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    server_name = db.Column(db.String(16))#secret_tcp
    sk = db.Column(db.String(16))#abcdefg
    bind_addr = db.Column(db.String(16))#127.0.0.1
    bind_port = db.Column(db.String(16))#9000
    use_encryption = db.Column(db.Boolean)#false
    use_compression = db.Column(db.Boolean)#false
    # web user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    service_id = db.Column(db.Integer, db.ForeignKey('frp_services.id'))
    def __repr__(self):
        return '<FrpProxy_STCPVistor %r>' % self.name