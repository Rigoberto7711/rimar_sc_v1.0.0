from flask import Blueprint

tasas_bp = Blueprint('tasas', __name__, template_folder='templates')

from . import views
