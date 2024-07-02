from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class OpWuForm(FlaskForm):
    transaccion = SelectField('Transacción', choices=[
        ('pago_remesa_wu_us', 'Pago de Remesa WU US'),
        ('pago_remesa_wu_cs', 'Pago de Remesa WU CS'),
        ('envio_remesa_wu_us', 'Envio de Remesa WU US'),
        ('envio_remesa_wu_cs', 'Envio de Remesa WU CS')
    ], validators=[DataRequired()])
    tipo_operacion = SelectField('Tipo de Operación', choices=[
        ('egreso', 'Egreso'),
        ('ingreso', 'Ingreso')
    ], validators=[DataRequired()])
    montotrus = FloatField('Monto Transacción US', validators=[DataRequired()])
    montopus = FloatField('Monto Pago US', validators=[DataRequired()])
    montotrcs = FloatField('Monto Transacción CS', validators=[DataRequired()])
    montopcs = FloatField('Monto Pago CS', validators=[DataRequired()])
    montoi_1000_CS = FloatField('1000 CS', validators=[DataRequired()])
    montoi_500_CS = FloatField('500 CS', validators=[DataRequired()])
    montoi_200_CS = FloatField('200 CS', validators=[DataRequired()])
    montoi_100_CS = FloatField('100 CS', validators=[DataRequired()])
    montoi_50_CS = FloatField('50 CS', validators=[DataRequired()])
    montoi_20_CS = FloatField('20 CS', validators=[DataRequired()])
    montoi_10_CS = FloatField('10 CS', validators=[DataRequired()])
    montoi_5_CS = FloatField('5 CS', validators=[DataRequired()])
    montoi_1_CS = FloatField('1 CS', validators=[DataRequired()])
    total_entradas_CS = FloatField('Total Entradas CS', validators=[DataRequired()])
    cambioi_CS = FloatField('Cambio Inicial CS', validators=[DataRequired()])
    montos_1000_CS = FloatField('1000 CS', validators=[DataRequired()])
    montos_500_CS = FloatField('500 CS', validators=[DataRequired()])
    montos_200_CS = FloatField('200 CS', validators=[DataRequired()])
    montos_100_CS = FloatField('100 CS', validators=[DataRequired()])
    montos_50_CS = FloatField('50 CS', validators=[DataRequired()])
    montos_20_CS = FloatField('20 CS', validators=[DataRequired()])
    montos_10_CS = FloatField('10 CS', validators=[DataRequired()])
    montos_5_CS = FloatField('5 CS', validators=[DataRequired()])
    montos_1_CS = FloatField('1 CS', validators=[DataRequired()])
    total_Salidas_CS = FloatField('Total Salidas CS', validators=[DataRequired()])
    ajuste_CS = FloatField('Ajuste CS', validators=[DataRequired()])
    montoE_100_US = FloatField('100 US', validators=[DataRequired()])
    montoE_50_US = FloatField('50 US', validators=[DataRequired()])
    montoE_20_US = FloatField('20 US', validators=[DataRequired()])
    montoE_10_US = FloatField('10 US', validators=[DataRequired()])
    montoE_5_US = FloatField('5 US', validators=[DataRequired()])
    montoE_1_US = FloatField('1 US', validators=[DataRequired()])
    total_entradas_US = FloatField('Total Entradas US', validators=[DataRequired()])
    cambioE_US = FloatField('Cambio Inicial US', validators=[DataRequired()])
    montoP_100_US = FloatField('100 US', validators=[DataRequired()])
    montoP_50_US = FloatField('50 US', validators=[DataRequired()])
    montoP_20_US = FloatField('20 US', validators=[DataRequired()])
    montoP_10_US = FloatField('10 US', validators=[DataRequired()])
    montoP_5_US = FloatField('5 US', validators=[DataRequired()])
    montoP_1_US = FloatField('1 US', validators=[DataRequired()])
    total_salidas_US = FloatField('Total Salidas US', validators=[DataRequired()])
    ajuste_US = FloatField('Ajuste US', validators=[DataRequired()])
    ajuste = FloatField('Ajuste', validators=[DataRequired()])
    submit = SubmitField('Guardar')
