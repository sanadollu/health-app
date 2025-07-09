from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Hasta, Sehir
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        sigorta_no = request.form.get('sigortano')
        sifre = request.form.get('sifre')

        hasta = Hasta.query.filter_by(sigorta_no=sigorta_no).first()
        if hasta:
            if check_password_hash(hasta.sifre, sifre):
                flash('Başarıyla Giriş Yapıldı!', category='success')
                login_user(hasta, remember=True)
                db.session.commit()
                return redirect(url_for('views.home'))
            else:
                flash('Yanlış Şifre, Tekrar Deneyiniz.', category='error')
        else:
            flash('Sigorta No Bulunmamakta!', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required # can't access unless logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        sigortano = request.form.get('sigortano')
        isimsoyisim = request.form.get('isim_soyisim')
        sifre1 = request.form.get('sifre1')
        sifre2 = request.form.get('sifre2')

        hasta = Hasta.query.filter_by(sigorta_no=sigortano).first()

        if hasta:
            flash('Sigorta No Zaten Kayıtlı.', category='error')
        elif (sigortano.isnumeric() is False):
            flash('Sigorta Numarası Sadece Sayı İçermeli.', category='error')
        elif (len(sigortano) != 11):
            flash('Sigorta Numarası 11 Haneli Olmalı.', category='error')
        elif (sifre1 != sifre2):
            flash('Şifreler eşleşmiyor.', category='error')
        else:
            hasta = Hasta(sigorta_no=sigortano,
                             isim_soyisim=isimsoyisim, sifre=generate_password_hash(sifre1, method='sha256'))
            db.session.add(hasta)
            db.session.commit()
            login_user(hasta, remember=True)
            flash('Hesap Oluşturuldu!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html",user=current_user)
