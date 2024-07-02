# app/blueprints/opwu/__init__.py
from flask import Blueprint

opwu_bp = Blueprint('opwu', __name__, template_folder='templates')

from . import views
