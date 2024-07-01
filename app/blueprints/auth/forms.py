from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.blueprints.auth.models import Usuarios
from wtforms.validators import DataRequired, Email

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    agency = SelectField('Agency', choices=[('wiwili3', 'WiWiLi3'), ('jicaro4', 'Jicaro4')], validators=[DataRequired()])
    role = SelectField('Role', choices=[('admin', 'Administrador'), ('supervisor', 'Supervisor'), ('user', 'Usuario')], validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = Usuarios.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nombre de usuario ya está en uso. Por favor, elija otro.')

    def validate_email(self, email):
        user = Usuarios.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este correo electrónico ya está en uso. Por favor, elija otro.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')