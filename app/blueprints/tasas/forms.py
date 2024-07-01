from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, DateField
from wtforms.validators import DataRequired

class DefinirTasaForm(FlaskForm):
    fecha = DateField('Fecha Actual', format='%Y-%m-%d', validators=[DataRequired()])
    tasa_oficial = FloatField('Tasa de Cambio Oficial', validators=[DataRequired()])
    tasa_compra = FloatField('Tasa de Compra', validators=[DataRequired()])
    tasa_venta = FloatField('Tasa de Venta', validators=[DataRequired()])
    tasa_wu = FloatField('Tasa WU', validators=[DataRequired()])
    tasac_bancos = FloatField('Tasa de Compra Bancos', validators=[DataRequired()])
    tasav_bancos = FloatField('Tasa de Venta Bancos', validators=[DataRequired()])
    tasap_banpro = FloatField('Tasa Preferencial Banpro', validators=[DataRequired()])
    tasap_lafise = FloatField('Tasa Preferencial La Fise', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class CalcularCambioForm(FlaskForm):
    tipo_cambio = StringField('Tipo de Cambio', validators=[DataRequired()])
    monto = FloatField('Monto', validators=[DataRequired()])
    submit = SubmitField('Calcular')
