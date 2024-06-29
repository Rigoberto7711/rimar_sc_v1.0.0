from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    with app.app_context():
        from app.blueprints.auth.models import User
        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
        
        from app.blueprints.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.routes import main_bp
        app.register_blueprint(main_bp)

        from app.errors import register_error_handlers
        register_error_handlers(app)

    return app
