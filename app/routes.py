from flask import render_template, Blueprint
from flask_login import login_required, current_user
from app import db
from sqlalchemy import text  # Asegúrate de que esta línea esté presente

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/admin')
@login_required
def admin():
    if current_user.role != 'administrador':
        return render_template('403.html'), 403
    return render_template('admin.html')

@main_bp.route('/cause_error')
def cause_error():
    # Intentionally cause a database error by querying a non-existent table
    result = db.session.execute(text('SELECT * FROM non_existent_table'))
    return result.fetchall()