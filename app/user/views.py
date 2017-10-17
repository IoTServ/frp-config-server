# coding:utf-8
from flask import request,render_template,redirect,url_for
from flask_login import current_user,login_required
from ..models import FrpProxy_HTTP, FrpProxy_HTTPS, FrpProxy_PluginHttp, FrpProxy_PluginUnixSocket, \
        FrpProxy_TCP, FrpProxy_STCP, FrpProxy_STCPVistor, FrpProxy_UDP, FrpServiceCommon
from app.user.forms import CommonForm,TCPForm,UDPForm,HTTPForm,HTTPSForm,PluginHttpForm,PluginUnixSocketForm,stcpForm,stcpVistorForm
from . import user
from .. import db

@user.route('/')
@login_required
def index():
    #相关说明
    return render_template('user/userindex.html')

@user.route('/Common')
@login_required
def Common():
    commons=FrpServiceCommon.query.filter_by(user_id=current_user.id).all()
    return render_template('user/Common.html',commons=commons)

@user.route('/HTTP')
@login_required
def HTTP():
    http_s=FrpProxy_HTTP.query.filter_by(user_id=current_user.id).all()
    return render_template('user/HTTP.html',http_s=http_s)

@user.route('/HTTPS')
@login_required
def HTTPS():
    https_s=FrpProxy_HTTPS.query.filter_by(user_id=current_user.id).all()
    return render_template('user/HTTPS.html',https_s=https_s)

@user.route('/Phttp')
@login_required
def Phttp():
    phttps=FrpProxy_PluginHttp.query.filter_by(user_id=current_user.id).all()
    return render_template('user/Phttp.html',phttps=phttps)

@user.route('/Psocket')
@login_required
def Psocket():
    psockets=FrpProxy_PluginUnixSocket.query.filter_by(user_id=current_user.id).all()
    return render_template('user/Psocket.html',psockets=psockets)

@user.route('/stcp')
@login_required
def stcp():
    stcps=FrpProxy_STCP.query.filter_by(user_id=current_user.id).all()
    return render_template('user/stcp.html',stcps=stcps)

@user.route('/stcpvistor')
@login_required
def stcpvistor():
    stcpvistors=FrpProxy_STCPVistor.query.filter_by(user_id=current_user.id).all()
    return render_template('user/stcpvistor.html',stcpvistors=stcpvistors)

@user.route('/TCP')
@login_required
def TCP():
    tcps=FrpProxy_TCP.query.filter_by(user_id=current_user.id).all()
    return render_template('user/TCP.html',tcps=tcps)

@user.route('/UDP')
@login_required
def UDP():
    udps=FrpProxy_UDP.query.filter_by(user_id=current_user.id).all()
    return render_template('user/UDP.html',udps=udps)

@user.route('/del')
@login_required
def delProxy():
    type = request.values.get('type')
    id = request.values.get('id')
    if type=='comm':
        comm = FrpServiceCommon.query.filter_by(id=id).first()
        if comm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(comm)
        db.session.commit()
    if type=='tcp':
        tcp = FrpProxy_TCP.query.filter_by(id=id).first()
        if tcp.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(tcp)
        db.session.commit()
    if type=='udp':
        udp = FrpProxy_UDP.query.filter_by(id=id).first()
        if udp.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(udp)
        db.session.commit()
    if type=='http':
        http = FrpProxy_HTTP.query.filter_by(id=id).first()
        if http.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(http)
        db.session.commit()
    if type=='https':
        https = FrpProxy_HTTPS.query.filter_by(id=id).first()
        if https.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(https)
        db.session.commit()
    if type=='psocket':
        ps = FrpProxy_PluginUnixSocket.query.filter_by(id=id).first()
        if ps.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(ps)
        db.session.commit()
    if type=='phttp':
        phttp = FrpProxy_PluginHttp.query.filter_by(id=id).first()
        if phttp.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(phttp)
        db.session.commit()
    if type=='stcp':
        stcp = FrpProxy_STCP.query.filter_by(id=id).first()
        if stcp.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(stcp)
        db.session.commit()
    if type=='stcpvistor':
        stcpvistor = FrpProxy_STCPVistor.query.filter_by(id=id).first()
        if stcpvistor.servcomm.webuser != current_user:
            return redirect(url_for('manage.index'))
        db.session.delete(stcpvistor)
        db.session.commit()
    return redirect(url_for('manage.index'))

