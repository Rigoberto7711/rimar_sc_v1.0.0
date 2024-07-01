from flask import Blueprint

auth = Blueprint('auth', __name__)

# Importa las rutas después de definir el blueprint
from app.blueprints.auth import routes

