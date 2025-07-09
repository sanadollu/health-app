from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Islem, Sehir, Doktor, Otel

views = Blueprint('views', __name__)


doktorlar = []
oteller = []
sehir2 = None

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    global sehir2, oteller
    if request.method == 'POST':
        sehir = request.form.get('sehirler')
        sehir2 = Sehir.query.filter_by(adı=sehir).first()
        oteller = Otel.query.filter_by(sehir_id=sehir2.id).all()
        return redirect(url_for('views.pick'))
    return render_template("home.html", user=current_user)

@views.route('pick', methods=['GET', 'POST'])
@login_required
def pick():
    global doktorlar
    if request.method == 'POST':
        islem = request.form.get('islemler')
        islem2 = Islem.query.filter_by(isim=islem).first()
        doktorlar = Doktor.query.filter_by(sehir_id=sehir2.id, dep_id=islem2.id).all()
        return redirect(url_for('views.info'))
    return render_template("selectprocess.html", user=current_user)

@views.route('info', methods=['GET', 'POST'])
@login_required
def info():
    global doktorlar, oteller
    if not doktorlar or not oteller:
        flash("Lütfen önce şehir ve işlem seçiniz.", category='error')
        return redirect(url_for('views.home'))

    if request.method == 'POST':
        girdi = request.form.get("rating[rating]")
        girdi_oy = int(girdi[0])
        girdi_class = girdi[2]
        girdi_id = girdi[4:]

        if girdi_class == 'd':
            upd = Doktor.query.filter_by(id=girdi_id).first()
            si = upd.sehir_id
            di = upd.dep_id
            toplam_oy = upd.oy * upd.oy_sayisi
            toplam_oy += girdi_oy
            yeni_oy = round(toplam_oy / (upd.oy_sayisi + 1), 2)
            upd.oy = yeni_oy
            upd.oy_sayisi += 1
            db.session.commit()
            doktorlar = Doktor.query.filter_by(sehir_id=si, dep_id=di).all()
            return render_template("doctorandhotel.html", user=current_user, dok=doktorlar, otel=oteller)

        elif girdi_class == 'o':
            upd = Otel.query.filter_by(id=girdi_id).first()
            si = upd.sehir_id
            toplam_oy = upd.yildiz_sayisi * upd.toplam_yildiz
            toplam_oy += girdi_oy
            yeni_oy = round(toplam_oy / (upd.toplam_yildiz + 1), 2)
            upd.yildiz_sayisi = yeni_oy
            upd.toplam_yildiz += 1
            db.session.commit()
            oteller = Otel.query.filter_by(sehir_id=si).all()
            return render_template("doctorandhotel.html", user=current_user, dok=doktorlar, otel=oteller)

    return render_template("doctorandhotel.html", user=current_user, dok=doktorlar, otel=oteller)
