from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from . import tasas_bp
from .forms import DefinirTasaForm, CalcularCambioForm
from .models import TasaDeCambio

@tasas_bp.route('/definir_tasas', methods=['GET', 'POST'])
@login_required
def definir_tasas():
    form = DefinirTasaForm()
    if form.validate_on_submit():
        tasa = TasaDeCambio(
            fecha=form.fecha.data,
            tasa_oficial=form.tasa_oficial.data,
            tasa_compra=form.tasa_compra.data,
            tasa_venta=form.tasa_venta.data,
            tasa_wu=form.tasa_wu.data,
            tasac_bancos=form.tasac_bancos.data,
            tasav_bancos=form.tasav_bancos.data,
            tasap_banpro=form.tasap_banpro.data,
            tasap_lafise=form.tasap_lafise.data,
            usuario_id=current_user.id,
            agencia=current_user.agency
        )
        db.session.add(tasa)
        db.session.commit()
        flash('Tasa de cambio definida exitosamente', 'success')
        return redirect(url_for('index'))
    else:
        flash('Error al definir las tasas. Por favor, revise los datos ingresados.', 'danger')
    return render_template('tasas/definir_tasas.html', form=form)

@tasas_bp.route('/calcular_cambio', methods=['GET', 'POST'])
def calcular_cambio():
    form = CalcularCambioForm()
    resultado = None
    if form.validate_on_submit():
        tipo_cambio = form.tipo_cambio.data
        monto = form.monto.data
        tasa = TasaDeCambio.query.order_by(TasaDeCambio.fecha.desc()).first()
        if tipo_cambio == 'compra':
            resultado = monto * tasa.tasa_compra
        elif tipo_cambio == 'venta':
            resultado = monto * tasa.tasa_venta
        else:
            flash('Tipo de cambio inválido', 'danger')
        # Cambiar a una ruta absoluta temporalmente
        return render_template('../templates/tasas/resultado_cambio.html', tipo_cambio=tipo_cambio, monto=monto, cambio=resultado)
    return render_template('tasas/calcular_cambio.html', form=form, resultado=resultado)
