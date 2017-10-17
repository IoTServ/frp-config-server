from flask import url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.utils import redirect


class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_administrator()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))