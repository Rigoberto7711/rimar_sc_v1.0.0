# app/blueprints/tasas/__init__.py
from flask import Blueprint

tasas_bp = Blueprint('tasas', __name__)

from app.blueprints.tasas import routes
