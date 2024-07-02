from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os
from config import Config


csrf = CSRFProtect()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    

    @login_manager.user_loader
    def load_user(user_id):
        from app.blueprints.auth.models import Usuarios
        return Usuarios.query.get(int(user_id))
    
    from app.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.blueprints.tasas import tasas_bp
    app.register_blueprint(tasas_bp, url_prefix='/tasas')

    from app.blueprints.opwu import opwu_bp
    app.register_blueprint(opwu_bp, url_prefix='/opwu')
    
    @app.route('/')
    def index():
        return render_template('index.html')

    return app
