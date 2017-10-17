# coding:utf-8
from flask import render_template, session, url_for, flash, current_app, jsonify
from flask_login import login_user, login_required, logout_user
from flask_login import current_user
from . import auth
from ..models import User
from flask import redirect
from flask import request
from .. import oauth
from config import Config
import json

qq = oauth.remote_app(
    'qq',
    consumer_key=Config.QQ_APP_ID,
    consumer_secret=Config.QQ_APP_KEY,
    base_url='https://graph.qq.com',
    request_token_url=None,
    request_token_params={'scope': 'get_user_info'},
    access_token_url='/oauth2.0/token',
    authorize_url='/oauth2.0/authorize',
)


def json_to_dict(x):
    '''OAuthResponse class can't parse the JSON data with content-type
-    text/html and because of a rubbish api, we can't just tell flask-oauthlib to treat it as json.'''
    if x.find(b'callback') > -1:
        # the rubbish api (https://graph.qq.com/oauth2.0/authorize) is handled here as special case
        pos_lb = x.find(b'{')
        pos_rb = x.find(b'}')
        x = x[pos_lb:pos_rb + 1]

    try:
        if type(x) != str:  # Py3k
            x = x.decode('utf-8')
        return json.loads(x, encoding='utf-8')
    except:
        return x


def update_qq_api_request_data(data={}):
    '''Update some required parameters for OAuth2.0 API calls'''
    defaults = {
        'openid': session.get('qq_openid'),
        'access_token': session.get('qq_token')[0],
        'oauth_consumer_key': Config.QQ_APP_ID,
    }
    defaults.update(data)
    return defaults


@auth.route('/')
def index():
    '''just for verify website owner here.'''
    return "auth"


@auth.route('/user_info')
def get_user_info():
    if 'qq_token' in session:
        data = update_qq_api_request_data()
        resp = qq.get('/user/get_user_info', data=data)
        return jsonify(status=resp.status, data=json_to_dict(resp.data))
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return redirect(url_for('auth.qqlogin'))

@auth.route('/qqlogin')
def qqlogin():
    return qq.authorize(callback='http://duapp.iotserv.com/auth/qqauthorized') #http://duapp.iotserv.com/login/authorized  #url_for('auth.authorized', _external=True)


@auth.route('/logout')
def logout():
    session.pop('qq_token', None)
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/qqauthorized')
def qqauthorized():
    resp = qq.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['qq_token'] = (resp['access_token'], '')

    # Get openid via access_token, openid and access_token are needed for API calls
    resp = qq.get('/oauth2.0/me', {'access_token': session['qq_token'][0]})
    resp = json_to_dict(resp.data)
    if isinstance(resp, dict):
        session['qq_openid'] = resp.get('openid')
    qq_openid = resp.get('openid')
    user = User.query.filter_by(qq_openid=qq_openid).first()
    if user is not None:
        login_user(user)
        return redirect(url_for("manage.index"))
    else:
        User.insert_user(qq_openid)
        user = User.query.filter_by(qq_openid=qq_openid).first()
        login_user(user)
        return redirect(url_for("manage.index"))

@qq.tokengetter
def get_qq_oauth_token():
    return session.get('qq_token')




# @auth.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if current_user.is_loged():
#         flash(u'您已经处于登录状态！', 'danger')
#         return redirect(url_for('main.index'))
#
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user is not None and user.verify_password(form.password.data):
#             login_user(user)
#             flash(u'登陆成功！欢迎回来，%s!' % user.username, 'success')
#             print request.values.get('next')
#             return redirect(request.values.get('next') or url_for("main.index"))
#         else:
#             flash(u'登陆失败！用户名或密码错误，请重新登陆。', 'danger')
#     if form.errors:
#         flash(u'登陆失败，请尝试重新登陆.', 'danger')
#
#     return render_template('auth/login.html', form=form, next=request.values.get("next"))
