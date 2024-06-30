# app/blueprints/tasas/models.py
from app import db

class TasaDeCambio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    tasa_oficial = db.Column(db.Float, nullable=False)
    tasa_compra = db.Column(db.Float, nullable=False)
    tasa_venta = db.Column(db.Float, nullable=False)
    tasa_wu = db.Column(db.Float, nullable=False)
    tasac_bancos = db.Column(db.Float, nullable=False)
    tasav_bancos = db.Column(db.Float, nullable=False)
    tasap_banpro = db.Column(db.Float, nullable=False)
    tasap_lafise = db.Column(db.Float, nullable=False)
