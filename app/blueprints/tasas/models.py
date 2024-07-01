from app import db
from flask_login import current_user
from datetime import datetime

class TasaDeCambio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    tasa_oficial = db.Column(db.Float, nullable=False)
    tasa_compra = db.Column(db.Float, nullable=False)
    tasa_venta = db.Column(db.Float, nullable=False)
    tasa_wu = db.Column(db.Float, nullable=False)
    tasac_bancos = db.Column(db.Float, nullable=False)
    tasav_bancos = db.Column(db.Float, nullable=False)
    tasap_banpro = db.Column(db.Float, nullable=False)
    tasap_lafise = db.Column(db.Float, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    agencia = db.Column(db.String(20), nullable=False)
    
    usuario = db.relationship('Usuarios', backref=db.backref('tasas', lazy=True))
