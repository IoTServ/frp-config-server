# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from flask_wtf import Form
from wtforms import SelectField, StringField, TextAreaField, SubmitField, PasswordField,IntegerField,FileField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class baseForm(Form):
    name = StringField(u'名称（仅仅作为标记）：', validators=[DataRequired(), Length(1, 64)])
class proxybaseForm(baseForm):
    frpc = SelectField(u'选择一个已经创建的Frpc：', coerce=int, validators=[DataRequired()])

class localproxybaseForm(proxybaseForm):
    local_ip = StringField(u'本地ip地址：')  # 127.0.0.1
    local_port = StringField(u'本地端口：', validators=[DataRequired()])  # 22
    use_encryption = BooleanField(u'是否加密：')  # false
    use_compression = BooleanField(u'是否压缩：')  # false

class CommonForm(baseForm):
    user = StringField(u'frpc用户名：', validators=[DataRequired(), Length(1, 64)])  # your_name
    server_addr = StringField(u'服务器地址：', validators=[DataRequired(), Length(1, 16)])  # 0.0.0.0
    server_port = StringField(u'服务器端口：', validators=[DataRequired()])  # 7000
    log_file = StringField(u'日志保存位置：')  # ./ frpc.log
    log_level = StringField(u'日志等级：')  # info
    log_max_days = StringField(u'日志存储天数：')  # 3
    privilege_token = StringField(u'服务器秘钥：')  # 12345678
    admin_addr = StringField(u'admin绑定地址：')  # 127.0.0.1
    admin_port = StringField(u'admin绑定端口：')  # 7400
    admin_user = StringField(u'admin用户名：')  # admin
    admin_pwd = StringField(u'admin密码：')  # admin
    pool_count = StringField(u'连接池数量：')  # 5
    tcp_mux = StringField(u'tcp_mux：')  # true
    login_fail_exit = StringField(u'登录失败退出：')  # true
    protocol = StringField(u'传输协议：')  # tcp
    start = StringField(u'启用的代理：')  # ssh,dns
    heartbeat_interval = StringField(u'心跳间隔：')  # 30
    heartbeat_timeout = StringField(u'心跳超时时间：')  # 90
    submit = SubmitField('添加')
class TCPForm(localproxybaseForm):
    remote_port = StringField(u'远程服务器端口：')  # 6001
    submit = SubmitField('添加')
class UDPForm(localproxybaseForm):
    remote_port = StringField(u'远程服务器端口：')  # 6002
    submit = SubmitField('添加')
class HTTPForm(localproxybaseForm):
    http_user = StringField(u'http用户名：')  # admin
    http_pwd = StringField(u'http密码：')  # admin
    subdomain = StringField(u'子域：')  # web01
    custom_domains = StringField(u'域名：')  # web02.yourdomain.com
    locations = StringField(u'路径：')  # /, / pic
    host_header_rewrite = StringField(u'头部重写：')  # example.com
    submit = SubmitField('添加')
class HTTPSForm(localproxybaseForm):
    subdomain = StringField(u'子域名：')  # web01
    custom_domains = StringField(u'域名：')  # web02.yourdomain.com
    submit = SubmitField('添加')
class PluginUnixSocketForm(proxybaseForm):
    remote_port = StringField(u'远程服务器端口：')  # 6003
    plugin_unix_path = StringField(u'Unix socket位置：')  # / var / run / docker.sock
    submit = SubmitField('添加')
class PluginHttpForm(proxybaseForm):
    remote_port = StringField(u'远程服务器端口：')  # 6004
    plugin_http_user = StringField(u'http用户名：')  # abc
    plugin_http_passwd = StringField(u'http密码：')  # abc
    submit = SubmitField('添加')
class stcpForm(localproxybaseForm):
    sk = StringField(u'校验码（sk）：')  # abcdefg
    submit = SubmitField('添加')
class stcpVistorForm(proxybaseForm):
    server_name = StringField(u'服务器名：')  # secret_tcp
    sk = StringField(u'校验码（sk）：')  # abcdefg
    bind_addr = StringField(u'绑定地址：')  # 127.0.0.1
    bind_port = StringField(u'绑定端口：')  # 9000
    use_encryption = BooleanField(u'是否加密：')  # false
    use_compression = BooleanField(u'是否压缩：')  # false
    submit = SubmitField('添加')
