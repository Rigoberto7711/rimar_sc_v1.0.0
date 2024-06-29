from flask import render_template, redirect, url_for, flash
from app.blueprints.auth import auth_bp
from flask_login import login_user, logout_user, login_required
from app import db

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    from app.blueprints.auth.forms import LoginForm
    form = LoginForm()
    if form.validate_on_submit():
        from app.blueprints.auth.models import User
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    from app.blueprints.auth.forms import RegistrationForm
    form = RegistrationForm()
    if form.validate_on_submit():
        from app.blueprints.auth.models import User
        user = User(username=form.username.data, role=form.role.data, agency=form.agency.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
