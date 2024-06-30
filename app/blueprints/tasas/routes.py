# app/blueprints/tasas/routes.py
from flask import render_template, redirect, url_for, flash
from app import db
from app.blueprints.tasas import tasas_bp
from app.blueprints.tasas.forms import TasaDeCambioForm
from app.blueprints.tasas.models import TasaDeCambio

@tasas_bp.route('/tasas', methods=['GET', 'POST'])
def index():
    form = TasaDeCambioForm()
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
            tasap_lafise=form.tasap_lafise.data
        )
        db.session.add(tasa)
        db.session.commit()
        flash('Tasa de cambio agregada con éxito', 'success')
        return redirect(url_for('tasas.index'))
    return render_template('tasas/index.html', form=form)

@tasas_bp.route('/tasas/add', methods=['GET', 'POST'])
def add_tasa():
    form = TasaDeCambioForm()
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
            tasap_lafise=form.tasap_lafise.data
        )
        db.session.add(tasa)
        db.session.commit()
        flash('Tasa de cambio agregada con éxito', 'success')
        return redirect(url_for('tasas.index'))
    return render_template('tasas/add_tasa.html', form=form)
