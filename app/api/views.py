# coding:utf-8
from flask import request,render_template
from flask_login import current_user
from . import api
from ..models import FrpServiceCommon

@api.route('/', methods=["GET"])
def api_index():
    return 'api'

@api.route('/get-frc-conf', methods=["GET"])
def get_frc_conf():
    user=request.values.get('user')
    if user:
        Common = FrpServiceCommon.query.filter_by(user=user).first()
        if Common != None:
            return render_template('api/frc.html', comm=Common, udp=Common.udp_s, vistor=Common.stcpvistor_s, stcp=Common.stcp_s, tcp=Common.tcp_s\
                                   , usocket=Common.pusocket_s, phttp=Common.phttp_s, https=Common.https_s, http=Common.http_s), {'Content-Type': 'text/plain'}
    return 'cant\'t get name and sk values'