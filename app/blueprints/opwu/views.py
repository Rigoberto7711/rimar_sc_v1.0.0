# app/blueprints/opwu/views.py
from app import db
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .forms import OpWuForm
from .models import OpWu

opwu_bp = Blueprint('opwu', __name__, template_folder='templates')

@opwu_bp.route('/operaciones_wu', methods=['GET', 'POST'])
@login_required
def operaciones_wu():
    form = OpWuForm()
    if form.validate_on_submit():
        opwu = OpWu(
            usuario_id=current_user.id,
            agencia='default_agency',  # Ajusta esto según tu lógica
            transaccion=form.transaccion.data,
            tipo_operacion=form.tipo_operacion.data,
            montotrus=form.montotrus.data,
            montopus=form.montopus.data,
            montotrcs=form.montotrcs.data,
            montopcs=form.montopcs.data,
            montoi_1000_CS=form.montoi_1000_CS.data,
            montoi_500_CS=form.montoi_500_CS.data,
            montoi_200_CS=form.montoi_200_CS.data,
            montoi_100_CS=form.montoi_100_CS.data,
            montoi_50_CS=form.montoi_50_CS.data,
            montoi_20_CS=form.montoi_20_CS.data,
            montoi_10_CS=form.montoi_10_CS.data,
            montoi_5_CS=form.montoi_5_CS.data,
            montoi_1_CS=form.montoi_1_CS.data,
            total_entradas_CS=form.total_entradas_CS.data,
            cambioi_CS=form.cambioi_CS.data,
            montos_1000_CS=form.montos_1000_CS.data,
            montos_500_CS=form.montos_500_CS.data,
            montos_200_CS=form.montos_200_CS.data,
            montos_100_CS=form.montos_100_CS.data,
            montos_50_CS=form.montos_50_CS.data,
            montos_20_CS=form.montos_20_CS.data,
            montos_10_CS=form.montos_10_CS.data,
            montos_5_CS=form.montos_5_CS.data,
            montos_1_CS=form.montos_1_CS.data,
            total_Salidas_CS=form.total_Salidas_CS.data,
            ajuste_CS=form.ajuste_CS.data,
            montoE_100_US=form.montoE_100_US.data,
            montoE_50_US=form.montoE_50_US.data,
            montoE_20_US=form.montoE_20_US.data,
            montoE_10_US=form.montoE_10_US.data,
            montoE_5_US=form.montoE_5_US.data,
            montoE_1_US=form.montoE_1_US.data,
            total_entradas_US=form.total_entradas_US.data,
            cambioE_US=form.cambioE_US.data,
            montoP_100_US=form.montoP_100_US.data,
            montoP_50_US=form.montoP_50_US.data,
            montoP_20_US=form.montoP_20_US.data,
            montoP_10_US=form.montoP_10_US.data,
            montoP_5_US=form.montoP_5_US.data,
            montoP_1_US=form.montoP_1_US.data,
            total_salidas_US=form.total_salidas_US.data,
            ajuste_US=form.ajuste_US.data,
            ajuste=form.ajuste.data
        )
        db.session.add(opwu)
        db.session.commit()
        flash('Operación guardada exitosamente.', 'success')
        return redirect(url_for('opwu.operaciones_wu'))
    return render_template('opwu/operaciones_wu.html', form=form)

@opwu_bp.route('/listar_opwu', methods=['GET'])
@login_required
def listar_opwu():
    operaciones = OpWu.query.all()
    return render_template('opwu/listar_opwu.html', operaciones=operaciones)
