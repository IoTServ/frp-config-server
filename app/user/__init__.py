from flask import Blueprint

user = Blueprint('manage', __name__)

from . import views