@user.route('/addCommon', methods=['GET', 'POST'])
@login_required
def addCommon():
    form = CommonForm()
    if form.validate_on_submit():
        proxy = FrpServiceCommon(
            name=form.name.data,
            server_addr = form.server_addr.data,  # 0.0.0.0
            server_port = form.server_port.data,  # 7000
            log_file = form.log_file.data,  # ./ frpc.log
            log_level = form.log_level.data,  # info
            log_max_days = form.log_max_days.data,  # 3
            privilege_token = form.privilege_token.data,  # 12345678
            admin_addr = form.admin_addr.data,  # 127.0.0.1
            admin_port = form.admin_port.data, # 7400
            admin_user = form.admin_user.data,  # admin
            admin_pwd = form.admin_pwd.data,  # admin
            pool_count = form.pool_count.data, # 5
            tcp_mux = form.tcp_mux.data,  # true
            user = form.user.data,  # your_name
            login_fail_exit = form.login_fail_exit.data,
            protocol = form.protocol.data,  # tcp
            start = form.start.data,  # ssh,dns
            heartbeat_interval = form.heartbeat_interval.data,  # 30
            heartbeat_timeout = form.heartbeat_timeout.data,  # 90
            webuser = current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        print form.errors
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addTCP', methods=['GET', 'POST'])
@login_required
def addTCP():
    form = TCPForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        print form.frpc.data
        proxy = FrpProxy_TCP(
            name=form.name.data,
            local_ip = form.local_ip.data,
            local_port = form.local_port.data,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            remote_port = form.remote_port.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser = current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        print form.errors
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addUDP', methods=['GET', 'POST'])
@login_required
def addUDP():
    form = UDPForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_UDP(
            name=form.name.data,
            local_ip = form.local_ip.data,
            local_port = form.local_port.data,
            remote_port = form.remote_port.data,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            servcomm = FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addHTTP', methods=['GET', 'POST'])
@login_required
def addHTTP():
    form = HTTPForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_HTTP(
            name=form.name.data,
            local_ip = form.local_ip.data,
            local_port = form.local_port.data,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            http_user = form.http_user.data,
            http_pwd = form.http_pwd.data,
            subdomain = form.subdomain.data,
            custom_domains = form.custom_domains.data,
            locations = form.locations.data,
            host_header_rewrite = form.host_header_rewrite.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addHTTPS', methods=['GET', 'POST'])
@login_required
def addHTTPS():
    form = HTTPSForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_HTTPS(
            name=form.name.data,
            local_ip = form.local_ip.data,
            local_port = form.local_port.data,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            subdomain = form.subdomain.data,
            custom_domains = form.custom_domains.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addPluginUnixSocket', methods=['GET', 'POST'])
@login_required
def addPluginUnixSocket():
    form = PluginUnixSocketForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_PluginUnixSocket(
            name=form.name.data,
            remote_port = form.remote_port.data,
            plugin_unix_path = form.plugin_unix_path.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addPluginHttp', methods=['GET', 'POST'])
@login_required
def addPluginHttp():
    form = PluginHttpForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_PluginHttp(
            name=form.name.data,
            remote_port = form.remote_port.data,
            plugin_http_user = form.plugin_http_user.data,
            plugin_http_passwd = form.plugin_http_passwd.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addstcp', methods=['GET', 'POST'])
@login_required
def addstcp():
    form = stcpForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_STCP(
            name=form.name.data,
            sk = form.sk.data,
            local_ip = form.local_ip.data,
            local_port = form.local_port.data,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            servcomm=FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)

@user.route('/addstcpVistor', methods=['GET', 'POST'])
@login_required
def addstcpVistor():
    form = stcpVistorForm()
    types = current_user.getallcomm()
    form.frpc.choices = types
    if form.validate_on_submit():
        proxy = FrpProxy_STCPVistor(
            name=form.name.data,
            server_name = form.server_name.data,
            sk = form.sk.data,
            bind_addr = form.bind_addr.data,
            bind_port = form.bind_port,
            use_encryption = form.use_encryption.data,
            use_compression = form.use_compression.data,
            servcomm = FrpServiceCommon.query.filter_by(id=int(form.frpc.data)).first(),
            webuser=current_user
        )
        db.session.add(proxy)
        db.session.commit()
        return redirect(url_for("manage.index"))
    if form.errors:
        return 'err'
    return render_template('user/addForm.html', form=form)