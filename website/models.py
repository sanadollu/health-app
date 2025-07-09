from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Doktor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim_soyisim = db.Column(db.String(100))
    telno = db.Column(db.String(11))
    foto = db.Column(db.String(100))
    hastane = db.Column(db.String(100))
    ucret = db.Column(db.Integer)
    oy = db.Column(db.Float)
    oy_sayisi = db.Column(db.Integer)
    dep_id = db.Column(db.Integer, db.ForeignKey('islem.id'))
    sehir_id = db.Column(db.Integer, db.ForeignKey('sehir.id'))

class Otel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(30))
    yildiz_sayisi = db.Column(db.Integer)
    toplam_yildiz = db.Column(db.Integer) # toplam verilen oy sayısı
    ucret = db.Column(db.Integer)
    foto = db.Column(db.String(100))
    telno = db.Column(db.String(11))
    sehir_id = db.Column(db.Integer, db.ForeignKey('sehir.id'))

class Sehir(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adı = db.Column(db.String(100))
    doktorlar = db.relationship('Doktor')
    oteller = db.relationship('Otel')

class Hasta(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    sigorta_no = db.Column(db.String(11))
    isim_soyisim = db.Column(db.String(100))
    sifre = db.Column(db.String(100))

class Islem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isim = db.Column(db.String(100))
    doktorlar = db.relationship('Doktor')


